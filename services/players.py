import random
from models.tweet import Tweet
from models.enums import TweetType
from models.enums import MatchType
from services.simulation import write_tweet
from services.store import get_dead_players, get_alive_players, kill_player, place_list, destroy_district_if_needed, \
    move_player
from services.config import config


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
    dead_players = get_dead_players()
    if len(dead_players) > 0:
        player = random.choice(dead_players)
        player.is_alive = True
        rebuild_district = config.general.match_type == MatchType.districts and player.district.destroyed

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
        tweet.type = TweetType.somebody_revived
        tweet.place = player.location
        tweet.player = player
        tweet.double = rebuild_district

        write_tweet(tweet)

        return True
    else:
        suicide()


def next_entrance():
    alive_players = get_alive_players()
    players_in_place = [x for x in alive_players if x.location is not None]
    players_out = [x for x in alive_players if x.location is None]
    if len(players_out) == 0:
        return False
    candidate = random.choice(players_out)
    move_player(candidate, place_list[0])

    tweet = Tweet()
    tweet.type = TweetType.next_entrance
    tweet.place = candidate.location
    tweet.player = candidate
    tweet.player_list = players_in_place
    write_tweet(tweet)

    return True
