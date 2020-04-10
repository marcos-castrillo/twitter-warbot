from data.es.literals import *
import random

def ATRACTION(place):
    if place == u'Bercianos':
        return u'Como son las grandes fiestas de Bercianos (#ProjectBercy), '

    return random.choice([
        u'Se han celebrado las fiestas de ' + place + u' y',
        u'Como son las fiestas de ' + place + u', ',
        u'Todo el mundo está en las fiestas de ' + place + u', ',
        u'Se ha montado un tremendo fiestón en ' + place + u' y',
        u'Hoy se lía en ' + place + u', '
    ])

def MONSTER_APPEARED(place):
    return random.choice([
        u'Una patrulla de la guardia ha aparecido en ' + place.name + '.',
        u'Una patrulla de la guardia ha sido avistada en ' + place.name + '.',
        u'Control en ' + place.name + '.',
        u'¡Ojo! Alguien ha avistado una patrulla de la guardia en ' + place.name + '.',
        u'Se ha producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
    ])

def MONSTER_DISAPPEARED(place):
    return random.choice([
        u'¡La guardia se ha esfumado de ' + place.name + u'!',
        u'La guardia ya no está en ' + place.name + '.',
        u'Se acabó el turno de la guardia, por lo que se han ido de ' + place.name + u'.'
    ])

def MONSTER_KILLED(player, place):
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

def MONSTER_MOVED(place, new_place):
    if new_place.name == u'Santa María':
        return (u'Ratonera sucia, la guardia se ha ido de ' + place.name + '.')
    if new_place.name == u'Bercianos':
        return (u'Como son las fiestas de Bercianos (#ProjectBercy) y todo el mundo está allí, la guardia se ha tenido que ir de ' + place.name + '.')

    return random.choice([
        u'Alguien se ha chivado de que hay un cultivo de maría en ' + new_place.name + u', por lo que la guardia se ha ido de ' + place.name + '.',
        u'¡La guardia se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la guardia ha tenido que irse de ' + place.name + '.',
        u'La guardia se ha movido de ' + place.name + u' a ' + new_place.name + '.'
    ])

MOVE_ACTION_ROAD = random.choice([
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
