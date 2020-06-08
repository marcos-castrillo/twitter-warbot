#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random

def START(tweet):
    return u'¡Todos en sus puestos! Que empiece la batalla.'

def WINNER_DISTRICTS_COMPOSED(winners_str, district, kills_count):
    return u' '.join((winners_str, u'han ganado, consiguiendo un total de', str(kills_count), u'muertes. ¡' + district.district_display_name, u'es la última ciudad en pie de España!'))

def DESTROYED_DISTRICT(district, tributes_str):
    if district.name != district.district_display_name:
        return random.choice([
            u'Los representantes de ' + district.district_display_name + u'(' + tributes_str  + u')' + u' han sido derrotados, así que ' + district.name + ' ha sido reducida a escombros.',
            u'Ninguno de los representantes de ' + district.district_display_name + u'(' + tributes_str  + u')' + u' sigue con vida, por lo que ' + district.name + ' ha sido destruida.',
        ])
    else:
        return random.choice([
            district.name + u' está en ruinas, ya que ' + tributes_str  + u' han caído en combate. Otra vez será',
            u'Los representantes de ' + district.name + u'(' + tributes_str  + u')' + u' no han estado a la altura y no la han conseguido salvar',
            tributes_str + u' no han dado la talla y ' + district.name + u' ha sido demolida. ¡Una pena!',
            u'Por desgracia, ' + district.name + u' no ha sido salvada por sus representantes (' + tributes_str  + u')',
            tributes_str + u' han sido derrotados. El mundo echará de menos a ' + district.name,
            tributes_str + u' nos han decepcionado a todos y ' + district.name + u' ha tenido que ser derruida'
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
        player.get_name() + u' creía que no iba a pasar nada por meter su voto en una urna, hasta que los antidisturbios de ' + place.name + ' cargaron contra ' + get_x_or_y(player, u'él', 'ella') + u'. ¡Mala suerte!',
        'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la policía. Se ' + get_x_or_y(player, 'lo han llevado detenido', 'la han llevado detenida') + ' de ' + place.name + u' por apología al terrorismo.',
        player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso', u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la policía en ' + place.name + u'.'
    ])

def MONSTER_MOVED(tweet):
    new_place = tweet.place
    place = tweet.place_2
    return random.choice([
        u'¡La policía se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la policía ha tenido que irse de ' + place.name + '.',
        u'Alguien se ha chivado de que hay una manifestación en ' + new_place.name + u', así que la policía se ha ido de ' + place.name + '.',
        u'La policía se ha movido de ' + place.name + u' a ' + new_place.name + '.',
        u'¡La policía se ha ido a un desahucio a ' + new_place.name + '!',    ])

def MOVED_ATRACTION_SING():
    return random.choice([
        u'ha ido',
        u'ha ido',
        u'ha ido',
        u'ha ido',
        u'ha ido',
        u'ha ido porque tenía ganas de marcha',
        u'ha ido porque le quedaba cerca',
        u'ha ido porque le quedaba de camino',
        u'se ha acercado a ver qué se cuece',
        u'ha ido en coche',
        u'ha ido a bailar',
        u'ha ido a mover el esqueleto',
        u'ha ido de copas'
    ])

def MOVED_ATRACTION_PL():
    return random.choice([
        u'han ido',
        u'han ido',
        u'han ido',
        u'han ido',
        u'han ido',
        u'han ido porque les quedaba cerca',
        u'han ido porque tenían ganas de marcha',
        u'han ido porque les quedaba de camino',
        u'se han acercado a ver qué se cuece',
        u'han ido en coche',
        u'han ido a bailar',
        u'han ido a mover el esqueleto',
        u'han ido de copas'
    ])

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
