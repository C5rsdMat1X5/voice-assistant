import pyttsx3
import speech_recognition as sr
from .commands import process_voice_command
from .speaker import speak_text

engine = pyttsx3.init()

def initialize_voice_engine():
    voices = engine.getProperty("voices")
    english_voice_id = None
    for voice in voices:
        if "en_US" in voice.languages or "en_GB" in voice.languages:
            if "Samantha" in voice.name or "Karen" in voice.name or "Moira" in voice.name:
                english_voice_id = voice.id
                break
            elif not english_voice_id and "com.apple.voice.compact.en" in voice.id:
                english_voice_id = voice.id
    if english_voice_id:
        print(f"Using English voice: {english_voice_id}")
        engine.setProperty("voice", english_voice_id)
    else:
        print("No specific English voice found, using default or first available.")
        if voices:
            engine.setProperty("voice", voices[0].id)

def select_microphone():
    available_mics = sr.Microphone.list_microphone_names()
    for i, mic in enumerate(available_mics):
        print(i + 1, mic)
    selected_index = int(input("Select a microphone: ")) - 1
    print("Selected:", available_mics[selected_index])
    return sr.Microphone(device_index=selected_index)

def listen_for_command(recognizer, source):
    print("Say 'hey robot' to activate...")
    try:
        audio = recognizer.listen(source)
        phrase = recognizer.recognize_google(audio, language="en-US").lower()
        if "hey robot" in phrase:
            speak_text("I'm listening")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-US").lower()
            print(command)
            process_voice_command(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak_text("Speech recognition error")