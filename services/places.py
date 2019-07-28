#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from data.places import raw_place_list
from models.place import Place

def get_place_list():
    list = []
    for i, p in enumerate(raw_place_list):
        place = Place(p[0], p[1], p[2])
        list.append(place)

    for i, p in enumerate(list):
        initialize_connections_list(list, p)

    return list

def initialize_connections_list(places_list, place):
    connections_list = []
    for i, c in enumerate(place.connections):
        connection = get_place_by_name(places_list, c)
        if connection != None:
            connections_list.append(connection)
    place.connections = connections_list

def get_place_by_name(place_list, name):
    place = [p for p in place_list if p.name == name]

    if place:
        return place[0]
    else:
        return None
