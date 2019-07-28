from item import Item
from services.simulation import write_tweet
from models.tweet_type import Tweet_type
from data.literals import *

class Player(object):
    avatar_dir = None
    name = ""
    username = ""
    fav_place = None
    kills = 0
    location = 0
    state = 0
    item_list = []
    friend_list = []
    injury_list = []

    # Constructor
    def __init__(self, name, location, username = None, friend_list = None, fav_place = None):
        self.friend_list = friend_list
        self.item_list = []
        self.injury_list = []
        self.fav_place = fav_place
        self.location = location
        self.state = 1
        self.name = name
        self.username = username

    def pick(self, player_list, item):
        if len(self.item_list) <= 1:
            self.item_list.append(item)
            write_tweet(Tweet_type.somebody_found_item, player_list, place_list, self.location, [self, item])
        else:
            if self.item_list[0].get_value() >= self.item_list[1].get_value():
                worst_item = self.item_list[1]
                best_item = self.item_list[0]
            else:
                worst_item = self.item_list[0]
                best_item = self.item_list[1]

            if item.get_value() > worst_item.get_value():
                self.item_list = [item, best_item]
                write_tweet(Tweet_type.somebody_replaced_item, player_list, place_list, self.location, [self, item, worst_item])
            else:
                write_tweet(Tweet_type.somebody_doesnt_want_item, player_list, place_list, self.location, [self, item])

    def get_attack(self):
        attack = 0
        for item in self.item_list:
            attack = attack + item.attack
        for injury in self.injury_list:
            attack = attack + injury.attack
        return attack

    def get_defense(self):
        defense = 0
        for item in self.item_list:
            defense = defense + item.defense
        for injury in self.injury_list:
            defense = defense + injury.defense
        return defense

    def get_best_item(self):
        if len(self.item_list) == 0:
            return None
        elif len(self.item_list) == 1:
            return self.item_list[0]
        else:
            if self.item_list[0].get_value() >= self.item_list[1].get_value():
                return self.item_list[0]
            else:
                return self.item_list[1]

    def get_best_attack_item(self):
        if len(self.item_list) == 0:
            return None
        elif len(self.item_list) == 1:
            return self.item_list[0]
        else:
            if self.item_list[0].attack >= self.item_list[1].attack:
                return self.item_list[0]
            else:
                return self.item_list[1]

    def get_worst_item(self):
        if len(self.item_list) == 0:
            return None
        elif len(self.item_list) == 1:
            return self.item_list[0]
        else:
            if self.item_list[0].get_value() < self.item_list[1].get_value():
                return self.item_list[0]
            else:
                return self.item_list[1]

    def get_name(self):
        if self.username != "":
            return self.name + '(@' + self.username + ')'
        else:
            self.name
