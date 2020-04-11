from data.literals import *
from services.simulation import write_tweet
from models.tweet_type import Tweet_type

def kill(player_list, place_list, player_1, player_2, place):
    player_2.state = 0
    place.players.pop(place.players.index(player_2))

    player_1.kills = player_1.kills + 1
    best_player_1_item = player_1.get_best_item()
    best_player_2_item = player_2.get_best_item()
    are_friends = is_friend(player_1, player_2)

    if best_player_2_item != None and len(player_1.item_list) == 2 and (best_player_1_item.get_value() < best_player_2_item.get_value()):
        player_1.item_list = [best_player_1_item, best_player_2_item]
        player_2.item_list.pop(player_2.item_list.index(best_player_2_item))

        old_item = player_1.get_worst_item()
        player_1.location.items.append(old_item)
        player_1.location.items = player_1.location.items + player_2.item_list

        write_tweet(Tweet_type.somebody_killed, player_list, place_list, place, [player_1, player_2, are_friends, best_player_1_item, best_player_2_item, old_item])
    elif best_player_2_item != None and len(player_1.item_list) < 2:
        if best_player_1_item != None:
            player_1.item_list = [best_player_1_item, best_player_2_item]
        else:
            player_1.item_list = [best_player_2_item]
        player_2.item_list.pop(player_2.item_list.index(best_player_2_item))

        player_1.location.items = player_1.location.items + player_2.item_list
        write_tweet(Tweet_type.somebody_killed, player_list, place_list, place, [player_1, player_2, are_friends, best_player_1_item, best_player_2_item])
    else:
        player_1.location.items = player_1.location.items + player_2.item_list
        write_tweet(Tweet_type.somebody_killed, player_list, place_list, place, [player_1, player_2, are_friends, best_player_1_item])

def tie(player_list, place_list, player_1, player_2):
    if not is_friend(player_1, player_2):
        friend(player_1, player_2)
        write_tweet(Tweet_type.somebody_tied_and_became_friend, player_list, place_list, player_1.location, [player_1, player_2])
    else:
        write_tweet(Tweet_type.somebody_tied_and_was_friend, player_list, place_list, player_1.location, [player_1, player_2])

def run_away(player_list, place_list, player_1, player_2):
    if is_friend(player_1, player_2):
        unfriend(player_1, player_2)
        write_tweet(Tweet_type.somebody_escaped, player_list, place_list, player_1.location, [player_1, player_2, True])
    else:
        write_tweet(Tweet_type.somebody_escaped, player_list, place_list, player_1.location, [player_1, player_2])

def stealing(player_list, place_list, player_1, player_2):
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
        write_tweet(Tweet_type.somebody_stole, player_list, place_list, robber.location, [robber, robbed, item])
        return True

    else:
        if robber.item_list[0].get_value() >= robber.item_list[1].get_value():
            worst_item = robber.item_list[1]
            best_item = robber.item_list[0]
        else:
            worst_item = robber.item_list[0]
            best_item = robber.item_list[1]

        if item.get_value() > worst_item.get_value():
            robber.item_list = [item, best_item]
            write_tweet(Tweet_type.somebody_stole_and_replaced, player_list, place_list, robber.location, [robber, robbed, item, worst_item])
            return True
        else:
            write_tweet(Tweet_type.somebody_stole_and_threw, player_list, place_list, robber.location, [robber, robbed, item])
            return True

def friend(player_1, player_2):
    if not player_2 in player_1.friend_list:
        player_1.friend_list.append(player_2)
    if not player_1 in player_2.friend_list:
        player_2.friend_list.append(player_1)

def unfriend(player_1, player_2):
    if player_2 in player_1.friend_list:
        player_1.friend_list.remove(player_2)
    if player_1 in player_2.friend_list:
        player_2.friend_list.remove(player_1)

def is_friend(player, candidate):
    if candidate in player.friend_list:
        return True

def kill_player(player):
    place = player.location
    player.state = 0
    place.items = place.items + player.item_list
    player.item_list = []
    place.players.pop(place.players.index(player))
