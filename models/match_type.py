class Match_type(object):
    standard = 1
    districts = 2
    rumble = 3

    def __init__(self):
        pass
    def __getattr__(self, attr):
        return self[attr]
