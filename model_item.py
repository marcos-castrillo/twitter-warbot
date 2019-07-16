class Item(object):
    name = ""
    defense = 0
    attack = 0

    # Constructor
    def __init__(self, name, defense, attack):
        self.name = name
        self.defense = defense
        self.attack = attack

    def get_value(item):
        return item.defense + item.attack
