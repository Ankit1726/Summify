import os
import re

import torch
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, T5ForConditionalGeneration


MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "Anki1726/Model_T5"
)

FRONTEND_DIR = os.getenv(
    "FRONTEND_DIR",
    "/app/frontend"
)

MAX_INPUT_LENGTH = 512
MAX_SUMMARY_LENGTH = 150

# Keep CPU memory/thread usage under control
TORCH_NUM_THREADS = int(
    os.getenv("TORCH_NUM_THREADS", "1")
)

torch.set_num_threads(TORCH_NUM_THREADS)
torch.set_num_interop_threads(1)


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Summify API",
    description="Text summarization powered by a fine-tuned T5 model",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# GLOBAL MODEL VARIABLES
# ============================================================

model = None
tokenizer = None

# Render CPU environment
device = torch.device("cpu")


# ============================================================
# DEVICE
# ============================================================

def get_device() -> torch.device:
    """
    Detect available device.

    Render normally runs on CPU.
    """

    if torch.cuda.is_available():
        return torch.device("cuda")

    if hasattr(torch.backends, "mps"):
        if torch.backends.mps.is_available():
            return torch.device("mps")

    return torch.device("cpu")


# ============================================================
# MODEL LOADING
# ============================================================

@app.on_event("startup")
def load_model() -> None:
    """
    Load tokenizer and model once during application startup.
    """

    global model
    global tokenizer
    global device

    print("=" * 60)
    print("Starting Summify API")
    print("=" * 60)

    device = get_device()

    print(f"Model: {MODEL_PATH}")
    print(f"Device: {device}")
    print(f"Torch threads: {TORCH_NUM_THREADS}")

    try:

        # ----------------------------------------------------
        # Load tokenizer
        # ----------------------------------------------------

        print("Loading tokenizer...")

        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_PATH
        )

        print("Tokenizer loaded.")

        # ----------------------------------------------------
        # Load T5 model
        # ----------------------------------------------------

        print("Loading T5 model...")

        model = T5ForConditionalGeneration.from_pretrained(
            MODEL_PATH,
            low_cpu_mem_usage=True
        )

        # ----------------------------------------------------
        # Move model to device
        # ----------------------------------------------------

        model.to(device)

        # ----------------------------------------------------
        # Evaluation mode
        # ----------------------------------------------------

        model.eval()

        print("Model loaded successfully.")
        print("=" * 60)

    except Exception as e:

        print("=" * 60)
        print("MODEL LOADING FAILED")
        print(str(e))
        print("=" * 60)

        model = None
        tokenizer = None

        raise


# ============================================================
# REQUEST MODEL
# ============================================================

class DialogueInput(BaseModel):

    dialogue: str = Field(
        ...,
        min_length=1,
        description="Dialogue or text to summarize"
    )


# ============================================================
# RESPONSE MODEL
# ============================================================

class SummaryOutput(BaseModel):

    summary: str


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_data(text: str) -> str:
    """
    Clean input text before sending it to the model.
    """

    # Normalize line breaks
    text = text.replace("\r\n", " ")
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    # Remove HTML tags
    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip().lower()


# ============================================================
# SUMMARIZATION
# ============================================================

def summarize_dialogue(dialogue: str) -> str:

    if model is None or tokenizer is None:
        raise RuntimeError(
            "Model is not loaded"
        )

    # Clean input
    dialogue = clean_data(dialogue)

    # --------------------------------------------------------
    # Tokenization
    # --------------------------------------------------------

    inputs = tokenizer(
        dialogue,
        max_length=MAX_INPUT_LENGTH,
        truncation=True,
        padding=False,
        return_tensors="pt"
    )

    # Move tensors to CPU/GPU
    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    # --------------------------------------------------------
    # Generate summary
    # --------------------------------------------------------

    with torch.inference_mode():

        generated_ids = model.generate(

            input_ids=inputs["input_ids"],

            attention_mask=inputs["attention_mask"],

            # Maximum generated tokens
            max_new_tokens=MAX_SUMMARY_LENGTH,

            # Beam search
            num_beams=4,

            # Stop when generation is complete
            early_stopping=True,

            # Prevent repeated phrases
            no_repeat_ngram_size=2,
        )

    # --------------------------------------------------------
    # Decode
    # --------------------------------------------------------

    summary = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens=True
    )

    return summary.strip()


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "model_loaded": model is not None,
        "device": str(device),
    }


# ============================================================
# API INFO
# ============================================================

@app.get("/api")
def api_info():

    return {
        "name": "Summify API",
        "version": "1.0.0",
        "model": MODEL_PATH,
        "device": str(device),
        "model_loaded": model is not None,
    }


# ============================================================
# SUMMARIZE ENDPOINT
# ============================================================

@app.post(
    "/summarize/",
    response_model=SummaryOutput
)
def summarize(payload: DialogueInput):

    dialogue = payload.dialogue.strip()

    # Validate input
    if not dialogue:

        raise HTTPException(
            status_code=400,
            detail="dialogue must not be empty"
        )

    # Check model
    if model is None or tokenizer is None:

        raise HTTPException(
            status_code=503,
            detail="Model is still loading. Please try again."
        )

    try:

        summary = summarize_dialogue(
            dialogue
        )

        return SummaryOutput(
            summary=summary
        )

    except Exception as e:

        print(
            f"Summarization error: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to generate summary."
        )


# ============================================================
# FRONTEND
# ============================================================

if os.path.isdir(FRONTEND_DIR):

    print(
        f"Frontend directory: {FRONTEND_DIR}"
    )

    app.mount(
        "/",
        StaticFiles(
            directory=FRONTEND_DIR,
            html=True
        ),
        name="frontend"
    )

else:

    print(
        f"WARNING: Frontend directory not found: "
        f"{FRONTEND_DIR}"
    )