#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

from data.config import MAX_ITEMS, PROBAB_RARITY_1, PROBAB_RARITY_2, PROBAB_RARITY_3
from data.places import raw_place_list
from models.place import Place
from services.items import get_item_list

def get_place_list():
    list = []
    item_list_1 = []
    item_list_2 = []
    item_list_3 = []
    item_list = get_item_list()

    for i, item in enumerate(item_list):
        if item.rarity == 1:
            item_list_1.append(item)
        if item.rarity == 2:
            item_list_2.append(item)
        if item.rarity == 3:
            item_list_3.append(item)
    for i, p in enumerate(raw_place_list):
        if len(p) == 3:
            p.append(None)

        items = get_items_in_place(item_list_1, item_list_2, item_list_3)
        place = Place(p[0], p[1], p[2], items, p[3])
        list.append(place)

    for i, p in enumerate(list):
        initialize_connections_list(list, p)

    for i, p in enumerate(list):
        if len(p.connections) == 0:
            sys.exit('Config error: place without connections: ' + p.name)

    return list

def initialize_connections_list(places_list, place):
    connections_list = []
    for i, c in enumerate(place.connections):
        connection = get_place_by_name(places_list, c)
        if connection != None:
            connections_list.append(connection)
    place.connections = connections_list

def get_place_by_name(place_list, name):
    place = [p for p in place_list if p.name == name]

    if place:
        return place[0]
    else:
        sys.exit('Config error: there are no places with that name: ' + name)

def move_player(player, new_location):
    player.location.players.pop(player.location.players.index(player))
    player.location = new_location
    new_location.players.append(player)

def get_items_in_place(item_list_1, item_list_2, item_list_3):
    items = []
    item_count = random.randint(0, MAX_ITEMS)

    while item_count > 0:
        action_number = random.randint(1, 100)
        print(len(item_list_1),len(item_list_2),len(item_list_3))
        if action_number < PROBAB_RARITY_1:
            item = random.choice(item_list_1)
            item_list_1.pop(item_list_1.index(item))
        elif action_number < PROBAB_RARITY_1 + PROBAB_RARITY_2:
            item = random.choice(item_list_2)
            item_list_2.pop(item_list_2.index(item))
        else:
            item = random.choice(item_list_3)
            item_list_3.pop(item_list_3.index(item))

        items.append(item)
        item_count = item_count - 1

    return items
