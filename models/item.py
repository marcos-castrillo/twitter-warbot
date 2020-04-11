class Item(object):
    name = ""
    defense = 0
    attack = 0
    rarity = 0

    # Constructor
    def __init__(self, name, defense, attack, rarity = None):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.rarity = rarity

    def get_value(item):
        return item.defense + item.attack
