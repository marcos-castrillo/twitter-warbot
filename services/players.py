import random
from data.players import raw_player_list
from models.player import Player

def get_player_list(place_list):
    list = []
    for i, p in enumerate(raw_player_list):
        location = random.choice(place_list)
        for i, pl in enumerate(place_list):
            if pl.name == p[3]:
                p[3] = pl
        player = Player(p[0], location, p[2], p[1], p[3])
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

def get_two_players_in_random_place(player_list, place_list):
    list = []
    for i, p in enumerate(place_list):
        if len(p.players) > 1:
            list.append(p)

    if len(list) > 0:
        place = random.choice(list)
        player_1 = random.choice(place.players)
        player_2 = random.choice(place.players)
        while player_2 == player_1:
            player_2 = random.choice(place.players)
        return player_1, player_2
    else:
        return None, None

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
