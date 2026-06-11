from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ollama runs locally at this address
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME  = "llama3"      # better code quality than tinyllama


class Question(BaseModel):
    prompt: str


@app.post("/ask")
def ask_ai(data: Question):
    payload = {
        "model": MODEL_NAME,
        "prompt": (
            "You are a professional coding assistant. "
            "Give clear and correct coding answers.\n\n"
            f"Instruction: {data.prompt}\nAnswer:"
        ),
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "repeat_penalty": 1.15,
            "num_predict": 350,
        },
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=120)
        res.raise_for_status()
        answer = res.json().get("response", "").strip()
        return {"response": answer}
    except requests.exceptions.ConnectionError:
        return {"response": "❌ Ollama is not running. Start it with: ollama serve"}
    except Exception as e:
        return {"response": f"❌ Error: {str(e)}"}
