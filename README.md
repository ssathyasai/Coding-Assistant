# AI Coding Mentor

A local AI-powered coding assistant built with TinyLlama, FastAPI, and React.
Ask coding questions and get answers instantly — runs fully on your machine.

---

## What This Project Does

- Chat UI where students can ask coding questions
- Questions are sent to a local AI model (via Ollama)
- AI answers in markdown with proper code formatting
- Covers Python, Java, SQL, React, and interview topics

---

## Project Structure

```
X/
├── coding-llm/
│   ├── expanded_dataset.jsonl   # 225 coding Q&A training records
│   ├── generate_dataset.py      # script to generate the dataset
│   ├── train_phi2.py            # fine-tuning script (LoRA + TinyLlama)
│   ├── api.py                   # FastAPI backend (connects UI to model)
│   └── chat.py                  # terminal chat interface
│
└── coding-ai-ui/
    └── src/
        ├── App.js               # React chat UI
        └── App.css              # styling
```

---

## Tech Stack

| Layer    | Technology        |
|----------|-------------------|
| Frontend | React             |
| Backend  | FastAPI (Python)  |
| Model    | Llama3 via Ollama |
| Training | HuggingFace + LoRA |

---

## How to Run

### Prerequisites
- Python 3.11
- Node.js
- [Ollama](https://ollama.com) installed

### Step 1 — Pull the model
```bash
ollama pull llama3
```

### Step 2 — Start the backend
```bash
cd coding-llm
venv\Scripts\activate
uvicorn api:app --reload
```

### Step 3 — Start the frontend
```bash
cd coding-ai-ui
npm install
npm start
```

### Step 4 — Open in browser
```
http://localhost:3000
```

---

## Note on Fine-Tuning

The dataset (`expanded_dataset.jsonl`) and training script (`train_phi2.py`)
are included but fine-tuning requires a GPU to complete.
To fine-tune, upload both files to Google Colab and run `train_phi2.py` there.
The current setup uses the base `llama3` model via Ollama.

---

## Author

**SATHYASAI**
