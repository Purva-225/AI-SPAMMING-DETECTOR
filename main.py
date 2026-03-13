from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

keywords = ["verify", "bank", "otp", "password", "urgent", "click here"]

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/analyze")
def analyze(message: Message):

    text = message.text.lower()
    risk = "LOW"
    reasons = []

    for word in keywords:
        if word in text:
            risk = "HIGH"
            reasons.append(f"Suspicious keyword: {word}")

    if not reasons:
        reasons.append("No suspicious keywords")

    return {
        "risk": risk,
        "reason": reasons
    }
