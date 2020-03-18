import sys

class Simulation_Probab(object):
    item_probab = 0
    move_probab = 0
    battle_probab = 0
    monster_probab = 0
    aop_probab = 0
    destroy_probab = 0
    trap_probab = 0
    infect_probab = 0
    suicide_probab = 0
    revive_probab = 0

    item_action_number = 0
    move_action_number = 0
    battle_action_number = 0
    monster_action_number = 0
    aop_action_number = 0
    destroy_action_number = 0
    trap_action_number = 0
    infect_action_number = 0
    suicide_action_number = 0
    revive_action_number = 0

    # Constructor
    def __init__(self, item, move, battle, monster, aop, destroy, trap, infect, suicide, revive):
        if (item + move + battle + monster + aop + destroy + trap + infect + suicide + revive) != 100:
            sys.exit('Config error: battle probabilities do not sum up 100')

        self.item_probab = item
        self.move_probab = move
        self.battle_probab = battle
        self.monster_probab = monster
        self.aop_probab = aop
        self.destroy_probab = destroy
        self.trap_probab = trap
        self.infect_probab = infect
        self.suicide_probab = suicide
        self.revive_probab = revive

        self.calculate_action_numbers()

    def calculate_action_numbers(self):
        self.item_action_number = self.item_probab
        self.move_action_number = self.item_action_number + self.move_probab
        self.battle_action_number = self.move_action_number + self.battle_probab
        self.monster_action_number = self.battle_action_number + self.monster_probab
        self.aop_action_number = self.monster_action_number + self.aop_probab
        self.destroy_action_number = self.aop_action_number + self.destroy_probab
        self.trap_action_number = self.destroy_action_number + self.trap_probab
        self.infect_action_number = self.trap_action_number + self.infect_probab
        self.suicide_action_number = self.infect_action_number + self.suicide_probab
        self.revive_action_number = self.suicide_action_number + self.revive_probab
