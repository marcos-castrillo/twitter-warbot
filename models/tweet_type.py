class Tweet_type(object):
    start = 1
    sleep = 2
    hour_threshold = 3
    final = 4
    winner = 5
    nobody_won = 6
    final_statistics_1 = 7
    final_statistics_2 = 8
    final_statistics_3 = 9
    somebody_got_ill = 10
    somebody_got_injured = 11
    somebody_found_item = 12
    somebody_replaced_item = 13
    somebody_doesnt_want_item = 14
    somebody_tied_and_became_friend = 15
    somebody_tied_and_was_friend = 16
    somebody_escaped = 17
    somebody_killed = 18
    somebody_revived = 19
    somebody_died = 20
    somebody_moved = 21
    destroyed = 22
    somebody_couldnt_move = 23

    def __init__(self):
        pass
    def __getattr__(self, attr):
        return self[attr]
