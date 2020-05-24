import sys
from data.config import MENTION_USERS

class Player(object):
    avatar_dir = None
    name = ""
    username = ""
    kills = 0
    state = 1
    location = None
    gender = None
    district = None
    item_list = []
    friend_list = []
    injury_list = []
    powerup_list = []
    monster_immunity = False
    injure_immunity = False
    infection_immunity = False
    infected = False
    attack = 0
    defense = 0

    # Constructor
    def __init__(self):
        self.item_list = []
        self.injury_list = []
        self.friend_list = []
        self.powerup_list = []
        return

    def get_attack(self):
        attack = self.attack
        for item in self.item_list:
            attack = attack + item.attack
        for injury in self.injury_list:
            attack = attack + injury.attack
        for powerup in self.powerup_list:
            attack = attack + powerup.attack
        return attack

    def get_defense(self):
        defense = self.defense
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
