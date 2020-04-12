class Item_type(object):
    weapon = 1
    powerup = 2
    special = 3
    injury = 4

    def __init__(self):
        pass
    def __getattr__(self, attr):
        return self[attr]
