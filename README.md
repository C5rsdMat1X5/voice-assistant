# 🤖 Voice Assistant with Gemini AI

This is a Python-based voice assistant that uses the Gemini model to answer questions and execute system commands.  
Designed originally for macOS, but now with improved compatibility for Windows and Linux. Perfect for automating tasks while sipping your coffee ☕.

---

## 🗂️ Project Structure

```plaintext
.
├── main.py                 # Main script to run the assistant
├── requirements.txt        # Project dependencies
└── utils                   # Helper modules
    ├── commands.py         # Command definitions and actions (multiplatform compatible)
    ├── config.py           # Configuration and environment variables
    ├── gemini.py           # Gemini API interaction
    ├── speaker.py          # Text-to-speech functionality (TTS)
    └── voice.py            # Voice recognition and microphone handling (auto voice selection by OS)
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
# On macOS and Linux
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
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
# macOS and Linux
python3 main.py

# Windows
python main.py
```

Upon starting, select the microphone you want to use.

To activate the assistant, say `"hey robot"` and then speak your command or question 🎤.

---

## 🧠 Example Available Commands

The commands have been cleaned to ensure compatibility across macOS, Windows, and Linux. Examples include:

* `hello`  
* `hey robot`  
* `current time`  
* `tell date`  
* `tell time`  
* `show ip`  
* `memory usage`  
* `disk usage`  
* `cpu usage`  
* `uptime`  
* `logged users`  
* `current user`  
* `cpu info`  
* `available disk space`  
* `tell a joke`  
* `open google`  
* `search wikipedia [topic]`  
* `public ip`  
* `who am i`  
* `list of commands` (to hear all commands)

For the full list, check `utils/commands.py`.

---

## ✅ Requirements

* Python 3.8+ 🐍  
* A valid Gemini API Key 🔐  
* Internet connection for Gemini API and speech recognition 🌐  

---

## 📝 Notes on Compatibility

- Originally designed for macOS 🍏, now also compatible with Windows 🪟 and Linux 🐧.  
- Some macOS-specific commands (like `open app`, `empty trash`, `lock device`, and `screenshot`) have been removed for cross-platform compatibility.  
- The voice engine auto-selects appropriate voices depending on the OS:  
  - macOS voices like Samantha, Karen, Moira  
  - Windows voices like Zira, David  
  - Linux uses the first available voice (usually espeak).  
- On Linux, make sure to install `espeak` and dependencies for `pyttsx3` and `speech_recognition` to work smoothly:  
  ```bash
  sudo apt install espeak portaudio19-dev python3-pyaudio
  ```  
- The assistant uses `pyttsx3` for text-to-speech and `speech_recognition` for capturing voice commands.

---

## 📄 License

This project is free for personal use. Feel free to modify and adapt it as you wish 🛠️.

---


## 🧠 Author

Developed by Matías Henríquez.

---

If you want help adding customized multiplatform commands or improving integration, just ask.
