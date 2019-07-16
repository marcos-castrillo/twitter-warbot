import random
from data_players import raw_player_list
from model_player import Player

def get_player_list():
    list = []
    for i, p in enumerate(raw_player_list):
        player = Player(p[0], p[1], p[2])
        list.append(player)

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

def get_random_player(player_list):
    player = random.choice(player_list)
    return player

def get_two_random_players(player_list):
    player1 = get_random_player(player_list)
    player2 = get_random_player(player_list)
    while player2 == player1:
        player2 = get_random_player(player_list)

    return player1, player2

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
