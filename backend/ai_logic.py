from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_message(message: str):
    response = client.chat.completions.create(
        model="gpt-4o",  # or gpt-3.5-turbo if you want
        messages=[
            {"role": "system", "content": "You're an assistant helping an influencer understand brand deal messages."},
            {"role": "user", "content": message}
        ]
    )

    full_text = response.choices[0].message.content.strip()

    # Optional: Split based on format
    summary = "Summary placeholder"
    info = "Info placeholder"
    reply = full_text

    return summary, info, reply

def generate_invoice(message_text):
    # TODO: parse message and render invoice template to PDF
    return b"FAKE_PDF_BYTES"