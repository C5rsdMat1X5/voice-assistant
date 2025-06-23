import requests
import json
from .config import GEMINI_URL

def query_gemini(user_prompt: str) -> str:
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "Respond in a maximum of 3 lines, or fewer if accurate. "
                            "Avoid special characters. Make it clear and easy to read for TTS. "
                            "Only provide the content: " + user_prompt
                        )
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_URL, headers=headers, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Request failed:", e)
        return f"Request error: {e}"

    try:
        data = response.json()
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
        print("Gemini response:")
        print(answer)
        return f"Gemini said: {answer}"
    except (json.JSONDecodeError, KeyError) as e:
        print("Error parsing JSON:", e)
        return f"JSON parsing error: {e}"