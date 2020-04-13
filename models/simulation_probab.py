import sys

class Simulation_Probab(object):
    item_probab = 0
    move_probab = 0
    battle_probab = 0
    steal_probab = 0
    monster_probab = 0
    injure_probab = 0
    destroy_probab = 0
    trap_probab = 0
    infect_probab = 0
    atract_probab = 0
    suicide_probab = 0
    revive_probab = 0

    item_action_number = 0
    move_action_number = 0
    battle_action_number = 0
    steal_action_number = 0
    monster_action_number = 0
    injure_action_number = 0
    destroy_action_number = 0
    atract_action_number = 0
    infect_action_number = 0
    suicide_action_number = 0
    revive_action_number = 0
    trap_action_number = 0

    # Constructor
    def __init__(self, item, move, battle, injure, steal, monster, destroy, infect, atract, suicide, revive, trap):
        if (item + move + battle + injure + steal + monster + destroy + infect + atract + suicide + revive + trap) != 100:
            sys.exit('Config error: battle probabilities do not sum up 100')

        self.item_probab = item
        self.move_probab = move
        self.battle_probab = battle
        self.injure_probab = injure
        self.steal_probab = steal
        self.monster_probab = monster
        self.destroy_probab = destroy
        self.infect_probab = infect
        self.atract_probab = atract
        self.suicide_probab = suicide
        self.revive_probab = revive
        self.trap_probab = trap

        self.calculate_action_numbers()

    def calculate_action_numbers(self):
        self.item_action_number = self.item_probab
        self.move_action_number = self.item_action_number + self.move_probab
        self.battle_action_number = self.move_action_number + self.battle_probab
        self.injure_action_number = self.battle_action_number + self.injure_probab
        self.steal_action_number = self.injure_action_number + self.steal_probab
        self.monster_action_number = self.steal_action_number + self.monster_probab
        self.destroy_action_number = self.monster_action_number + self.destroy_probab
        self.infect_action_number = self.destroy_action_number + self.infect_probab
        self.atract_action_number = self.infect_action_number + self.atract_probab
        self.suicide_action_number = self.atract_action_number + self.suicide_probab
        self.revive_action_number = self.suicide_action_number + self.revive_probab
        self.trap_action_number = self.revive_action_number + self.trap_probab
