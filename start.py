#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from services.store import player_list, get_alive_players_count, update_action_event_list
import services.store

from services.simulation import *
from services.items import *
from services.battles import *
from services.players import *
from services.places import *
from services.api import initialize_avatars

finished = False
previous_enabled_action_list = []
previous_enabled_event_list = []


def initialize():
    initialize_avatars()
    if config.general.match_type == MatchType.districts:
        for i, tweet in enumerate(introduction_tweet_list):
            write_tweet(tweet)
    start_battle()


def start_battle():
    if config.general.match_type != MatchType.rumble:
        tweet = Tweet()
        tweet.is_event = True
        tweet.type = 'start'
        write_tweet(tweet)
        tweet.type = 'start_2'
        write_tweet(tweet)

    while not finished:
        simulate_day()


def simulate_day():
    if services.store.hour_count == 1:
        first_day()
    services.store.hour_count = services.store.hour_count + 1
    if config.general.match_type == MatchType.rumble:
        if len(get_players_in_place(place_list[0])) < 2 or config.general.entrance_countdown == 0:
            config.general.entrance_countdown = 3
            next_entrance()
            return
        else:
            config.general.entrance_countdown = config.general.entrance_countdown - 1

    do_something()

    if config.general.match_type == MatchType.districts and get_alive_districts_count() <= 1:
        end_districts()
    elif get_alive_players_count() <= 1:
        end()


def first_day():
    global previous_enabled_action_list
    previous_enabled_action_list = services.store.enabled_action_list


def do_something():
    global previous_enabled_action_list, previous_enabled_event_list
    completed = False
    update_action_event_list()

    if services.store.hour_count > 2:
        if len(services.store.enabled_action_list) > len(previous_enabled_action_list):
            # actions
            new_action = next(x for x in services.store.enabled_action_list if x not in previous_enabled_action_list)
            tweet = Tweet()
            tweet.is_event = True
            tweet.type = new_action.name
            write_tweet(tweet)
            previous_enabled_action_list = services.store.enabled_action_list
        elif len(services.store.enabled_event_list) != len(previous_enabled_event_list):
            if len(services.store.enabled_event_list) > len(previous_enabled_event_list):
                # new event
                event = next(x for x in services.store.enabled_event_list if x not in previous_enabled_event_list)
            else:
                # finished event
                event = next(x for x in previous_enabled_event_list if x not in services.store.enabled_event_list)
                event.name = event.name + '_end'

            tweet = handle_event(event)
            write_tweet(tweet)
            previous_enabled_event_list = services.store.enabled_event_list

    total_enabled_action_list_probab = sum(a.probability for a in services.store.enabled_action_list)
    action_number = random.randint(1, total_enabled_action_list_probab)

    chosen_action = None
    i = 0
    accumulated_probab = 0
    while chosen_action is None:
        if action_number > (total_enabled_action_list_probab - accumulated_probab - services.store.enabled_action_list[
            i].probability):
            chosen_action = services.store.enabled_action_list[i].name
        else:
            accumulated_probab = accumulated_probab + services.store.enabled_action_list[i].probability
            i = i + 1

    if chosen_action == "suicide":
        completed = suicide()
    elif chosen_action == "revive":
        completed = revive()
    elif chosen_action == "trap":
        completed = trap()
    elif chosen_action == "infect":
        completed = infect()
    elif chosen_action == "destroy":
        completed = destroy()
    elif chosen_action == "attract":
        completed = attract()
    elif chosen_action == "monster":
        completed = monster()
    elif chosen_action == "steal":
        completed = steal()
    elif chosen_action == "move":
        completed = move()
    elif chosen_action == "pick_item":
        completed = pick_item()
    elif chosen_action == "battle":
        can_move = is_a_or_e_enabled('move')
        no_rivals = get_two_players_in_random_place(
            include_treasons=is_a_or_e_enabled('treason', is_action=False)) == (None, None, None)
        peace = is_a_or_e_enabled('peace', is_action=False)
        if no_rivals or peace:
            if can_move:
                completed = move()
            else:
                completed = pick_item()
        else:
            completed = battle()

    if not completed and config.general.match_type != MatchType.rumble:
        do_something()


def end():
    global finished
    alive_players = get_alive_players()
    if len(alive_players) == 1:
        player = alive_players[0]
        tweet = Tweet()
        tweet.type = TweetType.winner
        tweet.place = player.location
        tweet.player = player
        write_tweet(tweet)
    elif len(alive_players) == 0:
        tweet = Tweet()
        tweet.type = TweetType.nobody_won
        write_tweet(tweet)
    finished = True


def end_districts():
    global finished
    alive_players = get_alive_players()
    tweet = Tweet()
    tweet.type = TweetType.winner_districts
    tweet.player_list = [x for x in player_list if x.district.name == alive_players[0].district.name and x.is_alive]
    tweet.place = alive_players[0].district
    write_tweet(tweet)
    finished = True


initialize()
