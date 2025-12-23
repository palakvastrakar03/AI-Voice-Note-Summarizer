from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from backend.transcribe import transcribe_audio
from backend.ai_features import (
    generate_summary,
    generate_bullet_points,
    extract_keywords
)

app = FastAPI(title="AI Voice Note Summarizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def health():
    return {"status": "Backend running"}


@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"filename": file.filename}


from backend.transcribe import transcribe_audio
from backend.ai_features import (
    generate_summary,
    generate_bullet_points,
    extract_keywords
)

@app.post("/transcribe")
async def transcribe_audio_api(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")

    transcript = transcribe_audio(file_path)

    return {
        "transcript": transcript,
        "summary": generate_summary(transcript),
        "bullet_points": generate_bullet_points(transcript),
        "keywords": extract_keywords(transcript)
    }
