import sys

class Item_Rarity_Probab(object):
    rarity_1_probab = 0
    rarity_2_probab = 0
    rarity_3_probab = 0

    rarity_1_action_number = 0
    rarity_2_action_number = 0
    rarity_3_action_number = 0

    # Constructor
    def __init__(self, rarity_1, rarity_2, rarity_3):
        if (rarity_1 + rarity_2 + rarity_3) != 100:
            sys.exit('Config error: item rarity probabilities do not sum up 100')

        self.rarity_1_probab = rarity_1
        self.rarity_2_probab = rarity_2
        self.rarity_3_probab = rarity_3

        self.calculate_action_numbers()

    def increase(self, i):
        self.rarity_1_probab = self.rarity_1_probab - 15
        self.rarity_2_probab = self.rarity_2_probab + 10
        self.rarity_3_probab = self.rarity_3_probab + 5

        self.calculate_action_numbers()

    def calculate_action_numbers(self):
        self.rarity_1_action_number = self.rarity_1_probab
        self.rarity_2_action_number = self.rarity_1_action_number + self.rarity_2_probab
        self.rarity_3_action_number = self.rarity_2_action_number + self.rarity_3_probab
