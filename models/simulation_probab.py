import sys

class Simulation_Probab(object):
    item_probab = 0
    move_probab = 0
    battle_probab = 0
    destroy_probab = 0
    trap_probab = 0
    accident_probab = 0
    suicide_probab = 0
    revive_probab = 0

    item_action_number = 0
    move_action_number = 0
    battle_action_number = 0
    destroy_action_number = 0
    trap_action_number = 0
    accident_action_number = 0
    suicide_action_number = 0
    revive_action_number = 0

    # Constructor
    def __init__(self, item, move, battle, destroy, trap, accident, suicide, revive):
        if (item + move + battle + destroy + trap + accident + suicide + revive) != 100:
            sys.exit('Config error: battle probabilities do not sum up 100')

        self.item_probab = item
        self.move_probab = move
        self.battle_probab = battle
        self.destroy_probab = destroy
        self.trap_probab = trap
        self.accident_probab = accident
        self.suicide_probab = suicide
        self.revive_probab = revive

        self.calculate_action_numbers()

    def increase(self, i):
        self.item_probab = self.item_probab - 7
        self.move_probab = self.move_probab + 1
        self.battle_probab = self.battle_probab + 2
        self.destroy_probab = self.battle_probab + 2
        self.trap_probab = self.accident_probab + 1
        self.accident_probab = self.trap_probab + 1
        self.suicide_probab = self.suicide_probab + 1
        self.revive_probab = self.revive_probab - 1

        self.calculate_action_numbers()

    def calculate_action_numbers(self):
        self.item_action_number = self.item_probab
        self.move_action_number = self.item_action_number + self.move_probab
        self.battle_action_number = self.move_action_number + self.battle_probab
        self.destroy_action_number = self.battle_action_number + self.destroy_probab
        self.trap_action_number = self.destroy_action_number + self.trap_probab
        self.accident_action_number = self.trap_action_number + self.accident_probab
        self.suicide_action_number = self.accident_action_number + self.suicide_probab
        self.revive_action_number = self.suicide_action_number + self.revive_probab
