import pyttsx3

engine = pyttsx3.init()

def speak_text(text: str) -> None:
    print(f"[TTS] {text}")
    engine.say(text)
    engine.runAndWait()