import whisper
import subprocess
import uuid
import os

model = whisper.load_model("base")

def convert_to_wav(input_path):
    output_path = f"uploads/{uuid.uuid4().hex}.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", output_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return output_path


def transcribe_audio(file_path: str) -> str:
    wav_path = convert_to_wav(file_path)
    result = model.transcribe(wav_path)
    return result["text"]
