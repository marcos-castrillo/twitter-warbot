class Place(object):
    coord_x = None
    coord_y = None
    connections = []
    items = []
    road_connections = []
    sea_connections = []
    destroyed = False
    name = None
    players = []
    trap_by = None
    monster = None
    tributes = []

    # Constructor
    def __init__(self, name, road_connections, coordinates, items, sea_connections = None):
        self.name = name
        self.coord_x = coordinates[0]
        self.coord_y = coordinates[1]
        self.items = items
        self.road_connections = road_connections
        self.sea_connections = sea_connections
        self.connections = road_connections
        if sea_connections != None:
            self.connections = self.connections + sea_connections
        self.destroyed = False
        self.monster = None
        self.players = []
        self.tributes = []
        self.trap_by = None
