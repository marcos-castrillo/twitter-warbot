import sys
from models.item import Item
from services.simulation import write_tweet
from services.items import get_item_list
from models.tweet_type import Tweet_type
from data.literals import *
from data.config import *

class Player(object):
    avatar_dir = None
    name = ""
    username = ""
    kills = 0
    location = 0
    state = 0
    gender = None
    item_list = []
    friend_list = []
    injury_list = []
    powerup_list = []
    infected = False

    # Constructor
    def __init__(self, name, location, gender, username = None, item_list = None):
        self.friend_list = []
        self.item_list = []
        self.injury_list = []
        self.powerup_list = []
        self.location = location
        self.state = 1
        self.gender = gender
        self.name = name
        self.username = username
        self.infected = False
        whole_item_list = get_item_list()
        if item_list != None and (not isinstance(item_list, list) or len(item_list) > 2):
            sys.exit('Config error: Item list for player ' + self.name + ' is not an array or contains more than 2 items.')
        if item_list != None and len(item_list) > 0:
            for item in whole_item_list:
                if item.name == item_list[0] or (len(item_list) > 1 and item.name == item_list[1]):
                    self.item_list.append(item)
                    whole_item_list.pop(whole_item_list.index(item))

    def pick(self, player_list, place_list, item):
        if len(self.item_list) <= 1:
            self.item_list.append(item)
            self.location.items.pop(self.location.items.index(item))
            write_tweet(Tweet_type.somebody_found_item, player_list, place_list, self.location, [self, item])
            return True
        else:
            if self.item_list[0].get_value() >= self.item_list[1].get_value():
                worst_item = self.item_list[1]
                best_item = self.item_list[0]
            else:
                worst_item = self.item_list[0]
                best_item = self.item_list[1]

            if item.get_value() > worst_item.get_value():
                self.item_list = [item, best_item]
                self.location.items.pop(self.location.items.index(item))
                write_tweet(Tweet_type.somebody_replaced_item, player_list, place_list, self.location, [self, item, worst_item])
                return True
            else:
                return False

    def get_attack(self):
        attack = 0
        for item in self.item_list:
            attack = attack + item.attack
        for injury in self.injury_list:
            attack = attack + injury.attack
        for powerup in self.powerup_list:
            attack = attack + powerup.attack
        return attack

    def get_defense(self):
        defense = 0
        for item in self.item_list:
            defense = defense + item.defense
        for injury in self.injury_list:
            defense = defense + injury.defense
        for powerup in self.powerup_list:
            defense = defense + powerup.defense
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
        if len(self.item_list) == 1:
            if self.item_list[0].attack > 0:
                return self.item_list[0]
        elif len(self.item_list) == 2:
            if self.item_list[0].attack >= self.item_list[1].attack and self.item_list[0].attack > 0:
                return self.item_list[0]
            elif self.item_list[1].attack > 0:
                return self.item_list[1]
        return None

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
        if self.username != "" and MENTION_USERS:
            return self.name + u'(@' + self.username + u')'
        else:
            return self.name
