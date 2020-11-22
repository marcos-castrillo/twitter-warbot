#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.es.literals import *
import random


def START(tweet):
    return u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Que empiece la batalla.'


def WINNER_DISTRICTS_COMPOSED(winners_str, district, kills_count):
    return u' '.join((winners_str, u'ha(n) ganado, consiguiendo un total de', str(kills_count),
                      u'muerte(s). ¡' + district.district_display_name, u'es la última ciudad en pie de España!'))


def ATRACTION(place):
    if place == u'A Coruña':
        return u'Se han celebrado las Fiestas de Maria Pita en A Coruña y'
    elif place == u'Albacete':
        return u'Se ha celebrado la Feria de Albacete y'
    elif place == u'Alicante':
        return u'Se han celebrado las Fogueres d\'Alacant y'
    elif place == u'Almería':
        return u'Se ha celebrado la Feria de Almería y'
    elif place == u'Ávila':
        return u'Se han celebrado las Fiestas de Santa Teresa en Ávila y'
    elif place == u'Badajoz':
        return u'Se ha celebrado la Feria de San Juan en Badajoz y'
    elif place == u'Barcelona':
        return u'Se han celebrado las Fiestas de La Mercé en Barcelona y'
    elif place == u'Bilbao':
        return u'Se ha celebrado la Bilboko Aste Nagusia en Bilbao y'
    elif place == u'Burgos':
        return u'Se han celebrado los Sampedros en Burgos y'
    elif place == u'Cáceres':
        return u'Se ha celebrado la Feria de Mayo en Cáceres y'
    elif place == u'Cádiz':
        return u'Se ha celebrado el Carnaval de Cádiz y'
    elif place == u'Castellón de la Plana':
        return u'Se han celebrado las Fiestas de la Magdalena en Castellón de la Plana y'
    elif place == u'Ceuta':
        return u'Se han celebrado las Fiestas de la Virgen de África en Ceuta y'
    elif place == u'Ciudad Real':
        return u'Se han celebrado las Fiestas de la Virgen del Prado en Ciudad Real y'
    elif place == u'Córdoba':
        return u'Se ha celebrado la Feria de Córdoba y'
    elif place == u'Cuenca':
        return u'Se han celebrado las Fiestas de San Julián en Cuenca y'
    elif place == u'Girona':
        return u'Se han celebrado les Fires de Sant Narcís en Girona y'
    elif place == u'Granada':
        return u'Se ha celebrado el Día de la Cruz en Granada y'
    elif place == u'Guadalajara':
        return u'Se ha celebrado la Semana Grande de Guadalajara y'
    elif place == u'Huelva':
        return u'Se han celebrado las Fiestas Colombinas de Huelva y'
    elif place == u'Huesca':
        return u'Se han celebrado las Fiestas de San Lorenzo en Huesca y'
    elif place == u'Jaén':
        return u'Se ha celebrado la Feria San Lucas en Jaén y'
    elif place == u'Las Palmas de Gran Canaria':
        return u'Se ha celebrado el Carnaval de Las Palmas de Gran Canaria y'
    elif place == u'León':
        return u'Se ha celebrado la Fiesta de Genarín en León y'
    elif place == u'Lleida':
        return u'Se ha celebrado la Fiesta Mayor de Lleida y'
    elif place == u'Logroño':
        return u'Se han celebrado las Fiestas de San Mateo en Logroño y'
    elif place == u'Lugo':
        return u'Se han celebrado las Fiestas de San Froilán en Lugo y'
    elif place == u'Madrid':
        return u'Se han celebrado las Fiestas de San Isidro en Madrid y'
    elif place == u'Málaga':
        return u'Se ha celebrado la Feria de Málaga y'
    elif place == u'Melilla':
        return u'Se han celebrado las Fiestas de la Virgen de la Victoria en Melilla y'
    elif place == u'Murcia':
        return u'Se han celebrado las Fiestas de Primavera en Murcia y'
    elif place == u'Ourense':
        return u'Se han celebrado las Festas de Ourense y'
    elif place == u'Oviedo':
        return u'Se han celebrado las Fiestas de San Mateo en Oviedo y'
    elif place == u'Palencia':
        return u'Se han celebrado las Fiestas de San Antolín en Palencia y'
    elif place == u'Palma de Mallorca':
        return u'Se han celebrado las Festes de Sant Sebastià en Palma de Mallorca y'
    elif place == u'Pamplona':
        return u'Se han celebrado los Sanfermines en Pamplona y'
    elif place == u'Pontevedra':
        return u'Se han celebrado las Fiestas de la Peregrina en Pontevedra y'
    elif place == u'Salamanca':
        return u'Se ha celebrado el Lunes de Aguas en Salamanca y'
    elif place == u'San Sebastián':
        return u'Se ha celebrado la Semana Grande de San Sebastián y'
    elif place == u'Santa Cruz de Tenerife':
        return u'Se ha celebrado el Carnaval de Santa Cruz de Tenerife y'
    elif place == u'Santander':
        return u'Se ha celebrado la Semana Grande de Santander y'
    elif place == u'Segovia':
        return u'Se han celebrado las Fiestas de San Juan y San Pedro en Segovia y'
    elif place == u'Sevilla':
        return u'Se ha celebrado la Feria de Abril en Sevilla y'
    elif place == u'Soria':
        return u'Se han celebrado las Fiestas de San Juan en Soria y'
    elif place == u'Tarragona':
        return u'Se han celebrado las Festes de Santa Tecla en Tarragona y'
    elif place == u'Teruel':
        return u'Se han celebrado las Fiestas del Ángel en Teruel y'
    elif place == u'Toledo':
        return u'Se han celebrado las Fiestas de la Virgen del Sagrario en Toledo y'
    elif place == u'Valencia':
        return u'Se han celebrado las Fallas de Valencia y'
    elif place == u'Valladolid':
        return u'Se han celebrado las Fiestas de la Virgen de San Lorenzo en Valladolid y'
    elif place == u'Vitoria':
        return u'Se han celebrado las Fiestas de La Blanca en Vitoria y'
    elif place == u'Zamora':
        return u'Se han celebrado las Fiestas de San Pedro en Zamora y'
    elif place == u'Zaragoza':
        return u'Se han celebrado las Fiestas del Pilar en Zaragoza y'
    else:
        return u'Se han celebrado las fiestas de ' + place + u' y'


def DESTROYED_DISTRICT(district, tributes_str):
    if district.name != district.district_display_name:
        return random.choice([
            u'Los representantes de ' + district.district_display_name + u'(' + tributes_str + u')' + u' han sido derrotados, así que ' + district.name + ' ha sido reducida a escombros.',
            u'Ninguno de los representantes de ' + district.district_display_name + u'(' + tributes_str + u')' + u' sigue con vida, por lo que ' + district.name + ' ha sido destruida.',
        ])
    else:
        return random.choice([
            district.name + u' está en ruinas, ya que ' + tributes_str + u' han caído en combate. Otra vez será',
            u'Los representantes de ' + district.name + u'(' + tributes_str + u')' + u' no han estado a la altura y no la han conseguido salvar',
            tributes_str + u' no han dado la talla y ' + district.name + u' ha sido demolida. ¡Una pena!',
            u'Por desgracia, ' + district.name + u' no ha sido salvada por sus representantes (' + tributes_str + u')',
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


def MONSTER_IMMUNITY(player, shared=False):
    if shared:
        return random.choice([
            u'¡A partir de ahora la policía no le hará nada a su equipo.',
            u'¡A partir de ahora su equipo es inmune ante la justicia!',
            u'¡A partir de ahora su equipo es inmune ante la ley!',
            u'¡A partir de ahora ' + get_x_or_y(player, u'él',
                                                u'ella') + u' y el resto de su equipo son inmunes ante la policía!',
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
        player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado',
                                                      'arrestada') + u' por la policía de ' + place.name + u'. Aquí acaba su aventura.',
        u'¡La policía le ha pillado una bolsita a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(
            player, 'lo', 'la') + u' han llevado, hay que esconderla mejor!',
        u'La policía ha desahuciado a palos a ' + player.get_name() + u' de ' + place.name + u'. ¡Game over!',
        player.get_name() + u' creía que no iba a pasar nada por meter su voto en una urna, hasta que los antidisturbios de ' + place.name + ' cargaron contra ' + get_x_or_y(
            player, u'él', 'ella') + u'. ¡Mala suerte!',
        'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la policía. Se ' + get_x_or_y(
            player, 'lo han llevado detenido',
            'la han llevado detenida') + ' de ' + place.name + u' por apología al terrorismo.',
        player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso',
                                                            u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la policía en ' + place.name + u'.'
    ])


def MONSTER_MOVED(tweet):
    new_place = tweet.place
    place = tweet.place_2
    return random.choice([
        u'¡La policía se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la policía ha tenido que irse de ' + place.name + '.',
        u'Alguien se ha chivado de que hay una manifestación en ' + new_place.name + u', así que la policía se ha ido de ' + place.name + '.',
        u'La policía se ha movido de ' + place.name + u' a ' + new_place.name + '.',
        u'¡La policía se ha ido a un desahucio a ' + new_place.name + '!', ])


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
