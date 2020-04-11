import random
from data.items import *
from models.item import Item

def get_item_list():
    list = []

    for i, p in enumerate(raw_item_list):
        list.append(Item(p[1], p[2], p[3], p[0]))
    return list

def get_illness_list():
    list = []
    for i, p in enumerate(raw_illness_list):
        list.append(Item(p[0], p[1], p[2]))
    return list

def get_injury_list():
    list = []
    for i, p in enumerate(raw_injury_list):
        list.append(Item(p[0], p[1], p[2]))
    return list

def get_powerup_list():
    list = []
    for i, p in enumerate(raw_powerup_list):
        list.append(Item(p[0], p[1], p[2]))
    return list

def get_random_illness():
    return random.choice(get_illness_list())


def get_random_injury():
    return random.choice(get_injury_list())

def get_random_powerup():
    return random.choice(get_powerup_list())
