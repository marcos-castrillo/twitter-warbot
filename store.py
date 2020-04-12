#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

from data.items import raw_weapon_list, raw_special_list, raw_injury_list, raw_powerup_list
from data.places import raw_place_list
from data.players import raw_player_list
from config import *
from models.item import Item
from models.place import Place
from models.player import Player
from models.item_type import Item_type

def get_item_list():
    list = []

    for i, p in enumerate(raw_weapon_list):
        item = Item()
        item.type = Item_type.weapon
        item.rarity = p[0]
        item.name = p[1]
        item.defense = p[2]
        item.attack = p[3]
        list.append(item)

    for i, p in enumerate(raw_powerup_list):
        item = Item()
        item.type = Item_type.powerup
        item.rarity = p[0]
        item.name = p[1]
        item.defense = p[2]
        item.attack = p[3]
        list.append(item)

    for i, p in enumerate(raw_special_list):
        item = Item()
        item.type = Item_type.special
        item.rarity = 3
        item.name = p[0]
        item.monster_immunity = p[1]
        item.injure_immunity = p[2]
        list.append(item)

    return list

def get_place_list():
    list = []
    item_list_1 = []
    item_list_2 = []
    item_list_3 = []
    item_list = get_item_list()

    def get_items_in_place(item_list_1, item_list_2, item_list_3):
        items = []
        item_count = random.randint(0, MAX_ITEMS)
        item = None

        while item_count > 0:
            action_number = random.randint(1, 100)
            if action_number < PROBAB_RARITY_1:
                if len(item_list_1) > 0:
                    item = random.choice(item_list_1)
                    item_list_1.pop(item_list_1.index(item))
            elif action_number < PROBAB_RARITY_1 + PROBAB_RARITY_2:
                if len(item_list_2) > 0:
                    item = random.choice(item_list_2)
                    item_list_2.pop(item_list_2.index(item))
            else:
                if len(item_list_3) > 0:
                    item = random.choice(item_list_3)
                    item_list_3.pop(item_list_3.index(item))

            if item != None:
                items.append(item)
                item_count = item_count - 1

        return items

    def get_place_by_name(place_list, name):
        place = [p for p in place_list if p.name == name]

        if place:
            return place[0]
        else:
            sys.exit('Config error: there are no places with that name: ' + name)

    def initialize_connections_list(places_list, place):
        connections_list = []
        for i, c in enumerate(place.connections):
            connection = get_place_by_name(places_list, c)
            if connection != None:
                connections_list.append(connection)
        place.connections = connections_list

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

def get_player_list(place_list):
    list = []

    if USE_DISTRICTS and len(raw_player_list) > len(place_list) * MAX_TRIBUTES_PER_DISTRICT:
        sys.exit(u'Config error: player limit exceeded: Players: ' + str(len(raw_player_list)) + u', Locations: ' + str(len(place_list)) + u', Tributes/location: ' + str(MAX_TRIBUTES_PER_DISTRICT))

    for i, p in enumerate(raw_player_list):
        player = Player()
        player.name = p[0]
        player.username = p[1]
        player.gender = p[2]

        if USE_DISTRICTS and p[3] != None:
            district = next(x for x in place_list if x.name == p[3])
            player.district = district  #will override later, just to save p[3]
            district.tributes.append(player)
        else:
            location = random.choice(place_list)
            player.location = location

        #initial items
        initial_items = []
        if len(p) > 4:
            if initial_items != None and (not isinstance(initial_items, list) or len(initial_items) > 2):
                sys.exit('Config error: Item list for player ' + self.name + ' is not an array or contains more than 2 items.')
            for item in p[4]:
                reserved_item = [x for x in item_list if not x.name == item.name]
                initial_items.append(reserved_item)
                item_list.pop(item_list.index(reserved_item))

        player.item_list = initial_items

        list.append(player)
        if not USE_DISTRICTS:
            location.players.append(player)

    if USE_DISTRICTS:
        free_tributes = [x for x in list if x.district == None]
        tributes_per_district = round(len(list) / len(place_list))
        place_list_sorted = sorted(place_list, key=lambda x: len(x.tributes), reverse=True)
        enough_tributes_list = [x for x in place_list_sorted if len(x.tributes) >= tributes_per_district]
        not_enough_tributes_list = [x for x in place_list_sorted if len(x.tributes) < tributes_per_district]

        for j, place in enumerate(enough_tributes_list):
            index = len(place.tributes) - tributes_per_district
            while index > 0:
                player = random.choice(place.tributes)
                free_tributes.append(player)
                place.tributes.remove(player)
                index = index - 1

        while len(free_tributes) > 0:
            place = min(not_enough_tributes_list, key=lambda x: len(x.tributes))
            player = random.choice(free_tributes)
            free_tributes.remove(player)
            place.tributes.append(player)

        for j, place in enumerate(place_list):
            for k, player in enumerate(place.tributes):
                player.district = place
                player.location = place
                place.players.append(player)
    return list

def get_injury_list():
    list = []
    for i, p in enumerate(raw_injury_list):
        item = Item()
        item.type = Item_type.injury
        item.name = p[0]
        item.defense = p[1]
        item.attack = p[2]
        list.append(item)
    return list

def get_player_by_name(name):
    player = [p for p in player_list if p.name == name]
    if player:
        return player[0]
    else:
        return None

def get_two_players_in_random_place():
    list = []
    for i, p in enumerate(place_list):
        if len(p.players) > 1:
            list.append(p)

    while len(list) > 0:
        place = random.choice(list)
        player_1 = None
        player_2 = None

        alive = []
        for i, p in enumerate(place.players):
            if p.state == 1:
                alive.append(p)

        if len(alive) > 1:
            player_1 = random.choice(alive)
            alive.pop(alive.index(player_1))
            player_2 = random.choice(alive)
        else:
            list.pop(list.index(place))

        if player_1 != None and player_2 != None:
            if are_friends(player_1, player_2):
                action_number = random.randint(0, 100)
                if action_number > 50:
                    return None, None, None
            return player_1, player_2, place

    return None, None, None

def are_friends(player, candidate):
    return candidate in player.friend_list

def get_alive_players():
    return [p for p in player_list if p.state == 1]

def get_dead_players():
    return [p for p in player_list if p.state == 0]

def get_alive_players_count():
    count = 0
    for i, p in enumerate(player_list):
        if p.state == 1:
            count = count + 1
    return count

def move_player(player, new_location):
    player.location.players.pop(player.location.players.index(player))
    player.location = new_location
    new_location.players.append(player)
    if player.infected:
        new_location.infected = True

def kill_player(player):
    place = player.location
    player.state = 0
    player.infected = False
    place.items = place.items + player.item_list
    player.item_list = []
    place.players.pop(place.players.index(player))

place_list = get_place_list()
player_list = get_player_list(place_list)
injury_list = get_injury_list()
