import json
from types import SimpleNamespace
import os

current_dir = os.path.abspath(os.path.dirname(__file__))


def get_config():
    with open(current_dir + '/../data/config.json', 'r', encoding="utf-8") as configFile:
        data = configFile.read()
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


config = get_config()
