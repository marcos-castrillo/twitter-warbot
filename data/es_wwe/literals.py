#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random

def NEXT_ENTRANCE(tweet):
    return random.choice([
        tweet.player.get_name() + u' entra al ring.',
        tweet.player.get_name() + get_x_or_y(tweet.player, u' es el siguiente contendiente.', u' es la siguiente contendiente.'),
        tweet.player.get_name() + get_x_or_y(tweet.player, u' ya está preparado para entrar al ring.', u' ya está preparada para entrar al ring.'),
    ])

def SOFT_ATTACK(attacker, attacked):
    return random.choice([
        u' '.join((attacker.get_name(), u'le ha dado una patada voladora a', attacked.get_name() + u'.')),
    ])

def KILL_ACTION(attacker, attacked):
    if len(attacker.skill_list) > 0:
        skill = random.choice(attacker.skill_list)
        return u' '.join((attacker.get_name(), skill, attacked.get_name()))
    else:
        return random.choice([
            u' '.join((attacker.get_name(), u'se ha tirado desde la tercera cuerda encima de', attacked.get_name())),
            u' '.join((attacker.get_name(), u'le ha hecho el suplex a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'le ha hecho el DDT a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'le ha hecho un finisher a', attacked.get_name())),
            u' '.join((attacker.get_name(), u'le ha hecho una sumisión a', attacked.get_name())),
            Chokeslam
        ])

def HAS_ALREADY_KILLED(kills_count):
    return random.choice([
        u' '.join((u'y ya se ha cargado a', kills_count)),
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
