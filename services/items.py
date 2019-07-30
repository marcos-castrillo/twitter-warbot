import random
from data.items import *
from models.item import Item
from models.item_rarity_probab import Item_Rarity_Probab

def initialize_item_rarity_probab(probab_rarity_1, probab_rarity_2, probab_rarity_3):
    return Item_Rarity_Probab(probab_rarity_1, probab_rarity_2, probab_rarity_3)

def get_item_list(rarity = None):
    list = []
    if rarity != None:
        if rarity == 1:
            raw_list = raw_item_list_1
            if rarity == 1:
                raw_list = raw_item_list_1
                if rarity == 1:
                    raw_list = raw_item_list_1
    else:
        raw_list = raw_item_list
    for i, p in enumerate(raw_item_list):
        list.append(Item(p[0], p[1], p[2]))
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

def get_random_item(item_probab, loot = None):
    action_number = random.randint(1, 100)
    if loot:
        action_number = action_number + 30
        
    if action_number < item_probab.rarity_1_action_number:
        rarity = 1
    elif action_number < item_probab.rarity_2_action_number:
        rarity = 2
    else:
        rarity = 1
    return random.choice(get_item_list(rarity))

def get_random_illness():
    return random.choice(get_illness_list())


def get_random_injury():
    return random.choice(get_injury_list())

def get_random_powerup():
    return random.choice(get_powerup_list())
