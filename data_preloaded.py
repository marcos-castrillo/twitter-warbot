#!/usr/bin/env python
# -*- coding: utf-8 -*-

from service_battles import *
from service_items import *

def update_player_list(player_list, item_list):
    give_item(player_list, item_list, 'Diana', 'un cuchillo con forma de Q')
    give_item(player_list, item_list, 'Miguel', 'unas granadas')
    give_item(player_list, item_list, 'Jinx', 'una pistola de agua')
    give_item(player_list, item_list, 'Alicia', 'un chaleco antibalas')
    give_item(player_list, item_list, 'Jinx', 'un tiesto')
    give_item(player_list, item_list, 'Elsa', 'una barra de pan de hace una semana')
    give_death(player_list, 'Claudia', 'Leticia')
    give_item(player_list, item_list, 'Claudia', 'una barra de pan de hace una semana')
    give_item(player_list, item_list, 'Jony', 'unos shurikens')
    give_death(player_list, 'Rosa', 'Nerey')
    get_player(player_list, 'Jony').injury_list.append(get_illness('una otitis'))
    give_item(player_list, item_list, 'Clara', 'un pallet')
    friend(get_player(player_list, 'Jony'), get_player(player_list, 'Elsa'))
    give_item(player_list, item_list, 'Cristian', 'un abrigo feo')
    give_item(player_list, item_list, 'Miguel', 'una sudadera guapa')
    give_item(player_list, item_list, 'Laura', 'un perro agresivo pero muy obediente')
    give_item(player_list, item_list, 'Rik', 'un mero')
    give_item(player_list, item_list, 'Melissa', 'una escopeta de balines')
    give_item(player_list, item_list, 'Melissa', 'una escopeta de balines')
    get_player(player_list, 'Leticia').state = 1
    give_item(player_list, item_list, 'Clara', 'una espada con forma de Q')
    give_item(player_list, item_list, 'Kini', 'una escopeta de caza')
    give_item(player_list, item_list, 'Laura', 'una lata de sardinas')
    give_death(player_list, 'Hugo', u'Pérez')
    give_item(player_list, item_list, u'Ramón', 'un pedrolo')
    give_death(player_list, u'Víctor', 'Claudia')
    give_item(player_list, item_list, u'Víctor', 'una barra de pan de hace una semana')
    get_player(player_list, 'Claudia').item_list = []

def update_hour_count(hour_count):
    return 26

def get_item(item_list, item_name):
    for index, item in enumerate(item_list):
        if item.name == item_name:
            return item
    raise ValueError('A very specific bad thing happened.')

def get_player(player_list, player_name):
    for index, player in enumerate(player_list):
        if player.name == player_name:
            return player
    raise ValueError('A very specific bad thing happened.')

def get_illness(illness_name):
    for index, illness in enumerate(get_illness_list()):
        if illness.name == illness_name:
            return illness
    raise ValueError('A very specific bad thing happened.')

def give_item(player_list, item_list, player_name, item_name):
    get_player(player_list, player_name).item_list.append(get_item(item_list, item_name))

def give_death(player_list, killer_name, killed_name):
    get_player(player_list, killed_name).state = 0
    get_player(player_list, killer_name).kills = get_player(player_list, killer_name).kills + 1
