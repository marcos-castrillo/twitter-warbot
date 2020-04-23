from data.es.literals import *
import random

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
        return u'Se han celebrado la Feria de Abril en Sevilla y'
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

def MONSTER_APPEARED(tweet):
    place = tweet.place

    return random.choice([
        u'Una patrulla de la policía ha aparecido en ' + place.name + '.',
        u'Una patrulla de la policía ha sido avistada en ' + place.name + '.',
        u'¡Ojo! Alguien ha avistado una patrulla de la policía en ' + place.name + '.',
        u'Se ha producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
    ])

def MONSTER_DISAPPEARED(tweet):
    place = tweet.place

    return random.choice([
        u'¡La policía se ha esfumado de ' + place.name + u'!',
        u'La policía ya no está en ' + place.name + '.',
        u'Se acabó el turno de la policía, por lo que se han ido de ' + place.name + u'.'
    ])

def MONSTER_IMMUNITY():
    return random.choice([
        u'¡A partir de ahora la policía no le hará nada!',
        u'¡A partir de ahora es inmune ante la justicia!',
        u'¡A partir de ahora es inmune ante la policía!',
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

def MOVE_ACTION_AIR():
    return [
        u'ha ido en su jet privado de',
        u'ha ido en globo de',
        u'ha encontrado billetes de avión baratos para ir de',
        u'ha ido en avión en primera clase de',
    ]

def MOVE_ACTION_ROAD():
    return random.choice(
        MOVE_ACTION_AIR() + [
        u'ha ido de',
        u'ha ido de',
        u'ha ido de',
        u'ha ido de',
        u'ha ido de',
        u'ha ido de',
        u'ha viajado de',
        u'ha viajado de',
        u'ha viajado de',
        u'se ha movido de',
        u'se ha movido de',
        u'se ha movido de',
        u'se ha movido de',
        u'ha llamado a un taxi para que le lleve de',
        u'ha llamado a un Uber para que le lleve de',
        u'ha llamado a un Cabify para que le lleve de',
        u'está tan en forma que ha ido en bici de',
        u'ha hecho dedo desde',
        u'ha hecho autostop desde',
        u'ha robado un coche a lo GTA y se ha ido de',
        u'ha ido en moto de',
        u'ha ido en su scooter de',
        u'ha ido en AVE de',
        u'ha ido en mochillo de',
        u'ha ido en limusina con su chófer de',
        u'ha ido en patinete eléctrico de',
        u'ha ido en tren regional de',
        u'ha ido en Alsa de',
        u'ha cogido un Blablacar de'
    ])

def MOVE_ACTION_WATER():
    return random.choice(
        MOVE_ACTION_AIR() + [
        u'ha ido en barco de',
        u'ha ido en su barquito velero de',
        u'ha ido en un crucero de ocho plantas de',
        u'ha ido en lancha motora de',
        u'se ha colado de polizón en un barco de',
        u'ha ido en patera de'
    ])

def MOVED_ATRACTION_SING():
    return random.choice([
        u' ha ido.',
        u' ha ido.',
        u' ha ido.',
        u' ha ido.',
        u' ha ido.',
        u' ha ido porque tenía ganas de marcha.',
        u' ha ido porque le quedaba cerca.',
        u' ha ido porque le quedaba de camino.',
        u' se ha acercado a ver qué se cuece.',
        u' ha ido en coche.',
        u' ha ido a bailar.',
        u' ha ido a mover el esqueleto.',
        u' ha ido de copas.'
    ])

def MOVED_ATRACTION_PL():
    return random.choice([
        u' han ido.',
        u' han ido.',
        u' han ido.',
        u' han ido.',
        u' han ido.',
        u' han ido porque les quedaba cerca.',
        u' han ido porque tenían ganas de marcha.',
        u' han ido porque les quedaba de camino.',
        u' se han acercado a ver qué se cuece.',
        u' han ido en coche.',
        u' han ido a bailar.',
        u' han ido a mover el esqueleto.',
        u' han ido de copas.'
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
        u'Es un tifón.',
        u'No hay quién ' + get_x_or_y(player, u'lo', u'la') + ' pare.',
        u'A por la MOAB.',
        u'Tra tra.',
        u'WOW.',
        u'BIMBA.',
        u'Está on fire.',
        u'Está a tope.',
        u'Campear tanto da sus frutos.',
        u'No lo vio venir.',
        u'Y ya estaría.',
        get_x_or_y(player, u'Está mamadísimo.', u'Está mamadísima.')
    ])
