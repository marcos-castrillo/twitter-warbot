#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from data.config import *
from store import player_list, get_alive_players_count

from models.tweet import Tweet
from models.tweet_type import Tweet_type
from models.match_type import Match_type
from models.simulation_probab import Simulation_Probab

from services.simulation import *
from services.items import *
from services.battles import *
from services.players import *
from services.places import *
from services.api import initialize_avatars

simulation_probab = Simulation_Probab(PROBAB_SUICIDE[0], PROBAB_REVIVE[0], PROBAB_TRAP[0], PROBAB_INFECT[0], PROBAB_DESTROY[0], PROBAB_ATRACT[0], PROBAB_MONSTER[0], PROBAB_STEAL[0], PROBAB_MOVE[0], PROBAB_ITEM[0], PROBAB_BATTLE[0])
finished = False
entrance_countdown = LIMIT_TIME_RUMBLE

def initialize():
    initialize_avatars()
    if MATCH_TYPE == Match_type.districts:
        for i, tweet in enumerate(introduction_tweet_list):
            write_tweet(tweet)
    start_battle()

def start_battle():
    if len(player_list) == 0:
        sys.exit('Config error: no players configured.')

    tweet = Tweet()
    tweet.type = Tweet_type.start
    write_tweet(tweet)

    while not finished:
        simulate_day()

def simulate_day():
    global hour_count, simulation_probab, entrance_countdown
    hour_count = hour_count + 1
    for i, th in enumerate(THRESHOLD_LIST):
        if hour_count == th and MATCH_TYPE != Match_type.rumble:
            simulation_probab = Simulation_Probab(PROBAB_SUICIDE[i], PROBAB_REVIVE[i], PROBAB_TRAP[i], PROBAB_INFECT[i], PROBAB_DESTROY[i], PROBAB_ATRACT[i], PROBAB_MONSTER[i], PROBAB_STEAL[i], PROBAB_MOVE[i], PROBAB_ITEM[i], PROBAB_BATTLE[i])
    if MATCH_TYPE == Match_type.rumble:
        if len(get_players_in_place(place_list[0])) < 2 or entrance_countdown == 0:
            entrance_countdown = LIMIT_TIME_RUMBLE
            next_entrance()
            return
        else:
            entrance_countdown = entrance_countdown - 1

    do_something()

    if MATCH_TYPE == Match_type.districts and get_alive_districts_count() <= 1:
        end_districts()
    elif get_alive_players_count() <= 1:
        end()

def do_something():
    completed = False
    action_number = random.randint(1, 100)

    if action_number < simulation_probab.suicide_action_number:
        completed = suicide()
    elif action_number < simulation_probab.revive_action_number:
        completed = revive()
    elif action_number < simulation_probab.trap_action_number:
        completed = trap()
    elif action_number < simulation_probab.infect_action_number:
        completed = infect()
    elif action_number < simulation_probab.destroy_action_number:
        completed = destroy()
    elif action_number < simulation_probab.atract_action_number:
        completed = atract()
    elif action_number < simulation_probab.monster_action_number:
        completed = monster()
    elif action_number < simulation_probab.steal_action_number:
        completed = steal()
    elif action_number < simulation_probab.move_action_number:
        completed = move()
    elif action_number < simulation_probab.item_action_number:
        completed = pick_item()
    elif action_number < simulation_probab.battle_action_number:
        completed = battle()

    if not completed:
         do_something()

def end():
    global finished
    alive_players = get_alive_players()
    if len(alive_players) == 1:
        player = alive_players[0]
        tweet = Tweet()
        tweet.type = Tweet_type.winner
        tweet.place = player.location
        tweet.player = player
        write_tweet(tweet)
    elif len(alive_players) == 0:
        tweet = Tweet()
        tweet.type = Tweet_type.nobody_won
        write_tweet(tweet)
    finished = True

def end_districts():
    global finished
    alive_players = get_alive_players()
    tweet = Tweet()
    tweet.type = Tweet_type.winner_districts
    tweet.player_list = [x for x in player_list if x.district.name == alive_players[0].district.name and x.state == 1]
    tweet.place = alive_players[0].district
    write_tweet(tweet)
    finished = True

initialize()
