#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Place(object):
    coord_x = None
    coord_y = None
    name = None
    trap_by = None
    monster = None
    items = []
    connection_list = []
    road_connection_list = []
    water_connection_list = []
    players = []
    tributes = []
    destroyed = False
    attracted = False

    def __init__(self, name, road_connection_list, coordinates, items, district_display_name=None,
                 water_connection_list=None):
        self.name = name
        self.coord_x = coordinates[0]
        self.coord_y = coordinates[1]
        self.items = items
        self.road_connection_list = road_connection_list
        self.connection_list = road_connection_list
        self.destroyed = False
        self.monster = None
        self.water_connection_list = water_connection_list
        if water_connection_list is not None:
            self.connection_list = self.connection_list + water_connection_list
        self.players = []
        self.tributes = []
        self.trap_by = None
        self.district_display_name = self.name
        if district_display_name is not None:
            self.district_display_name = district_display_name
