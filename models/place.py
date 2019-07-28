class Place(object):
    coord_x = None
    coord_y = None
    connections = []
    destroyed = False
    name = None
    players = []
    trap_by = None

    # Constructor
    def __init__(self, name, coordinates, connections):
        self.name = name
        self.coord_x = coordinates[0]
        self.coord_y = coordinates[1]
        self.connections = connections
        self.destroyed = False
        self.players = []
        self.trap_by = None
