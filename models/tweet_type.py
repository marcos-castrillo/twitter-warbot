class Tweet_type(object):
    start = 1
    hour_threshold = 3
    somebody_powerup = 4
    winner = 5
    nobody_won = 6
    somebody_stole = 7
    somebody_stole_and_replaced = 8
    somebody_stole_and_threw = 9
    somebody_got_ill = 10
    somebody_got_injured = 11
    somebody_found_item = 12
    somebody_replaced_item = 13
    somebody_tied_and_became_friend = 15
    somebody_tied_and_was_friend = 16
    somebody_escaped = 17
    somebody_killed = 18
    somebody_revived = 19
    somebody_suicided = 20
    somebody_moved = 21
    destroyed = 22
    somebody_couldnt_move = 23
    trap = 24
    trapped = 25
    trap_dodged = 26
    monster_appeared = 28
    monster_disappeared = 29
    monster_moved = 30
    monster_killed = 31
    somebody_died_of_infection = 32
    somebody_was_infected = 33
    atraction = 34

    def __init__(self):
        pass
    def __getattr__(self, attr):
        return self[attr]
