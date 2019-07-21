#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from service_battles import *
# from service_items import *

# def update_player_list(player_list, item_list):
    # give_item(player_list, item_list, player_name, item_name)
    # give_death(player_list, killer_name, killed_name)
    # get_player(player_list, player_name).injury_list.append(get_illness(illness_name))
    # friend(get_player(player_list, player_1), get_player(player_list, player_2))
    # get_player(player_list, player_name).state = 1

# def update_hour_count(hour_count):
#     return new_hour_count
#
# def get_item(item_list, item_name):
#     for index, item in enumerate(item_list):
#         if item.name == item_name:
#             return item
#     raise ValueError('A very specific bad thing happened.')
#
# def get_player(player_list, player_name):
#     for index, player in enumerate(player_list):
#         if player.name == player_name:
#             return player
#     raise ValueError('A very specific bad thing happened.')
#
# def get_illness(illness_name):
#     for index, illness in enumerate(get_illness_list()):
#         if illness.name == illness_name:
#             return illness
#     raise ValueError('A very specific bad thing happened.')
#
# def give_item(player_list, item_list, player_name, item_name):
#     get_player(player_list, player_name).item_list.append(get_item(item_list, item_name))
#
# def give_death(player_list, killer_name, killed_name):
#     get_player(player_list, killed_name).state = 0
#     get_player(player_list, killer_name).kills = get_player(player_list, killer_name).kills + 1
