import random
from models.tweet import Tweet
from models.enums import TweetType
from models.enums import MatchType
from services.simulation import write_tweet
from services.store import get_dead_players, get_alive_players, kill_player, place_list, destroy_district_if_needed, \
    move_player
from data.config import config


def befriend(player_1, player_2):
    if not player_2 in player_1.friend_list:
        player_1.friend_list.append(player_2)
    if not player_1 in player_2.friend_list:
        player_2.friend_list.append(player_1)


def suicide():
    alive_players = get_alive_players()
    if len(alive_players) < 5:
        return False
    player = random.choice(alive_players)
    kill_player(player)
    tweet = Tweet()
    tweet.type = TweetType.somebody_suicided
    tweet.place = player.location
    tweet.player = player
    write_tweet(tweet)
    if config.general.match_type == MatchType.districts:
        destroy_tweet = destroy_district_if_needed(player.district)
        if destroy_tweet is not None:
            write_tweet(destroy_tweet)
    return True


def revive():
    dead_players = [x for x in get_dead_players() if not x.is_zombie]
    if len(dead_players) > 0 and len(get_alive_players()) > 5:
        player = random.choice(dead_players)
        player.is_alive = True
        rebuild_district = config.general.match_type == MatchType.districts and player.district.destroyed

        if rebuild_district:
            player.district.destroyed = False

        place = player.location
        if place.destroyed:
            if config.general.match_type == MatchType.districts:
                place = player.district
            while place.destroyed:
                place = random.choice(place_list)
            move_player(player, place)

        tweet = Tweet()
        if player.infected and len([x for x in place.players if x.is_alive]) > 1:
            tweet.there_was_infection = True

        tweet.type = TweetType.somebody_revived
        tweet.place = player.location
        tweet.player = player
        tweet.double = rebuild_district

        write_tweet(tweet)

        return True
    else:
        suicide()
