import speech_recognition as sr
from utils.voice import initialize_voice_engine, select_microphone, listen_for_command

def main():
    initialize_voice_engine()

    recognizer = sr.Recognizer()
    microphone = select_microphone()

    while True:
        try:
            with microphone as source:
                listen_for_command(recognizer, source)
        except KeyboardInterrupt:
            print("\nExiting voice assistant...")
            break
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()