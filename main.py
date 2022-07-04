import json
import os
import webbrowser

from commands import load_data, start_app

load_data(json.load(open("data.json")))


while True:
    try:
        command = input(">>> ")
    except KeyboardInterrupt:
        exit()
    if command == "exit":
        exit()
    if command == "cls":
        os.system("cls")
    if command == "whoami":
        print(os.getlogin())
    if command == "shutdown":
        if input("are you sure?(y/n) ") == "y":
            os.system("shutdown -s -t 0")

    if "open" in command:
        if "chrome" in command: start_app("chrome")
        if "vscode" in command: start_app("vscode")
        if "cmd" in command: start_app("cmd")
        if "notion" in command: start_app("notion")

    if "search" in command:
        query = command.replace("search", "")
        os.system(f"start https://www.google.com/search?q={query.replace(' ', '+')}")
