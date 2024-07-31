#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from services.simulation import write_tweet

from services.store import *


def attract():
    loc_candidates = []

    for i, p in enumerate(place_list):
        if not p.destroyed and not p.attracted and (
                config.general.max_attracted_players == 0 or len([x for x in p.players if x.is_alive]) < config.general.max_attracted_players):
            loc_candidates.append(p)

    if len(loc_candidates) == 0:
        return False

    place = random.choice(loc_candidates)
    place.attracted = True
    attracted_players = []

    def append_players_from(location):
        for j, player in enumerate([x for x in location.players if x.is_alive]):
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
                elif not player.infection_immunity:
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
    candidates_list = [x for x in get_alive_players() if x.location.trap_by is None]

    if len(candidates_list) == 0:
        return False

    player = random.choice(candidates_list)
    place = player.location
    place.trap_by = player
    tweet = Tweet()
    tweet.type = TweetType.trap
    tweet.place = place
    tweet.player = player
    write_tweet(tweet)
    return True


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

    there_was_infection, infected_or_was_infected_by = who_infected_who(player, [x for x in new_location.players if x.is_alive])

    move_together_with = None
    if action_number > 75 and len(player.location.players) > 0 and len(player.friend_list) > 0:
        next_to_him = player.location.players
        friends = player.friend_list
        random.shuffle(next_to_him)
        random.shuffle(friends)
        for i, p in enumerate(next_to_him):
            friend_next_to_him = next((x for x in friends if x.username != player.username and x.username == p.username and x.is_alive), None)
            if friend_next_to_him is not None:
                move_together_with = friend_next_to_him
                break

    if new_location.trap_by is not None and new_location.trap_by.get_name() != player.get_name() and not are_friends(
            new_location.trap_by, player) and not move_together_with:
        if action_number + int(5 * player.get_power()) < 50:
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
        if move_together_with is not None:
            tweet.type = TweetType.somebody_moved_together_with
            tweet.player_2 = move_together_with
            move_player(move_together_with, new_location)
        else:
            tweet.type = TweetType.somebody_moved
            if action_number > 90 and len(powerup_list) > 0:
                powerup = random.choice(powerup_list)
                player.powerup_list.append(powerup)
                tweet.item = powerup
            elif action_number > 70:
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
            if len(player.item_list) == 0:
                return False

            item = random.choice(player.item_list)
            index = player.item_list.index(item)
            player.item_list.pop(index)

            tweet = Tweet()
            tweet.type = TweetType.monster_took
            tweet.place = player.location
            tweet.player = player
            tweet.item = item
            write_tweet(tweet)
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


def zombie():
    zombie_player = [x for x in get_dead_players() if x.is_zombie]

    if len(zombie_player) > 0:
        zombie_player = zombie_player[0]
        place = zombie_player.location
        action_number = random.randint(1, 100)
        people_list = [x for x in place.players if x.is_alive]

        if len(people_list) == 0 or action_number < 20:
            place.zombie = False
            loc_candidates = [x for x in place.connection_list if not x.destroyed]

            if len(loc_candidates) == 0:
                return False

            new_place = random.choice(loc_candidates)
            new_place.zombie = True
            place.players.pop(place.players.index(zombie_player))
            zombie_player.location = new_place
            new_place.players.append(zombie_player)

            tweet = Tweet()
            tweet.type = TweetType.zombie_moved
            tweet.place = new_place
            tweet.place_2 = place
            tweet.player = zombie_player
            write_tweet(tweet)
        else:
            player = random.choice(people_list)

            if action_number < 50 and not player.zombie_immunity:
                kill_player(player)

                tweet = Tweet()
                tweet.type = TweetType.zombie_killed
                tweet.place = player.location
                tweet.player = player
                tweet.player_2 = zombie_player
                write_tweet(tweet)

                if config.general.match_type == MatchType.districts:
                    destroy_tweet = destroy_district_if_needed(player.district)
                    if destroy_tweet is not None:
                        write_tweet(destroy_tweet)
            else:
                place.zombie = False
                zombie_player.is_zombie = False

                tweet = Tweet()
                tweet.type = TweetType.zombie_was_defeated
                tweet.place = player.location
                tweet.player = player
                tweet.player_2 = zombie_player
                write_tweet(tweet)
    else:
        zombie_candidates = [x for x in get_dead_players() if not x.is_alive and not x.zombie_immunity and not x.location.destroyed]
        if len(zombie_candidates) == 0:
            return False
        new_zombie = random.choice(zombie_candidates)
        new_zombie.is_zombie = True

        loc_candidates = [x for x in new_zombie.location.connection_list if not x.destroyed]
        if new_zombie.location.name == new_zombie.district.name and len(loc_candidates) > 0:
            new_zombie.location.players.pop(new_zombie.location.players.index(new_zombie))
            place = random.choice(loc_candidates)
            place.players.append(new_zombie)
            new_zombie.location = place
            moved = True
        else:
            place = new_zombie.location
            moved = False

        place.zombie = True
        tweet = Tweet()
        tweet.type = TweetType.zombie_appeared
        tweet.place = new_zombie.location
        tweet.player = new_zombie
        tweet.double = moved
        write_tweet(tweet)
    return True


def doctor():
    place = [x for x in place_list if x.doctor]
    action_number = random.randint(0, 100)
    
    if len(place) > 0:
        place = place[0]
        people_list = [x for x in place.players if x.is_alive]

        if action_number > 70 and len(people_list) > 0:
            player = random.choice(people_list)

            item = Item()
            item.type = ItemType.powerup
            item.power = random.randint(config.items.min_power_powerup, config.items.max_power_powerup - 1)
            player.powerup_list.append(item)
            
            injures = 0
            for i, inj in enumerate(player.injury_list):
                injures += inj.power * -1

            player.injury_list = []

            tweet = Tweet()
            tweet.type = TweetType.doctor_cured
            tweet.place = player.location
            tweet.player = player
            tweet.factor = item.power + injures
            write_tweet(tweet)
        else:
            place.doctor = False
            loc_candidates = [x for x in place.connection_list if not x.destroyed]
            loc_candidates_to_cure = [x for x in loc_candidates if any(y for y in x.players if y.is_alive and len(y.injury_list) > 0)]
            if len(loc_candidates_to_cure) > 0:
                loc_candidates = loc_candidates_to_cure

            if len(loc_candidates) > 0:
                new_place = random.choice(loc_candidates)
                new_place.doctor = True
                tweet = Tweet()
                tweet.type = TweetType.doctor_moved
                tweet.place = new_place
                tweet.place_2 = place
                write_tweet(tweet)
            else:
                return False
    else:
        loc_candidates = [x for x in place_list if not x.destroyed]

        new_place = random.choice(loc_candidates)
        new_place.doctor = True
        tweet = Tweet()
        tweet.type = TweetType.doctor_appeared
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
    place.zombie = False
    place.trap_by = None
    place.doctor = None
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
        if p.is_zombie:
            p.is_zombie = False
        elif p.is_alive:
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
        elif not p.infection_immunity:
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
