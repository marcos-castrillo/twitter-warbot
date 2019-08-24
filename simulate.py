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

from services.simulation import *
from services.items import *
from services.battles import *
from services.players import *
from services.places import *

item_list = get_item_list()
place_list = get_place_list()
player_list = get_player_list(place_list)
initialize_avatars(player_list)
simulation_probab = initialize_simulation_probabs(probab_item, probab_move, probab_battle, probab_destroy, probab_trap, probab_suicide, probab_revive)
item_rarity_probab = initialize_item_rarity_probab(probab_rarity_1, probab_rarity_2, probab_rarity_3)
finished = False
hour_count = 0

def start_battle():
    global hour_count, player_list, item_list
    if probab_tie + probab_friend_tie > 50:
        sys.exit('Config error: tie probabilities cannot be higher than 50.')
    if len(player_list) > max_players:
        sys.exit('Config error: player limit exceeded.')

    write_tweet(Tweet_type.start, player_list, place_list)

    while not finished:
        simulate_day()

def simulate_day():
    global hour_count, simulation_probab, item_rarity_probab
    hour_count = hour_count + 1
    for i, th in enumerate(hour_thresholds):
        if hour_count == th:
            simulation_probab.increase(i)
            item_rarity_probab.increase(i)
            write_tweet(Tweet_type.hour_threshold, player_list, place_list, None, [hour_count])

    action_number = random.randint(1, 100)

    if action_number < simulation_probab.item_action_number:
        pick_item()
    elif action_number < simulation_probab.move_action_number:
        move()
    elif action_number < simulation_probab.battle_action_number:
        battle()
    elif action_number < simulation_probab.destroy_action_number:
        destroy()
    elif action_number < simulation_probab.trap_action_number:
        trap()
    elif action_number == simulation_probab.suicide_action_number:
        suicide()
    elif action_number == simulation_probab.revive_action_number:
        revive()

    if get_alive_players_count(player_list) <= 1:
        end()

def pick_item():
    action_number = random.randint(1, 100)

    if action_number > 70:
        monster()
    else:
        alive_players = filter_player_list_by_state(player_list, 1)
        player = random.choice(alive_players)

        better_loot = player.location.loot or player.location == player.fav_place
        item = get_random_item(item_rarity_probab, better_loot)
        player.pick(player_list, place_list, item)

def monster():
    place = None
    for i, p in enumerate(place_list):
        if p.monster:
            place = p

    if place != None:
        action_number = random.randint(1, 100)

        if action_number > 20 and len(place.players) > 0:
            player = random.choice(place.players)
            player.state = 0
            place.players.pop(place.players.index(player))
            write_tweet(Tweet_type.monster_killed, player_list, place_list, place, [player, place])
        else:
            place.monster = False

            loc_candidates = []
            for i, l in enumerate(place.connections):
                if not l.destroyed:
                    loc_candidates.append(l)

            if len(loc_candidates) > 0:
                new_place = random.choice(loc_candidates)
                new_place.monster = True
                write_tweet(Tweet_type.monster_moved, player_list, place_list, new_place, [place, new_place])
            else:
                write_tweet(Tweet_type.monster_dissappeared, player_list, place_list, place, [place])
    else:
        loc_candidates = []

        for i, p in enumerate(place_list):
            if not p.destroyed:
                loc_candidates.append(p)

        new_place = random.choice(loc_candidates)
        new_place.monster = True

        write_tweet(Tweet_type.monster_appeared, player_list, place_list, new_place, [new_place])

def move():
    global place_list

    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)

    loc_candidates = []
    for i, l in enumerate(player.location.connections):
        if not l.destroyed:
            loc_candidates.append(l)

    if len(loc_candidates) == 0:
        player.state = 0
        player.location.players.pop(player.location.players.index(player))

        write_tweet(Tweet_type.somebody_couldnt_move, player_list, place_list, player.location, [player])
        return

    new_location = random.choice(loc_candidates)
    action_number = random.randint(1, 100)

    if new_location.trap_by != None and new_location.trap_by != player:
        if action_number < 75:
            player.state = 0

            trapped_by = new_location.trap_by
            new_location.trap_by.kills = new_location.trap_by.kills + 1
            new_location.trap_by = None
            player.location.players.pop(player.location.players.index(player))
            new_location.players.append(player)
            player.location = new_location

            write_tweet(Tweet_type.trapped, player_list, place_list, player.location, [player, trapped_by, new_location])
        else:
            trapped_by = new_location.trap_by
            new_location.trap_by = None

            player.location.players.pop(player.location.players.index(player))
            new_location.players.append(player)
            player.location = new_location

            write_tweet(Tweet_type.dodged_trap, player_list, place_list, player.location, [player, trapped_by, new_location])

    else:
        old_location = player.location
        player.location.players.pop(player.location.players.index(player))

        new_location.players.append(player)
        player.location = new_location

        if action_number < 25:
            accident_or_powerup(player)
        else:
            write_tweet(Tweet_type.somebody_moved, player_list, place_list, player.location, [player, old_location, player.location])

def battle():
    alive_players = filter_player_list_by_state(player_list, 1)
    player_1, player_2 = get_two_players_in_random_place(place_list)

    if (player_1, player_2) == (None, None):
        move()
        return


    factor_1 = 1 - player_1.get_defense() + player_2.get_attack()
    factor_2 = 100 + player_2.get_defense() - player_1.get_attack()

    if player_1.location == player_1.fav_place:
        factor_1 = factor_1 + 10

    if player_2.location == player_2.fav_place:
        factor_2 = factor_2 + 10

    if is_friend(player_1, player_2):
        winner_1 = 50 - probab_tie - probab_friend_tie
        winner_2 = 50 + probab_tie + probab_friend_tie
    else:
        winner_1 = 50 - probab_tie
        winner_2 = 50 + probab_tie

    kill_number = random.randint(factor_1, factor_2)

    if kill_number == int((factor_2 - factor_1) / 2):
        run_away(player_list, place_list, player_1, player_2)
    elif kill_number <= int((factor_2 - factor_1) / 2) + 2 and kill_number >= int((factor_2 - factor_1) / 2) - 2 and (len(player_1.item_list) > 0 or len(player_2.item_list) > 0):
        steal(player_list, place_list, player_1, player_2)
    elif kill_number < winner_1:
        kill(player_list, place_list, player_1, player_2)
    elif kill_number > winner_2:
        kill(player_list, place_list, player_2, player_1)
    else:
        tie(player_list, place_list, player_1, player_2)

def destroy():
    connected_list = []
    list = []
    for i, p in enumerate(place_list):
        append = False
        if not p.destroyed:
            list.append(p)
            for j, q in enumerate(p.connections):
                if q.destroyed:
                    append = True
            if append:
                connected_list.append(p)

    if len(connected_list) == 0:
        place = random.choice(list)
    else:
        place = random.choice(connected_list)

    place.destroyed = True
    dead_list = []

    for i, p in enumerate(place.players):
        if p.state == 1:
            p.state = 0
            dead_list.append(p)

    for i, p in enumerate(place.players):
        for j, q in enumerate(dead_list):
            if p == q:
                p.location.players.pop(p.location.players.index(p))

    if place.monster:
        place.monster = None

    write_tweet(Tweet_type.destroyed, player_list, place_list, place, [place, dead_list])

def trap():
    list = []
    for i, p in enumerate(place_list):
        if p.trap_by == None and len(p.players) > 0:
            any_alive = False
            for j, q in enumerate(p.players):
                if q.state == 1:
                    any_alive = True
            if any_alive:
                list.append(p)

    if len(list) > 0:
        candidates_list = []
        while len(candidates_list) == 0:
            place = random.choice(list)
            for i, p in enumerate(place.players):
                if p.state == 1:
                    candidates_list.append(p)

        player = random.choice(candidates_list)

        place.trap_by = player
        write_tweet(Tweet_type.trap, player_list, place_list, place, [player, place])
    else:
        move()

def accident_or_powerup(player):
    action_number = random.randint(0, 100)

    if action_number > 75:
        powerup(player)
    elif action_number > 50:
        injure(player)
    else:
        illness(player)

def illness(player):
    illness = get_random_illness()
    player.injury_list.append(illness)
    write_tweet(Tweet_type.somebody_got_ill, player_list, place_list, player.location, [player, illness])

def injure(player):
    injury = get_random_injury()
    player.injury_list.append(injury)
    write_tweet(Tweet_type.somebody_got_injured, player_list, place_list, player.location, [player, injury])

def powerup(player):
    powerup = get_random_powerup()
    player.powerup_list.append(powerup)
    write_tweet(Tweet_type.somebody_powerup, player_list, place_list, player.location, [player, powerup])

def revive():
    dead_players = filter_player_list_by_state(player_list, 0)
    if len(dead_players) > 0:
        player = random.choice(dead_players)
        player.state = 1

        place = player.location
        while place.destroyed:
            place = random.choice(place_list)
        player.location = place
        place.players.append(player)
        write_tweet(Tweet_type.somebody_revived, player_list, place_list, player.location, [player])
    else:
        suicide()

def suicide():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)
    player.state = 0
    player.location.players.pop(player.location.players.index(player))

    write_tweet(Tweet_type.somebody_died, player_list, place_list, player.location, [player])

def end():
    global finished
    alive_players = filter_player_list_by_state(player_list, 1)
    if len(alive_players) == 1:
        write_tweet(Tweet_type.winner, player_list, place_list, alive_players[0].location, [alive_players[0]])
    elif len(alive_players) == 0:
        write_tweet(Tweet_type.nobody_won, player_list, place_list)
    finished = True

start_battle()
