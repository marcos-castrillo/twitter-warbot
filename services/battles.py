from data.literals import *
from services.simulation import write_tweet
from models.tweet_type import Tweet_type

def kill(player_list, player_1, player_2):
    player_2.state = 0
    player_1.kills = player_1.kills + 1
    best_player_1_item = player_1.get_best_item()
    best_player_2_item = player_2.get_best_item()
    are_friends = is_friend(player_1, player_2)

    if best_player_1_item != None and best_player_2_item != None and (best_player_1_item.get_value() < best_player_2_item.get_value()):
        old_item = player_1.get_worst_item()
        write_tweet(Tweet_type.somebody_killed, player_list, [player_1, player_2, are_friends, best_player_2_item, old_item])
        player_1.item_list = [best_player_1_item, best_player_2_item]
    elif best_player_2_item != None and best_player_1_item == None:
        old_item = player_1.get_worst_item()
        write_tweet(Tweet_type.somebody_killed, player_list, [player_1, player_2, are_friends, best_player_2_item])
        player_1.item_list = [best_player_2_item]
    else:
        write_tweet(Tweet_type.somebody_killed, player_list, [player_1, player_2, are_friends])

def tie(player_list, player_1, player_2):
    if not is_friend(player_1, player_2):
        friend(player_1, player_2)
        write_tweet(Tweet_type.somebody_tied_and_became_friend, player_list, [player_1, player_2])
    else:
        write_tweet(Tweet_type.somebody_tied_and_was_friend, player_list, [player_1, player_2])

def run_away(player_list, player_1, player_2):
    if is_friend(player_1, player_2):
        unfriend(player_1, player_2)
        write_tweet(Tweet_type.somebody_escaped, player_list, [player_1, player_2, True])
    else:
        write_tweet(Tweet_type.somebody_escaped, player_list, [player_1, player_2])

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
