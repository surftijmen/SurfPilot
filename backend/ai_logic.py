from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_message(text, profile):
    prompt = f"""
You are a virtual assistant helping an influencer respond to brand emails.

Here is the influencer's personal profile:
{profile}

Here is the brand message:
{text}

TASKS:
1. Extract this info:
   - Brand Name
   - Product
   - Deliverables
   - Deadline
   - Payment Offered

2. Summarize the request in simple terms.

3. Write a smart, polite, and confident reply that matches the influencer's tone and preferences. Mention rate if it's missing. Include relevant product interest if possible.

Respond in this format:

SUMMARY:
...

EXTRACTED INFO:
...

SUGGESTED REPLY:
...

"""
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content

    parts = content.split("\n\n")
    return parts[0], parts[1], parts[2]


def generate_invoice(message_text):
    # TODO: parse message and render invoice template to PDF
    return b"FAKE_PDF_BYTES"