#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
from models.item import Item
from models.place import Place
from models.tweet import Tweet
from models.player import Player
from models.enums import *

from data.config import config

abducted_username = None
item_list = []
spare_item_list = []
place_list = []
player_list = []
powerup_list = []
introduction_tweet_list = []
injury_list = []
enabled_action_list = []
enabled_event_list = []
hour_count = None


def initialize_item_list():
    for i, group in enumerate(config.weapon_list):
        for j, weapon in enumerate(group.suffix_list):
            item = Item()
            item.type = ItemType.weapon
            item.name = weapon
            item.prefix_list = group.prefix_list
            item.power = random.randint(config.items.min_power_weapon, config.items.max_power_weapon)
            item_list.append(item)

    for i, special in enumerate(config.special_list):
        for j, special_name in enumerate(special.friendship_boost_list):
            item = Item()
            item.type = ItemType.special
            item.name = special_name
            item.special = SpecialType.friendship_boost
            item_list.append(item)
        for j, special_name in enumerate(special.monster_immunity_list):
            item = Item()
            item.type = ItemType.special
            item.name = special_name
            item.special = SpecialType.monster_immunity
            item_list.append(item)
        for j, special_name in enumerate(special.injure_immunity_list):
            item = Item()
            item.type = ItemType.special
            item.name = special_name
            item.special = SpecialType.injure_immunity
            item_list.append(item)
        # for j, special_name in enumerate(special.infection_immunity_list):
        #     item = Item()
        #     item.type = ItemType.special
        #     item.name = special_name
        #     item.special = SpecialType.infection_immunity
        #     item_list.append(item)
        for j, special_name in enumerate(special.movement_boost_list):
            item = Item()
            item.type = ItemType.special
            item.name = special_name
            item.special = SpecialType.movement_boost
            item_list.append(item)
        for j, special_name in enumerate(special.zombie_immunity_list):
            item = Item()
            item.type = ItemType.special
            item.name = special_name
            item.special = SpecialType.zombie_immunity
            item_list.append(item)

def initialize_powerup_list():
    for i, group in enumerate(config.powerup_list):
        for j, powerup in enumerate(group.suffix_list):
            item = Item()
            item.type = ItemType.powerup
            item.name = powerup
            item.prefix_list = group.prefix_list
            item.power = random.randint(config.items.min_power_powerup, config.items.max_power_powerup)
            powerup_list.append(item)


def initialize_injury_list():
    for i, group in enumerate(config.injury_list):
        for j, injury in enumerate(group.suffix_list):
            item = Item()
            item.type = ItemType.injury
            item.name = injury
            item.prefix_list = group.prefix_list
            item.power = - random.randint(config.items.min_power_injury, config.items.max_power_injury)
            injury_list.append(item)


def should_action_or_event_be_enabled(a_or_e, is_action=True):
    if a_or_e.name == 'destroy' and config.general.match_type == MatchType.districts:
        return False

    current_percentage = len(100 * get_dead_players()) / len(player_list)
    percentage_enabled = a_or_e.is_percentage and current_percentage >= a_or_e.enable_from

    time_enabled = not a_or_e.is_percentage and hour_count >= a_or_e.enable_from

    should_be_enabled = (not hasattr(a_or_e, 'probability') or a_or_e.probability > 0) and \
                        (percentage_enabled or time_enabled)

    if should_be_enabled and hasattr(a_or_e, 'duration'):
        if a_or_e.duration == 0:
            return False
        a_or_e.duration = a_or_e.duration - 1

    return should_be_enabled


def update_action_event_list():
    global enabled_action_list, enabled_event_list

    enabled_actions = [a for a in config.action_list if should_action_or_event_be_enabled(a)]
    sorted(enabled_actions, key=lambda x: x.probability, reverse=False)
    enabled_action_list = enabled_actions

    enabled_event_list = [e for e in config.event_list if should_action_or_event_be_enabled(e, is_action=False)]


def get_items_in_place(item_list_1, item_list_2, item_list_3, airdrop=False):
    items = []
    item_count = random.randint(config.items.min_items_in_place, config.items.max_items_in_place)
    if airdrop:
        item_count = item_count - 1
    special_added = False

    while item_count > 0 and len(item_list_1) + len(item_list_2) + len(item_list_3) > 0:
        action_number = random.randint(1, 100)
        item = None
        specials_left = [x for x in item_list_3 if x.special is not None]

        if not special_added and len(specials_left) > 0:
            item = random.choice(specials_left)
            item_list_3.pop(item_list_3.index(item))
            special_added = True
        elif action_number < config.items.probabilities.rarity_1:
            if len(item_list_1) > 0:
                item = random.choice(item_list_1)
                item_list_1.pop(item_list_1.index(item))
        elif action_number < config.items.probabilities.rarity_1 + config.items.probabilities.rarity_2:
            if len(item_list_2) > 0:
                item = random.choice(item_list_2)
                item_list_2.pop(item_list_2.index(item))
        else:
            if len(item_list_3) > 0:
                item = random.choice(item_list_3)
                item_list_3.pop(item_list_3.index(item))

        if item is not None:
            items.append(item)
            item_count = item_count - 1

    return items


def initialize_place_and_player_list():
    global player_list, spare_item_list
    raw_place_list = config.place_list
    raw_player_list = []
    item_list_1 = []
    item_list_2 = []
    item_list_3 = []

    def initialize_connection_list(places_list, place):
        connections_list = []
        road_connection_list = []
        water_connection_list = []

        for i, c in enumerate(place.connection_list):
            connection = get_place_by_name(places_list, c)
            if connection is not None:
                connections_list.append(connection)
        for i, c in enumerate(place.road_connection_list):
            connection = get_place_by_name(places_list, c)
            if connection is not None:
                road_connection_list.append(connection)
        for i, c in enumerate(place.water_connection_list):
            connection = get_place_by_name(places_list, c)
            if connection is not None:
                water_connection_list.append(connection)

        place.connection_list = connections_list
        place.road_connection_list = road_connection_list
        place.water_connection_list = water_connection_list

    def fill_player_list(raw_place=None, place=None):
        global player_list

        for i, raw_player in enumerate(raw_place.player_list):
            player = Player()
            player.name = raw_player.name
            player.username = raw_player.username
            player.is_female = raw_player.is_female
            player.district = place

            # initial items
            initial_weapons = []
            if hasattr(raw_player, 'weapon_list'):
                for weapon_name in raw_player.weapon_list:
                    reserved_weapon = next(x for x in item_list if x.name == weapon_name)

                    initial_weapons.append(reserved_weapon)
                    item_list.pop(item_list.index(reserved_weapon))
            player.item_list = initial_weapons

            initial_powerups = []
            if hasattr(raw_player, 'powerup_list'):
                for powerup_name in raw_player.powerup_list:
                    reserved_powerup = next(x for x in powerup_list if x.name == powerup_name)
                    initial_powerups.append(reserved_powerup)
                    powerup_list.pop(powerup_list.index(reserved_powerup))
            player.powerup_list = initial_powerups

            player_list.append(player)
            if config.general.match_type == MatchType.districts:
                if raw_player is not None and player.district != '':
                    location = next(x for x in place_list if x.name == place.name)
                    player.district = location  # only to store p[3]
                    location.tributes.append(player)  # idem
            elif config.general.match_type == MatchType.standard:
                location = random.choice(place_list)
                player.location = location
                location.players.append(player)

    random.shuffle(item_list)
    for i, item in enumerate(item_list):
        if item.get_rarity() == 1:
            item_list_1.append(item)
        elif item.get_rarity() == 2:
            item_list_2.append(item)
        elif item.get_rarity() == 3:
            item_list_3.append(item)

    max_coord_x = 0
    max_coord_y = 0
    min_coord_x = 999
    min_coord_y = 999

    random.shuffle(raw_place_list)
    for i, raw_place in enumerate(raw_place_list):
        if raw_place.coordinates[0] > max_coord_x:
            max_coord_x = raw_place.coordinates[0]
        if raw_place.coordinates[1] > max_coord_y:
            max_coord_y = raw_place.coordinates[1]
        if raw_place.coordinates[0] < min_coord_x:
            min_coord_x = raw_place.coordinates[0]
        if raw_place.coordinates[1] < min_coord_y:
            min_coord_y = raw_place.coordinates[1]
        district_display_name = None
        road_connection_list = []
        water_connection_list = []

        items = []
        if len(raw_place.player_list) > 0 or not config.general.destroy_initial_empty_places:
            items = get_items_in_place(item_list_1, item_list_2, item_list_3)

        if hasattr(raw_place, 'district_display_name'):
            district_display_name = raw_place.district_display_name
        if hasattr(raw_place, 'road_connection_list'):
            road_connection_list = raw_place.road_connection_list
        if hasattr(raw_place, 'water_connection_list'):
            water_connection_list = raw_place.water_connection_list

        new_place = Place(raw_place.name, road_connection_list, raw_place.coordinates, items,
                          district_display_name, water_connection_list)
        place_list.append(new_place)
        # Print player list
        # if (len(raw_place.player_list) > 0):
        #     print(raw_place.name)
        #     a = []
        #     for i, raw_player in enumerate(raw_place.player_list):
        #         a.append(raw_player.name)
        #     print(a)
        fill_player_list(raw_place, new_place)
        if config.general.destroy_initial_empty_places and len(raw_place.player_list) == 0:
            new_place.destroyed = True

    spare_item_list = item_list_1 + item_list_2 + item_list_3
    for i, pl in enumerate(place_list):
        initialize_connection_list(place_list, pl)


def initialize_tributes():
    global player_list

    if config.general.redistribute_tributes:
        # Initialize and distribute the tributes per district
        free_tributes = [x for x in player_list if x.district is None]
        tributes_per_district = round(len(player_list) / len(place_list))
        random.shuffle(place_list)
        enough_tributes_list = [x for x in place_list if len(x.tributes) >= tributes_per_district]
        not_enough_tributes_list = [x for x in place_list if len(x.tributes) < tributes_per_district]

        # Districts with enough tributes
        for j, enough_tributes_district in enumerate(enough_tributes_list):
            exported_tributes = []

            index = len(enough_tributes_district.tributes) - tributes_per_district
            while index > 0:
                excess_tribute = random.choice(enough_tributes_district.tributes)
                free_tributes.append(excess_tribute)
                exported_tributes.append(excess_tribute)
                enough_tributes_district.tributes.remove(excess_tribute)
                index = index - 1

            tweet = Tweet()
            tweet.type = TweetType.introduce_players
            tweet.place = enough_tributes_district
            tweet.player_list = enough_tributes_district.tributes
            tweet.player_list_2 = exported_tributes
            introduction_tweet_list.append(tweet)

        # Districts with not enough tributes
        index = tributes_per_district

        while index > 0:
            for j, not_enough_tributes_district in enumerate(not_enough_tributes_list):
                if len(not_enough_tributes_district.tributes) < tributes_per_district and len(free_tributes) > 0:
                    chosen_tribute = random.choice(free_tributes)
                    free_tributes.remove(chosen_tribute)
                    chosen_tribute.location = not_enough_tributes_district
                    not_enough_tributes_district.tributes.append(chosen_tribute)
            index = index - 1

        for j, not_enough_tributes_district in enumerate(not_enough_tributes_list):

            imported_tributes = [x for x in not_enough_tributes_district.tributes if
                                 (x.district is None or x.district.name != not_enough_tributes_district.name)]
            local_tributes = [x for x in not_enough_tributes_district.tributes if
                              x.district is not None and x.district.name == not_enough_tributes_district.name]

            for j, imported in enumerate(imported_tributes):
                imported.district = not_enough_tributes_district

            tweet = Tweet()
            tweet.type = TweetType.introduce_players
            tweet.place = not_enough_tributes_district
            tweet.player_list = local_tributes
            tweet.player_list_2 = imported_tributes
            tweet.inverse = True
            introduction_tweet_list.append(tweet)
    else:
        random.shuffle(place_list)
        district_list = [x for x in place_list if len(x.tributes) > 0]
        for i, district in enumerate(district_list):
            tweet = Tweet()
            tweet.type = TweetType.introduce_players
            tweet.place = district
            tweet.player_list = district.tributes
            introduction_tweet_list.append(tweet)

    # Friends list
    for j, place in enumerate(place_list):
        for k, tribute in enumerate(place.tributes):
            tribute.district = place
            tribute.location = place
            place.players.append(tribute)
            tribute.friend_list = tribute.friend_list + [x for x in place.tributes if
                                                         x.get_name() != tribute.get_name()]


def get_player_by_name(name):
    return next(p for p in player_list if p.name == name)


def get_two_players_in_random_place(include_treasons=True):
    place_with_people_list = [x for x in place_list if any(p for p in x.players if p.is_alive)]
    candidates_list = []

    for i, place in enumerate(place_with_people_list):
        alive_players = [p for p in place.players if p.is_alive]
        for p1 in range(len(alive_players)):
            for p2 in range(p1 + 1, len(alive_players)):
                friends = are_friends(alive_players[p1], alive_players[p2])
                if not friends or \
                        (friends and include_treasons and is_a_or_e_enabled('treason', is_action=False)):
                    candidates_list.append([alive_players[p1], alive_players[p2]])

    if len(candidates_list) == 0:
        return None, None, None

    couple = random.choice(candidates_list)
    player_1 = couple[0]
    player_2 = couple[1]
    place = player_1.location

    return player_1, player_2, place


def handle_event(event):
    global abducted_username
    tweet = Tweet()
    tweet.is_event = True
    tweet.type = event.name

    if event.name == 'airdrop':
        item_list_1 = []
        item_list_2 = []
        item_list_3 = []
        for i, item in enumerate(spare_item_list):
            if item.get_rarity() == 1:
                item_list_1.append(item)
            elif item.get_rarity() == 2:
                item_list_2.append(item)
            elif item.get_rarity() == 3:
                item_list_3.append(item)

        alive_districts = [x for x in place_list if not x.destroyed and len([y for y in x.tributes if y.is_alive]) > 0]
        for i, district in enumerate(alive_districts):
            district.items = district.items + get_items_in_place(item_list_1, item_list_2, item_list_3, airdrop=True)
    elif event.name == 'abduction_1':
        abducted = random.choice(get_alive_players())
        abducted.is_alive = False
        abducted.location.players.pop(abducted.location.players.index(abducted))
        abducted_username = abducted.username
        tweet.player = abducted
        tweet.place = abducted.location
    elif event.name == 'abduction_1_end':
        abducted = next(x for x in get_dead_players() if x.username == abducted_username)
        abducted.is_alive = True
        abducted.power = abducted.power + 7.4

        new_place = random.choice(place_list)
        while new_place.name == abducted.location.name:
            new_place = random.choice(place_list)
        abducted.location = new_place
        new_place.players.append(abducted)

        tweet.player = abducted
        tweet.place = abducted.location
    elif event.name == 'abduction_2':
        alive_players = get_alive_players()
        random.shuffle(alive_players)
        abducted_1 = alive_players[0]
        abducted_2 = alive_players[1]
        while abducted_1.location.name == abducted_2.location.name:
            random.shuffle(alive_players)
            abducted_1 = alive_players[0]
            abducted_2 = alive_players[1]
        abducted_1.location.players.pop(abducted_1.location.players.index(abducted_1))
        abducted_2.location.players.pop(abducted_2.location.players.index(abducted_2))
        abducted_1.location.players.append(abducted_2)
        abducted_2.location.players.append(abducted_1)
        abducted_1.location, abducted_2.location = abducted_2.location, abducted_1.location

        tweet.player = abducted_1
        tweet.player_2 = abducted_2

        tweet.player = abducted_1
        tweet.player_2 = abducted_2
        tweet.place = abducted_1.location
        tweet.place_2 = abducted_2.location
    elif event.name == 'zombie':
        zombie = random.choice(get_dead_players())
        zombie.is_zombie = True
        zombie.location.zombie = True
        tweet.player = zombie
        tweet.place = zombie.location
    return tweet


def is_a_or_e_enabled(name, is_action=True):
    a_or_e_list = enabled_action_list if is_action else enabled_event_list
    return any(x for x in a_or_e_list if x.name == name)


def are_friends(player, candidate):
    return any(x for x in player.friend_list if x.get_name() == candidate.get_name()) and any(
        x for x in candidate.friend_list if x.get_name() == player.get_name())


def get_alive_players():
    return [p for p in player_list if p.is_alive]


def get_dead_players():
    return [p for p in player_list if not p.is_alive]


def get_alive_players_count():
    return len([x for x in player_list if x.is_alive])


def get_alive_districts_count():
    return len([x for x in place_list if not x.destroyed and len([y for y in x.tributes if y.is_alive]) > 0])


def get_place_by_name(place_list, name):
    return next((i for i in place_list if i.name == name), None)


def move_player(player, new_location, infect=True):
    if player.location is not None:
        player.location.players.pop(player.location.players.index(player))
    player.location = new_location
    new_location.players.append(player)

    players_in_place = [x for x in new_location.players if x.is_alive]
    if infect:
        if player.infected:
            for j, p in enumerate(players_in_place):
                if not p.infection_immunity:
                    p.infected = True
        elif any(x for x in players_in_place if x.infected and x.is_alive) and not player.infection_immunity:
            player.infected = True


def destroy_district_if_needed(district):
    if any(x for x in district.tributes if x.is_alive):
        return None

    district.destroyed = True
    district.monster = False
    district.zombie = False
    district.trap_by = None
    district.items = []
    district.doctor = None

    tributes_list = district.tributes
    escaped_list = []
    route_list = []
    new_location = False

    for j, c in enumerate(district.connection_list):
        if not c.destroyed:
            route_list.append(c)

    if len(route_list) == 0:
        for j, c in enumerate(district.connection_list):
            for k, sc in enumerate(c.connection_list):
                if not sc.destroyed and sc.name != district.name:
                    route_list.append(sc)

    if len(route_list) == 0:
        for j, c in enumerate(district.connection_list):
            for k, sc in enumerate(c.connection_list):
                for l, ssc in enumerate(sc.connection_list):
                    if not ssc.destroyed and ssc.name != district.name:
                        route_list.append(ssc)

    if len(route_list) == 0:
        for j, c in enumerate(district.connection_list):
            for k, sc in enumerate(c.connection_list):
                for l, ssc in enumerate(sc.connection_list):
                    for m, sssc in enumerate(ssc.connection_list):
                        if not sssc.destroyed and sssc.name != district.name:
                            route_list.append(sssc)

    if len(route_list) == 0:
        new_location = random.choice([x for x in place_list if not x.destroyed and x.name != district.name])
    else:
        new_location = random.choice(route_list)

    for i, p in enumerate(district.players):
        if p.is_zombie:
            p.is_zombie = False
        elif p.is_alive:
            escaped_list.append(p)

    any_infected = False
    any_healthy = False

    for i, p in enumerate(escaped_list + [x for x in new_location.players if x.is_alive]):
        if p.infected:
            any_infected = True
        elif not p.infection_immunity:
            any_healthy = True
        if p.is_alive:
            move_player(p, new_location)

    tweet = Tweet()
    tweet.type = TweetType.destroyed_district
    tweet.place = district
    tweet.place_2 = new_location
    tweet.player_list = tributes_list
    tweet.player_list_2 = escaped_list
    if any_infected and any_healthy:
        tweet.there_was_infection = True
    return tweet


def split_multiline_text(text, width, font):
    text_lines = []
    text_line = []
    text = text.replace('\n', ' [br] ')
    words = text.split()

    for word in words:
        if word == '[br]':
            text_lines.append(' '.join(text_line))
            text_line = []
            continue
        text_line.append(word)
        w, h = font.getsize(' '.join(text_line))
        if w > width and len(words) > 1:
            text_line.pop()
            text_lines.append(' '.join(text_line))
            text_line = [word]

    if len(text_line) > 0:
        text_lines.append(' '.join(text_line))

    return text_lines


def kill_player(player):
    place = player.location

    for i, item in enumerate(player.item_list):
        item.thrown_away_by = player

    place.items = place.items + player.item_list
    # place.players.pop(place.players.index(player))
    player.is_alive = False
    player.power = 0
    player.item_list = []
    player.injury_list = []
    player.powerup_list = []
    player.infected = False
    player.friendship_boost = False
    player.injure_immunity = False
    player.infection_immunity = False
    player.monster_immunity = False
    player.movement_boost = False
    player.zombie_immunity = False


def who_infected_who(player, list_of_players):
    any_infected = False
    any_healthy = False
    was_infected = False
    there_was_infection = False
    infected_or_was_infected_by = False

    if len(list_of_players) > 0:
        for i, p in enumerate(list_of_players):
            if p.infected:
                any_infected = True
            elif not p.infection_immunity:
                any_healthy = True
        if player.infected:
            was_infected = True
            any_infected = True
        elif not player.infection_immunity:
            any_healthy = True

        there_was_infection = any_infected and any_healthy
        infected_or_was_infected_by = there_was_infection and was_infected
    return there_was_infection, infected_or_was_infected_by


def any_players_around(place):
    return any([p for p in place_list if
                p.name != place.name and
                any([x for x in p.players if x.is_alive]) and
                abs(p.coord_x - place.coord_x) < config.map.avatar_size * 3 and
                 abs(p.coord_y - place.coord_y) < config.map.avatar_size * 3])


def get_players_in_place(place):
    alive_players = get_alive_players()
    players_in_place = [x for x in alive_players if x.location is not None and x.location.name == place.name]
    return players_in_place


def initialize():
    global hour_count
    hour_count = 0
    initialize_item_list()
    initialize_powerup_list()
    initialize_injury_list()
    initialize_place_and_player_list()
    if config.general.match_type == MatchType.districts:
        initialize_tributes()
    update_action_event_list()


initialize()
