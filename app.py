import os, re
import torch

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import AutoTokenizer, T5ForConditionalGeneration

MODEL_PATH = os.getenv("MODEL_PATH", "Anki1726/Model_T5")
FRONTEND_DIR = os.getenv("FRONTEND_DIR", "./frontend")
MAX_INPUT_LENGTH = 512
MAX_SUMMARY_LENGTH = 150

app = FastAPI(
    title="Summify API",
    description="Text summarization powered by a fine-tuned T5 model",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
tokenizer = None
device = torch.device("cpu")


def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


@app.on_event("startup")
def load_model() -> None:
    global model, tokenizer, device
    device = get_device()
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model.to(device)
    model.eval()


class DialogueInput(BaseModel):
    dialogue: str


class SummaryOutput(BaseModel):
    summary: str


def clean_data(text: str) -> str:
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def summarize_dialogue(dialogue: str) -> str:
    dialogue = clean_data(dialogue)

    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=MAX_INPUT_LENGTH,
        truncation=True,
        return_tensors="pt",
    ).to(device)

    with torch.no_grad():
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=MAX_SUMMARY_LENGTH,
            num_beams=4,
            early_stopping=True,
        )
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "device": str(device)}


@app.post("/summarize/", response_model=SummaryOutput)
async def summarize(payload: DialogueInput) -> SummaryOutput:
    dialogue = payload.dialogue.strip()
    if not dialogue:
        raise HTTPException(status_code=400, detail="dialogue must not be empty")
    if model is None or tokenizer is None:
        raise HTTPException(
            status_code=503, detail="model is still loading, try again shortly"
        )

    summary = summarize_dialogue(dialogue)
    return SummaryOutput(summary=summary)


if os.path.isdir(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")