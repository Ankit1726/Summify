import os
import re
import torch
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, T5ForConditionalGeneration

MODEL_PATH = os.getenv("MODEL_PATH", "Anki1726/Model_T5")
FRONTEND_DIR = os.getenv("FRONTEND_DIR", "/app/frontend")

MAX_INPUT_LENGTH = 512
MAX_SUMMARY_LENGTH = 150

# CPU optimization
torch.set_num_threads(int(os.getenv("TORCH_NUM_THREADS", "2")))

app = FastAPI(
    title="Summify API",
    description="Text summarization powered by a fine-tuned T5 model",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
tokenizer = None
device = torch.device("cpu")


def get_device() -> torch.device:
    """
    Detect the best available device.
    Render will normally use CPU.
    """

    if torch.cuda.is_available():
        return torch.device("cuda")

    if hasattr(torch.backends, "mps"):
        if torch.backends.mps.is_available():
            return torch.device("mps")

    return torch.device("cpu")


@app.on_event("startup")
def load_model() -> None:
    """
    Load tokenizer and model once when FastAPI starts.
    """

    global model
    global tokenizer
    global device

    print("=" * 50)
    print("Starting Summify API")
    print("=" * 50)

    device = get_device()

    print(f"Model: {MODEL_PATH}")
    print(f"Device: {device}")

    try:
        # Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

        # Load model
        model = T5ForConditionalGeneration.from_pretrained(
            MODEL_PATH, low_cpu_mem_usage=True
        )

        # Move model to CPU/GPU
        model.to(device)

        # Inference mode
        model.eval()

        print("Model loaded successfully.")

    except Exception as e:

        print(f"Model loading failed: {e}")

        model = None
        tokenizer = None

        raise


class DialogueInput(BaseModel):

    dialogue: str = Field(
        ..., min_length=1, description="Dialogue or text to summarize"
    )


class SummaryOutput(BaseModel):

    summary: str


def clean_data(text: str) -> str:
    """
    Clean input text before tokenization.
    """

    # Replace line breaks
    text = text.replace("\r\n", " ")
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def summarize_dialogue(dialogue: str) -> str:

    if model is None or tokenizer is None:
        raise RuntimeError("Model is not loaded")

    dialogue = clean_data(dialogue)

    # Tokenization
    inputs = tokenizer(
        dialogue,
        max_length=MAX_INPUT_LENGTH,
        truncation=True,
        padding=True,
        return_tensors="pt",
    )

    # Move tensors to device
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Inference only
    with torch.inference_mode():

        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            # Output length
            max_new_tokens=MAX_SUMMARY_LENGTH,
            # Beam search
            num_beams=4,
            # Stop when appropriate
            early_stopping=True,
            # Reduce repeated phrases
            no_repeat_ngram_size=2,
        )

    summary = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return summary.strip()

@app.get("/health")
def health():

    return {"status": "ok", "model_loaded": model is not None, "device": str(device)}

@app.get("/api")
def api_info():

    return {
        "name": "Summify API",
        "version": "1.0.0",
        "model": MODEL_PATH,
        "device": str(device),
        "model_loaded": model is not None,
    }


@app.post("/summarize/", response_model=SummaryOutput)
def summarize(payload: DialogueInput):

    dialogue = payload.dialogue.strip()

    if not dialogue:

        raise HTTPException(status_code=400, detail="dialogue must not be empty")

    if model is None or tokenizer is None:

        raise HTTPException(
            status_code=503, detail="Model is still loading. Please try again."
        )

    try:

        summary = summarize_dialogue(dialogue)
        return SummaryOutput(summary=summary)

    except Exception as e:
        print(f"Summarization error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate summary.")




if os.path.isdir(FRONTEND_DIR):
    print(f"Frontend directory: {FRONTEND_DIR}")
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
else:
    print(f"WARNING: Frontend directory not found: " f"{FRONTEND_DIR}")