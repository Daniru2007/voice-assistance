import os
"""
TODO Open Most common apps ✔
Chrome ✔
Vscode
CMD
Notion
"""


data = {}


def load_data(dt):
    global data
    data = dt


def start_app(name):
    os.startfile(data["apps"][name])


