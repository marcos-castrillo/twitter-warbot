#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random





def SOFT_ATTACK(attacker, attacked):
    return random.choice([
        u' '.join((attacker.get_name(), u'le ha dado una patada voladora a', attacked.get_name() + u'.')),
        u' '.join((attacker.get_name(), u'se ha tirado desde la tercera cuerda encima de', attacked.get_name())),
        u' '.join((attacker.get_name(), u'le ha hecho un suplex a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'le ha hecho una llave a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'le ha hecho una lanza a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'le ha dado un patadón a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'le ha dado un codazo a', attacked.get_name())),
    ])


def KILL_ACTION(attacker, attacked):
    if len(attacker.skill_list) > 0:
        skill = random.choice(attacker.skill_list)
        return u' '.join((attacker.get_name(), skill, attacked.get_name()))
    else:
        return random.choice([
            u' '.join((attacker.get_name(), u'se ha tirado desde la tercera cuerda encima de', attacked.get_name())),
            u' '.join((attacker.get_name(), u'le ha hecho un DDT a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'ha echado del ring a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'ha echado del cuadrilátero a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'ha mandado fuera del ring a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'ha mandado fuera del cuadrilátero a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'le ha hecho una sumisión a', attacked.get_name(), u'y',
                       get_x_or_y(attacked, u'éste', u'ésta'), u'no se ha podido levantar')),
            u' '.join((attacker.get_name(), u'le ha hecho una sumisión a', attacked.get_name(), u'y',
                       get_x_or_y(attacked, u'éste', u'ésta'), u'no se ha podido zafar')),
            u' '.join((attacker.get_name(), u'le ha hecho una sumisión a', attacked.get_name(), u'y',
                       get_x_or_y(attacked, u'éste', u'ésta'), u'no ha podido liberarse')),
            u' '.join((attacker.get_name(), u'ha tumbado a', attacked.get_name(), u'y',
                       get_x_or_y(attacked, u'éste', u'ésta'), u'no se ha podido levantar')),
        ])


def HAS_ALREADY_KILLED(kills_count):
    return random.choice([
        u' '.join((u'y ya ha despachado a', kills_count)),
        u' '.join((u'y ya van', kills_count)),
        u' '.join((u'y con éste ya van', kills_count)),
    ])


def KILL_METHOD(player):
    return random.choice([
        u'',
    ])


def FIND_ACTION():
    return random.choice([
        u'ha cogido',
    ])
