#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random

def START(tweet):
    return u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Que empiece la batalla.'

def ATRACTION(place):
    if place == u'Bercianos':
        return u'Como son las grandes fiestas de Bercianos (#ProjectBercy),'

    return random.choice([
        u'Se han celebrado las fiestas de ' + place + u' y',
        u'Como son las fiestas de ' + place + u', ',
        u'Todo el mundo está en las fiestas de ' + place + u', ',
    ])

def MONSTER_APPEARED(tweet):
    place = tweet.place
    return random.choice([
        u'Una patrulla de la guardia ha aparecido en ' + place.name + '.',
        u'Una patrulla de la guardia ha sido avistada en ' + place.name + '.',
        u'Control en ' + place.name + '.',
        u'¡Ojo! Alguien ha avistado una patrulla de la guardia en ' + place.name + '.',
        u'Se ha producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
    ])

def MONSTER_DISAPPEARED(tweet):
    place = tweet.place
    return random.choice([
        u'¡La guardia se ha esfumado de ' + place.name + u'!',
        u'La guardia ya no está en ' + place.name + '.',
        u'Se acabó el turno de la guardia, por lo que se han ido de ' + place.name + u'.'
    ])

def MONSTER_IMMUNITY():
    return random.choice([
        u'¡A partir de ahora la guardia no le hará nada.',
        u'¡A partir de ahora es inmune ante la justicia!',
        u'¡A partir de ahora es inmune ante la guardia!',
    ])

def MONSTER_KILLED(tweet):
    player = tweet.player
    place = tweet.place
    return random.choice([
        player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado', 'arrestada') + u' por la guardia de ' + place.name + u'. Aquí acaba su aventura.',
         player.get_name() + ' tiene una pinta sospechosa y la guardia se lo ha llevado de ' + place.name + u' sólo por si acaso.',
        u'¡La guardia le ha pillado una bolsita a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(player, 'lo', 'la') + u' han llevado a comisaría, hay que esconderla mejor!',
        u'La guardia ha desahuciado a palos a ' + player.get_name() + u' de ' + place.name + u'. ¡Game over!',
        u'La guardia ha detenido a ' + player.get_name() + u' por salir a correr en mitad de la cuarentena.',
        u'La guardia ha detenido a ' + player.get_name() + u' por salir a pasear a su perro en mitad de la cuarentena.',
        'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la guardia. Se ' + get_x_or_y(player, 'lo han llevado detenido', 'la han llevado detenida') + ' de ' + place.name + u' por apología al terrorismo.',
        player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso', u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la guardia en ' + place.name + u'.'
    ])

def MONSTER_MOVED(tweet):
    new_place = tweet.place
    place = tweet.place_2
    return random.choice([
        u'¡La policía se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la policía ha tenido que irse de ' + place.name + '.',
        u'Alguien se ha chivado de que hay una manifestación en ' + new_place.name + u', así que la policía se ha ido de ' + place.name + '.',
        u'La policía se ha movido de ' + place.name + u' a ' + new_place.name + '.',
        u'¡La policía se ha ido a un desahucio a ' + new_place.name + '!',
    ])

def MOVE_ACTION_ROAD():
    return random.choice([
        u'ha ido desde',
        u'ha ido desde',
        u'ha ido desde',
        u'ha ido de',
        u'ha ido de',
        u'ha caminado desde',
        u'ha caminado desde',
        u'ha conducido de',
        u'ha hecho dedo desde',
        u'está tan en forma que ha hecho un sprint de',
        u'se aburría y ha ido a la pata coja desde',
        u'ha llamado al taxi de ' + random.choice([u'Rebollo', u'Santi', u'Aquilino', u'Germán']) + u' para que le lleve de',
        u'ha llamado al taxi de ' + random.choice([u'Rebollo', u'Santi', u'Aquilino', u'Germán']) + u' para que le lleve de',
        u'ha ido en ' + random.choice([u'tractor', u'patinete', u'motorrabo', u'bici']) + u' de',
        u'ha ido en ' + random.choice([u'tractor', u'patinete', u'motorrabo', u'bici']) + u' de',
        u'ha ido en skate haciendo backflips de',
        u'ha cogido el coche y ha hecho un derrape de',
        u'ha ido patinando de',
        u'ha cogido un Blabacar de'
    ])

def MOVED_ATRACTION_SING():
    return random.choice([
        u'se ha acercado a ver qué se cuece',
        u'ha llamado a un taxi para ir',
        u'ha ido en coche',
        u'ha ido a bailar'
    ])

def MOVED_ATRACTION_PL():
    return random.choice([
        u'se han acercado a ver qué se cuece',
        u'han llamado a un taxi para ir',
        u'han ido en coche',
        u'han ido a bailar'
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
        u'Qué ' + get_x_or_y(player, u'tío.', u'tía.'),
        u'Vaya fiera.',
        u'Impresionante.',
        u'Es ' + get_x_or_y(player, u'un', u'una') + u' máquina.',
        u'Menudo monstruo.',
        u'Está ' + get_x_or_y(player, u'rocoso.', u'rocosa.'),
        u'Qué crack.',
        u'JO-DER.',
        u'Redios.',
        u'Es un tifón.',
        u'No hay quién ' + get_x_or_y(player, u'lo', u'la') + ' pare.',
        u'A por la MOAB.',
        u'Tra tra.',
        u'WOW.',
        u'BIMBA.',
        u'Menudo hostiazo.',
        u'Está on fire.',
        u'Está a tope.',
        u'Campear tanto da sus frutos.',
        u'No lo vio venir.',
        u'Y ya estaría.',
        get_x_or_y(player, u'Está mamadísimo.', u'Está mamadísima.')
    ])
