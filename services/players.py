import random
import sys
from models.tweet import Tweet
from models.tweet_type import Tweet_type
from models.match_type import Match_type
from services.simulation import write_tweet
from store import get_dead_players, get_alive_players, kill_player, place_list, destroy_district_if_needed, move_player
from data.config import MATCH_TYPE

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
    if MATCH_TYPE == Match_type.districts:
        destroy_tweet = destroy_district_if_needed(player.district)
        if destroy_tweet != None:
            write_tweet(destroy_tweet)
    return True

def revive():
    dead_players = get_dead_players()
    if len(dead_players) > 0:
        player = random.choice(dead_players)
        player.state = 1
        rebuild_district = MATCH_TYPE == Match_type.districts and player.district.destroyed

        if rebuild_district:
            place = player.district
            place.destroyed = False
        else:
            place = player.location
            while place.destroyed:
                place = random.choice(place_list)

        tweet = Tweet()
        player.location = place
        for i, pl in enumerate(place.players):
            if pl.infected:
                player.infected = True
                tweet.there_was_infection = True
        place.players.append(player)
        tweet.type = Tweet_type.somebody_revived
        tweet.place = player.location
        tweet.player = player
        tweet.double = rebuild_district

        write_tweet(tweet)

        return True
    else:
        suicide()

def next_entrance():
    alive_players = get_alive_players()
    players_in_place = [x for x in alive_players if x.location != None]
    players_out = [x for x in alive_players if x.location == None]
    if len(players_out) == 0:
        return False
    candidate = random.choice(players_out)
    move_player(candidate, place_list[0])

    tweet = Tweet()
    tweet.type = Tweet_type.next_entrance
    tweet.place = candidate.location
    tweet.player = candidate
    tweet.player_list = players_in_place
    write_tweet(tweet)

    return True
