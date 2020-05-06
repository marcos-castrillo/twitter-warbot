class Localization(object):
    es_paramo = 1
    es_spain = 2
    es_interneto = 3

    def __init__(self):
        pass
    def __getattr__(self, attr):
        return self[attr]
