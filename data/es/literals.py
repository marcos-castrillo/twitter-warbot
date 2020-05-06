#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

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
    if player.gender == 0:
        return x
    else:
        return y

def get_x_or_y_plural(player_list, x, y):
    for i, p in enumerate(player_list):
        if p.gender == 0:
            return x
    return y

def ALSO_STOLE():
    return random.choice([
        u'Además, le ha robado',
        u'Ya que no lo va a necesitar, le ha robado',
        u'Además, le ha quitado',
        u'También ha saqueado su cadáver y ha encontrado'
    ])

AND = 'y'

def COULDNT_MOVE(player):
    return random.choice([
        u' '.join((player.get_name(), u'se ha terminado toda la comida de', player.location.name, u'y no ha podido acceder a otros lugares, por lo que ha muerto de hambre.'))
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
       u'El mundo está mejor sin ' + place  + u', así que el creador de este bot ha decidido cargárselo sin más',
       place + u' se ha ido a la puta mierda',
       u'Una terrible sequía ha asolado ' + place
      ])

def DESTROYED_DISTRICT(district, tributes_str):
    if district.name != district.district_display_name:
        return random.choice([
            u'Los representantes de ' + district.district_display_name + u'(' + tributes_str  + u')' + u' han sido derrotados, así que ' + district.name + ' ha sido reducida a escombros.',
            u'Ninguno de los representantes de ' + district.district_display_name + u'(' + tributes_str  + u')' + u' sigue con vida, por lo que ' + district.name + ' ha sido destruida.',
        ])
    else:
        return random.choice([
            district.name + u' está en ruinas, ya que ' + tributes_str  + u' han caído en combate. Otra vez será.',
            u'Los representantes de ' + district.name + u'(' + tributes_str  + u')' + u' no han estado a la altura y no la han conseguido salvar.',
            tributes_str + u' no han dado la talla y ' + district.name + u' ha sido demolida. ¡Una pena!',
            u'Por desgracia, ' + district.name + u' no ha sido salvada por sus representantes (' + tributes_str  + u')',
            tributes_str + u' han sido derrotados. El mundo echará de menos a ' + district.name + '.',
            tributes_str + u' nos han decepcionado a todos y ' + district.name + u' ha tenido que ser derruida.'
        ])

def DIED(player, multiple = False):
    if multiple:
        conj = u'han'
    else:
        conj = u'ha'

    return random.choice([
        ' y ' + player + ' ' + conj + u' fallecido en el trágico accidente.',
        ' y ' + player + ' ' + conj + u' amochado.',
        ' y ' + player + ' ' + conj + u' sobrevivido.',
        ' y ' + player + ' ' + conj + u' muerto.',
        ' y ' + player + ' ' + conj + u' ha palmado.',
        ' y ' + player + ' ' + conj + u' ha espichado.',
        ' y ' + player + u' se ' + conj + u' ido al otro barrio.',
        ' y se ha llevado por delante a ' + player + u'.',
        u' y hay un luto de 3 días por ' + player + u'.',
        u' . DEP ' + player + u'.'
        u' . F ' + player + u'.'
    ])

def DISTRICT_REBUILD(tweet):
    return random.choice([
        u'Además, ¡su provincia (' + tweet.player.district.district_display_name + u') ha sido reconstruida!',
        u'¡' + tweet.player.district.district_display_name + u' ha sido reconstruida!',
        u'¡' + tweet.player.district.district_display_name + u' vuelve a estar en pie!',
        u'¡' + tweet.player.district.district_display_name + u' vuelve a la vida!'
    ])

def ESCAPED(player_1, player_2):
    return random.choice([
        player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_2.name + u' ha salido por patas a ' + player_2.location.name + u'.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_2.name + u' ha huido cual cobarde a ' + player_2.location.name + u'.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' han empezado a pelear, pero ' + player_2.name + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.name + u' en los ojos y huyó a ' + player_2.location.name + u'.',
        player_2.get_name() + u' iba a pillar a ' + player_1.get_name() + u' por la espalda, pero ' + get_x_or_y(player_1, 'éste', 'ésta') + ' se dio cuenta en el último momento. ' + player_2.name + u' ha huido a ' + player_2.location.name + u'.',
        u'A ' + player_2.get_name() + u' le da miedo ' + player_1.get_name() + u' y ha huido a ' + player_2.location.name + u'.',
        player_1.get_name() + u' se ha encarado con ' + player_2.get_name() + u', pero ' + player_2.name + u' se ha achantado y escapado a ' + player_2.location.name + u'.'
    ])

def FIND_ACTION():
    return random.choice([
        u'ahora tiene',
        u'ahora tiene',
        u'ahora tiene',
        u'ahora tiene',
        u'ha encontrado',
        u'ha encontrado',
        u'ha encontrado',
        u'ha encontrado',
        u'se ha encontrado',
        u'se ha encontrado',
        u'se ha encontrado',
        u'se ha encontrado',
        u'ha cogido',
        u'ha cogido',
        u'ha cogido',
        u'ha cogido',
        u'ha entrado en una casa y ha robado',
        u'se ha colado en una casa y ha robado',
        u'ha robado',
        u'ha robado',
        u'ha robado',
        u'ha recogido',
        u'ha recogido',
        u'ha recogido',
        u'ha recogido',
        u'ha recogido',
        u'se ha agenciado',
        u'se ha agenciado',
        u'ha conseguido',
        u'ha conseguido',
        u'ha conseguido',
        u'ha conseguido',
        u'tras suplicárselo al creador del bot, se ha llevado',
        u'tiene enchufe con el programador y se ha llevado',
        u'ha encontrado rebuscando entre la basura',
        u'se ha agachado a recoger',
        u'se ha llevado en la tómbola',
        u'se ha llevado',
        u'se ha llevado',
        u'ha intercambiado ' + random.choice([u'dos cigarros', u'un porro', u'una chusta', 'una calada']) + ' por',
        u'ha ganado en una apuesta',
        u'se ha comprado en un estanco',
        u'se ha comprado en un todo a cien',
        u'se ha comprado clandestinamente en un kiosko',
        u'ha comprado en el ' + random.choice([u'Lidl', u'Corte Inglés', u'Alcampo', u'Carrefour', u'Mercadona', u'Día%', u'Masymas']),
        u'ha recibido un paquete de ' + random.choice([u'Ebay', u'Amazon', u'MediaMarkt']) + u' con',
        u'ha comprado por ' + random.choice([u'Wallapop']),
        u'ha ido al mercadillo y ha comprado',
        u'se ha llevado en una caja de cereales',
        u'se ha encontrado una caja en la que había',
        u'se ha encontrado un cofre en el que había',
        u'ha recibido por su cumpleaños',
        u'se ha llevado por la puta cara',
        u'se ha llevado por su cara bonita',
        u'se ha llevado como premio en ' + random.choice([u'un concurso de talentos', u'una batalla de gallos', u'una concurso de baile', u'un show de belleza']),
        u'se ha llevado en un sorteo de ' + random.choice([u'@HTCMania', u'@PcComponentes', u'la ONCE', u'Forocoches']),
        u'llevaba mucho tiempo ahorrando para comprarse',
        u'iba por la calle cuando alguien le regaló',
        u'llevaba meses coleccionando tapas de yogurt para conseguir',
        u'ha ido coleccionando fascículos para montar',
        u'es tan manitas que se ha construido',
        u'vio a alguien desprevenido y le robó',
        u'se ha comprado en la deep web'
    ])

def FRIENDS_TIED(player_1, player_2):
    return (random.choice([
        player_1.get_name() + ' y ' + player_2.get_name() + u' son tan ' + get_x_or_y_plural([player_1, player_2],
        'buenos amigos', 'buenas amigas') + ' que no han querido pelearse.',
        player_1.get_name() + u' iba a reventar a ' + player_2.get_name() + u', pero se dio cuenta de que en el fondo le cae bien.',
        u'La amistad ha impedido que ' + player_1.get_name() + u' se cargase a ' + player_2.get_name() + u'.',
        player_1.get_name() + u' contó un chiste tan malo que ' + player_2.get_name() + u' estuvo a punto de ' + get_x_or_y(player_1, 'matarlo', 'matarla') + u', pero cambió de opinión en el último momento porque son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        player_1.get_name() + ' se ha negado a pelearse con ' + player_2.get_name() + u' a pesar de que le tenga ganas, ya que son ' + get_x_or_y_plural([player_1, player_2], 'amigos', 'amigas') + '.'
    ]))

GETS_RID_OF = u'se ha deshecho de'

def HAS_ALREADY_KILLED(kills_count):
    return u' '.join((u'y ya lleva', kills_count, u'muertes'))

def HAS_NOW(attack, defense):
    if attack != None and defense != None:
        return random.choice([
            u' '.join([u'Ahora tiene', attack, u'en ataque y', defense, u'en defensa.']),
            u' '.join([u'Ataque', attack, u'y defensa', defense + '.']),
            u' '.join([u'Su ataque es ahora de', attack, u'y su defensa de', defense + '.']),
        ])
    elif attack != None:
        return random.choice([
            u' '.join([u'Ahora tiene', attack, u'en ataque.']),
            u' '.join([u'Ataque', attack + u'.']),
            u' '.join([u'Su ataque es ahora de', attack + u'.']),
            u' '.join([u'Su nuevo ataque es', attack + u'.'])
        ])
    elif defense != None:
        return random.choice([
            u' '.join([u'Ahora tiene', defense, u'en defensa.']),
            u' '.join([u'Defensa', defense + u'.']),
            u' '.join([u'Su defensa es ahora de', defense + u'.']),
            u' '.join([u'Su nueva defensa es', defense + u'.'])
        ])

def I_COMPOSED(player, action, event, has_now):
    return u' '.join((u'¡' + player.get_name(), action, event.name + '!', has_now))


def INFECTION_IMMUNITY():
    return random.choice([
        u'¡A partir de ahora es inmune al COVID-19!',
        u'¡A partir de ahora tiene inmunidad contra el COVID-19!',
        u'¡A partir de ahora el COVID-19 no le afecta!',
        u'¡A partir de ahora no puede ser infectado con el COVID-19!'
    ])

def INJURE_ACTION():
    return random.choice([u'ha recibido', u'ha padecido'])

def INJURE_IMMUNITY():
    return random.choice([
        u'¡A partir de ahora no sufrirá heridas ni lesiones!',
        u'¡A partir de ahora es inmune a heridas y lesiones!',
        u'¡A partir de ahora tiene inmunidad contra lesiones y heridas!',
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
            u'ha sido ' + get_x_or_y(players[0], 'seleccionado', 'seleccionada') + ' para representar a ' + place_name + u'.',
        ])
    else:
        return random.choice([
            u'representarán a ' + place_name + u'.',
            u'ya están ' + get_x_or_y_plural(players, 'preparados', 'preparadas') + ' para representar a ' + place_name + u'.',
            u'han sido ' + get_x_or_y_plural(players, 'elegidos', 'elegidas') + ' para representar a ' + place_name + u'.',
            u'han sido ' + get_x_or_y_plural(players, 'seleccionados', 'seleccionadas') + ' para representar a ' + place_name + u'.',
        ])

def KILL_ACTION():
    return random.choice([
        u'se ha cargado a',
        u'ha matado a',
        u'se ha llevado por delante a',
        u'ha destrozado a',
        u'ha desintegrado a',
        u'ha dejado KO a',
        u'ha ejecutado a',
        u'ha despachado a',
        u'ha emboscado a',
        u'ha terminado con el sufrimiento que era la vida de',
        u'ha asesinado a sangre fría a',
        u'se ha quitado de en medio a',
        u'se ha quitado de encima a',
        u'ha degollado a',
        u'ha asfixiado a',
        u'ha lapidado a',
        u'ha desnucado a',
        u'ha mandado al otro barrio a',
        u'ha reventado a',
        u'ha liquidado a',
        u'ha aniquilado a',
        u'ha despachado a',
        u'ha acabado con',
        u'ha apuñalado a',
        u'ha acribillado a',
        u'ha estrangulado a',
        u'ha apaleado a'
    ])

def KILL_METHOD(player):
    return random.choice([
        u'con sus puños',
        u'por quitarle el último rollo de papel higiénico',
        u'a lo jíbiri',
        u'y le ha hecho tea-bag',
        u'a tortazo limpio',
        u'por la gloria de ESPAÑA',
        u'de un cabezazo',
        u'de un codazo',
        u'y le ha hecho un dab',
        u'y le ha hecho un baile del fortnite',
        u'y le ha hecho el Swish Swish',
        u'sin despeinarse',
        u'con una llave de kárate',
        u'con una llave de taekwondo',
        u'y le ha cantado una canción triste',
        u'y ha hecho un perreo duro hasta el suelo',
        u'haciendo capoeira',
        u'y se ha puesto a bailar',
        u'a hostia limpia',
        u'y le ha cantado una bulería',
        u'y le ha recitado un poema de Neruda',
        u'y le ha cantado una balada',
        u'y le ha recitado un poema',
        u'y le ha quitado el trabajo',
        u'sin esforzarse',
        u'sin inmutarse',
        u'y ha seguido a lo suyo',
        u'y se ha acabado el bocata tranquilamente',
        u'con lágrimas en los ojos',
        u'con mirada de psicópata',
        u'y ha gritado SUUUUUUUUUUUUUUUUU',
        u'y ha gritado ' + get_x_or_y(player, u'ESTOY MAMADÍSIMO HIJO DE PUTA', u'ESTOY MAMADÍSIMA HIJO DE PUTA'),
        u'en una epic prank',
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

def NOBODY_WON(tweet):
    return u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado... ¡otra vez será!'

REPLACED = u'Se lo queda y se deshace de'

def REVIVED(tweet):
    player = tweet.player
    return u' '.join((player.get_name(), random.choice([
        u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!', u'la muerta. ¡Qué zooorrraaaaa! (sin trazas de patriarcado).'),
        u'ha vuelto a la vida bajo extrañas circunstancias.',
        u'ha vuelto en forma de chapa y ahora es un zombie.',
        u'ha resucitado en mitad de su funeral y ha vuelto a la batalla.',
        u'tiene enchufe y el creador del bot le ha resucitado.',
        u'ha vuelto del otro barrio.'
    ])))

def WAS_INFECTED(tweet):
    player = tweet.player
    return random.choice([
        player.get_name() + u' ha pillado el coronavirus.',
        u'Alguien ha infectado a ' + player.get_name() + u' con el coronavirus.',
        player.get_name() + u' no se ha lavado las manos lo suficiente y ha contraído el coronavirus.',
        player.get_name() + u' debería de haber seguido las recomendaciones para no pillar el coronavirus.',
        player.get_name() + u' ha contraído el coronavirus por ir al Mercadona a comprar papel higiénico.',
        player.get_name() + u' se saltó la cuarentena para fumarse uno y ha pillado el coronavirus.'
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
    return random.choice([
        MOVE_ACTION_AIR(),
        u'ha ido de',
        u'ha viajado de',
        u'se ha movido de',
        u'ha conducido su ' + random.choice([u'Seat León', u'Fiat Multipla', u'Renault Megane', u'Seat Ibiza', u'Golf', u'Opel Corsa', u'Ford Focus', u'Opel Astra', u'BMW Serie 3']) + ' de',
        random.choice([u'está tan en forma que ha ', u'se aburría y ha ', u'está tan cachas que ha ', u'está tan fuerte que ha ']) + random.choice([u'ido en bici', u'ido a trote', u'hecho un sprint', u'ido a la pata coja', u'ido corriendo', u'ha hecho footing']) + u' de',
        u'ha llamado a ' + random.choice([u'un taxi', u'un Uber', u'un Cabify']) + u' para que le lleve de',
        u'ha hecho ' + random.choice([u'autostop', u'dedo']) + u' para que le lleve de',
        u'ha ido en ' + random.choice([u'moto', u'su scooter', u'AVE', u'mochillo', u'limusina con su chófer', u'patinete eléctrico', u'tren regional', u'Alsa', u'Blablacar', u'un coche robado a lo GTA']) + u' de'
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

def POWERUP_ACTION():
    return random.choice([
        u'ha cogido',
        u'ha encontrado'
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
        u'Hello darkness, my old friend. I´ve come to talk with you again.',
        u'Me voy a dormir, cualquier emergencia me avisan que yo al medio día les respondo.',
        u'Buenas noches, que pasen una linda y bendecida noche. Dulces sueños hasta mañana amigos ya amigas.',
        u'Se me acabaron las pilas. Buenas noches. Chistes cortos buenos, graciosos y divertidos para pasar un momento genial para compartir con las amistades y familiares.',
        u'Hello darkness, my old friend. I´ve come to talk with you again.',
        u'Hello darkness, my old friend. I´ve come to talk with you again.',
        u'Hello darkness, my old friend. I´ve come to talk with you again.',
    ])

def SPECIAL_ACTION():
    return random.choice([u'ha encontrado', u'ha cogido'])

def START(tweet):
    return u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Que empiece el juego.'

def STOLE(tweet):
    return u' '.join((tweet.player.get_name(), u'le ha robado', tweet.item.name, u'a', tweet.player_2.get_name() + '.'))

def STOLE_AND_REPLACED(tweet):
    return u' '.join((STOLE(tweet), u'Como es mejor, se ha deshecho de su', tweet.old_item.name + '.'))

def STOLE_AND_THREW(tweet):
    return u' '.join((STOLE(tweet), u'Como tiene cosas mejores, lo ha tirado a la basura.'))

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
        player_1.get_name() + ' y ' + player_2.get_name() + u' se han peleado, pero se han cansado antes de que nadie cayera en combate, así que se han hecho ' + get_x_or_y_plural([player_1, player_2],'amigos.', 'amigas.'),
        player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho una tregua y ahora son ' + get_x_or_y_plural([player_1, player_2],'amigos.', 'amigas.'),
        player_1.get_name() + ' ha formado una alianza con ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        'Aunque no se caigan muy bien, ' + player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho un pacto y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        'Una bonita amistad ha surgido entre ' + player_1.get_name() + ' y ' + player_2.get_name() + u'. A partir de ahora se ayudarán mutuamente.',
        player_1.get_name() + ' y ' + player_2.get_name() + u' iban tan ' + get_x_or_y_plural([player_1, player_2], 'ciegos', 'ciegas') + ' anoche que se habían olvidado de que eran ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        'Usando sus encantos, ' + player_1.get_name() + ' ha conquistado a ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
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
    return u' '.join((player.get_name(), MOVED_SING(), location.name, trapped, trapped_by.get_name() + u'. ¡Qué torpe!'))

def TREASON(tweet):
    player_1 = tweet.player
    player_2 = tweet.player_2
    return random.choice([
        u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Parece que no se caían tan bien, ',
        get_x_or_y([player_1, u'Menudo', u'Menuda']) + ' judas, ',
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
        'Ya no son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        'Han dejado de ser ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        'Su amistad se ha roto.'
    ])

WINNER_INFECTION = u'¡Incluso ha sobrevivido al coronavirus!'
WINNER_INJURY_LIST = u'Todo ello a pesar de padecer'
WINNER_ITEM_LIST = u'Además, ha acabado teniendo'
WINNER_NO_KILLS = u'Lo ha conseguido sin llevarse por delante a nadie.'
WINNER_ONE_KILL = u'Lo ha conseguido llevándose por delante a un sólo participante.'

def WINNER_MULTI_KILL(kill_count):
    return u' '.join([u'Lo ha conseguido llevándose por delante a', kill_count, 'participantes.'])

def WINNER_COMPOSED(winner, kills, item_list, infection):
    return u' '.join((u'¡' + winner.get_name(), u'ha ganado en ' + winner.location.name + '! ' + kills + item_list, 'El ataque de', winner.get_name(), u'llegó a ser de', str(winner.get_attack()), u'y su defensa de', str(winner.get_defense()) + '.', infection))

def WINNER_DISTRICTS_COMPOSED(winners_str, district, kills_count):
    return u' '.join((winners_str, u'han ganado, consiguiendo un total de', str(kills_count), u'muertes. ¡' + district, u'es la última ciudad en pie de España!'))

WITH = u'con'
