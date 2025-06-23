import operator
import subprocess
import psutil
import socket
import os
import shutil
import webbrowser
import time
import datetime
import sys
import cpuinfo
import pyjokes
import getpass

from .gemini import query_gemini
from .speaker import speak_text

command_actions = {
    "hey robot": lambda: speak_text("What's up?"),
    "exit": lambda: (speak_text("See you next time!"), sys.exit()),
    "answer a question": lambda query=None: speak_text(query_gemini(query)),
    "what is": lambda query=None: speak_text(query_gemini(query)),
    "list of commands": lambda: speak_text(
        "Available commands are: " + ", ".join(command_actions.keys())
    ),
    "hello": lambda: speak_text("Hello, how can I help you?"),
    "current time": lambda: speak_text(
        f"The current time is {time.strftime('%H:%M:%S', time.localtime())}"
    ),
    "tell date": lambda: speak_text(
        datetime.datetime.now().strftime("Today is %A, %d %B %Y")
    ),
    "tell time": lambda: speak_text(
        datetime.datetime.now().strftime("The time is %H:%M:%S")
    ),
    "show ip": lambda: speak_text(socket.gethostbyname(socket.gethostname())),
    "memory usage": lambda: speak_text(
        f"Memory usage is {psutil.virtual_memory().percent} percent"
    ),
    "disk usage": lambda: speak_text(
        f"Disk usage is {psutil.disk_usage('/').percent} percent"
    ),
    "cpu usage": lambda: speak_text(
        f"Current CPU usage is {psutil.cpu_percent()} percent"
    ),
    "uptime": lambda: subprocess.run(["uptime"]),
    "logged users": lambda: subprocess.run(["who"]),
    "current user": lambda: speak_text(f"Current user is {getpass.getuser()}"),
    "cpu info": lambda: speak_text(f"Your CPU is {cpuinfo.get_cpu_info()['brand_raw']}"),
    "available disk space": lambda: speak_text(
        f"Available space: {shutil.disk_usage('/').free // (2**30)} GB"
    ),
    "tell a joke": lambda: speak_text(pyjokes.get_joke("en")),
    "open google": lambda: webbrowser.open("https://www.google.com"),
    "search wikipedia": lambda query=None: webbrowser.open(
        "https://en.wikipedia.org/wiki/Special:Search?search="
        + query.replace("search wikipedia", "").strip()
    ),
    "public ip": lambda: speak_text(subprocess.getoutput("curl -s ifconfig.me")),
    "who am i": lambda: speak_text(f"You are logged in as {getpass.getuser()}"),
}


def process_voice_command(command_text: str) -> None:
    if "how much is" in command_text:
        try:
            result = evaluate_math_expression(command_text)
            speak_text(f"The result is {result}")
        except Exception:
            speak_text("Error understanding the command")
        return

    for keyword, action in command_actions.items():
        if keyword in command_text:
            if callable(action):
                if keyword in ["answer a question", "what is", "search wikipedia"]:
                    action(command_text)
                else:
                    action()
            return

    if not any(
        trigger in command_text
        for trigger in ["listen to my question", "how much is"]
    ):
        speak_text("Command not recognized")


def evaluate_math_expression(input_text: str) -> float:
    math_operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "times": operator.mul,
        "divided": operator.truediv,
        "/": operator.truediv,
        "to the power of": operator.pow,
        "^": operator.pow,
    }

    input_text = input_text.replace("how much is", "").strip()
    input_text = input_text.replace("to the power of", "power")
    input_text = input_text.replace("divided by", "divided")
    tokens = input_text.split()
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator_word = tokens[i]
        next_number = int(tokens[i + 1])
        result = math_operators[operator_word](result, next_number)

    return result