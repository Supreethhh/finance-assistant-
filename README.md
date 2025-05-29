#  Multi-Agent Finance Assistant

##  Architecture

```
Voice Input (Whisper) --> Orchestrator (FastAPI or Streamlit) -->
    ├── API Agent (yfinance)
    ├── Scraping Agent (BeautifulSoup)
    ├── Retriever Agent (FAISS)
    ├── Language Agent (Gemini)
    └── Voice Agent (pyttsx3)
```

## Setup Instructions

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python data_ingestion/ingest.py
streamlit run streamlit_app/app.py
```

##  Toolkit Comparisons
- RAG: FAISS vs Pinecone (FAISS used)
- STT: Whisper (local, accurate)
- TTS: pyttsx3 (offline)
- LLM: Gemini via google-generativeai

##  Performance
- Cold start: ~5s
- Response generation: ~2-3s
- Voice playback: near real-time



1. Install requirements
2. Run Streamlit
