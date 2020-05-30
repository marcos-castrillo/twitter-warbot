class Place(object):
    coord_x = None
    coord_y = None
    name = None
    trap_by = None
    monster = None
    connections = []
    items = []
    road_connections = []
    water_connections = []
    players = []
    tributes = []
    destroyed = False
    atracted = False

    # Constructor
    def __init__(self, name, road_connections, coordinates, items, district_display_name = None, water_connections = None):
        self.name = name
        self.coord_x = coordinates[0]
        self.coord_y = coordinates[1]
        self.items = items
        self.road_connections = road_connections
        self.connections = road_connections
        self.destroyed = False
        self.monster = None
        self.water_connections = water_connections
        if water_connections != None:
            self.connections = self.connections + water_connections
        self.players = []
        self.tributes = []
        self.trap_by = None
        self.district_display_name = self.name
        if district_display_name != None:
            self.district_display_name = district_display_name
