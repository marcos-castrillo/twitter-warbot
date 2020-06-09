#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random

def START(tweet):
    return u'¡Todos en sus puestos! Que empiece la batalla.'

def NEXT_ENTRANCE(tweet):
    return random.choice([
        tweet.player.get_name() + u' entra al ring.'
    ])

def PRAISE(player):
    return random.choice([
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        u'Qué ' + get_x_or_y(player, u'tío', u'tía'),
        u'Vaya fiera',
        u'Impresionante',
        u'Es ' + get_x_or_y(player, u'un', u'una') + u' máquina',
        u'Menudo monstruo',
        u'Está ' + get_x_or_y(player, u'rocoso', u'rocosa'),
        u'Qué crack',
        u'JO-DER',
        u'Es un tifón',
        u'No hay quién ' + get_x_or_y(player, u'lo', u'la') + ' pare',
        u'A por la MOAB',
        u'Tra tra',
        u'WOW',
        u'BIMBA',
        u'Está on fire',
        u'Está a tope',
        u'Campear tanto da sus frutos',
        u'No lo vio venir',
        u'Y ya estaría',
        get_x_or_y(player, u'Está mamadísimo', u'Está mamadísima')
    ])

def SKILL_ATTACK(attacker, attacked):
    if len(attacker.skill_list) > 0:
        skill = random.choice(attacker.skill_list)
    else:
        skill = SKILL()

    return random.choice([
        u' '.join((attacker.get_name(), skill, attacked.get_name() + u'.'))
    ])

def SKILL():
    return random.choice([
        u'se ha tirado desde la tercera cuerda encima de'
    ])

def KILL_ACTION():
    return random.choice([
        u'ha tirado fuera del ring a',
    ])

def KILL_METHOD(player):
    return random.choice([
        u'',
    ])

def FIND_ACTION():
    return random.choice([
        u'ha cogido',
    ])
