#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from services.simulation import write_tweet

from services.store import *


def attract():
    loc_candidates = []

    for i, p in enumerate(place_list):
        if not p.destroyed and not p.attracted and (
                config.general.max_attracted_players == 0 or len(p.players) < config.general.max_attracted_players):
            loc_candidates.append(p)

    if len(loc_candidates) == 0:
        return False

    place = random.choice(loc_candidates)
    place.attracted = True
    attracted_players = []

    def append_players_from(location):
        for j, player in enumerate(location.players):
            if player.is_alive and player not in attracted_players:
                attracted_players.append(player)

    attract_range = int(100 / 100 * len([x for x in place_list if not x.destroyed]) / len(place_list))
    append_players_from(place)
    for i, connection in enumerate(place.connection_list):
        append_players_from(connection)
        if attract_range > 1:
            for j, subconnection in enumerate(connection.connection_list):
                append_players_from(subconnection)
                if attract_range > 2:
                    for k, subsubconnection in enumerate(subconnection.connection_list):
                        append_players_from(subsubconnection)

    if len(attracted_players) > sum(player.is_alive for player in place.players):
        if config.general.max_attracted_players > 0 and len(attracted_players) > config.general.max_attracted_players:
            attracted_players = attracted_players[:config.general.max_attracted_players]
        alive_players = get_alive_players()

        any_infected = False
        any_healthy = False
        for i, player in enumerate(alive_players):
            if player in attracted_players:
                if player.infected:
                    any_infected = True
                else:
                    any_healthy = True
                move_player(player, place)

        tweet = Tweet()
        tweet.type = TweetType.attraction
        tweet.place = place
        if any_infected and any_healthy:
            tweet.there_was_infection = True
        tweet.player_list = attracted_players
        write_tweet(tweet)
        return True
    else:
        attract()


def trap():
    list = []
    for i, p in enumerate(place_list):
        if p.trap_by is None and len(p.players) > 0:
            any_alive = False
            for j, q in enumerate(p.players):
                if q.is_alive:
                    any_alive = True
            if any_alive:
                list.append(p)

    if len(list) > 0:
        candidates_list = []
        while len(candidates_list) == 0:
            place = random.choice(list)
            for i, p in enumerate(place.players):
                if p.is_alive:
                    candidates_list.append(p)

        player = random.choice(candidates_list)

        place.trap_by = player
        tweet = Tweet()
        tweet.type = TweetType.trap
        tweet.place = place
        tweet.player = player
        write_tweet(tweet)
        return True
    else:
        return False


def move():
    alive_players = get_alive_players()
    player = random.choice(alive_players)

    loc_candidates = []

    for i, l in enumerate(player.location.connection_list):
        if not l.destroyed:
            loc_candidates.append(l)

    if len(loc_candidates) == 0:
        for j, c in enumerate(player.location.connection_list):
            for k, sc in enumerate(c.connection_list):
                if not sc.destroyed and sc.name != player.location.name:
                    loc_candidates.append(sc)

    if len(loc_candidates) == 0 or player.movement_boost:
        for j, c in enumerate(player.location.connection_list):
            for k, sc in enumerate(c.connection_list):
                for l, ssc in enumerate(sc.connection_list):
                    if not ssc.destroyed and ssc.name != player.location.name:
                        loc_candidates.append(ssc)

    if len(loc_candidates) == 0:
        for j, c in enumerate(player.location.connection_list):
            for k, sc in enumerate(c.connection_list):
                for l, ssc in enumerate(sc.connection_list):
                    for m, sssc in enumerate(ssc.connection_list):
                        if not sssc.destroyed and sssc.name != player.location.name:
                            loc_candidates.append(sssc)

    if len(loc_candidates) == 0:
        candidates = [x for x in place_list if not x.destroyed and x.name != player.location.name]
        if len(candidates) == 0:
            return False
        else:
            new_location = random.choice(candidates)
    else:
        new_location = random.choice(loc_candidates)

    action_number = random.randint(1, 100)

    tweet = Tweet()

    there_was_infection, infected_or_was_infected_by = who_infected_who(player, new_location.players)

    if new_location.trap_by is not None and new_location.trap_by.get_name() != player.get_name() and not are_friends(
            new_location.trap_by, player):
        if action_number < 50:
            trapped_by = new_location.trap_by
            new_location.trap_by.kills = new_location.trap_by.kills + 1
            move_player(player, new_location, False)
            kill_player(player)
            tweet.type = TweetType.trapped
            tweet.place = player.location
            tweet.player = player
            tweet.player_2 = trapped_by
            write_tweet(tweet)
            if config.general.match_type == MatchType.districts:
                destroy_tweet = destroy_district_if_needed(player.district)
                if destroy_tweet is not None:
                    write_tweet(destroy_tweet)
        else:
            trapped_by = new_location.trap_by
            new_location.trap_by = None
            tweet.there_was_infection = there_was_infection
            tweet.infected_or_was_infected_by = infected_or_was_infected_by
            move_player(player, new_location)
            tweet = Tweet()
            tweet.type = TweetType.trap_dodged
            tweet.place = player.location
            tweet.player = player
            tweet.player_2 = trapped_by
            write_tweet(tweet)
    else:
        tweet = Tweet()
        if action_number > 90 and len(powerup_list) > 0:
            powerup = random.choice(powerup_list)
            player.powerup_list.append(powerup)
            tweet.item = powerup
        elif action_number > 80:
            player.power = player.power + 2
            tweet.double = True
        elif action_number > 60 and not player.injure_immunity:
            injury = random.choice(injury_list)
            player.injury_list.append(injury)
            tweet.item = injury

        old_location = player.location
        tweet.there_was_infection = there_was_infection
        tweet.infected_or_was_infected_by = infected_or_was_infected_by
        move_player(player, new_location)

        tweet.type = TweetType.somebody_moved
        tweet.place = player.location
        tweet.place_2 = old_location
        tweet.player = player
        write_tweet(tweet)
    return True


def monster():
    place = [x for x in place_list if x.monster]

    if len(place) > 0:
        place = place[0]
        action_number = random.randint(1, 100)
        people_list = [x for x in place.players if x.is_alive and not x.monster_immunity]

        if action_number < 50 and len(people_list) > 0:
            player = random.choice(people_list)
            kill_player(player)
            tweet = Tweet()
            tweet.type = TweetType.monster_killed
            tweet.place = player.location
            tweet.player = player
            write_tweet(tweet)
            if config.general.match_type == MatchType.districts:
                destroy_tweet = destroy_district_if_needed(player.district)
                if destroy_tweet is not None:
                    write_tweet(destroy_tweet)
        else:
            place.monster = False
            loc_candidates = [x for x in place.connection_list if not x.destroyed]

            if len(loc_candidates) > 0 and action_number < 75:
                new_place = random.choice(loc_candidates)
                new_place.monster = True
                tweet = Tweet()
                tweet.type = TweetType.monster_moved
                tweet.place = new_place
                tweet.place_2 = place
                write_tweet(tweet)
            else:
                return False
    else:
        loc_candidates = [x for x in place_list if not x.destroyed]

        new_place = random.choice(loc_candidates)
        new_place.monster = True
        tweet = Tweet()
        tweet.type = TweetType.monster_appeared
        tweet.place = new_place
        write_tweet(tweet)
    return True


def destroy():
    if config.general.match_type == MatchType.districts:
        return False
    list = [x for x in place_list if not x.destroyed]
    if len(list) == 0:
        sys.exit('Error: everything is destroyed')
    place = random.choice(list)

    place.destroyed = True
    place.monster = False
    place.trap_by = None
    place.items = []
    dead_list = []
    escaped_list = []
    route_list = []
    new_location = None

    for j, c in enumerate(place.connection_list):
        if not c.destroyed:
            route_list.append(c)

    if len(route_list) > 0:
        new_location = random.choice(route_list)
    else:
        for j, c in enumerate(place.connection_list):
            for k, sc in enumerate(c.connection_list):
                if not sc.destroyed:
                    route_list.append(sc)

    if len(route_list) > 0:
        new_location = random.choice(route_list)
    else:
        for j, c in enumerate(place.connection_list):
            for k, sc in enumerate(c.connection_list):
                for k, ssc in enumerate(sc.connection_list):
                    if not ssc.destroyed:
                        route_list.append(ssc)

    new_location = random.choice(route_list)

    for i, p in enumerate(place.players):
        if p.is_alive:
            if random.randint(0, 100) >= 75:
                escaped_list.append(p)
            else:
                kill_player(p)
                dead_list.append(p)

    any_infected = False
    any_healthy = False

    for i, p in enumerate(escaped_list):
        if p.infected:
            any_infected = True
        else:
            any_healthy = True
        move_player(p, new_location)

    tweet = Tweet()
    tweet.type = TweetType.destroyed
    tweet.place = place
    tweet.place_2 = new_location
    tweet.player_list = dead_list
    tweet.player_list_2 = escaped_list
    if any_infected and any_healthy:
        tweet.there_was_infection = True
    write_tweet(tweet)
    return True
