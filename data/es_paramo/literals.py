#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random

def START(tweet):
    return u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Que empiece la batalla.'

def ATRACTION(place):
    if place == u'Ardoncino':
        return u'Como son las grandes fiestas de Ardoncino (San Miguel),'
    elif place == u'Armellada':
        return u'Son las fiestas de Nuestra Señora de la Asunción en Armellada y'
    elif place == u'Astorga':
        return u'Son las fiestas de Santa Marta en Astorga y'
    elif place == u'Bustillo':
        return u'Son las fiestas de Bustillo (San Pedro) y'
    elif place == u'Bercianos del Páramo':
        return u'Como son las grandes fiestas de Bercianos (San Vicente),'
    elif place == u'Cabreros del Río':
        return u'Son las fiestas de Cabreros (San Miguel) y'
    elif place == u'Carrizo de la Ribera':
        return u'Son las Fiestas de la Virgen del Villar en Carrizo de la Ribera y'
    elif place == u'La Bañeza':
        return u'Se han celebrado las fiestas patronales de La Bañeza y'
    elif place == u'Laguna de Negrillos':
        return u'Se ha celebrado la Alubia y'
    elif place == u'Celadilla del Páramo':
        return u'Como son las grandes fiestas de Celadilla (San Blas),'
    elif place == u'Laguna de Negrillos':
        return u'Se ha celebrado la Alubia y'
    elif place == u'Grisuela del Páramo':
        return u'Se han celebrado las fiestas de Grisuela y'
    elif place == u'La Milla del Río':
        return u'Se han celebrado las fiestas de San Juan en La Milla y'
    elif place == u'León':
        return u'Como es la Fiesta de Genarín,'
    elif place == u'Palacios de Fontecha':
        return u'Como son las Fiestas de San Adrián,'
    elif place == u'Riego de la Vega':
        return u'Se ha celebrado el Corpus Cristi en Riego de la Vega y'
    elif place == u'Roperuelos del Páramo':
        return u'Como son las fiestas de Roperuelos (San Miguel),'
    elif place == u'Santa María del Páramo':
        return u'Se ha celebrado la Feria Multisectorial y'
    elif place == u'Tabuyuelo de Jamuz':
        return u'Como son las fiestas de San Fabián en Tabuyuelo de Jamuz,'
    elif place == u'Toral de los Guzmanes':
        return u'Como es El Cristo en Toral de los Guzmanes,'
    elif place == u'Urdiales del Páramo':
        return u'Como es San Cipriano,'
    elif place == u'Valdevimbre':
        return u'Como es la Fiesta del Vino,'
    elif place == u'Valencia de Don Juan':
        return u'Se han celebrado las fiestas de Coyanza y'
    elif place == u'Veguellina de Órbigo':
        return u'Se han celebrado las fiestas del Carmen y'
    elif place == u'Villadangos del Páramo':
        return u'Se han celebrado las Fiestas de Pascua de Resurrección en Villadangos y'
    elif place == u'Villademor de la Vega':
        return u'Se han celebrado las Fiestas del Señor y'
    elif place == u'Villagallegos':
        return u'Como son las Fiestas de San Roque,'
    elif place == u'Villamorico':
        return u'Se han celebrado las fiestas en honor a la Virgen del Carmen en Villamorico y'
    elif place == u'Villar del Yermo':
        return u'Se han celebrado las fiestas de Santiago en Villar del Yermo y'
    elif place == u'Zambroncinos':
        return u'Como es el ZambronRock,'
    elif place == u'Zotes del Páramo':
        return u'Se ha celebrado el XXIII Zotes Rock y'

    return random.choice([
        u'Se han celebrado las grandes fiestas de ' + place + u' y',
        u'Se han celebrado las fiestas de ' + place + u' y',
        u'Se han celebrado las fiestas patronales de ' + place + u' y',
        u'Como son las fiestas de ' + place + u','
    ])

def DESTROYED_DISTRICT(district, tributes_str):
    return random.choice([
        district.name + u' está en ruinas, ya que sus representantes han caído en combate. Otra vez será',
        u'Los representantes de ' + district.name + u' no han estado a la altura y no la han conseguido salvar',
        u'Sus participantes no han dado la talla y ' + district.name + u' ha sido demolida. ¡Una pena!',
        u'Por desgracia, ' + district.name + u' no ha sido salvada por sus representantes',
        u'Sus representantes han sido derrotados. El mundo echará de menos a ' + district.name,
        u'Sus participantes nos han decepcionado a todos y ' + district.name + u' ha tenido que ser derruida'
    ])

def WINNER_DISTRICTS_COMPOSED(winners_str, district, kills_count):
    max_kills = district.tributes[0]
    for i, tribute in enumerate(district.tributes):
        if tribute.kills > max_kills.kills:
            max_kills = tribute
    if len(winners_str) > 130:
        return u' '.join((u'¡' + district.district_display_name, u'es el ganador de la Páramo War! Sus representantes han conseguido un total de', str(kills_count), u'muertes, siendo ' + max_kills.get_name() + u' quien más ha conseguido con ' + str(max_kills.kills) + u'.'))
    else:
        return u' '.join((winners_str, u'han ganado, consiguiendo un total de', str(kills_count), u'muertes, siendo ' + max_kills.get_name() + u' quien más ha conseguido con ' + str(max_kills.kills) + u'. ¡' + district.district_display_name, u'es el ganador de la Páramo War!'))

def MONSTER_APPEARED(tweet):
    place = tweet.place
    return random.choice([
        u'Una patrulla de la guardia ha aparecido en ' + place.name + '.',
        u'Una patrulla de la guardia ha sido avistada en ' + place.name + '.',
        u'Control en ' + place.name + '.',
        u'¡Ojo! Alguien ha avistado una patrulla de la guardia en ' + place.name + '.',
        u'Se ha producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
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
         player.get_name() + ' tiene una pinta sospechosa y la guardia se ' + get_x_or_y(player, 'lo', 'la') + ' ha llevado de ' + place.name + u' sólo por si acaso.',
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
        u'ha ido a bailar',
        u'ha ido a mover el esqueleto',
        u'ha ido a partir la pana',
        u'ha ido a liarla',
        u'ha ido a perrear',
    ])

def MOVED_ATRACTION_PL():
    return random.choice([
        u'se han acercado a ver qué se cuece',
        u'han llamado a un taxi para ir',
        u'han ido en coche',
        u'han ido a bailar',
        u'han ido a mover el esqueleto',
        u'han ido a partir la pana',
        u'han ido a liarla',
        u'han ido a perrear',
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
        u'Redios',
        u'Es un tifón',
        u'No hay quién ' + get_x_or_y(player, u'lo', u'la') + ' pare',
        u'A por la MOAB',
        u'Tra tra',
        u'WOW',
        u'BIMBA',
        u'Menudo hostiazo',
        u'Está on fire',
        u'Está a tope',
        u'Campear tanto da sus frutos',
        u'No lo vio venir',
        u'Y ya estaría',
        get_x_or_y(player, u'Está mamadísimo', u'Está mamadísima')
    ])
