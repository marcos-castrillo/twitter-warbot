import random
import sys
from models.tweet import Tweet
from models.tweet_type import Tweet_type
from services.simulation import write_tweet
from store import get_dead_players, get_alive_players, kill_player, place_list, destroy_district_if_needed
from config import USE_DISTRICTS

def befriend(player_1, player_2):
    if not player_2 in player_1.friend_list:
        player_1.friend_list.append(player_2)
    if not player_1 in player_2.friend_list:
        player_2.friend_list.append(player_1)

def suicide():
    alive_players = get_alive_players()
    player = random.choice(alive_players)
    kill_player(player)
    tweet = Tweet()
    tweet.type = Tweet_type.somebody_suicided
    tweet.place = player.location
    tweet.player = player
    write_tweet(tweet)
    if USE_DISTRICTS:
        destroy_tweet = destroy_district_if_needed(player.district)
        if destroy_tweet != None:
            write_tweet(destroy_tweet)
    return True

def revive():
    dead_players = get_dead_players()
    if len(dead_players) > 0:
        player = random.choice(dead_players)
        player.state = 1
        rebuild_district = USE_DISTRICTS and player.district.destroyed

        if rebuild_district:
            place = player.district
            place.destroyed = False
        else:
            place = player.location
            while place.destroyed:
                place = random.choice(place_list)
        player.location = place
        place.players.append(player)
        tweet = Tweet()
        tweet.type = Tweet_type.somebody_revived
        tweet.place = player.location
        tweet.player = player
        tweet.double = rebuild_district
        write_tweet(tweet)

        return True
    else:
        suicide()
