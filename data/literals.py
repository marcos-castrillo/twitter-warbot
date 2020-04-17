#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import LOCALIZATION
from models.tweet_type import Tweet_type
from store import are_friends

if LOCALIZATION == "es_paramo" or LOCALIZATION == "es_spain":
    from data.es.literals import *
    if LOCALIZATION == "es_paramo":
        from data.es_paramo.literals import *
    elif LOCALIZATION == "es_spain":
        from data.es_spain.literals import *

def get_message(tweet):
    message = ''

    if tweet.type == Tweet_type.start:
        message = START(tweet)
    elif tweet.type == Tweet_type.introduce_players:
        message = introduce_players(tweet)
    elif tweet.type == Tweet_type.winner:
        message = winner(tweet)
    elif tweet.type == Tweet_type.winner_districts:
        message = winner_districts(tweet)
    elif tweet.type == Tweet_type.nobody_won:
        message = NOBODY_WON(tweet)
    elif tweet.type == Tweet_type.somebody_got_injured:
        message = somebody_got_injured(tweet)
    elif tweet.type == Tweet_type.somebody_got_special:
        message = somebody_got_special(tweet)
    elif tweet.type == Tweet_type.somebody_found_item:
        message = somebody_found_item(tweet)
    elif tweet.type == Tweet_type.somebody_replaced_item:
        message = somebody_replaced_item(tweet)
    elif tweet.type == Tweet_type.somebody_tied_and_became_friend:
        message = TIED_AND_BEFRIEND(tweet)
    elif tweet.type == Tweet_type.somebody_tied_and_was_friend:
        message = FRIENDS_TIED(tweet)
    elif tweet.type == Tweet_type.somebody_escaped:
        message = somebody_escaped(tweet)
    elif tweet.type == Tweet_type.somebody_killed:
        message = somebody_killed(tweet)
    elif tweet.type == Tweet_type.somebody_revived:
        message = somebody_revived(tweet)
    elif tweet.type == Tweet_type.somebody_suicided:
        message = somebody_suicided(tweet)
    elif tweet.type == Tweet_type.somebody_moved:
        message = somebody_moved(tweet)
    elif tweet.type == Tweet_type.destroyed:
        message = destroyed(tweet)
    elif tweet.type == Tweet_type.destroyed_district:
        message = destroyed_district(tweet)
    elif tweet.type == Tweet_type.somebody_couldnt_move:
        message = COULDNT_MOVE(tweet)
    elif tweet.type == Tweet_type.trap:
        message = TRAP(tweet)
    elif tweet.type == Tweet_type.trapped:
        message = TRAPPED(tweet)
    elif tweet.type == Tweet_type.trap_dodged:
        message = TRAP_DODGED(tweet)
    elif tweet.type == Tweet_type.somebody_stole:
        message = STOLE(tweet)
    elif tweet.type == Tweet_type.somebody_stole_and_replaced:
        message = STOLE_AND_REPLACED(tweet)
    elif tweet.type == Tweet_type.somebody_stole_and_threw:
        message = STOLE_AND_THREW(tweet)
    elif tweet.type == Tweet_type.somebody_powerup:
        message = somebody_powerup(tweet)
    elif tweet.type == Tweet_type.monster_appeared:
        message = MONSTER_APPEARED(tweet)
    elif tweet.type == Tweet_type.monster_moved:
        message = MONSTER_MOVED(tweet)
    elif tweet.type == Tweet_type.somebody_died_of_infection:
        message = INFECTED_DIED(tweet)
    elif tweet.type == Tweet_type.somebody_was_infected:
        message = infected(tweet)
    elif tweet.type == Tweet_type.atraction:
        message = atraction(tweet)
    elif tweet.type == Tweet_type.monster_disappeared:
        message = MONSTER_DISAPPEARED(tweet)
    elif tweet.type == Tweet_type.monster_killed:
        message = MONSTER_KILLED(tweet)
    return (message + '\n').encode('utf-8')

def introduce_players(tweet):
    locals_str = ''
    if len(tweet.player_list) > 0:
        for i, player in enumerate(tweet.player_list):
            if i == 0:
                locals_str = player.get_name()
            elif i == len(tweet.player_list) - 1:
                locals_str = u' '.join([locals_str, AND, player.get_name()])
            else:
                locals_str = locals_str + ', ' + player.get_name()
        locals_str = u' '.join([locals_str, INTRODUCE_PLACE(tweet)])

    sufix = ''
    if len(tweet.player_list) > 0:
        sufix = ' '

    if len(tweet.player_list_2) > 0:
        if tweet.inverse:
            sufix = sufix + TRIBUTES_NOT_ENOUGH(tweet.place.name)
            for i, player in enumerate(tweet.player_list_2):
                if i == 0:
                    sufix = sufix + player.get_name()
                elif i == len(tweet.player_list_2) - 1:
                    sufix = u' '.join([sufix, AND, player.get_name()])
                else:
                    sufix = sufix + ', ' + player.get_name()
            sufix = u' '.join([sufix, TRIBUTES_RANDOMLY_CHOSEN(tweet.player_list_2)])
        else:
            sufix = sufix +  TRIBUTES_WERE_DIVIDED(tweet.place.name)

    return locals_str + sufix

def winner(tweet):
    item_list = ''
    injury_list = ''
    kills = ''
    infection = ''

    if tweet.player.kills == 0:
        kills = WINNER_NO_KILLS
    elif tweet.player.kills == 1:
        kills = WINNER_ONE_KILL
    else:
        kills = WINNER_MULTI_KILL(str(tweet.player.kills))

    if len(tweet.player.item_list) > 0:
        list = ''
        for i, item in enumerate(tweet.player.item_list):
            if i == 0:
                list = item.name
            elif i == len(tweet.player.item_list) - 1:
                list = u' '.join([list, AND, item.name])
            else:
                list = list + ', ' + item.name

        item_list = u' ' + u' '.join([WINNER_ITEM_LIST, list + '.'])

    if len(tweet.player.injury_list) > 0:
        list = ''
        for i, injury in enumerate(tweet.player.injury_list):
            if i == 0:
                list = injury.name
            elif i == len(tweet.player.injury_list):
                list = u' '.join([list, AND, injury.name])
            else:
                list = list + ', ' + injury.name
        injury_list = u' ' + u' '.join([WINNER_INJURY_LIST, list + '.'])

    if tweet.player.infected:
        infection = WINNER_INFECTION

    return WINNER_COMPOSED(tweet.player, kills, item_list, infection)

def winner_districts(tweet):
    tributes_str = ''
    for i, winner in enumerate(tweet.player_list):
        if i == 0:
            tributes_str = winner.get_name()
        elif i == len(tweet.player_list):
            tributes_str = u' '.join([tributes_str, AND, winner.get_name()])
        else:
            tributes_str = tributes_str + ', ' + winner.get_name()

    kills = 0
    for i, player in enumerate(tweet.player_list):
        kills = kills + player.kills

    return WINNER_DISTRICTS_COMPOSED(tributes_str, tweet.place.name, kills)

def somebody_got_injured(tweet):
    return I_COMPOSED(tweet.player, INJURE_ACTION(), tweet.item, has_now(tweet.player, tweet.item))

def somebody_got_special(tweet):
    immunity = ''
    if tweet.item.injure_immunity:
        immunity = INJURE_IMMUNITY()
    if tweet.item.monster_immunity:
        immunity = MONSTER_IMMUNITY()
    if tweet.item.infection_immunity:
        immunity = INFECTION_IMMUNITY()
    return I_COMPOSED(tweet.player, SPECIAL_ACTION(), tweet.item, immunity)

def somebody_powerup(tweet):
    return I_COMPOSED(tweet.player, POWERUP_ACTION(), tweet.item, has_now(tweet.player, tweet.item))

def somebody_found_item(tweet):
    return I_COMPOSED(tweet.player, FIND_ACTION(), tweet.item, has_now(tweet.player, tweet.item))

def somebody_replaced_item(tweet):
    return I_COMPOSED(tweet.player, FIND_ACTION(), tweet.item, REPLACED + '' + tweet.old_item.name + '. ' + has_now(tweet.player, tweet.item, tweet.old_item))

def somebody_escaped(tweet):
    if tweet.inverse:
        escaped = ESCAPED(tweet.player_2, tweet.player)
    else:
        escaped = ESCAPED(tweet.player, tweet.player_2)

    sufix = ''
    if tweet.unfriend:
        sufix = ' ' + UNFRIEND

    return escaped + sufix

def somebody_killed(tweet):
    player_1 = tweet.player
    player_2 = tweet.player_2
    if tweet.inverse:
        player_1 = tweet.player_2
        player_2 = tweet.player
    killing_item = tweet.item
    new_item = tweet.new_item
    old_item = tweet.old_item

    kill_verb = KILL_ACTION()
    kill_method = KILL_METHOD(player_1)
    were_friends = are_friends(player_1, player_2)
    friend_message = ''
    kills_count = '.'
    stole = ''
    fav = ''

    if were_friends:
        friend_message = TREASON(tweet)
    if killing_item != None:
        kill_method = u' '.join((WITH, killing_item.name))
    if player_1.kills > 1:
        kills_count = u' ' + u' '.join((HAS_ALREADY_KILLED(str(player_1.kills)), PRAISE(player_1)))
    if new_item != None and old_item != None:
        stole = u' ' + u' '.join((ALSO_STOLE(), new_item.name, AND, GETS_RID_OF, old_item.name + '.'))
    elif new_item != None:
        stole = u' ' + u' '.join((ALSO_STOLE(), new_item.name + '.'))

    return u' '.join((friend_message + player_1.get_name(), kill_verb, player_2.get_name(), kill_method + kills_count + stole))

def somebody_revived(tweet):
    revived = REVIVED(tweet)
    sufix = ''
    if tweet.double:
        sufix = u' ' + DISTRICT_REBUILD(tweet)
    return revived + sufix

def somebody_suicided(tweet):
    return u' '.join((tweet.player.get_name(), SUICIDE()))

def somebody_moved(tweet):
    action = ''
    road = True

    for i, c in enumerate(tweet.place_2.sea_connections):
        if c.encode('utf-8') == tweet.place.name.encode('utf-8'):
            road = True

    if road:
        action = MOVE_ACTION_ROAD()
    else:
        action = MOVE_ACTION_WATER()

    return u' '.join((tweet.player.get_name(), action, tweet.place_2.name, TO, tweet.place.name + '.'))

def destroyed(tweet):
    place = tweet.place
    new_location = tweet.place_2
    dead_list = tweet.player_list
    escaped_list = tweet.player_list_2

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

        susufix = u' ' + u' '.join((susufix_str + '.', get_sing_or_pl(escaped_list, MOVED_SING(), MOVED_PL()), new_location.name + u'.'))

    return (prefix + sufix + susufix)

def destroyed_district(tweet):
    place = tweet.place
    new_location = tweet.place_2
    tribute_list = tweet.player_list
    escaped_list = tweet.player_list_2

    if len(tribute_list) == 0:
        tributes_str = '.'
    elif len(tribute_list) == 1:
        tributes_str = tribute_list[0].get_name()
    else:
        tributes = []
        tributes_str = ''
        for i, d in enumerate(tribute_list):
            tributes.append(d.get_name())
        for i, d in enumerate(tributes):
            if i == 0:
                tributes_str = d
            elif i == len(tributes) - 1:
                tributes_str = tributes_str + ' ' + AND + ' ' + d
            else:
                tributes_str = tributes_str + ', ' + d

    prefix = DESTROYED_DISTRICT(place.name, tributes_str)

    sufix = ''
    escaped = []

    if new_location and len(escaped_list) > 0:
        for i, d in enumerate(escaped_list):
            escaped.append(d.get_name())
        for i, d in enumerate(escaped):
            if i == 0:
                sufix_str = d
            elif i == len(escaped) - 1:
                sufix_str = sufix_str + ' ' +  AND + ' ' + d
            else:
                sufix_str = sufix_str + ', ' + d

        sufix = u' ' + u' '.join((sufix_str, get_sing_or_pl(escaped_list, MOVED_SING(), MOVED_PL()), new_location.name + u'.'))

    return (prefix + sufix)

def infected(tweet):
    player = tweet.player
    place_infected = PLACE_INFECTED(tweet)
    also = '.'
    if len(tweet.player_list) > 0:
        also = u' infectando también a'
        for i, player in enumerate(tweet.player_list):
            if i == 0:
                also = player.get_name()
            elif i == len(tweet.player_list) - 1:
                also = u' '.join((also, AND, player.get_name()))
            else:
                also = also + ', ' + player.get_name()

    return u' '.join((WAS_INFECTED(tweet), PLACE_INFECTED(tweet) + also))

def atraction(tweet):
    place = tweet.place
    atracted_players = tweet.player_list

    location = ATRACTION(place.name)
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
        composed = u' '.join([HAS_NOW(), str(player.get_attack()) + get_amount(event.attack - previous_attack), IN_ATTACK])
    if event.attack != 0 and event.defense != 0:
        composed = u' '.join([composed, AND, str(player.get_defense()) + get_amount(event.defense - previous_defense), IN_DEFENSE + '.'])
    elif event.defense != 0:
        composed = u' '.join([HAS_NOW(), str(player.get_defense()) + get_amount(event.defense - previous_defense), IN_DEFENSE + '.'])
    elif event.attack == 0:
        composed = ''
    else:
        composed = composed + '.'

    return composed
