from data.literals import *
from data.config import PROBAB_NEUTRAL, MATCH_TYPE, TREASONS_ENABLED_LIST
from store import *
from models.tweet import Tweet
from models.tweet_type import Tweet_type
from models.match_type import Match_type
from services.simulation import write_tweet

def battle():
    alive_players = get_alive_players()
    player_1, player_2, place = get_two_players_in_random_place()

    if (player_1, player_2) == (None, None):
        return False

    kill_number = random.randint(0, 100)
    treasons_enabled = TREASONS_ENABLED_LIST[hour_count]
    if are_friends(player_1, player_2):
        if not treasons_enabled:
            return False
        elif MATCH_TYPE != Match_type.rumble and kill_number > 15 and kill_number < 85:
            return False

    factor = 50 + 2*(player_1.get_defense() + player_1.get_attack()) - 2*(player_2.get_attack() + player_2.get_defense())
    if factor > 100:
        factor = 100
    if factor < 0:
        factor = 0

    success = False
    if kill_number >= factor - int((PROBAB_TIE - 1) / 2) and kill_number <= factor + int((PROBAB_TIE - 1) / 2):
        if get_alive_players_count() == 2:
            return
        success = tie(player_1, player_2, factor, kill_number)
    elif kill_number > factor - PROBAB_NEUTRAL and kill_number < factor:
        if MATCH_TYPE == Match_type.rumble:
            success = soft_attack(player_1, player_2, factor, kill_number, False)
        else:
            success = run_away(player_1, player_2, factor, kill_number, False)
    elif kill_number > factor and kill_number < factor + PROBAB_NEUTRAL:
        if MATCH_TYPE == Match_type.rumble:
            success = soft_attack(player_1, player_2, factor, kill_number, True)
        else:
            success = run_away(player_1, player_2, factor, kill_number, True)
    elif kill_number < factor - PROBAB_NEUTRAL:
        success = kill(player_1, player_2, place, factor, kill_number, False)
    elif kill_number > factor + PROBAB_NEUTRAL:
        success = kill(player_1, player_2, place, factor, kill_number, True)
    return success

def kill(player_1, player_2, place, factor, action_number, inverse):
    killer = player_1
    killed = player_2
    if inverse:
        killer = player_2
        killed = player_1

    killer.kills = killer.kills + 1
    if MATCH_TYPE == Match_type.rumble:
        best_killer_item = None
        best_killed_item = None
    else:
        best_killer_item = killer.get_best_item()
        best_killed_item = killed.get_best_item()
    friendship = are_friends(killer, killed)

    tweet = Tweet()
    tweet.type = Tweet_type.somebody_killed
    tweet.place = place
    tweet.player = player_1
    tweet.player_2 = player_2
    tweet.factor = factor
    tweet.action_number = action_number
    tweet.inverse = inverse
    tweet.item = killer.get_best_attack_item()

    if best_killed_item != None and len(killer.item_list) == 2 and (best_killer_item.get_value() < best_killed_item.get_value()):
        # Steal item and throw away
        killer.item_list = [best_killer_item, best_killed_item]
        killed.item_list.pop(killed.item_list.index(best_killed_item))

        old_item = killer.get_worst_item()
        killer.location.items.append(old_item)
        old_item.thrown_away_by = killer
        tweet.old_item = old_item
        tweet.new_item = best_killed_item
    elif best_killed_item != None and len(killer.item_list) < 2:
        # Steal item
        if best_killer_item != None:
            killer.item_list = [best_killer_item, best_killed_item]
        else:
            killer.item_list = [best_killed_item]
        killed.item_list.pop(killed.item_list.index(best_killed_item))

        tweet.new_item = best_killed_item

    place = killed.location
    place.players.pop(place.players.index(killed))
    killed.state = 0

    write_tweet(tweet)
    kill_player(killed)

    if MATCH_TYPE == Match_type.districts:
        destroy_tweet = destroy_district_if_needed(killed.district)
        if destroy_tweet != None:
            write_tweet(destroy_tweet)
    return True

def tie(player_1, player_2, factor, action_number):
    if not are_friends(player_1, player_2):
        befriend(player_1, player_2)
        tweet = Tweet()
        tweet.type = Tweet_type.somebody_tied_and_became_friend
        tweet.place = player_1.location
        tweet.player = player_1
        tweet.player_2 = player_2
        tweet.factor = factor
        tweet.action_number = action_number
        write_tweet(tweet)
    else:
        tweet = Tweet()
        tweet.type = Tweet_type.somebody_tied_and_was_friend
        tweet.place = player_1.location
        tweet.player = player_1
        tweet.player_2 = player_2
        tweet.factor = factor
        tweet.action_number = action_number
        write_tweet(tweet)
    return True

def run_away(player_1, player_2, factor, action_number, inverse):
    tweet = Tweet()

    candidates = [x for x in player_1.location.connections if not x.destroyed]

    if len(candidates) == 0:
        return False

    new_location = random.choice(candidates)

    if inverse:
        there_was_infection, infected_or_was_infected_by = who_infected_who(player_1, new_location.players)
        move_player(player_1, new_location)
        tweet.place = player_2.location
        tweet.place_2 = player_1.location
    else:
        there_was_infection, infected_or_was_infected_by = who_infected_who(player_1, new_location.players)
        move_player(player_2, new_location)
        tweet.place = player_1.location
        tweet.place_2 = player_2.location

    tweet.type = Tweet_type.somebody_escaped
    tweet.player = player_1
    tweet.player_2 = player_2
    tweet.factor = factor
    tweet.action_number = action_number
    tweet.inverse = inverse
    if there_was_infection:
        tweet.there_was_infection = True
    tweet.infected_or_was_infected_by = infected_or_was_infected_by

    if are_friends(player_1, player_2):
        unfriend(player_1, player_2)
        tweet.unfriend = True

    write_tweet(tweet)
    return True

def soft_attack(player_1, player_2, factor, action_number, inverse):
    tweet = Tweet()
    tweet.item = Item()

    if inverse:
        tweet.player = player_1
        tweet.player_2 = player_2
    else:
        tweet.player = player_2
        tweet.player_2 = player_1

    attack_loss = 0
    defense_loss = 0
    while attack_loss == 0 and defense_loss == 0:
        attack_loss = random.randint(-3, 0)
        defense_loss = random.randint(-3, 0)

    tweet.player_2.attack = tweet.player_2.attack + attack_loss
    tweet.player_2.defense = tweet.player_2.defense + defense_loss
    tweet.item.attack = attack_loss
    tweet.item.defense = defense_loss
    tweet.place = player_1.location
    tweet.type = Tweet_type.soft_attack
    tweet.factor = factor
    tweet.action_number = action_number
    tweet.inverse = inverse

    if are_friends(player_1, player_2):
        unfriend(player_1, player_2)
        tweet.unfriend = True

    write_tweet(tweet)
    return True

def steal():
    alive_players = get_alive_players()
    player_1, player_2, place = get_two_players_in_random_place()

    if (player_1, player_2) == (None, None) or are_friends(player_1, player_2):
        return False

    if len(player_1.item_list) > 0:
        robbed = player_1
        robber = player_2
    elif len(player_2.item_list) > 0:
        robbed = player_2
        robber = player_1
    else:
        return False

    item = random.choice(robbed.item_list)
    index = robbed.item_list.index(item)
    robbed.item_list.pop(index)

    if len(robber.item_list) <= 1:
        robber.item_list.append(item)
        tweet = Tweet()
        tweet.type = Tweet_type.somebody_stole
        tweet.place = robber.location
        tweet.player = robber
        tweet.player_2 = robbed
        tweet.item = item
        write_tweet(tweet)
    else:
        if robber.item_list[0].get_value() >= robber.item_list[1].get_value():
            worst_item = robber.item_list[1]
            best_item = robber.item_list[0]
        else:
            worst_item = robber.item_list[0]
            best_item = robber.item_list[1]

        if item.get_value() > worst_item.get_value():
            robber.item_list = [item, best_item]
            tweet = Tweet()
            tweet.type = Tweet_type.somebody_stole_and_replaced
            tweet.place = robber.location
            tweet.player = robber
            tweet.player_2 = robbed
            tweet.item = item
            tweet.old_item = worst_item
            write_tweet(tweet)
        else:
            tweet = Tweet()
            tweet.type = Tweet_type.somebody_stole_and_threw
            tweet.place = robber.location
            tweet.player = robber
            tweet.player_2 = robbed
            tweet.item = item
            write_tweet(tweet)
    return True

def befriend(player_1, player_2):
    if not player_2 in player_1.friend_list:
        player_1.friend_list.append(player_2)
    if not player_1 in player_2.friend_list:
        player_2.friend_list.append(player_1)

def unfriend(player_1, player_2):
    if player_2 in player_1.friend_list:
        player_1.friend_list.remove(player_2)
    if player_1 in player_2.friend_list:
        player_2.friend_list.remove(player_1)

def kill_player(player):
    place = player.location

    for i, item in enumerate(player.item_list):
        item.thrown_away_by = player

    place.items = place.items + player.item_list
    #place.players.pop(place.players.index(player))
    #player.state = 0
    player.attack = 0
    player.defense = 0
    player.item_list = []
    player.injury_list = []
    player.powerup_list = []
    player.infected = False
    player.monster_immunity = False
    player.injure_immunity = False
    player.infection_immunity = False
