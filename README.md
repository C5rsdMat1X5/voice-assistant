# 🤖 Voice Assistant with Gemini AI

This is a Python-based voice assistant that uses the Gemini model to answer questions and execute system commands on macOS. Perfect for automating tasks while sipping your coffee ☕.

---

## 🗂️ Project Structure

```plaintext
.
├── main.py                 # Main script to run the assistant
├── requirements.txt        # Project dependencies
└── utils                   # Helper modules
    ├── commands.py         # Command definitions and actions
    ├── config.py           # Configuration and environment variables
    ├── gemini.py           # Gemini API interaction
    ├── speaker.py          # Text-to-speech functionality (TTS)
    └── voice.py            # Voice recognition and microphone handling
```

---

## ⚙️ Installation

### 1. Clone the repository:

```bash
git clone https://github.com/C5rsdMat1X5/voice-assistant
cd voice-assistant
```

### 2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key:

Create a `.env` file at the root of the project and add:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 🚀 Usage

Run the assistant with:

```bash
python3 main.py
```

Upon starting, select the microphone you want to use.

To activate the assistant, say `"hey robot"` and then speak your command or question 🎤.

### 🧠 Example Available Commands:

* `open browser` 🌐
* `open spotify` 🎵
* `current time` 🕒
* `tell a joke` 😂
* `what is [your question]` ❓
* `search wikipedia [topic]` 📚
* `empty trash` 🗑️
* `show ip` 🌍
* `list of commands` For all the commands 📝

And many more listed in `utils/commands.py`.

---

## ✅ Requirements

* macOS 🍏
* Python 3.8+ 🐍
* Valid Gemini API Key 🔐

---

## 📝 Notes

* Uses `pyttsx3` for text-to-speech 🗣️.
* Uses `speech_recognition` to capture voice commands 🎧.
* Gemini responses are limited to 3 lines to be easily read aloud 📏.
* Internet connection is required to function properly 🌐.

---

## 📄 License

This project is free for personal use. Feel free to modify and adapt it as you wish 🛠️.
