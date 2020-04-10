#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import datetime

from data.literals import *
from data.config import *

from models.player import Player
from models.item import Item
from models.tweet_type import Tweet_type
from models.item_rarity_probab import Item_Rarity_Probab
from models.simulation_probab import Simulation_Probab

from services.simulation import *
from services.items import *
from services.battles import *
from services.players import *
from services.places import *

item_list = get_item_list()
place_list = get_place_list()
player_list = get_player_list(place_list)
initialize_avatars(player_list)
simulation_probab = Simulation_Probab(PROBAB_ITEM[0], PROBAB_MOVE[0], PROBAB_BATTLE[0], PROBAB_AOP[0], PROBAB_STEAL[0], PROBAB_MONSTER[0], PROBAB_DESTROY[0], PROBAB_TRAP[0], PROBAB_INFECT[0], PROBAB_ATRACT[0], PROBAB_SUICIDE[0], PROBAB_REVIVE[0])
item_rarity_probab = Item_Rarity_Probab(PROBAB_RARITY_1[0], PROBAB_RARITY_2[0], PROBAB_RARITY_3[0])
finished = False
hour_count = 0

def start_battle():
    global hour_count, player_list, item_list
    if len(player_list) > MAX_PLAYERS:
        sys.exit('Config error: player limit exceeded.')

    write_tweet(Tweet_type.start, player_list, place_list)

    while not finished:
        simulate_day()

def simulate_day():
    global hour_count, simulation_probab, item_rarity_probab
    hour_count = hour_count + 1
    for i, th in enumerate(THRESHOLD_LIST):
        if hour_count == th:
            simulation_probab = Simulation_Probab(PROBAB_ITEM[i], PROBAB_MOVE[i], PROBAB_BATTLE[i], PROBAB_AOP[i], PROBAB_STEAL[i], PROBAB_MONSTER[i], PROBAB_DESTROY[i], PROBAB_TRAP[i], PROBAB_INFECT[i], PROBAB_ATRACT[i], PROBAB_SUICIDE[i], PROBAB_REVIVE[i])
            item_rarity_probab = Item_Rarity_Probab(PROBAB_RARITY_1[i], PROBAB_RARITY_2[i], PROBAB_RARITY_3[i])

    do_something()

    stop = True
    for i, p in enumerate(place_list):
        if not p.destroyed:
            stop = False

    if stop or get_alive_players_count(player_list) <= 1:
        end()

def do_something():
    action_number = random.randint(1, 100)

    if action_number < simulation_probab.item_action_number:
        pick_item()
    elif action_number < simulation_probab.move_action_number:
        move()
    elif action_number < simulation_probab.battle_action_number:
        battle()
    elif action_number < simulation_probab.aop_action_number:
        accident_or_powerup()
    elif action_number < simulation_probab.steal_action_number:
        steal()
    elif action_number < simulation_probab.monster_action_number:
        monster()
    elif action_number < simulation_probab.destroy_action_number:
        destroy()
    elif action_number < simulation_probab.trap_action_number:
        trap()
    elif action_number < simulation_probab.infect_action_number:
        infect()
    elif action_number < simulation_probab.atract_action_number:
        atract()
    elif action_number < simulation_probab.suicide_action_number:
        suicide()
    elif action_number == simulation_probab.revive_action_number:
        revive()
    else:
        do_something()

def pick_item():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)

    better_loot = player.location.loot
    item = get_random_item(item_rarity_probab, better_loot)
    picked = player.pick(player_list, place_list, item)
    if not picked:
        do_something()

def move():
    global place_list

    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)

    loc_candidates = []
    jump_candidates = []

    for i, l in enumerate(player.location.connections):
        if not l.destroyed:
            loc_candidates.append(l)

    if len(loc_candidates) == 0:
        for i, l in enumerate(player.location.connections):
            for j, sl in enumerate(l.connections):
                if not sl.destroyed:
                    loc_candidates.append(sl)
                    jump_candidates.append(l)

    if len(loc_candidates) == 0:
        do_something()
        return

    new_location = random.choice(loc_candidates)
    jump = None
    if len(jump_candidates) > 0:
        jump = jump_candidates[loc_candidates.index(new_location)]
    action_number = random.randint(1, 100)

    if new_location.trap_by != None and new_location.trap_by != player:
        if action_number < 75:
            trapped_by = new_location.trap_by
            new_location.trap_by.kills = new_location.trap_by.kills + 1
            new_location.trap_by = None
            move_player(player, new_location)
            kill_player(player)
            write_tweet(Tweet_type.trapped, player_list, place_list, player.location, [player, trapped_by, player.location])
        else:
            trapped_by = new_location.trap_by
            new_location.trap_by = None

            move_player(player, new_location)
            write_tweet(Tweet_type.trap_dodged, player_list, place_list, player.location, [player, trapped_by, player.location])

    else:
        old_location = player.location
        move_player(player, new_location)

        write_tweet(Tweet_type.somebody_moved, player_list, place_list, player.location, [player, old_location, player.location, jump])

def battle():
    alive_players = filter_player_list_by_state(player_list, 1)
    player_1, player_2, place = get_two_players_in_random_place(place_list)

    if (player_1, player_2) == (None, None):
        do_something()
        return

    factor_1 = 1 - player_1.get_defense() + player_2.get_attack()
    factor_2 = 100 + player_2.get_defense() - player_1.get_attack()

    winner_1 = 50 - PROBAB_TIE
    winner_2 = 50 + PROBAB_TIE

    kill_number = random.randint(factor_1, factor_2)

    if is_friend(player_1, player_2):
        if kill_number > 20 or kill_number < 80:
            #tie(player_list, place_list, player_1, player_2)
            do_something()
            return
    else:
        if kill_number == int((factor_2 - factor_1) / 2):
            run_away(player_list, place_list, player_1, player_2)
        elif kill_number < winner_1:
            kill(player_list, place_list, player_1, player_2, place)
        elif kill_number > winner_2:
            kill(player_list, place_list, player_2, player_1, place)
        else:
            tie(player_list, place_list, player_1, player_2)

def monster():
    place = None
    for i, p in enumerate(place_list):
        if p.monster:
            place = p

    if place != None:
        action_number = random.randint(1, 100)
        people_list = []
        for i, p in enumerate(place.players):
            if p.state == 1:
                people_list.append(p)
        if action_number > 20 and len(people_list) > 0:
            player = random.choice(people_list)
            kill_player(player)
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
                write_tweet(Tweet_type.monster_disappeared, player_list, place_list, place, [place])
    else:
        loc_candidates = []

        for i, p in enumerate(place_list):
            if not p.destroyed:
                loc_candidates.append(p)

        new_place = random.choice(loc_candidates)
        new_place.monster = True

def destroy():
    list = []
    limit = 1
    while len(list) == 0:
        for i, p in enumerate(place_list):
            if not p.destroyed:
                count = 0
                for j, q in enumerate(p.connections):
                    if not q.destroyed:
                        count = count + 1
                if count <= limit:
                    list.append(p)
        limit = limit + 1

    place = random.choice(list)

    place.destroyed = True
    place.monster = False
    place.trap_by = None
    place.loot = False
    dead_list = []
    escaped_list = []
    route_list = []
    new_location = False

    for j, c in enumerate(place.connections):
        if not c.destroyed:
            route_list.append(c)

    if len(route_list) > 0:
        new_location = random.choice(route_list)

    for i, p in enumerate(place.players):
        if p.state == 1:
            if new_location and random.randint(0, 100) >= 75:
                move_player(p, new_location)
                escaped_list.append(p)
            else:
                kill_player(p)
                dead_list.append(p)

    if place.monster:
        place.monster = None

    write_tweet(Tweet_type.destroyed, player_list, place_list, place, [place, dead_list, escaped_list, new_location])

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
        write_tweet(Tweet_type.trap, player_list, place_list, place, [player])
    else:
        do_something()

def accident_or_powerup():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)
    action_number = random.randint(0, 100)

    if action_number > 50:
        powerup(player)
    elif action_number > 25:
        injure(player)
    else:
        illness(player)

def steal():
    alive_players = filter_player_list_by_state(player_list, 1)
    player_1, player_2, place = get_two_players_in_random_place(place_list)

    if (player_1, player_2) == (None, None):
        do_something()
        return

    stealing(player_list, place_list, player_1, player_2)

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

def atract():
    loc_candidates = []
    action_number = random.randint(0, 100)
    double = action_number > 60

    for i, p in enumerate(place_list):
        if not p.destroyed:
            loc_candidates.append(p)

    place = random.choice(loc_candidates)
    atracted_players = []

    def append_players_from(location):
        for j, player in enumerate(location.players):
            if player.state == 1 and player not in atracted_players:
                atracted_players.append(player)

    append_players_from(place)
    for i, connection in enumerate(place.connections):
        append_players_from(connection)
        if double:
            for j, subconnection in enumerate(connection.connections):
                 append_players_from(subconnection)

    alive_players = filter_player_list_by_state(player_list, 1)
    for i, player in enumerate(alive_players):
        if player in atracted_players:
            move_player(player, place)

    write_tweet(Tweet_type.atraction, player_list, place_list, place, [place, atracted_players, double])

def infect():
    alive_players = filter_player_list_by_state(player_list, 1)
    infected_players = []
    healthy_players = []
    for i, p in enumerate(alive_players):
        if p.infected:
            infected_players.append(p)
        else:
            healthy_players.append(p)

    action_number = random.randint(1, 100)

    if action_number > 75 or len(infected_players) == 0:
        player = random.choice(healthy_players)
        player.infected = True
        write_tweet(Tweet_type.somebody_was_infected, player_list, place_list, player.location, [player])
    else:
        player = random.choice(infected_players)
        kill_player(player)
        write_tweet(Tweet_type.somebody_died_of_infection, player_list, place_list, player.location, [player])

def suicide():
    alive_players = filter_player_list_by_state(player_list, 1)
    player = random.choice(alive_players)
    kill_player(player)

    write_tweet(Tweet_type.somebody_suicided, player_list, place_list, player.location, [player])

def end():
    global finished
    alive_players = filter_player_list_by_state(player_list, 1)
    if len(alive_players) == 1:
        write_tweet(Tweet_type.winner, player_list, place_list, alive_players[0].location, [alive_players[0]])
    elif len(alive_players) == 0:
        write_tweet(Tweet_type.nobody_won, player_list, place_list)
    finished = True

start_battle()
