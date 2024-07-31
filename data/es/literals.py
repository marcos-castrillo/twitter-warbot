#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from data.config import config


def get_amount(number):
    if number == 0:
        return ''
    elif number > 0:
        return '(+' + str(number) + ')'
    else:
        return '(' + str(number) + ')'


def get_sing_or_pl(player_list, x, y):
    if len(player_list) == 1:
        return x
    elif len(player_list) > 1:
        return y


def get_x_or_y(player, x, y):
    if player.is_female:
        return y
    else:
        return x


def get_x_or_y_plural(player_list, x, y):
    females = 0
    for i, p in enumerate(player_list):
        if p.is_female:
            females = females + 1
    if females == len(player_list):
        return y
    return x


def ALSO_STOLE():
    return random.choice([
        u'Además, le ha robado',
        u'Ya que no lo va a necesitar, le ha robado',
        u'Como no le va a hacer falta, ha cogido',
        u'Además, le ha quitado',
        u'Además, le ha saqueado',
        u'Le ha quitado',
        u'Le ha saqueado y ha encontrado',
        u'Le ha looteado y se ha llevado'
    ])


def ALSO_INFECTING():
    return random.choice([
        u'infectando también a',
        u'contagiando a',
    ])


def AND():
    return 'y'


def ATRACTION(place):
    if place == u'Ardoncino':
        return u'Como son las grandes fiestas de Ardoncino (San Miguel),'
    elif place == u'Armellada':
        return u'Son las fiestas de Armellada (Nuestra Señora de la Asunción) y'
    elif place == u'Astorga':
        return u'Son las fiestas de Astorga (Santa Marta) y'
    elif place == u'Bustillo':
        return u'Son las fiestas de Bustillo (San Pedro) y'
    elif place == u'Bercianos del Páramo':
        return u'Como son las grandes fiestas de Bercianos (San Vicente),'
    elif place == u'Cabreros del Río':
        return u'Son las fiestas de Cabreros (San Miguel) y'
    elif place == u'Carrizo de la Ribera':
        return u'Son las Fiestas de Carrizo de la Ribera (Virgen del Villar) y'
    elif place == u'Cembranos':
        return u'Son las Fiestas de Cembranos (Nuestra Señora de La Asunción) y'
    elif place == u'La Bañeza':
        return u'Se han celebrado las fiestas de La Bañeza y'
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
    elif place == u'Villamañán':
        return u'Se han celebrado las fiestas de la Zarza en Villamañán y'
    elif place == u'Villamorico':
        return u'Se han celebrado las fiestas en honor a la Virgen del Carmen en Villamorico y'
    elif place == u'Villar del Yermo':
        return u'Se han celebrado las fiestas de Villar del Yermo y'
    elif place == u'Zambroncinos':
        return u'Como es el ZambronRock,'
    elif place == u'Zotes del Páramo':
        return u'Se ha celebrado el XXIII Zotes Rock y'

    return random.choice([
        u'Se han celebrado las grandes fiestas de ' + place + u' y',
        u'Se han celebrado las fiestas de ' + place + u' y',
        u'Se han celebrado las fiestas de ' + place + u' y',
        u'Como son las fiestas de ' + place + u','
    ])


def OTHERS(amount):
    if amount == 1:
        return 'otro más'
    else:
        return 'otros ' + str(amount)


def CURED(tweet):
    return random.choice([
        u' '.join((tweet.player.get_name(), u'se ha curado del COVID-19. A partir de ahora es inmune al virus.')),
        u' '.join((tweet.player.get_name(), u'ya no tiene COVID-19. A partir de ahora es inmune al virus.')),
        u' '.join((u'¡' + tweet.player.get_name(),
                   u'ha pasado la cuarentena y ya no tiene coronavirus! Además, a partir de ahora es inmune.')),
    ])


def DESTROYED_DISTRICT(district, tributes_str):
    return random.choice([
        district.name + u' está en ruinas, ya que ' + tributes_str + u' ha(n) caído en combate',
        u'Los representantes de ' + district.name + u'(' + tributes_str + u')' + u' no la han salvado',
        tributes_str + u' no ha(n) dado la talla y ' + district.name + u' ha sido demolida',
        district.name + u' no ha sido salvada por sus representantes (' + tributes_str + u')',
        tributes_str + u' ha(n) sido derrotados. Echaremos de menos a ' + district.name,
        tributes_str + u' nos ha(n) decepcionado y ' + district.name + u' ha sido derruida'
    ])


def DESTROYED(place):
    return random.choice([
        u'Un meteorito ha caído en ' + place + u' y lo ha destruido',
        place + u' ha colapsado',
        u'Un terrible incendio ha reducizo ' + place + u' a cenizas',
        u'Un terrorista ha dinamitado ' + place,
        u'Una riada ha inundado todo ' + place,
        u'Una bomba nuclear ha reducido ' + place + u' a pedazos',
        u'Un huracán ha arrasado todo ' + place,
        u'Una nube de gas tóxico ha llegado a ' + place + u' haciéndolo inhabitable',
        u'Una epidemia de listeriosis se ha extendido por ' + place,
        u'El mundo está mejor sin ' + place + u', así que el creador de este bot ha decidido cargárselo sin más',
        place + u' se ha ido a la puta mierda',
        u'Una terrible sequía ha asolado ' + place
    ])


def DIED(player, multiple=False):
    if multiple:
        conj = u'han'
    else:
        conj = u'ha'

    return random.choice([
        ' y ' + player + ' ' + conj + u' fallecido en el trágico accidente.',
        ' y ' + player + ' ' + conj + u' amochado.',
        ' y ' + player + ' ' + conj + u' sobrevivido.',
        ' y ' + player + ' ' + conj + u' muerto.',
        ' y ' + player + ' ' + conj + u' palmado.',
        ' y ' + player + ' ' + conj + u' espichado.',
        ' y ' + player + u' se ' + conj + u' ido al otro barrio.',
        ' y se ha llevado por delante a ' + player + u'.',
        u' y hay un luto de 3 días por ' + player + u'.',
        u'. DEP ' + player + u'.',
        u'. F ' + player + u'.'
    ])


def DISTRICT_REBUILD(tweet):
    return random.choice([
        u'¡' + tweet.player.district.district_display_name + u' ha sido reconstruida!',
        u'¡' + tweet.player.district.district_display_name + u' vuelve a estar en pie!',
        u'¡' + tweet.player.district.district_display_name + u' vuelve a la lucha!'
    ])


def ESCAPED(player_1, player_2):
    return random.choice([
        player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_2.name + u' ha salido por patas a ' + player_2.location.name + u'.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_2.name + u' ha huido cual cobarde a ' + player_2.location.name + u'.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' han empezado a pelear, pero ' + player_2.name + u' sabía que iba a perder y huyó a ' + player_2.location.name + u'.',
        player_2.get_name() + u' cogió un puñado de arena, se lo echó a ' + player_1.get_name() + u' en los ojos y huyó a ' + player_2.location.name + u'.',
        player_2.get_name() + u' iba a pillar a ' + player_1.get_name() + u' por la espalda, pero ' + get_x_or_y(
            player_1, 'éste',
            'ésta') + ' se dio cuenta en el último momento.' + LINEBREAK() + player_2.name + u' ha huido a ' + player_2.location.name + u'.',
        player_2.get_name() + u' ha visto a ' + player_1.get_name() + u' y ha huido a ' + player_2.location.name + u'.',
        u'A ' + player_2.get_name() + u' le da miedo ' + player_1.get_name() + u' y ha huido a ' + player_2.location.name + u'.',
        u'A ' + player_2.get_name() + u' le da asco ' + player_1.get_name() + u' y se ha ido a ' + player_2.location.name + u'.',
        player_1.get_name() + u' se ha encarado con ' + player_2.get_name() + u', pero ' + player_2.name + u' se ha achantado y escapado a ' + player_2.location.name + u'.'
    ])


def HURT(player_1, player_2, hurt_amount):
    return random.choice([
        player_1.get_name() + u' le arreó tremendo hostión a ' + player_2.get_name() + u', que ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le dio tal colleja a ' + player_2.get_name() + u' que le quitó ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le dio un patadón a ' + player_2.get_name() + u' que le quitó ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le dio un puñetazo a ' + player_2.get_name() + u' que le quitó ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le dio una hostia a mano abierta a ' + player_2.get_name() + u'. ' + player_2.name + u' ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le hizo una llave de kárate a ' + player_2.get_name() + u'. ' + player_2.name + u' ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le hizo un mataleón a ' + player_2.get_name() + u'. ' + player_2.name + u' ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le hizo un 619 a ' + player_2.get_name() + u'. ' + player_2.name + u' ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le ha dado un cabezazo a ' + player_2.get_name() + u'. ' + player_2.name + u' ' + str(hurt_amount) + u' de poder.',
        player_1.get_name() + u' le ha dado un codazo a ' + player_2.get_name() + u'. ' + player_2.name + u' ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le ha dado una patada en la rodilla a ' + player_2.get_name() + u' que le ha quitado ' + str(abs(hurt_amount)) + u' de poder.',
        player_1.get_name() + u' le ha dado un puñetazo en el estómago a ' + player_2.get_name() + u'. ' + player_2.name + u' ha perdido ' + str(abs(hurt_amount)) + u' de poder.',
    ])


def FROM(owner):
    return random.choice([
        u'(que antes era de @' + owner + u')',
        u'(que era de @' + owner + u')',
        u'(que pertenecía a @' + owner + u')'
    ])


def FRIENDS_TIED(player_1, player_2):
    return (random.choice([
        player_1.get_name() + u' y ' + player_2.get_name() + u' se molan y son incapaces de hacerse daño.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' siguen a lo suyo.',
        player_1.get_name() + u' sigue ' + get_x_or_y(player_1, 'liado', 'liada') + ' con ' + player_2.get_name() + u' y no pueden luchar.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' son tan ' + get_x_or_y_plural([player_1, player_2], 'monos', 'monas') + ' que en vez de pelear se han abrazado.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' siguen ' + get_x_or_y_plural([player_1, player_2], 'enamorados.', 'enamoradas.'),
    ]))


GETS_RID_OF = u'se ha deshecho de'


def HAS_ALREADY_KILLED(kills_count):
    return random.choice([
        u' '.join((u'Ya lleva', kills_count)),
        u' '.join((u'Ya se ha cargado a', kills_count)),
        u' '.join((u'Ya ha despachado a', kills_count)),
        u' '.join((u'Ya van', kills_count)),
        u' '.join((u'Con éste ya van', kills_count)),
        u' '.join((u'Lleva una racha de', kills_count)),
    ])


def HAS_NOW(power, short=False):
    if power is not None:
        if short:
            return u' '.join([u'Poder', power + '.'])
        else:
            return random.choice([
                u' '.join([u'Ahora tiene', power, u'de poder.']),
                u' '.join([u'Poder', power + '.']),
                u' '.join([u'Su poder es ahora de', power + '.']),
            ])


def I_COMPOSED(player, action, event, has_now, thrown_away_by=''):
    return u' '.join((u'¡' + player.get_name(), action, event + thrown_away_by + '!' + LINEBREAK() + has_now))


def FIRST_DEAD(player):
    return u' '.join([u'Ya me jodería ser', get_x_or_y(player, u'el primero', u'la primera'), 'en morir..'])

def INITIAL_WEAPON():
    return u'una barra de hace 5 días'

def INFECTED_EVERYBODY():
    return random.choice([
        u'Todos ellos se han infectado.'
    ])


def INFECTED_OTHERS(tweet, other_players):
    if len(other_players) == 1:
        player = other_players[0]
        return random.choice([
            u'Ha infectado a ' + player.get_name() + u' con el coronavirus.',
            u'Ha contagiado a ' + player.get_name() + u' con el coronavirus.',
            player.get_name() + u' ha sido ' + get_x_or_y(player, u'contagiado', u'contagiada') + u' con el COVID-19.',
            player.get_name() + u' ha sido ' + get_x_or_y(player, u'contagiado',
                                                          u'contagiada') + u' con el coronavirus.',
            player.get_name() + u' ha sido ' + get_x_or_y(player, u'infectado', u'infectada') + u' con el COVID-19.',
        ])
    else:
        return random.choice([
            u'Ha infectado con el COVID-19 a todos los que estaban allí.',
            u'Ha contagiado con el COVID-19 a todos los que estaban allí.',
            u'Todos los que estaban allí han sido infectados con el COVID-19.',
            u'Quienes estaban allí han sido infectados con el COVID-19.',
        ])

def INFECTED_OTHERS_PL(tweet, other_players):
    return INFECTED_OTHERS(tweet, other_players).replace('Ha', 'Han').replace(' ha ', ' han ')

def SOMEBODY_INFECTED(tweet, other_players):
    if len(other_players) == 1:
        player = other_players[0]
        return random.choice([
            player.get_name() + u' le ha infectado con el coronavirus.',
            player.get_name() + u' le ha contagiado el coronavirus.',
            player.get_name() + u' le ha contagiado el COVID-19.',
            u'Ha sido ' + get_x_or_y(tweet.player, u'contagiado',
                                     u'contagiada') + u' con el COVID-19 por ' + player.get_name(),
            u'Ha sido ' + get_x_or_y(tweet.player, u'contagiado',
                                     u'contagiada') + u' con el coronavirus por ' + player.get_name(),
            u'Ha sido ' + get_x_or_y(tweet.player, u'infectado',
                                     u'infectada') + u' con el COVID-19 por ' + player.get_name(),
        ])
    else:
        return random.choice([
            u'Alguien le ha infectado con el COVID-19...',
            u'Ha tenido la mala suerte de infectarse con el COVID-19...',
            u'Alguien le ha contagiado el COVID-19...',
            u'Aunque alguien le ha contagiado el coronavirus...',
            u'Parece que alguien le ha infectado con el coronavirus...',
        ])


def INFECTION_IMMUNITY(player, shared=False):
    if shared:
        return random.choice([
            u'¡A partir de ahora ' + get_x_or_y(player, u'él',
                                                u'ella') + u' y el resto de su equipo son inmunes al COVID-19!',
            u'¡A partir de ahora ' + get_x_or_y(player, u'él',
                                                u'ella') + u' y el resto de su equipo tienen inmunidad contra el COVID-19!',
            u'¡A partir de ahora el COVID-19 no afecta a su equipo!',
            u'¡A partir de ahora su equipo no puede ser infectado con el COVID-19!'
        ])
    else:
        return random.choice([
            u'¡A partir de ahora es inmune al COVID-19!',
            u'¡A partir de ahora tiene inmunidad contra el COVID-19!',
            u'¡A partir de ahora el COVID-19 no le afecta!',
            u'¡A partir de ahora no puede ser infectado con el COVID-19!'
        ])


def INJURE_IMMUNITY(player, shared=False):
    if shared:
        return random.choice([
            u'¡A partir de ahora ' + get_x_or_y(player, u'él',
                                                u'ella') + ' y el resto de su equipo no sufrirán heridas ni lesiones!',
            u'¡A partir de ahora su equipo es inmune a heridas y lesiones!',
            u'¡A partir de ahora su equipo tiene inmunidad contra lesiones y heridas!',
        ])
    else:
        return random.choice([
            u'¡A partir de ahora no sufrirá heridas ni lesiones!',
            u'¡A partir de ahora es inmune a heridas y lesiones!',
            u'¡A partir de ahora tiene inmunidad contra lesiones y heridas!',
        ])


def FRIENDSHIP_BOOST(player):
    return random.choice([
        u'¡A partir de ahora será ' + get_x_or_y(player, u'un', u'una') + ' rompecorazones!',
        u'¡A partir de ahora va a atraer todas las miradas!',
        u'¡Ahora va a conquistar a todos y todas!'
    ])


def MOVEMENT_BOOST(player, shared=False):
    if shared:
        return random.choice([
            u'¡A partir de ahora ' + get_x_or_y(player, u'él',
                                                u'ella') + ' y el resto de su equipo podrá viajar más lejos!',
            u'¡A partir de ahora su equipo podrá viajar más lejos!',
            u'¡A partir de ahora su equipo podrá viajar a pueblos más lejanos!'
        ])
    else:
        return random.choice([
            u'¡A partir de ahora podrá viajar más lejos!',
            u'¡A partir de ahora podrá viajar a pueblos más lejanos!'
        ])


def ZOMBIE_IMMUNITY(player, shared=False):
    if shared:
        return random.choice([
            u'¡Los zombies ya no perseguirán a ' + get_x_or_y(player, u'él', u'ella') + ' ni a su equipo!',
            u'¡A partir de ahora su equipo es inmune a zombies!',
            u'¡A partir de ahora su equipo tiene inmunidad contra zombies!',
        ])
    else:
        return random.choice([
            u'¡A partir de ahora los zombies no le perseguirán!',
            u'¡A partir de ahora es inmune a zombies!',
            u'¡A partir de ahora tiene inmunidad contra zombies!',
        ])


def INTRODUCE_PLACE(tweet):
    place_name = tweet.place.district_display_name
    players = tweet.player_list
    singular = len(players) == 1

    if singular:
        return random.choice([
            u'representará a ' + place_name + u'.',
            u'ya está ' + get_x_or_y(players[0], 'preparado', 'preparada') + ' para representar a ' + place_name + u'.',
            u'ha sido ' + get_x_or_y(players[0], 'elegido', 'elegida') + ' para representar a ' + place_name + u'.',
            u'es ' + get_x_or_y(players[0], 'el elegido', 'la elegida') + ' para representar a ' + place_name + u'.',
            u'ha sido ' + get_x_or_y(players[0], 'seleccionado',
                                     'seleccionada') + ' para representar a ' + place_name + u'.',
        ])
    else:
        return random.choice([
            u'representarán a ' + place_name + u'.',
            u'ya están ' + get_x_or_y_plural(players, 'preparados',
                                             'preparadas') + ' para representar a ' + place_name + u'.',
            u'han sido ' + get_x_or_y_plural(players, 'elegidos',
                                             'elegidas') + ' para representar a ' + place_name + u'.',
            u'han sido ' + get_x_or_y_plural(players, 'seleccionados',
                                             'seleccionadas') + ' para representar a ' + place_name + u'.',
        ])


def KILL_ACTION(attacker, attacked):
    return random.choice([
        u' '.join((attacker.get_name(), u'se ha cargado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha matado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'se ha llevado por delante a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha destrozado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha desintegrado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha dejado KO a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha ejecutado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha despachado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha emboscado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha terminado con el sufrimiento que era la vida de', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha asesinado a sangre fría a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'se ha quitado de en medio a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'se ha quitado de encima a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha degollado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha asfixiado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha lapidado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha desnucado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha mandado al otro barrio a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha reventado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha liquidado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha aniquilado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha despachado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha acabado con', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha apuñalado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha acribillado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha estrangulado a', attacked.get_name())),
        u' '.join((attacker.get_name(), u'ha apaleado a', attacked.get_name())),
    ])


def KILL_METHOD(player):
    return random.choice([
        u'',
        u'con sus puños',
        u'y le ha hecho tea-bag',
        u'a tortazo limpio',
        u'por la gloria de ESPAÑA',
        u'de un ' + random.choice(['cabezazo', 'codazo', 'gancho']),
        u'y le ha hecho ' + random.choice(['un dab', 'un baile del fortnite', 'el Swish Swish']),
        u'sin despeinarse',
        u'con ' + random.choice(['una llave de kárate', 'una llave de taekwondo']),
        u'y le ha cantado ' + random.choice(['una canción triste', 'una bulería', 'una balada']),
        u'y ha hecho un perreo duro hasta el suelo',
        u'haciendo capoeira',
        u'y se ha puesto a bailar',
        u'a hostia limpia',
        u'y le ha recitado ' + random.choice(['un poema de Neruda', 'un poema', 'un poema de Bécquer']),
        u'y le ha quitado el trabajo',
        u'sin esforzarse',
        u'sin inmutarse',
        u'y ha seguido a lo suyo',
        u'y se ha acabado el bocata tranquilamente',
        u'con lágrimas en los ojos',
        u'con mirada de psicópata',
        u'y ha gritado SUUUUUUUUUUUUUUUUU',
        u'y ha gritado ' + get_x_or_y(player, u'ESTOY MAMADÍSIMO HIJO DE PUTA', u'ESTOY MAMADÍSIMA HIJO DE PUTA'),
        u'en un abrir y cerrar de ojos',
        u'sin pestañear',
        u'por turras',
        u'y lo ha grabado y subido a su instagram',
        u'y lo ha tuiteado',
        u'y le ha sacado una foto de recuerdo',
        u'y ha tirado su cadáver al contenedor de basura',
        u'y se ha ido de cañas',
        u'haciendo una buena escabechina con sus restos',
        u'sudando mogollón',
        u'y se ha fumado un cigarrito',
        u'mientras sus colegas le gritaban ACÁBALO',
        u'y se ha tirado un eructo',
        u'sin mucho esfuerzo'
    ])


def LINEBREAK():
    return u'//n'


REPLACED = u'Se lo queda y se deshace de'


def REVIVED(tweet):
    player = tweet.player
    return u' '.join((player.get_name(), random.choice([
        u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!',
                                                 u'la muerta. ¡Qué zooorrraaaaa! (sin trazas de patriarcado).'),
        u'ha vuelto a la vida bajo extrañas circunstancias.',
        u'ha vuelto en forma de chapa.',
        u'ha resucitado en mitad de su funeral y ha vuelto a la batalla.',
        u'tiene enchufe y el creador del bot le ha resucitado.',
        u'ha vuelto del otro barrio.'
    ])))


def WAS_INFECTED(tweet):
    player = tweet.player
    return random.choice([
        player.get_name() + u' no se ha lavado las manos lo suficiente y ha contraído el coronavirus.',
        player.get_name() + u' debería de haber seguido las recomendaciones para no pillar el coronavirus.',
        player.get_name() + u' ha pillado el coronavirus.'
    ])


def PLACE_INFECTED(tweet):
    return u'El virus se ha propagado rápidamente por ' + tweet.place.name


def INFECTED_DIED(tweet):
    player = tweet.player
    return random.choice([
        u'El coronavirus ha acabado con ' + player.get_name() + u'. Aquí acaba su aventura.',
        u'Los hospitales están colapsados y no quedan camas para ' + player.get_name() + u'. Ha muerto por una neumonía provocada por coronavirus.',
        player.get_name() + u' ha fallecido por coronavirus.',
        player.get_name() + u' ha tosido hasta ahogarse por culpa del coronavirus.'
    ])


def MONSTER_APPEARED(tweet):
    place = tweet.place

    if place.name == u'Santa María del Páramo':
        return u'Ratonera sucia.'

    return random.choice([
        u'¡Ojo! Alguien ha avistado una patrulla de la guardia en ' + place.name + '.',
        u'Una patrulla de la guardia ha aparecido en ' + place.name + '.',
    ])


def MONSTER_IMMUNITY(player, shared=False):
    if shared:
        return random.choice([
            u'¡A partir de ahora la guardia no le hará nada a su equipo.',
            u'¡A partir de ahora su equipo es inmune ante la justicia!',
            u'¡A partir de ahora su equipo es inmune ante la ley!',
            u'¡A partir de ahora ' + get_x_or_y(player, u'él',
                                                u'ella') + u' y el resto de su equipo son inmunes ante la guardia!',
        ])
    else:
        return random.choice([
            u'¡A partir de ahora la guardia no le hará nada.',
            u'¡A partir de ahora es inmune ante la justicia!',
            u'¡A partir de ahora es inmune ante la guardia!',
            u'¡A partir de ahora es inmune ante la ley!',
        ])


def DOCTOR_APPEARED(tweet):
    place = tweet.place
    return u'¡Un médico ha aparecido en ' + place.name + u'!'


def DOCTOR_MOVED(tweet):
    place = tweet.place
    place_2 = tweet.place_2
    return u'El médico se ha movido de ' + place_2.name + u' a ' + place.name + u'.'


def DOCTOR_CURED(tweet):
    place = tweet.place
    player = tweet.player
    return random.choice([
        u'¡El médico de ' + place.name + u' ha curado completamente a ' + player.get_name() + u'!',
        u'¡El médico de ' + place.name + u' le ha dado una pastillita misteriosa a ' + player.get_name() + u'!',
        u'¡El médico de ' + place.name + u' le ha pinchado algo a ' + player.get_name() + u'!',
        u'¡El médico de ' + place.name + u' ha dopado a ' + player.get_name() + u'!',
        u'¡' + player.get_name() + u' ha ido al médico de ' + place.name + u' y se ha curado de todos los males!',
    ]) 


def ZOMBIE_APPEARED(tweet):
    player = tweet.player
    place = tweet.place
    moved = tweet.double

    if moved:
        return player.get_name() + u' ha vuelto a la vida en forma de zombi y se ha ido a liarla a ' + place.name + u'.'
    else:
        return player.get_name() + u' ha vuelto a la vida en forma de zombi y está sembrando el caos en ' + place.name + u'.'


def ZOMBIE_MOVED(tweet):
    player_zombie = tweet.player
    place = tweet.place
    place_2 = tweet.place_2
    return u'El zombi (' + player_zombie.get_name() + u') se ha movido de ' + place_2.name + u' a ' + place.name + u'.'


def ZOMBIE_KILLED(tweet):
    player = tweet.player
    player_zombie = tweet.player_2
    return random.choice([
        u'El zombi (' + player_zombie.get_name() + u') se ha cargado a ' + player.get_name() + u'.',
        u'El zombi (' + player_zombie.get_name() + u') no conoce y ha matado a ' + player.get_name() + u'.',
        player.get_name() + u' no ha podido sobrevivir contra el zombi (' + player_zombie.get_name() + u').',
        player.get_name() + u' tendría que haberse visto más pelis de zombies para sobrevivir contra ' + player_zombie.get_name() + u'.'
    ])


def ZOMBIE_WAS_DEFEATED(tweet):
    player = tweet.player
    player_zombie = tweet.player_2
    return u'El zombi (' + player_zombie.get_name() + u') ha sido vencido por ' + player.get_name() + u', que se ha visto muchas pelis de zombies.'


def MONSTER_TOOK(tweet):
    player = tweet.player
    item = tweet.item
    return random.choice([
        player.get_name() + u' ha sido ' + get_x_or_y(player, 'registrado', 'registrada') + u' y le han requisado ' + item.name + u'.',
        player.get_name() + ' tiene una pinta sospechosa y la guardia le ha quitado ' + item.name + u' sólo por si acaso.',
        u'La guardia ha parado a ' + player.get_name() + u' y le ha quitado ' + item.name + u'.',
        u'La guardia le ha requisado ' + item.name + u' a ' + player.get_name() + u'.',
    ])


def MONSTER_MOVED(tweet):
    new_place = tweet.place
    place = tweet.place_2

    if new_place.name == u'Santa María del Páramo':
        return u'Ratonera sucia.'

    return random.choice([
        u'¡La guardia se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la guardia ha tenido que irse de ' + place.name + '.',
        u'La guardia se ha movido de ' + place.name + u' a ' + new_place.name + '.',
        u'Una patrulla de la guardia ha sido avistada en ' + new_place.name + '.',
        u'Control en ' + new_place.name + '.',
        u'Hay movida en ' + new_place.name + ' y la guardia ha intervenido.',
        u'Se ha producido una serie de altercados en ' + new_place.name + u', por lo que la guardia se ha visto obligada a desplazarse allí.',
    ])

def MOVE_ACTION_AIR():
    return random.choice([
        u'ha ido en helicóptero de',
        u'ha ido en su jet privado de',
        u'ha ido en globo de',
        u'ha ido en avión de',
        u'ha ido en Ryanair de',
        u'ha ido en Iberia de',
        u'ha ido en zeppelin de',
        u'ha encontrado billetes de avión baratos para ir de',
        u'ha ido en avión en primera clase de',
    ])


def MOVE_ACTION_ROAD():
    if config.map.short_distance:
        return MOVE_ACTION_ROAD_SHORT()
    else:
        return MOVE_ACTION_ROAD_LONG()

def MOVE_ACTION_ROAD_PL():
    return MOVE_ACTION_ROAD().replace("ha ", "han ").replace("está ", "están ").replace(" le ", " les ").replace("aburría", "aburrían").replace("fuerte", "fuertes")

def MOVE_ACTION_ROAD_LONG():
    return random.choice([
        MOVE_ACTION_AIR(),
        u'ha ido de',
        u'ha viajado de',
        u'se ha movido de',
        u'ha conducido su ' + random.choice(
            [u'Seat León', u'Fiat Multipla', u'Renault Megane', u'Seat Ibiza', u'Golf', u'Opel Corsa', u'Ford Focus',
             u'Opel Astra', u'BMW Serie 3']) + ' de',
        random.choice([u'está tan en forma que ha ', u'se aburría y ha ', u'está tan cachas que ha ',
                       u'está tan fuerte que ha ']) + random.choice(
            [u'ido en bici', u'ido a trote', u'hecho un sprint', u'ido a la pata coja', u'ido corriendo',
             u'hecho footing']) + u' de',
        u'ha llamado a ' + random.choice([u'un taxi', u'un Uber', u'un Cabify']) + u' para que le lleve de',
        u'ha hecho ' + random.choice([u'autostop', u'dedo']) + u' para que le lleven de',
        u'ha ido en ' + random.choice(
            [u'moto', u'motoniveladora', u'su scooter', u'AVE', u'mochillo', u'limusina con su chófer', u'patinete eléctrico',
             u'tren regional', u'Alsa', u'Blablacar', u'un coche robado a lo GTA']) + u' de'
    ])


def MOVE_ACTION_ROAD_SHORT():
    return random.choice([
        u'ha ido de',
        u'ha ido desde',
        u'ha caminado desde',
        u'ha conducido de',
        u'se ha movido de',
        u'ha llamado al taxi de ' + random.choice(
            [u'Rebollo', u'Santi', u'Aquilino', u'Germán']) + u' para que le lleve de',
        u'ha conducido su ' + random.choice(
            [u'Seat León', u'Fiat Multipla', u'Renault Megane', u'Seat Ibiza', u'Golf', u'Opel Corsa', u'Ford Focus',
             u'Opel Astra', u'BMW Serie 3']) + ' de',
        random.choice([u'está tan en forma que ha ', u'se aburría y ha ', u'está tan cachas que ha ',
                       u'está tan fuerte que ha ']) + random.choice(
            [u'ido en bici', u'ido a trote', u'hecho un sprint', u'ido a la pata coja', u'ido corriendo',
             u'hecho footing']) + u' de',
        u'ha hecho ' + random.choice([u'autostop', u'dedo']) + u' para que le lleven de',
        u'ha ido en ' + random.choice(
            [u'moto', u'su scooter', u'vespa', u'mochillo', u'triciclo', u'limusina con su chófer', u'patinete',
             u'triciclo', u'patinete eléctrico', u'bus', u'un coche robado a lo GTA']) + u' de'
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


def MOVE_ACTION_WATER():
    return random.choice([
        MOVE_ACTION_AIR(),
        u'ha ido en barco de',
        u'ha ido en su barquito velero de',
        u'ha ido en un crucero de ocho plantas de',
        u'ha ido en barcaza de',
        u'ha ido en canoa de',
        u'ha ido en kayak de',
        u'ha ido en submarino nuclear de',
        u'ha ido en lancha motora de',
        u'ha ido en un barco pesquero de',
        u'ha ido en patera de',
        u'se ha colado de polizón en un barco de'
    ])

def MOVE_ACTION_WATER_PL():
    return MOVE_ACTION_WATER().replace(" ha ", " han ")

def MOVED_SING():
    return random.choice([
        u'se ha movido a',
        u'ha ido a',
        u'se ha ido a'
    ])


def MOVED_PL():
    return random.choice([
        u'se han movido a',
        u'se han ido a',
        u'han ido a'
    ])


def SLEEP():
    return random.choice([
        u'Los participantes se han ido a dormir tras un largo día.',
        u'Los participantes se han ido a dormir tras un largo día.',
        u'Los participantes se han ido a dormir tras un largo día.',
        u'Todo el mundo está durmiendo. Mañana será otro día.',
        u'Todo el mundo está durmiendo. Mañana será otro día.',
        u'Todo el mundo está durmiendo. Mañana será otro día.',
        u'Buenas noches hasta mañana, los lunnis y los niños, nos vamos a la cama.',
        u'Te diría que sueñes con los angelitos, pero creo que ya me has visto bastante el día de hoy.',
        u'Antes de dormir mira bien debajo de tu cama. No sea que a medianoche algo intente jalarte los pies.',
        u'¡Buenas noches y ten cuidado con las chinches!',
        u'Te deseo que tengas dulces sueños y que en cada uno de ellos, me veas para que puedas dormir bien.',
        u'Duerme bien y aseguráte de cerrar el armario, no sea que el coco vaya a venir por ti.',
        u'Hasta los tontos como tú deben descansar, ¡así que a la cama! Mañana habrá tiempo de que hagas más tonterías.',
        u'Me voy a dormir, cualquier emergencia me avisan que yo al medio día les respondo.',
        u'Buenas noches, que pasen una linda y bendecida noche. Dulces sueños hasta mañana amigos ya amigas.',
        u'Se me acabaron las pilas. Buenas noches. Chistes cortos buenos, graciosos y divertidos para pasar un momento genial para compartir con las amistades y familiares.',
        u"Hello darkness, my old friend. I've come to talk with you again.",
        u'Soñar es barato, así que me voy a dormir un rato.',
        u'Me voy a dormir con la ventana abierta (a 19 mosquitos les gusta esto).',
        u'A dormir ya porque mañana hay que madrugar para pasear de la cama al sofá.',
        u'Me voy a misa' + LINEBREAK() + u'A mi sabrosa cama',
        u'Vayan a dormir' + LINEBREAK() + u'Que mañana toca descansar otra vez',
        u'Me voy a la cama feliz porque mañana ya es sábado, BUENAS NOCHES',
        u'Buenas noches alakama',
        u'Colacao y a la cama',
        u'Me estoy quedando sobao',
        u'Si usted está leyendo esto… Acuéstese a dormir, mire la hora que es.',
        u'Algunos tienen la belleza' + LINEBREAK() + u'Otros el dinero' + LINEBREAK() + u'Y yo lo que tengo es sueño',
    ])


def SPECIAL_ACTION():
    return random.choice([u'ha encontrado', u'ha cogido'])


def STOLE(tweet):
    return u' '.join((tweet.player.get_name(), u'le ha robado', tweet.item.name, u'a', tweet.player_2.get_name() + '.'))


def STOLE_AND_REPLACED(tweet):
    return u' '.join((STOLE(tweet), u'Como es mejor, se ha deshecho de su', tweet.old_item.name + '.'))


def STOLE_AND_THREW(tweet):
    return u' '.join((STOLE(tweet), u'Como tiene cosas mejores, lo ha tirado a la basura.'))


def STRONGER_POWER(tweet):
    return random.choice([
        u'Ha aprovechado el viaje para hacer unas flexiones y ha conseguido +2 en poder.',
        u'A mitad de camino se ha parado para hacer unas sentadillas, ¡+2 en poder!',
        u'Hacía mucho tiempo que no se levantaba del sofá, así que ha ganado 2 en poder.',
        u'Ha ganado 2 en poder por irse a la aventura.',
        u'De repente se siente más fuerte... ¡+2 en poder!',
    ])


def SUICIDE():
    return random.choice([
        u'ha sido víctima de un rayo y se ha muerto en el acto.',
        u'ha bebido un chupito de lejía.',
        u'ha bebido un chupito de cianuro.',
        u'se ha pegado un tiro.',
        u'se ha olvidado de cómo respirar.',
        u'se ha esnucado.',
        u'se la ha pegado por conducir con unas copas de más.',
        u'tuvo un piñazo con un Seat Panda.',
        u'ha muerto repentinamente por un fallo cardíaco. ¡Hay que hacer más deporte!',
        u'ha empezado a toser, a toser y a toser y se ha acabado asfixiando. Estos chavalitos...',
        u'ha amochado de repente.',
        u'ha sido atropellado por una moto y se fue a la puta.'
    ])


def TIED_AND_BEFRIEND(tweet):
    player_1 = tweet.player
    player_2 = tweet.player_2

    return random.choice([
        player_1.get_name() + u' y ' + player_2.get_name() + u' ahora están liados.',
        player_1.get_name() + u' se ha liado con ' + player_2.get_name() + u'.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' ahora son algo más que ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        player_1.get_name() + u' llevaba tiempo detrás de ' + player_2.get_name() + u' y por fin lo ha conseguido.',
        player_1.get_name() + u' por fin se ha declarado a su crush, ' + player_2.get_name() + u', y le ha salido bien.',
        player_1.get_name() + u' no ha podido resistirse a los encantos de ' + player_2.get_name() + u'.',
        player_1.get_name() + u' ha conquistado a ' + player_2.get_name() + u'.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' hacen una pareja muy bonita.',
        u'De tanto pelearse, ' + player_1.get_name() + u' y ' + player_2.get_name() + u' se han enamorado.',
    ])


TO = 'a'


def TRAP(tweet):
    set_up = random.choice([
        u'ha puesto una trampa en',
        u'ha colocado una trampa en',
        u'ha escondido una trampa en'
    ])
    return u' '.join((tweet.player.get_name(), set_up, tweet.player.location.name + '.'))


def TRAP_DODGED(tweet):
    player = tweet.player
    trapped_by = tweet.player_2
    location = tweet.place
    destroyed = random.choice([
        u', ha visto la trampa que había puesto ' + trapped_by.get_name() + ' y la ha destruido.',
        u' y se ha cargado la trampa de ' + trapped_by.get_name() + '.',
        u' pero no ha caído en la trampa de ' + trapped_by.get_name() + '.'
    ])
    return u' '.join((player.get_name(), MOVED_SING(), location.name + destroyed))


def TRAPPED(tweet):
    player = tweet.player
    trapped_by = tweet.player_2
    location = tweet.place
    trapped = random.choice([
        u'pero se ha comido la trampa que había puesto',
        u'pero ha caído en la trampa de',
        u'y no se ha dado cuenta de que había una trampa colocada por'
    ])
    return u' '.join(
        (player.get_name(), MOVED_SING(), location.name, trapped, trapped_by.get_name() + u'. ¡Qué torpe!'))


def TREASON(tweet):
    player_1 = tweet.player
    player_2 = tweet.player_2
    return random.choice([
        u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Parece que no se caían tan bien, ',
        get_x_or_y(player_1, u'Menudo', u'Menuda') + ' judas, ',
        u'Vaya puñalada por la espalda, ',
        u'Menuda traición, ',
        u'Por el interés te quiero Andrés, ',
        u'Aunque parecía una amistad verdadera, ',
        u'Habían vivido buenos momentos, hasta que ',
        u'A pesar de que parecían muy ' + get_x_or_y_plural([player_1, player_2], u'unidos, ', u'unidas, '),
        u'Por lo visto no eran tan ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        ''
    ])


def TRIBUTES_NOT_ENOUGH(place_name):
    return random.choice([
        u'Dado que no había suficientes participantes de ' + place_name + u', ',
        u'Por la falta de participación en ' + place_name + u', ',
        u'Debido a la despoblación de ' + place_name + u', ',
        u'Dado que ' + place_name + ' no tenía suficientes participantes, ',
        u'Debido a que en ' + place_name + ' escasean los participantes, ',
        u'Ya que ' + place_name + ' no tenía suficientes participantes, ',
        u'Como no había suficientes participantes de ' + place_name + u', ',
        place_name + u' no tenía sufientes representantes, por lo que '
    ])


def TRIBUTES_RANDOMLY_CHOSEN(tributes_list):
    if len(tributes_list) == 1:
        return random.choice([
            u'ha sido ' + get_x_or_y(tributes_list[0], u'seleccionado al azar.', u'seleccionada al azar.')
        ])
    else:
        return random.choice([
            u'han sido ' + get_x_or_y_plural(tributes_list, u'seleccionados al azar.', u'seleccionadas al azar.')
        ])


def TRIBUTES_WERE_DIVIDED(place_name):
    return random.choice([
        u'El resto de participantes de ' + place_name + u' serán repartidos entre otros lugares.'
    ])


def UNFRIEND():
    return random.choice([
        'Ya no están ' + get_x_or_y_plural([player_1, player_2], 'liados.', 'liadas.'),
        'Ya no están a líos.',
        'Ya no están juntos.',
        'Se ve que lo suyo no funcionó.',
    ])


def WINNER_DISTRICTS_COMPOSED(winners_str, district, kills_count):
    max_kills = district.tributes[0]
    for i, tribute in enumerate(district.tributes):
        if tribute.kills > max_kills.kills:
            max_kills = tribute
    winner_1 = u' '.join((winners_str, u'ha(n) ganado, consiguiendo un total de', str(kills_count), u'muerte(s)'))
    if len([x for x in district.players if x.is_alive]) == 1 or max_kills.is_alive:
        winner_2 = '.'
    else:
        winner_2 = u' '.join((u', siendo', max_kills.get_name(), u'quien más ha conseguido con', str(max_kills.kills)+ u'.'))
    winner_3 = u' '.join((LINEBREAK() + u'¡' + district.district_display_name, u'es el ganador de la batalla!'))
    return winner_1 + winner_2 + winner_3


def WINNER_INFECTION():
    return u'¡Incluso ha sobrevivido al coronavirus!'


def WINNER_INJURY_LIST():
    return u'Todo ello a pesar de padecer'


def WINNER_ITEM_LIST():
    return u'Además, ha acabado teniendo'


def WINNER_NO_KILLS():
    return u'Lo ha conseguido sin llevarse por delante a nadie.'


def WINNER_ONE_KILL():
    return u'Lo ha conseguido llevándose por delante a un sólo participante.'


def WINNER_MULTI_KILL(kill_count):
    return u' '.join([u'Lo ha conseguido llevándose por delante a', kill_count, 'participantes.'])


def WINNER_COMPOSED(winner, kills, item_list, infection):
    return u' '.join((u'¡' + winner.get_name(), u'ha ganado en ' + winner.location.name + '! ' + kills + item_list,
                      'El poder de', winner.get_name(), u'llegó a ser de', str(winner.get_power()), u'.', infection))


WITH = u'con'
