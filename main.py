import json

from commands import load_data, start_app

load_data(json.load(open("data.json")))

while True:
    try:
        command = input(">>> ")
    except KeyboardInterrupt:
        exit()
    if command == "exit":
        exit()

    if "open" in command:
        if "chrome" in command:
            start_app("chrome")
