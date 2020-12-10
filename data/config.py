import json
from types import SimpleNamespace
import os

current_dir = os.path.abspath(os.path.dirname(__file__))


def get_json(filename) -> object:
    with open(os.path.join(current_dir, filename + '.json'), 'r', encoding="utf-8") as file:
        data = file.read()
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


def get_config():
    class Object(object):
        pass

    new_config = Object()
    new_config = get_json('config')
    new_config.injury_list = get_json(new_config.general.language + '/injury_list')
    new_config.literals = get_json(new_config.general.language + '/literals')
    new_config.place_list = get_json(new_config.general.language + '/place_list')
    new_config.powerup_list = get_json(new_config.general.language + '/powerup_list')
    new_config.special_list = get_json(new_config.general.language + '/special_list')
    new_config.weapon_list = get_json(new_config.general.language + '/weapon_list')
    return new_config


config = get_config()
