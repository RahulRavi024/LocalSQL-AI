
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"


def ask_llm(prompt: str) -> str:

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "num_predict": 256,
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    data = response.json()

    result = data.get("response", "").strip()

    print("\n========== RAW OLLAMA RESPONSE ==========")
    print(repr(result))
    print("=====================================\n")

    if not result:
        raise ValueError("The LLM returned an empty response.")

    return result
