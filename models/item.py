class Item(object):
    type = None
    name = ""
    defense = 0
    attack = 0
    rarity = 0
    monster_immunity = False
    injure_immunity = False
    infection_immunity = False

    # Constructor
    def __init__(self):
        return

    def get_value(item):
        return item.defense + item.attack
