import random
from services.store import *
from services.config import config
from services.simulation import write_tweet
from models.tweet import Tweet
from models.enums import *


def pick_item():
    alive_players = get_alive_players()
    players_with_items = [x for x in alive_players if x.location is not None and len(x.location.items) > 0]

    if len(players_with_items) == 0:
        return False

    player = random.choice(players_with_items)
    item = random.choice(player.location.items)

    success = False

    if item.type == ItemType.weapon:
        success = pick_weapon(player, item)
    elif item.type == ItemType.special:
        success = pick_special(player, item)

    return success


def pick_weapon(player, weapon):
    if len(player.item_list) <= 1:
        player.item_list.append(weapon)
        player.location.items.pop(player.location.items.index(weapon))
        tweet = Tweet()
        tweet.type = TweetType.somebody_found_item
        tweet.player = player
        tweet.place = player.location
        tweet.item = weapon
        write_tweet(tweet)
    else:
        if player.item_list[0].power >= player.item_list[1].power:
            worst_item = player.item_list[1]
            best_item = player.item_list[0]
        else:
            worst_item = player.item_list[0]
            best_item = player.item_list[1]

        if weapon.power > worst_item.power:
            player.item_list = [weapon, best_item]
            player.location.items.pop(player.location.items.index(weapon))
            tweet = Tweet()
            tweet.type = TweetType.somebody_replaced_item
            tweet.place = player.location
            tweet.item = weapon
            tweet.old_item = worst_item
            tweet.player = player
            write_tweet(tweet)
        else:
            return False
    return True


def pick_special(player, item):
    if item.special == SpecialType.injure_immunity:
        player.injure_immunity = True
    if item.special == SpecialType.monster_immunity:
        player.monster_immunity = True
    if item.special == SpecialType.infection_immunity:
        player.infection_immunity = True

    if config.general.match_type == MatchType.districts:
        others_in_district = [x for x in get_alive_players() if
                              x.district.name == player.district.name and x.get_name() != player.get_name()]
        if len(others_in_district) > 0:
            for i, pl in enumerate(others_in_district):
                pl.injure_immunity = player.injure_immunity
                pl.monster_immunity = player.monster_immunity
                pl.infection_immunity = player.infection_immunity

    player.location.items.pop(player.location.items.index(item))
    tweet = Tweet()
    tweet.type = TweetType.somebody_got_special
    tweet.place = player.location
    tweet.item = item
    tweet.player = player
    if config.general.match_type == MatchType.districts and len(others_in_district) > 0:
        tweet.player_list = others_in_district
    write_tweet(tweet)
    return True


def infect():
    any_infection = any(x for x in player_list if x.infected)
    alive_players = get_alive_players()
    infected_players = []
    healthy_players = []
    for i, p in enumerate(alive_players):
        if p.infected:
            infected_players.append(p)
        elif not p.infection_immunity:
            healthy_players.append(p)

    if not any_infection and len(healthy_players) > 0:
        player = random.choice(healthy_players)
        if not player.infection_immunity:
            player.infected = True
        affected = [x for x in player.location.players if x.name != player.name]
        for i, p in enumerate(affected):
            if not p.infection_immunity:
                p.infected = True

        tweet = Tweet()
        tweet.type = TweetType.somebody_was_infected
        tweet.place = player.location
        tweet.player = player
        tweet.player_list = affected
        write_tweet(tweet)
    elif len(infected_players) > 0:
        player = random.choice(infected_players)
        action_number = random.randint(1, 100)
        if action_number > 60:
            player.infected = False
            player.infection_immunity = True
            tweet = Tweet()
            tweet.type = TweetType.somebody_got_cured
            tweet.place = player.location
            tweet.player = player
            write_tweet(tweet)
        else:
            kill_player(player)
            tweet = Tweet()
            tweet.type = TweetType.somebody_died_of_infection
            tweet.place = player.location
            tweet.player = player
            write_tweet(tweet)
            if config.general.match_type == MatchType.districts:
                destroy_tweet = destroy_district_if_needed(player.district)
                if destroy_tweet is not None:
                    write_tweet(destroy_tweet)
    else:
        return False
    return True
