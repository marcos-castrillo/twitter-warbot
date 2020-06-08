#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

from data.items import raw_weapon_list, raw_special_list, raw_injury_list, raw_powerup_list
from data.places import raw_place_list
from data.players import raw_player_list
from data.config import *

from models.item import Item
from models.place import Place
from models.tweet import Tweet
from models.player import Player
from models.item_type import Item_type
from models.tweet_type import Tweet_type
from models.match_type import Match_type

def get_item_list():
    item_list = []

    for i, p in enumerate(raw_weapon_list):
        item = Item()
        item.type = Item_type.weapon
        item.name = p[0]
        item.defense = p[1]
        item.attack = p[2]
        item_list.append(item)

    for i, p in enumerate(raw_special_list):
        item = Item()
        item.type = Item_type.special
        item.name = p[0]
        item.monster_immunity = p[1]
        item.injure_immunity = p[2]
        item.infection_immunity = p[3]
        item_list.append(item)

    return item_list

def get_powerup_list():
    powerup_list = []
    for i, p in enumerate(raw_powerup_list):
        item = Item()
        item.type = Item_type.powerup
        item.name = p[0]
        item.defense = p[1]
        item.attack = p[2]
        powerup_list.append(item)
    return powerup_list

def get_place_list():
    place_list = []
    item_list_1 = []
    item_list_2 = []
    item_list_3 = []
    item_list = get_item_list()

    def get_items_in_place(item_list_1, item_list_2, item_list_3):
        items = []
        item_count = random.randint(MIN_ITEMS, MAX_ITEMS)
        item = None

        while item_count > 0 and len(item_list_1) + len(item_list_2) + len(item_list_3) > 0:
            action_number = random.randint(1, 100)
            item = None

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
        road_connections_list = []
        water_connections_list = []

        for i, c in enumerate(place.connections):
            connection = get_place_by_name(places_list, c)
            if connection != None:
                connections_list.append(connection)
        for i, c in enumerate(place.road_connections):
            connection = get_place_by_name(places_list, c)
            if connection != None:
                road_connections_list.append(connection)
        for i, c in enumerate(place.water_connections):
            connection = get_place_by_name(places_list, c)
            if connection != None:
                water_connections_list.append(connection)
        place.connections = connections_list
        place.road_connections = road_connections_list
        place.water_connections = water_connections_list

    for i, item in enumerate(item_list):
        if item.get_rarity() == 1:
            item_list_1.append(item)
        elif item.get_rarity() == 2:
            item_list_2.append(item)
        elif item.get_rarity() == 3:
            item_list_3.append(item)
        random.shuffle(raw_place_list)

    for i, p in enumerate(raw_place_list):
        if len(p) == 3:
            p.append(None)
        if len(p) == 4:
            p.append([])
        items = get_items_in_place(item_list_1, item_list_2, item_list_3)
        name = p[0]
        road_connections = p[1]
        coordinates = p[2]
        district_display_name = p[3]
        water_connections = p[4]

        place = Place(name, road_connections, coordinates, items, district_display_name, water_connections)
        place_list.append(place)

    spare_item_list = item_list_1 + item_list_2 + item_list_3

    for i, p in enumerate(place_list):
        initialize_connections_list(place_list, p)

    for i, p in enumerate(place_list):
        if len(place_list) > 1 and len(p.connections) == 0:
            sys.exit('Config error: place without connections: ' + p.name)
        for j, connection in enumerate(p.connections):
            if not any(subconnection.name == p.name for subconnection in connection.connections):
                sys.exit('Config error: ' + p.name + ' is not mutually connected to other place')

    return place_list

def initialize_tributes():
    global player_list
    tweet_list = []

    if REDISTRIBUTE_TRIBUTES:
        #Initialize and distribute the tributes per district
        free_tributes = [x for x in player_list if x.district == None]
        tributes_per_district = round(len(player_list) / len(place_list))
        place_list_sorted = sorted(place_list, key=lambda x: len(x.tributes), reverse=True)
        enough_tributes_list = [x for x in place_list_sorted if len(x.tributes) >= tributes_per_district]
        not_enough_tributes_list = [x for x in place_list_sorted if len(x.tributes) < tributes_per_district]

        #Districts with enough tributes
        for j, enough_tributes_district in enumerate(enough_tributes_list):
            exported_tributes = []

            index = len(enough_tributes_district.tributes) - tributes_per_district
            while index > 0:
                excess_tribute = random.choice(enough_tributes_district.tributes)
                free_tributes.append(excess_tribute)
                exported_tributes.append(excess_tribute)
                enough_tributes_district.tributes.remove(excess_tribute)
                index = index - 1

            tweet = Tweet()
            tweet.type = Tweet_type.introduce_players
            tweet.place = enough_tributes_district
            tweet.player_list = enough_tributes_district.tributes
            tweet.player_list_2 = exported_tributes
            tweet_list.append(tweet)

        #Districts with not enough tributes
        index = tributes_per_district

        while index > 0:
            for j, not_enough_tributes_district in enumerate(not_enough_tributes_list):
                if len(not_enough_tributes_district.tributes) < tributes_per_district and len(free_tributes) > 0:
                    chosen_tribute = random.choice(free_tributes)
                    free_tributes.remove(chosen_tribute)
                    chosen_tribute.location = not_enough_tributes_district
                    not_enough_tributes_district.tributes.append(chosen_tribute)
            index = index - 1

        for j, not_enough_tributes_district in enumerate(not_enough_tributes_list):

            imported_tributes = [x for x in not_enough_tributes_district.tributes if (x.district == None or x.district.name != not_enough_tributes_district.name)]
            local_tributes = [x for x in not_enough_tributes_district.tributes if x.district != None and x.district.name == not_enough_tributes_district.name]

            for j, imported in enumerate(imported_tributes):
                imported.district = not_enough_tributes_district

            tweet = Tweet()
            tweet.type = Tweet_type.introduce_players
            tweet.place = not_enough_tributes_district
            tweet.player_list = local_tributes
            tweet.player_list_2 = imported_tributes
            tweet.inverse = True
            tweet_list.append(tweet)
    else:
        place_list_sorted = sorted(place_list, key=lambda x: len(x.tributes))
        district_list = [x for x in place_list_sorted if len(x.tributes) > 0]
        for i,district in enumerate(district_list):
            tweet = Tweet()
            tweet.type = Tweet_type.introduce_players
            tweet.place = district
            tweet.player_list = district.tributes
            tweet_list.append(tweet)
    #Friends list
    for j, place in enumerate(place_list):
        for k, tribute in enumerate(place.tributes):
            tribute.district = place
            tribute.location = place
            place.players.append(tribute)
            tribute.friend_list = tribute.friend_list + [x for x in place.tributes if x.name != tribute.name]
    return tweet_list

def get_player_list(place_list):
    player_list = []

    if MAX_TRIBUTES_PER_DISTRICT > 0 and MATCH_TYPE == Match_type.districts and len(raw_player_list) > len(place_list) * MAX_TRIBUTES_PER_DISTRICT:
        sys.exit(u'Config error: player limit exceeded: Players: ' + str(len(raw_player_list)) + u', Locations: ' + str(len(place_list)) + u', Tributes/location: ' + str(MAX_TRIBUTES_PER_DISTRICT))

    for i, p in enumerate(raw_player_list):
        # Name, username, gender, place, weapon_list
        player = Player()
        player.name = p[0]
        player.username = p[1]
        player.gender = p[2]

        #initial items
        initial_items = []
        if len(p) > 4:
            for item_name in p[4]:
                reserved_item = [x for x in powerup_list if x.name == item_name]
                if len(reserved_item) == 0:
                    sys.exit('Config error: Reserved item doesnt exist: ' + item_name)

                initial_items.append(reserved_item[0])
                powerup_list.pop(powerup_list.index(reserved_item[0]))
        player.powerup_list = initial_items

        player_list.append(player)

        if MATCH_TYPE == Match_type.districts and p[3] != None and p[3] != '':
            try:
                location = next(x for x in place_list if x.name == p[3])
            except:
                sys.exit('Config error: no place called ' + p[3])
            player.district = location #only to store p[3]
            location.tributes.append(player) #idem
        elif MATCH_TYPE == Match_type.standard:
            location = random.choice(place_list)
            player.location = location
            location.players.append(player)

    return player_list

def get_injury_list():
    injury_list = []
    for i, p in enumerate(raw_injury_list):
        item = Item()
        item.type = Item_type.injury
        item.name = p[0]
        item.defense = p[1]
        item.attack = p[2]
        injury_list.append(item)
    return injury_list

def get_player_by_name(name):
    return next(p for p in player_list if p.name == name)

def get_two_players_in_random_place():
    candidates_list = [x for x in place_list if len(x.players) > 1]

    while len(candidates_list) > 0:
        place = random.choice(candidates_list)
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
            candidates_list.pop(candidates_list.index(place))

        if player_1 != None and player_2 != None:
            if are_friends(player_1, player_2):
                action_number = random.randint(0, 100)
                if action_number > 50:
                    return None, None, None
            return player_1, player_2, place

    return None, None, None

def are_friends(player, candidate):
    return any(x for x in player.friend_list if x.get_name() == candidate.get_name()) and any(x for x in candidate.friend_list if x.get_name() == player.get_name())

def get_alive_players():
    return [p for p in player_list if p.state == 1]

def get_dead_players():
    return [p for p in player_list if p.state == 0]

def get_alive_players_count():
    return len([x for x in player_list if x.state == 1])

def get_alive_districts_count():
    return len([x for x in place_list if not x.destroyed and len([y for y in x.tributes if y.state == 1]) > 0])

def move_player(player, new_location):
    if player.location != None:
        player.location.players.pop(player.location.players.index(player))
    player.location = new_location
    new_location.players.append(player)

    players_in_place = [x for x in new_location.players if x.state == 1]
    if player.infected:
        for j, p in enumerate(players_in_place):
            if not p.infection_immunity:
                p.infected = True
    elif any(x for x in players_in_place if x.infected) and not player.infection_immunity:
        player.infected = True

def destroy_district_if_needed(district):
    if any(x for x in district.tributes if x.state == 1):
        return None

    district.destroyed = True
    district.monster = False
    district.trap_by = None
    tributes_list = district.tributes
    escaped_list = []
    route_list = []
    new_location = False

    for j, c in enumerate(district.connections):
        if not c.destroyed:
            route_list.append(c)

    if len(route_list) == 0:
        for j, c in enumerate(district.connections):
            for k, sc in enumerate(c.connections):
                if not sc.destroyed and sc.name != district.name:
                    route_list.append(sc)

    if len(route_list) == 0:
        for j, c in enumerate(district.connections):
            for k, sc in enumerate(c.connections):
                for l, ssc in enumerate(sc.connections):
                    if not ssc.destroyed and ssc.name != district.name:
                        route_list.append(ssc)

    if len(route_list) == 0:
        for j, c in enumerate(district.connections):
            for k, sc in enumerate(c.connections):
                for l, ssc in enumerate(sc.connections):
                    for m, sssc in enumerate(ssc.connections):
                        if not sssc.destroyed and sssc.name != district.name:
                            route_list.append(sssc)

    if len(route_list) == 0:
        new_location = random.choice([x for x in place_list if not x.destroyed and x.name != district.name])
    else:
        new_location = random.choice(route_list)

    for i, p in enumerate(district.players):
        if p.state == 1:
            escaped_list.append(p)

    any_infected = False
    any_healthy = False

    for i, p in enumerate(escaped_list + new_location.players):
        if p.infected:
            any_infected = True
        else:
            any_healthy = True
        move_player(p, new_location)

    tweet = Tweet()
    tweet.type = Tweet_type.destroyed_district
    tweet.place = district
    tweet.place_2 = new_location
    tweet.player_list = tributes_list
    tweet.player_list_2 = escaped_list
    if any_infected and any_healthy:
        tweet.there_was_infection = True
    return tweet

def kill_player(player):
    place = player.location

    for i, item in enumerate(player.item_list):
        item.thrown_away_by = player

    place.items = place.items + player.item_list
    place.players.pop(place.players.index(player))
    player.state = 0
    player.attack = 0
    player.defense = 0
    player.item_list = []
    player.injury_list = []
    player.powerup_list = []
    player.infected = False
    player.monster_immunity = False
    player.injure_immunity = False
    player.infection_immunity = False

def who_infected_who(player, list_of_players):
    any_infected = False
    any_healthy = False
    was_infected = False
    for i, p in enumerate(list_of_players):
        if p.infected:
            any_infected = True
        else:
            any_healthy = True
    if player.infected:
        was_infected = True
        any_infected = True
    else:
        any_healthy = True

    there_was_infection = any_infected and any_healthy
    infected_or_was_infected_by = there_was_infection and was_infected
    return there_was_infection, infected_or_was_infected_by

def get_players_in_place(place):
    alive_players = get_alive_players()
    players_in_place = [x for x in alive_players if x.location != None and x.location.name == place.name]
    return players_in_place

place_list = get_place_list()
powerup_list = get_powerup_list()
player_list = get_player_list(place_list)
if MATCH_TYPE == Match_type.districts:
    introduction_tweet_list = initialize_tributes()
injury_list = get_injury_list()
hour_count = 0
