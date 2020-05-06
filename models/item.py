from data.config import MAX_VALUE_RARITY_1, MAX_VALUE_RARITY_2
from models.item_type import Item_type

class Item(object):
    type = None
    name = ""
    defense = 0
    attack = 0
    monster_immunity = False
    injure_immunity = False
    infection_immunity = False

    # Constructor
    def __init__(self):
        return

    def get_value(self):
        return self.defense + self.attack

    def get_rarity(self):
        value = self.get_value()

        if self.type == Item_type.special:
            return 3

        if value <= MAX_VALUE_RARITY_1:
            return 1
        elif value <= MAX_VALUE_RARITY_2:
            return 2
        else:
            return 3
