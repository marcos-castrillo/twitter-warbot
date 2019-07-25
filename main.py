#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import sys
import datetime

from data.literals import *
from data.constants import *

from models.player import Player
from models.item import Item
from models.tweet_type import Tweet_type

from services.simulation import write_tweet
from services.items import *
from services.battles import *
from services.players import *

item_list = get_item_list()
player_list = get_player_list()
finished = False
hour_count = 0

def start_battle():
    global hour_count, player_list, item_list
    if sum(simulation_probab) != 100:
        sys.exit('Config error: battle probabilities do not sum up 100')
    if sum(item_probab) != 100:
        sys.exit('Config error: item probabilities do not sum up 100')
    if probab_tie + probab_friend_tie > 50:
        sys.exit('Config error: tie probabilities cannot be higher than 50')


    write_tweet(Tweet_type.start, player_list)
    simulate_day()

    while not finished:
        if datetime.datetime.now().hour in sleeping_hours:
            write_tweet(Tweet_type.sleep, player_list, [sleeping_hours[-1] + 1])
        while datetime.datetime.now().hour in sleeping_hours:
            time.sleep(sleeping_interval)

        time.sleep(tweeting_interval)
        simulate_day()

def simulate_day():
    global hour_count, simulation_probab, item_probab
    hour_count = hour_count + 1
    for i, th in enumerate(hour_thresholds):
        if hour_count == th:
            if i == 0:
                simulation_probab = simulation_probab_0
                item_probab = item_probab_0
            if i == 1:
                simulation_probab = simulation_probab_1
                item_probab = item_probab_1
            if i == 2:
                simulation_probab = simulation_probab_2
                item_probab = item_probab_2
            write_tweet(Tweet_type.hour_threshold, player_list, [hour_count])
    action_number = random.randint(1, 100)
    if action_number < simulation_probab[0]:
        pick_item()
    elif action_number < sum(simulation_probab[0:2]):
        battle()
    elif action_number < sum(simulation_probab[0:3]):
        accident()
    elif action_number == sum(simulation_probab[0:4]):
        suicide()
    elif action_number == sum(simulation_probab[0:5]):
        revive()

    if get_alive_players_count(player_list) <= 1:
        end()

def pick_item():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = get_random_player(alive_players)
    item = get_random_item(item_probab)
    player.pick(player_list, item)

def battle():
    alive_players = filter_player_list_by_state(player_list, 1)
    player_1, player_2 = get_two_random_players(alive_players)

    factor_1 = 1 - player_1.get_defense() + player_2.get_attack()
    factor_2 = 100 + player_2.get_defense() - player_1.get_attack()

    if is_friend(player_1, player_2):
        winner_1 = 50 - probab_tie - probab_friend_tie
        winner_2 = 50 + probab_tie + probab_friend_tie
    else:
        winner_1 = 50 - probab_tie
        winner_2 = 50 + probab_tie

    kill_number = random.randint(factor_1, factor_2)

    if kill_number < winner_1:
        kill(player_list, player_1, player_2)
    elif kill_number > winner_2:
        kill(player_list, player_2, player_1)
    elif kill_number == 50:
        run_away(player_list, player_1, player_2)
    else:
        tie(player_list, player_1, player_2)

def accident():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)
    if len(player.item_list) == 0:
        illness(player)
    else:
        action_number = random.randint(0, 100)
        if action_number <= 50:
            injure(player)
        else:
            illness(player)

def illness(player):
    illness = get_random_illness()
    player.injury_list.append(illness)
    write_tweet(Tweet_type.somebody_got_ill, player_list, [player, illness])


def injure(player):
    injury = get_random_injury()
    player.injury_list.append(injury)
    write_tweet(Tweet_type.somebody_got_injured, player_list, [player, injury])

def revive():
    dead_players = filter_player_list_by_state(player_list, 0)
    if len(dead_players) > 0:
        player = random.choice(dead_players)
        player.state = 1
        write_tweet(Tweet_type.somebody_revived, player_list, [player])
    else:
        suicide()

def suicide():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)
    player.state = 0
    write_tweet(Tweet_type.somebody_died, player_list, [player])

def end():
    global finished
    alive_players = filter_player_list_by_state(player_list, 1)
    write_tweet(Tweet_type.final, player_list)
    write_tweet(Tweet_type.final_statistics_1, player_list)
    write_tweet(Tweet_type.final_statistics_2, player_list)
    write_tweet(Tweet_type.final_statistics_3, player_list)
    if len(alive_players) == 1:
        write_tweet(Tweet_type.winner, player_list, [alive_players[0]])
    elif len(alive_players) == 0:
        write_tweet(Tweet_type.nobody_won, player_list)
    finished = True

start_battle()
