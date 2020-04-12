from data.es.literals import *
import random

def ATRACTION(place):
    if place == u'Bercianos':
        return u'Como son las grandes fiestas de Bercianos (#ProjectBercy),'

    return random.choice([
        u'Se han celebrado las fiestas de ' + place + u' y',
        u'Como son las fiestas de ' + place + u',',
        u'Todo el mundo está en las fiestas de ' + place + u',',
        u'Se ha montado un tremendo fiestón en ' + place + u' y',
        u'Hoy se lía en ' + place + u','
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
    return random.choice([u'¡A partir de ahora la policía no le hará nada!.'])

def MONSTER_KILLED(tweet):
    place = tweet.place
    player = tweet.player
    return random.choice([
        player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado', 'arrestada') + u' por la policía de ' + place.name + u'. Aquí acaba su aventura.',
        u'¡La guardia le ha pillado una bolsita a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(player, 'lo', 'la') + u' han llevado, hay que esconderla mejor!',
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

def MOVE_ACTION_ROAD():
    return random.choice([
        u'ha llamado a un taxi para que le lleve de',
        u'ha llamado a un Uber para que le lleve de',
        u'ha llamado a un Cabify para que le lleve de',
        u'está tan en forma que ha ido en bici de',
        u'ha hecho dedo desde',
        u'ha hecho autostop desde',
        u'ha robado un coche descapotable a lo GTA y se ha ido de',
        u'ha ido en moto de',
        u'ha ido en su jet privado de',
        u'ha ido en su scooter de',
        u'ha ido en AVE de',
        u'ha ido en mochillo de',
        u'ha ido en limusina con su chófer de',
        u'ha ido en patinete eléctrico de',
        u'ha ido en tren regional de',
        u'ha ido en Alsa de',
        u'ha ido en globo de',
        u'ha encontrado billetes de avión baratos para ir de',
        u'ha ido en avión en primera clase de',
        u'ha cogido un Blablacar de'
    ])

def MOVE_ACTION_WATER():
    return random.choice([
        u'ha ido en su barquito velero de',
        u'ha ido en un crucero de cinco plantas de',
        u'ha ido en lancha motora de',
        u'se ha colado de polizón en un barco de',
        u'ha ido en patera de'
    ])
