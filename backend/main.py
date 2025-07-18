from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.ai_logic import analyze_message, generate_invoice
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageInput(BaseModel):
    message: str

@app.post("/analyze")
async def analyze(input: MessageInput):
    summary, info, reply = analyze_message(input.message)
    return {"summary": summary, "info": info, "reply": reply}

@app.post("/generate-invoice")
async def invoice(input: MessageInput):
    pdf_bytes = generate_invoice(input.message)
    return {"invoice": pdf_bytes.decode('latin1')}  # For demo purposes
