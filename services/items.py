import random
from data.items import *
from store import get_two_players_in_random_place, get_alive_players, injury_list, kill_player, destroy_district_if_needed
from data.config import USE_DISTRICTS
from models.tweet import Tweet
from models.tweet_type import Tweet_type
from models.item_type import Item_type
from services.simulation import write_tweet

first_infection = False


def pick_item():
    alive_players = get_alive_players()
    players_with_items = [x for x in alive_players if len(x.location.items) > 0]

    if len(players_with_items) == 0:
        return False

    player = random.choice(players_with_items)
    item = random.choice(player.location.items)

    success = False

    if item.type == Item_type.weapon:
        success = pick_weapon(player, item)
    elif item.type == Item_type.special:
        success = pick_special(player, item)

    return success

def pick_weapon(player, weapon):
    if len(player.item_list) <= 1:
        player.item_list.append(weapon)
        player.location.items.pop(player.location.items.index(weapon))
        tweet = Tweet()
        tweet.type = Tweet_type.somebody_found_item
        tweet.player = player
        tweet.place = player.location
        tweet.item = weapon
        write_tweet(tweet)
    else:
        if player.item_list[0].get_value() >= player.item_list[1].get_value():
            worst_item = player.item_list[1]
            best_item = player.item_list[0]
        else:
            worst_item = player.item_list[0]
            best_item = player.item_list[1]

        if weapon.get_value() > worst_item.get_value():
            player.item_list = [weapon, best_item]
            player.location.items.pop(player.location.items.index(weapon))
            tweet = Tweet()
            tweet.type = Tweet_type.somebody_replaced_item
            tweet.place = player.location
            tweet.item = weapon
            tweet.old_item = worst_item
            tweet.player = player
            write_tweet(tweet)
        else:
            return False
    return True

def pick_special(player, special):
    if special.injure_immunity:
        player.injure_immunity = True
    if special.monster_immunity:
        player.monster_immunity = True
    if special.infection_immunity:
        player.infection_immunity = True

    player.location.items.pop(player.location.items.index(special))
    tweet = Tweet()
    tweet.type = Tweet_type.somebody_got_special
    tweet.place = player.location
    tweet.item = special
    tweet.player = player
    write_tweet(tweet)
    return True

def infect():
    global first_infection
    alive_players = get_alive_players()
    infected_players = []
    healthy_players = []
    for i, p in enumerate(alive_players):
        if p.infected:
            infected_players.append(p)
        elif not p.infection_immunity:
            healthy_players.append(p)

    if not first_infection:
        player = random.choice(healthy_players)
        player.location.infected = True
        if not player.infection_immunity:
            player.infected = True
        affected = [x for x in player.location.players if x.name != player.name]
        for i,p in enumerate(affected):
            if not p.infection_immunity:
                p.infected = True
        first_infection = True

        tweet = Tweet()
        tweet.type = Tweet_type.somebody_was_infected
        tweet.place = player.location
        tweet.player = player
        tweet.player_list = affected
        write_tweet(tweet)
    elif len(infected_players) > 0:
        player = random.choice(infected_players)
        action_number = random.randint(1, 100)
        if action_number > 75:
            player.infected = False
            player.infection_immunity = True
            tweet = Tweet()
            tweet.type = Tweet_type.somebody_got_cured
            tweet.place = player.location
            tweet.player = player
            write_tweet(tweet)
        else:
            kill_player(player)
            tweet = Tweet()
            tweet.type = Tweet_type.somebody_died_of_infection
            tweet.place = player.location
            tweet.player = player
            write_tweet(tweet)
            if USE_DISTRICTS:
                destroy_tweet = destroy_district_if_needed(player.district)
                if destroy_tweet != None:
                    write_tweet(destroy_tweet)
    else:
        return False
    return True
