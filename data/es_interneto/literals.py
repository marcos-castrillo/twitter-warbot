#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random

def START(tweet):
    return u'Todos en sus puestos, ¡comienza la batalla por ser el campeón de los chavalitos!'

def ATRACTION(place):
    return random.choice([
        u'Están regalando porros en ' + place + u' y'
    ])

def MONSTER_APPEARED(tweet):
    place = tweet.place

    return random.choice([
        u'Una patrulla de la policía ha aparecido en ' + place.name + '.',
        u'Una patrulla de la policía ha sido avistada en ' + place.name + '.',
        u'¡Ojo! Alguien ha avistado una patrulla de la policía en ' + place.name + '.',
        u'Se ha producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
    ])

def MONSTER_IMMUNITY(player, shared = False):
    if shared:
        return random.choice([
            u'¡A partir de ahora la policía no le hará nada a su equipo.',
            u'¡A partir de ahora su equipo es inmune ante la justicia!',
            u'¡A partir de ahora su equipo es inmune ante la ley!',
            u'¡A partir de ahora ' + get_x_or_y(player, u'él', u'ella') + u' y el resto de su equipo son inmunes ante la policía!',
        ])
    else:
        return random.choice([
            u'¡A partir de ahora la policía no le hará nada.',
            u'¡A partir de ahora es inmune ante la justicia!',
            u'¡A partir de ahora es inmune ante la policía!',
            u'¡A partir de ahora es inmune ante la ley!',
        ])

def MONSTER_KILLED(tweet):
    place = tweet.place
    player = tweet.player
    return random.choice([
        player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado', 'arrestada') + u' por la policía de ' + place.name + u'. Aquí acaba su aventura.',
        u'¡La policía le ha pillado una bolsita a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(player, 'lo', 'la') + u' han llevado, hay que esconderla mejor!',
        u'La policía ha desahuciado a palos a ' + player.get_name() + u' de ' + place.name + u'. ¡Game over!',
        u'La policía ha pillado a ' + player.get_name() + u' meando detrás de un contenedor en ' + place.name + u' y se lo han llevado a comisaría.',
        player.get_name() + u' ha escupido a un policía en ' + place.name + u' y se lo han llevado a comisaría.',
        'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la policía. Se ' + get_x_or_y(player, 'lo han llevado detenido', 'la han llevado detenida') + ' de ' + place.name + u' por apología al terrorismo.',
        player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso', u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la policía en ' + place.name + u'.'
    ])

def MONSTER_MOVED(tweet):
    new_place = tweet.place
    place = tweet.place_2
    return random.choice([
        u'¡La policía se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la policía ha tenido que irse de ' + place.name + '.',
        u'La policía se ha movido de ' + place.name + u' a ' + new_place.name + '.'
    ])

def MOVED_ATRACTION_SING():
    return random.choice([
        u'ha ido',
        u'se ha acercado',
    ])

def MOVED_ATRACTION_PL():
    return random.choice([
        u'han ido',
        u'se han acercado',
    ])
