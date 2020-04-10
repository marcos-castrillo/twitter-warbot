import random
import sys
from data.players import raw_player_list
from models.player import Player

def get_player_list(place_list):
    list = []
    for i, p in enumerate(raw_player_list):
        location = random.choice(place_list)
        initial_items = None
        if len(p) > 4:
            initial_items = p[4]

        player = Player(p[0], location, p[2], p[1], initial_items)
        list.append(player)
        location.players.append(player)

    for i, p in enumerate(list):
        initialize_friend_list(list, p)

    return list

def initialize_friend_list(player_list, player):
    friend_list = []
    for i, f in enumerate(player.friend_list):
        friend = get_player_by_name(player_list, f)
        if friend != None:
            friend_list.append(friend)
    player.friend_list = friend_list

def get_player_by_name(player_list, name):
    player = [p for p in player_list if p.name == name]
    if player:
        return player[0]
    else:
        return None

def get_two_players_in_random_place(place_list):
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
            if is_friend(player_1, player_2):
                action_number = random.randint(0, 100)
                if action_number > 50:
                    return None, None, None
            return player_1, player_2, place

    return None, None, None

def filter_player_list_by_state(player_list, value):
    list = []
    for i, p in enumerate(player_list):
        if p.state == value:
            list.append(p)
    return list

def get_alive_players_count(player_list):
    count = 0
    for i, p in enumerate(player_list):
        if p.state == 1:
            count = count + 1
    return count

def friend(player_1, player_2):
    if not player_2 in player_1.friend_list:
        player_1.friend_list.append(player_2)
    if not player_1 in player_2.friend_list:
        player_2.friend_list.append(player_1)

def is_friend(player, candidate):
    if candidate in player.friend_list:
        return True
    else:
        return False
