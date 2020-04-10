#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.config import LOCALIZATION
from models.tweet_type import Tweet_type

if LOCALIZATION == "es_paramo" or LOCALIZATION == "es_spain":
    from data.es.literals import *
    if LOCALIZATION == "es_paramo":
        from data.es_paramo.literals import *
    elif LOCALIZATION == "es_spain":
        from data.es_spain.literals import *

def get_message(type, args = None):
    message = ''

    if type == Tweet_type.start:
        message = START
    elif type == Tweet_type.winner:
        message = winner(args[0])
    elif type == Tweet_type.nobody_won:
        message = NOBODY_WON
    elif type == Tweet_type.somebody_got_ill:
        message = somebody_got_ill(args[0], args[1])
    elif type == Tweet_type.somebody_got_injured:
        message = somebody_got_injured(args[0], args[1])
    elif type == Tweet_type.somebody_found_item:
        message = somebody_found_item(args[0], args[1])
    elif type == Tweet_type.somebody_replaced_item:
        message = somebody_replaced_item(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_tied_and_became_friend:
        message = TIED_AND_BEFRIEND(args[0], args[1])
    elif type == Tweet_type.somebody_tied_and_was_friend:
        message = FRIENDS_TIED(args[0], args[1])
    elif type == Tweet_type.somebody_escaped:
        if len(args) == 3:
            message = somebody_escaped(args[0], args[1], args[2])
        elif len(args) == 2:
            message = somebody_escaped(args[0], args[1])
    elif type == Tweet_type.somebody_killed:
        if len(args) == 6:
            message = somebody_killed(args[0], args[1], args[2], args[3], args[4], args[5])
        elif len(args) == 5:
            message = somebody_killed(args[0], args[1], args[2], args[3], args[4])
        elif len(args) == 4:
            message = somebody_killed(args[0], args[1], args[2], args[3])
    elif type == Tweet_type.somebody_revived:
        message = REVIVED(args[0])
    elif type == Tweet_type.somebody_suicided:
        message = somebody_suicided(args[0])
    elif type == Tweet_type.somebody_moved:
        message = somebody_moved(args[0], args[1], args[2], args[3])
    elif type == Tweet_type.destroyed:
        message = destroyed(args[0], args[1], args[2], args[3])
    elif type == Tweet_type.somebody_couldnt_move:
        message = COULDNT_MOVE(args[0])
    elif type == Tweet_type.trap:
        message = TRAP(args[0])
    elif type == Tweet_type.trapped:
        message = TRAPPED(args[0], args[1], args[2])
    elif type == Tweet_type.trap_dodged:
        message = TRAP_DODGED(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_stole:
        message = STOLE(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_stole_and_replaced:
        message = STOLE_AND_REPLACED(args[0], args[1], args[2], args[3])
    elif type == Tweet_type.somebody_stole_and_threw:
        message = STOLE_AND_THREW(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_powerup:
        message = somebody_powerup(args[0], args[1])
    elif type == Tweet_type.monster_appeared:
        message = MONSTER_APPEARED(args[0])
    elif type == Tweet_type.monster_moved:
        message = MONSTER_MOVED(args[0], args[1])
    elif type == Tweet_type.somebody_died_of_infection:
        message = INFECTED_DIED(args[0])
    elif type == Tweet_type.somebody_was_infected:
        message = INFECTED(args[0])
    elif type == Tweet_type.atraction:
        message = atraction(args[0], args[1], args[2])
    elif type == Tweet_type.monster_disappeared:
        message = MONSTER_DISAPPEARED(args[0])
    elif type == Tweet_type.monster_killed:
        message = MONSTER_KILLED(args[0], args[1])
    return (message + '\n').encode('utf-8')

def winner(player):
    item_list = ''
    injury_list = ''
    kills = ''
    infection = ''

    if player.kills == 0:
        kills = WINNER_NO_KILL
    elif player.kills == 1:
        kills = WINNER_ONE_KILL
    else:
        kills = WINNER_MULTI_KILL(str(player.kills))

    if len(player.item_list) > 0:
        list = ''
        for i, item in enumerate(player.item_list):
            if i == 0:
                list = item.name
            elif i == len(player.item_list) - 1:
                list = u' '.join([list, AND, item.name])
            else:
                list = list + ', ' + item.name

        item_list = u' ' + u' '.join([WINNER_ITEM_LIST, list + '.'])

    if len(player.injury_list) > 0:
        list = ''
        for i, injury in enumerate(player.injury_list):
            if i == 0:
                list = injury.name
            elif i == len(player.injury_list):
                list = u' '.join([list, AND, injury.name])
            else:
                list = list + ', ' + injury.name
        injury_list = u' ' + u' '.join([WINNER_INJURY_LIST, list + '.'])

    if player.infected:
        infection = WINNER_INFECTION

    return WINNER_COMPOSED(player, kills, item_list, infection)

def somebody_got_ill(player, illness):
    return I_COMPOSED(player, ILLNESS_ACTION(), illness, has_now(player, illness))

def somebody_got_injured(player, injury):
    return I_COMPOSED(player, INJURE_ACTION(), injury, has_now(player, injury))

def somebody_powerup(player, powerup):
    return I_COMPOSED(player, POWERUP_ACTION(), powerup, has_now(player, powerup))

def somebody_found_item(player, item):
    loot = ''
    if player.location.loot:
        loot = BETTER_LOOT(player.location.name)

    return I_COMPOSED(player, FIND_ACTION(), item, has_now(player, item) + u' ' + loot)

def somebody_replaced_item(player, item_new, item_old):
    return I_COMPOSED(player, FIND_ACTION(), item_new, REPLACED + '' + item_old.name + '. ' + has_now(player, item_new, item_old))

def somebody_escaped(player_1, player_2, unfriend = False):
    sufix = ''
    if unfriend:
        sufix = ' ' + UNFRIEND
    return ESCAPED(player_1, player_2) + sufix

def somebody_killed(player_1, player_2, were_friends, killing_item, new_item = None, old_item = None):
    kill_verb = KILL_ACTION()
    kill_method = KILL_METHOD(player_1)

    friend_message = ''
    kills_count = '.'
    stole = ''
    fav = ''

    if were_friends:
        friend_message = TREASON
    if killing_item != None:
        kill_method = u' '.join((WITH, killing_item.name))
    if player_1.kills > 1:
        kills_count = u' ' + u' '.join((HAS_ALREADY_KILLED(str(player_1.kills)), PRAISE(player_1)))
    if new_item != None and old_item != None:
        stole = u' ' + u' '.join((ALSO_STOLE, new_item.name, AND, GETS_RID_OF, old_item.name + '.'))
    elif new_item != None:
        stole = u' ' + u' '.join((ALSO_STOLE, new_item.name + '.'))

    return u' '.join((friend_message + player_1.get_name(), kill_verb, player_2.get_name() + kill_method + kills_count + stole))

def somebody_suicided(player):
    return u' '.join((player.get_name(), SUICIDE()))

def somebody_moved(player, old_location, new_location, crossed = None):
    crossing = ''
    action = ''
    road = False

    for i, c in enumerate(old_location.road_connections):
        if c.encode('utf-8') == new_location.name.encode('utf-8'):
            road = True

    if crossed != None:
        crossing = CROSSING + crossed.name

    if road:
        action = MOVE_ACTION_ROAD()
    else:
        action = MOVE_ACTION_WATER()

    return u' '.join((player.get_name(), action, old_location.name + crossing, TO, new_location.name + '.'))

def destroyed(place, dead_list, escaped_list, new_location):
    prefix = DESTROYED(place.name)

    if len(dead_list) == 0:
        sufix = '.'
    elif len(dead_list) == 1:
        sufix = DIED(dead_list[0].get_name())
    else:
        dead = []
        dead_str = ''
        for i, d in enumerate(dead_list):
            dead.append(d.get_name())
        for i, d in enumerate(dead):
            if i == 0:
                dead_str = d
            elif i == len(dead) - 1:
                dead_str = dead_str + AND + d
            else:
                dead_str = dead_str + ', ' + d
        sufix = DIED(dead_str, True)

    susufix = ''
    escaped = []

    if new_location and len(escaped_list) > 0:
        for i, d in enumerate(escaped_list):
            escaped.append(d.get_name())
        for i, d in enumerate(escaped):
            if i == 0:
                susufix_str = d
            elif i == len(escaped) - 1:
                susufix_str = susufix_str + AND + d
            else:
                susufix_str = susufix_str + ', ' + d

        susufix = u' ' + u' '.join((susufix_str, get_sing_or_pl(escaped_list, MOVED_SING, MOVED_PL), new_location.name + u'.'))

    return (prefix + sufix + susufix)

def atraction(place, atracted_players, double):
    location = ATRACTION(place.name)
    players = ATRACTION_NOBODY()

    if len(atracted_players) > 0:
        players = u' ' + AND + u' '

        for i, player in enumerate(atracted_players):
            if i == 0:
                players = player.get_name()
            elif i == len(atracted_players) - 1:
                players = u' '.join((players, AND, player.get_name()))
            else:
                players = players + ', ' + player.get_name()

        if len(atracted_players) > 1:
            players = players + MOVED_ATRACTION_PL()
        else:
            players = players + MOVED_ATRACTION_SING()

    return u' '.join([location, players])

def has_now(player, event, previous_event = None):
    previous_attack = 0
    previous_defense = 0

    if previous_event != None:
        previous_attack = previous_event.attack
        previous_defense = previous_event.defense

    if event.attack != 0:
        composed = u' '.join([HAS_NOW, str(player.get_attack()), get_amount(event.attack - previous_attack), IN_ATTACK])
    if event.attack != 0 and event.defense != 0:
        composed = u' '.join([composed, AND, str(player.get_defense()), get_amount(event.defense - previous_defense), IN_DEFENSE + '.'])
    elif event.defense != 0:
        composed = u' '.join([HAS_NOW, str(player.get_defense()), get_amount(event.defense - previous_defense), IN_DEFENSE + '.'])
    elif event.attack == 0:
        composed = ''
    else:
        composed = composed + '.'

    return composed
