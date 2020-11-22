import json
from types import SimpleNamespace


def get_config():
    with open('data/config.json', 'r', encoding="utf-8") as configFile:
        data = configFile.read()
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


config = get_config()
