#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.enums import *
from services.config import config
from services.store import are_friends
import emoji

if config.general.language == 'es':
    from data.es.literals import *


def get_message(tweet):
    message = u''

    if tweet.type == TweetType.start:
        message = config.literals.default_start
    elif tweet.type == TweetType.introduce_players:
        message = introduce_players(tweet)
    elif tweet.type == TweetType.winner:
        message = winner(tweet)
    elif tweet.type == TweetType.winner_districts:
        message = winner_districts(tweet)
    elif tweet.type == TweetType.nobody_won:
        message = NOBODY_WON(tweet)
    elif tweet.type == TweetType.somebody_got_special:
        message = somebody_got_special(tweet)
    elif tweet.type == TweetType.somebody_found_item:
        message = emoji.emojize(':package:') + LINEBREAK() + somebody_found_item(tweet)
    elif tweet.type == TweetType.somebody_replaced_item:
        message = emoji.emojize(':package:') + LINEBREAK() + somebody_replaced_item(tweet)
    elif tweet.type == TweetType.somebody_tied_and_became_friend:
        message = emoji.emojize(':handshake:') + LINEBREAK() + TIED_AND_BEFRIEND(tweet)
    elif tweet.type == TweetType.somebody_tied_and_was_friend:
        message = emoji.emojize(':handshake:') + LINEBREAK() + FRIENDS_TIED(tweet)
    elif tweet.type == TweetType.somebody_escaped:
        message = emoji.emojize(':running:') + LINEBREAK() + somebody_escaped(tweet)
    elif tweet.type == TweetType.somebody_killed:
        message = somebody_killed(tweet)
    elif tweet.type == TweetType.somebody_revived:
        message = emoji.emojize(':angel:') + LINEBREAK() + somebody_revived(tweet)
    elif tweet.type == TweetType.somebody_suicided:
        message = somebody_suicided(tweet)
    elif tweet.type == TweetType.somebody_moved:
        message = somebody_moved(tweet)
    elif tweet.type == TweetType.destroyed:
        message = destroyed(tweet)
    elif tweet.type == TweetType.destroyed_district:
        message = destroyed_district(tweet)
    elif tweet.type == TweetType.somebody_couldnt_move:
        message = COULDNT_MOVE(tweet)
    elif tweet.type == TweetType.trap:
        message = TRAP(tweet)
    elif tweet.type == TweetType.trapped:
        message = TRAPPED(tweet)
    elif tweet.type == TweetType.trap_dodged:
        message = TRAP_DODGED(tweet)
    elif tweet.type == TweetType.somebody_stole:
        message = emoji.emojize(':moneybag:') + LINEBREAK() + STOLE(tweet)
    elif tweet.type == TweetType.somebody_stole_and_replaced:
        message = emoji.emojize(':moneybag:') + LINEBREAK() + STOLE_AND_REPLACED(tweet)
    elif tweet.type == TweetType.somebody_stole_and_threw:
        message = emoji.emojize(':moneybag:') + LINEBREAK() + STOLE_AND_THREW(tweet)
    elif tweet.type == TweetType.monster_appeared:
        message = MONSTER_APPEARED(tweet)
    elif tweet.type == TweetType.monster_moved:
        message = MONSTER_MOVED(tweet)
    elif tweet.type == TweetType.somebody_died_of_infection:
        message = INFECTED_DIED(tweet)
    elif tweet.type == TweetType.somebody_was_infected:
        message = infected(tweet)
    elif tweet.type == TweetType.attraction:
        message = attraction(tweet)
    elif tweet.type == TweetType.monster_killed:
        message = MONSTER_KILLED(tweet)
    elif tweet.type == TweetType.somebody_got_cured:
        message = CURED(tweet)
    elif tweet.type == TweetType.next_entrance:
        message = NEXT_ENTRANCE(tweet)
    elif tweet.type == TweetType.soft_attack:
        message = soft_attack(tweet)

    if tweet.is_event:
        message = tweet.type

    return (message + '\n').encode('utf-8')


def introduce_players(tweet):
    locals_str = ''
    limit_length = 12
    if len(tweet.player_list) > 0:
        players = tweet.player_list
        if len(players) > limit_length:
            players = players[:limit_length]
        for i, player in enumerate(players):
            if len(players) > 7:
                name = '@' + player.username
            else:
                name = player.get_name()

            if i == 0:
                locals_str = name
            elif i == len(tweet.player_list) - 1:
                locals_str = u' '.join([locals_str, AND(), name])
            else:
                locals_str = locals_str + ', ' + name
        if len(tweet.player_list) == limit_length + 1:
            locals_str = locals_str + u' y otro más'
        elif len(tweet.player_list) > limit_length:
            locals_str = locals_str + u' y otros ' + str(len(tweet.player_list) - limit_length)
        locals_str = u' '.join([locals_str, INTRODUCE_PLACE(tweet)])

    suffix = ''

    if len(tweet.player_list_2) > 0:
        suffix = ' '

        if tweet.inverse:
            suffix = suffix + TRIBUTES_NOT_ENOUGH(tweet.place.district_display_name)
            for i, player in enumerate(tweet.player_list_2):
                if len(tweet.player_list_2) > 7:
                    name = '@' + player.username
                else:
                    name = player.get_name()
                if i == 0:
                    suffix = suffix + name
                elif i == len(tweet.player_list_2) - 1:
                    suffix = u' '.join([suffix, AND(), name])
                else:
                    suffix = suffix + ', ' + name
            suffix = u' '.join([suffix, TRIBUTES_RANDOMLY_CHOSEN(tweet.player_list_2)])
        else:
            suffix = suffix + TRIBUTES_WERE_DIVIDED(tweet.place.district_display_name)

    return locals_str + suffix


def winner(tweet):
    item_list = ''
    kills = ''
    infection = ''

    if tweet.player.kills == 0:
        kills = LINEBREAK() + WINNER_NO_KILLS()
    elif tweet.player.kills == 1:
        kills = LINEBREAK() + WINNER_ONE_KILL()
    else:
        kills = LINEBREAK() + WINNER_MULTI_KILL(str(tweet.player.kills))

    if len(tweet.player.item_list) > 0:
        items = ''
        for i, item in enumerate(tweet.player.item_list):
            if i == 0:
                items = item.name
            elif i == len(tweet.player.item_list) - 1:
                items = u' '.join([items, AND(), item.name])
            else:
                items = items + ', ' + item.name

        item_list = u' ' + u' '.join([LINEBREAK() + WINNER_ITEM_LIST(), items + '.'])

    if tweet.player.infected:
        infection = WINNER_INFECTION()

    return WINNER_COMPOSED(tweet.player, kills, item_list, infection)


def winner_districts(tweet):
    tributes_str = ''
    for i, player in enumerate(tweet.player_list):
        if i == 0:
            tributes_str = player.get_name()
        elif i == len(tweet.player_list) - 1:
            tributes_str = u' '.join([tributes_str, AND(), player.get_name()])
        else:
            tributes_str = tributes_str + ', ' + player.get_name()

    kills = 0
    for i, player in enumerate(tweet.player_list):
        kills = kills + player.kills

    return WINNER_DISTRICTS_COMPOSED(tributes_str, tweet.place, kills)


def somebody_got_special(tweet):
    shared = False
    if len(tweet.player_list) > 0:
        shared = True

    immunity = ''
    if tweet.item.special == SpecialType.injure_immunity:
        immunity = INJURE_IMMUNITY(tweet.player, shared)
    if tweet.item.special == SpecialType.monster_immunity:
        immunity = MONSTER_IMMUNITY(tweet.player, shared)
    if tweet.item.special == SpecialType.infection_immunity:
        immunity = INFECTION_IMMUNITY(tweet.player, shared)

    return I_COMPOSED(tweet.player, SPECIAL_ACTION(), tweet.item.name, immunity)


def soft_attack(tweet):
    attacker = tweet.player
    attacked = tweet.player_2
    if tweet.inverse:
        attacker = tweet.player_2
        attacked = tweet.player

    soft = SOFT_ATTACK(attacker, attacked)
    change = LINEBREAK() + has_now(attacked, tweet.item)

    sufix = ''
    if tweet.unfriend:
        sufix = LINEBREAK() + UNFRIEND()
    return soft + change + sufix


def somebody_found_item(tweet):
    if tweet.item.thrown_away_by is not None and config.general.match_type != MatchType.rumble:
        thrown_away_by = FROM(tweet.item.thrown_away_by.name)
        return I_COMPOSED(tweet.player, FIND_ACTION_SIMPLE(), tweet.item.name, has_now(tweet.player, tweet.item),
                          thrown_away_by)
    else:
        return I_COMPOSED(tweet.player, FIND_ACTION(), tweet.item.name, has_now(tweet.player, tweet.item))


def somebody_replaced_item(tweet):
    if tweet.item.thrown_away_by is not None and config.general.match_type != MatchType.rumble:
        thrown_away_by = FROM(tweet.item.thrown_away_by.name)
        return I_COMPOSED(tweet.player, FIND_ACTION_SIMPLE(), tweet.item.name,
                          REPLACED + ' ' + tweet.old_item.name + '. ' + has_now(tweet.player, tweet.item,
                                                                                tweet.old_item), thrown_away_by)
    else:
        return I_COMPOSED(tweet.player, FIND_ACTION(), tweet.item.name,
                          REPLACED + ' ' + tweet.old_item.name + '. ' + has_now(tweet.player, tweet.item,
                                                                                tweet.old_item))


def somebody_escaped(tweet):
    if tweet.inverse:
        player_escaped = tweet.player
        player_not_escaped = tweet.player_2
    else:
        player_escaped = tweet.player_2
        player_not_escaped = tweet.player

    escaped = ESCAPED(player_not_escaped, player_escaped)

    sufix = ''
    if tweet.unfriend:
        sufix = LINEBREAK() + UNFRIEND()
    if tweet.there_was_infection:
        other_players = [x for x in tweet.place_2.players if x.get_name() != player_escaped.get_name()]
        if tweet.infected_or_was_infected_by:
            sufix = sufix + LINEBREAK() + INFECTED_OTHERS(tweet, other_players)
        else:
            sufix = sufix + LINEBREAK() + SOMEBODY_INFECTED(tweet, other_players)
    return escaped + sufix


def somebody_killed(tweet):
    attacker = tweet.player
    attacked = tweet.player_2
    if tweet.inverse:
        attacker = tweet.player_2
        attacked = tweet.player
    killing_item = tweet.item
    new_item = tweet.new_item
    old_item = tweet.old_item

    kill_action = KILL_ACTION(attacker, attacked)

    friend_message = ''
    if are_friends(attacker, attacked):
        friend_message = TREASON(tweet)

    kill_method = KILL_METHOD(attacker)
    if len(kill_method) > 1:
        kill_method = u' ' + kill_method
    if killing_item is not None and config.general.match_type != MatchType.rumble:
        kill_method = u' ' + u' '.join((WITH, killing_item.name))

    kills_count = ''
    if attacker.kills > 1:
        kills_count = u' ' + HAS_ALREADY_KILLED(str(attacker.kills))

    stole = ''
    if new_item is not None and old_item is not None:
        stole = '.' + LINEBREAK() + u' '.join((ALSO_STOLE(), new_item.name, AND(), GETS_RID_OF, old_item.name))
    elif new_item is not None:
        stole = '.' + LINEBREAK() + u' '.join((ALSO_STOLE(), new_item.name))

    return friend_message + kill_action + kill_method + kills_count + stole + '.'


def somebody_revived(tweet):
    revived = REVIVED(tweet)
    suffix = ''
    if tweet.double:
        suffix = LINEBREAK() + DISTRICT_REBUILD(tweet)
    if tweet.there_was_infection:
        suffix = LINEBREAK() + SOMEBODY_INFECTED(tweet, tweet.player.location.players)

    return revived + suffix


def somebody_suicided(tweet):
    return u' '.join((tweet.player.get_name(), SUICIDE()))


def somebody_moved(tweet):
    if any(x for x in tweet.place_2.water_connection_list if x.name == tweet.place.name) or len(
            tweet.place.road_connection_list) == 0 or len(tweet.place_2.road_connection_list) == 0:
        action = MOVE_ACTION_WATER()
    else:
        action = MOVE_ACTION_ROAD()

    item = u''
    if tweet.double:
        item = LINEBREAK() + emoji.emojize(
            ':flexedbiceps:') + LINEBREAK() + STRONGER_POWER(tweet)
    elif tweet.item is not None:
        if tweet.item.type == ItemType.powerup:
            item = LINEBREAK() + FOUND_ON_THE_WAY(tweet) + u' ' + has_now_short(tweet.player, tweet.item)
        elif tweet.item.type == ItemType.injury:
            item = LINEBREAK() + emoji.emojize(':hospital:') + LINEBREAK() + INJURE_ON_THE_WAY(
                tweet) + u' ' + has_now_short(tweet.player, tweet.item)

    infection = u''
    if tweet.there_was_infection:
        other_players = [x for x in tweet.place.players if x.get_name() != tweet.player.get_name()]
        if tweet.infected_or_was_infected_by:
            infection = LINEBREAK() + INFECTED_OTHERS(tweet, other_players)
        else:
            infection = LINEBREAK() + SOMEBODY_INFECTED(tweet, other_players)

    return u' '.join(
        (tweet.player.get_name(), action, tweet.place_2.name, TO, tweet.place.name + '.' + item + infection))


def destroyed(tweet):
    place = tweet.place
    new_location = tweet.place_2
    dead_list = tweet.player_list
    escaped_list = tweet.player_list_2

    prefix = DESTROYED(place.name)

    if len(dead_list) == 0:
        suffix = '.'
    elif len(dead_list) == 1:
        suffix = DIED(dead_list[0].get_name())
    else:
        dead = []
        dead_str = ''
        for i, d in enumerate(dead_list):
            if len(dead_list) > 7:
                name = '@' + d.username
            else:
                name = d.get_name()
            dead.append(name)

        for i, d in enumerate(dead):
            if i == 0:
                dead_str = d
            elif i == len(dead) - 1:
                dead_str = dead_str + u' ' + AND() + u' ' + d
            else:
                dead_str = dead_str + ', ' + d
        suffix = DIED(dead_str, True)

    susufix = ''
    escaped = []

    if new_location and len(escaped_list) > 0:
        for i, d in enumerate(escaped_list):
            escaped.append('@' + d.username)
        for i, d in enumerate(escaped):
            if i == 0:
                susufix_str = LINEBREAK() + d
            elif i == len(escaped) - 1:
                susufix_str = susufix_str + AND() + d
            else:
                susufix_str = susufix_str + ', ' + d

        susufix = u' ' + u' '.join(
            (susufix_str, get_sing_or_pl(escaped_list, MOVED_SING(), MOVED_PL()), new_location.name + u'.'))
        if tweet.there_was_infection:
            susufix = susufix + LINEBREAK() + INFECTED_EVERYBODY()

    return prefix + suffix + susufix


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
            tributes.append(u'@' + d.username)
        for i, d in enumerate(tributes):
            if len(tweet.player_list) > 5 and i == 4:
                tributes_str = u' '.join((tributes_str, AND(), OTHERS(len(tweet.player_list) - i)))
                break
            if i == 0:
                tributes_str = d
            elif i == len(tributes) - 1:
                tributes_str = tributes_str + ' ' + AND() + ' ' + d
            else:
                tributes_str = tributes_str + ', ' + d

    prefix = DESTROYED_DISTRICT(place, tributes_str) + '.'

    suffix = ''
    escaped = []

    if new_location and len(escaped_list) > 0:
        for i, d in enumerate(escaped_list):
            escaped.append(u'@' + d.username)
        for i, d in enumerate(escaped):
            if i == 0:
                suffix_str = LINEBREAK() + d
            elif i == len(escaped) - 1:
                suffix_str = suffix_str + ' ' + AND() + ' ' + d
            else:
                suffix_str = suffix_str + ', ' + d

        suffix = u' ' + u' '.join(
            (suffix_str, get_sing_or_pl(escaped_list, MOVED_SING(), MOVED_PL()), new_location.name + u'.'))

        if tweet.there_was_infection:
            suffix = suffix + LINEBREAK() + INFECTED_EVERYBODY()

    return prefix + suffix


def infected(tweet):
    player = tweet.player
    suffix = u''
    if len(tweet.player_list) > 0:
        suffix = LINEBREAK() + PLACE_INFECTED(tweet) + ' ' + ALSO_INFECTING() + ' '
        for i, player in enumerate(tweet.player_list):
            if len(tweet.player_list) > 2 and i == 1:
                suffix = u' '.join((suffix, AND(), OTHERS(len(tweet.player_list) - i)))
                break
            if i == 0:
                suffix = suffix + player.get_name()
            elif i == len(tweet.player_list) - 1:
                suffix = u' '.join((suffix, AND(), player.get_name()))
            else:
                suffix = suffix + ', ' + player.get_name()
        suffix = suffix + '.'
    return WAS_INFECTED(tweet) + suffix


def attraction(tweet):
    place = tweet.place
    attracted_players = tweet.player_list

    location = ATRACTION(place.name)
    players = u' ' + AND() + u' '

    for i, player in enumerate(attracted_players):
        if tweet.there_was_infection:
            name = '@' + player.username
        else:
            name = player.get_name()

        if i == 0:
            players = name
        elif i == len(attracted_players) - 1:
            players = u' '.join((players, AND(), name))
        else:
            players = players + ', ' + name

    if len(attracted_players) > 1:
        players = u' '.join([players, MOVED_ATRACTION_PL() + '.'])
    else:
        players = u' '.join([players, MOVED_ATRACTION_SING() + '.'])

    infection = u''
    if tweet.there_was_infection:
        infection = LINEBREAK() + INFECTED_EVERYBODY()
    return u' '.join(
        [emoji.emojize(':partyingface:') + LINEBREAK(), location, players + infection])


def has_now(player, event, previous_event=None, short=False):
    previous_power = 0

    if previous_event is not None:
        previous_power = previous_event.power

    composed = ''
    if event.power != 0:
        power = str(player.get_power()) + get_amount(event.power - previous_power)
        composed = HAS_NOW(power, short)

    return composed


def has_now_short(player, event):
    return has_now(player, event, None, True)
