
# 🌊 SurfPilot.ai — Influencer Co-Pilot

Surf.ai is a smart AI assistant designed for micro-influencers and content creators. Paste your brand DMs or emails, and Surf.ai will instantly:
- Summarize the brand deal
- Extract key info (like product, deliverables, payment)
- Suggest a professional reply
- (Soon) Generate a downloadable invoice PDF

Built with **FastAPI + Streamlit + OpenAI GPT-4o**.

---

## 🧠 Features

- ✉️ Paste any email or brand message  
- 🔍 Extract deliverables, deadlines, and payment info  
- 💬 Get a professional AI-suggested reply  
- 🧾 [Planned] Auto-generate invoices from the offer

---

## 🏗️ Tech Stack

- `frontend/` — [Streamlit](https://streamlit.io/) app for user input & display  
- `backend/` — [FastAPI](https://fastapi.tiangolo.com/) server for AI processing  
- `OpenAI GPT-4o` — AI model for analysis and generation  

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/surf-ai.git
cd surf-ai
```

### 2. Set up environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> Make sure `openai`, `fastapi`, `streamlit`, `python-dotenv`, `requests`, and `uvicorn` are included in `requirements.txt`.

### 3. Add your OpenAI API key

Create a `.env` file in the root:

```
OPENAI_API_KEY=sk-xxxxxxx
```

---

## 🧪 Run the app

### Run the backend (FastAPI)
```bash
uvicorn backend.main:app --reload
```

### Run the frontend (Streamlit)
```bash
streamlit run frontend/app.py
```

Open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 📦 Planned Features

- ✅ Analyze messages with GPT-4o  
- ✅ Auto-reply suggestions  
- ⏳ Smart invoice PDF generator  
- ⏳ Analytics dashboard for campaigns  
- ⏳ CRM / calendar sync for deal tracking  

---

## 📄 License

MIT — free to use, remix, improve.

---

## 🤙 Author

Built with ❤️ by Tijmen, for creators who want less admin and more surfing.
