import random
from data_items import raw_item_list, raw_item_list_1, raw_item_list_2, raw_item_list_3
from model_item import Item

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

def get_random_item(item_probab):
    action_number = random.randint(1, 100)
    if action_number < item_probab[0]:
        rarity = 1
    elif action_number < sum(item_probab[0:2]):
        rarity = 2
    elif action_number <= sum(item_probab[0:3]):
        rarity = 1
    return random.choice(get_item_list(rarity))
