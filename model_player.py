from model_item import Item
from service_api import print_or_tweet
from literals import *

class Player(object):
    name = ""
    kills = 0
    state = 0
    item_list = []
    friend_list = []
    injury_list = []

    # Constructor
    def __init__(self, name, username = None, friend_list = None):
        self.friend_list = friend_list
        self.item_list = []
        self.injury_list = []
        self.state = 1
        if username != None:
            self.name = name + '(@' + username + ')'
        else:
            self.name = name

    def pick(self, item):
        if len(self.item_list) <= 1:
            self.item_list.append(item)
            print_or_tweet(somebody_found_item(self, item))
        else:
            if self.item_list[0].get_value() >= self.item_list[1].get_value():
                worst_item = self.item_list[1]
                best_item = self.item_list[0]
            else:
                worst_item = self.item_list[0]
                best_item = self.item_list[1]

            if item.get_value() > worst_item.get_value():
                self.item_list = [item, best_item]
                print_or_tweet(somebody_replaced_item(self, item, worst_item))
            else:
                print_or_tweet(somebody_doesnt_want_item(self, item))

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
