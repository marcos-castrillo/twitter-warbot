#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from models.tweet_type import Tweet_type

def get_message(type, args = None):
    message = ''

    if type == Tweet_type.start:
        message = start()
    elif type == Tweet_type.winner:
        message = winner(args[0])
    elif type == Tweet_type.nobody_won:
        message = nobody_won()
    elif type == Tweet_type.somebody_got_ill:
        message = somebody_got_ill(args[0], args[1])
    elif type == Tweet_type.somebody_got_injured:
        message = somebody_got_injured(args[0], args[1])
    elif type == Tweet_type.somebody_found_item:
        message = somebody_found_item(args[0], args[1])
    elif type == Tweet_type.somebody_replaced_item:
        message = somebody_replaced_item(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_doesnt_want_item:
        message = somebody_doesnt_want_item(args[0], args[1])
    elif type == Tweet_type.somebody_tied_and_became_friend:
        message = somebody_tied_and_became_friend(args[0], args[1])
    elif type == Tweet_type.somebody_tied_and_was_friend:
        message = somebody_tied_and_was_friend(args[0], args[1])
    elif type == Tweet_type.somebody_escaped:
        if len(args) == 3:
            message = somebody_escaped(args[0], args[1], args[2])
        elif len(args) == 2:
            message = somebody_escaped(args[0], args[1])
    elif type == Tweet_type.somebody_killed:
        if len(args) == 5:
            message = somebody_killed(args[0], args[1], args[2], args[3], args[4])
        elif len(args) == 4:
            message = somebody_killed(args[0], args[1], args[2], args[3])
        elif len(args) == 3:
            message = somebody_killed(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_revived:
        message = somebody_revived(args[0], args[1])
    elif type == Tweet_type.somebody_died:
        message = somebody_died(args[0])
    elif type == Tweet_type.somebody_moved:
        message = somebody_moved(args[0], args[1], args[2])
    elif type == Tweet_type.destroyed:
        message = destroyed(args[0], args[1], args[2], args[3])
    elif type == Tweet_type.somebody_couldnt_move:
        message = somebody_couldnt_move(args[0])
    elif type == Tweet_type.trap:
        message = trap(args[0], args[1])
    elif type == Tweet_type.trapped:
        message = trapped(args[0], args[1], args[2])
    elif type == Tweet_type.dodged_trap:
        message = dodged_trap(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_stole:
        message = somebody_stole(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_stole_and_replaced:
        message = somebody_stole_and_replaced(args[0], args[1], args[2], args[3])
    elif type == Tweet_type.somebody_stole_and_threw:
        message = somebody_stole_and_threw(args[0], args[1], args[2])
    elif type == Tweet_type.somebody_powerup:
        message = somebody_powerup(args[0], args[1])
    elif type == Tweet_type.monster_appeared:
        message = monster_appeared(args[0])
    elif type == Tweet_type.monster_moved:
        message = monster_moved(args[0], args[1])
    elif type == Tweet_type.somebody_died_of_infection:
        message = somebody_died_of_infection(args[0])
    elif type == Tweet_type.somebody_was_infected:
        message = somebody_was_infected(args[0])
    elif type == Tweet_type.monster_disappeared:
        message = monster_disappeared(args[0])
    elif monster_killed(args[0], args[1]):
        message = monster_killed(args[0], args[1])
    return (message + '\n').encode('utf-8')

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

def get_find_action():
    return random.choice([
        u'ahora tiene',
        u'ahora tiene',
        u'ha encontrado',
        u'ha encontrado',
        u'se ha encontrado',
        u'se ha encontrado',
        u'ha cogido',
        u'ha cogido',
        u'ha entrado en una casa y ha robado',
        u'ha robado',
        u'ha robado',
        u'ha recogido',
        u'ha recogido',
        u'se ha agenciado',
        u'ha conseguido',
        u'ha conseguido',
        u'por suplicarle al creador de este bot que le diera algo, se ha llevado',
        u'por tener enchufe con el programador de esto se ha llevado',
        u'rebuscando entre la basura ha encontrado',
        u'se ha llevado en la tómbola',
        u'se ha llevado',
        u'se ha llevado',
        u'ha intercambiado ' + random.choice(['un gramo', u'dos cigarros', u'medio porro', u'un porro', u'una chusta', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por',
        u'ha ganado en una apuesta',
        u'se ha comprado en un estanco',
        u'se ha comprado en un todo a cien',
        u'se ha comprado clandestinamente en un kiosko',
        u'ha comprado en el ' + random.choice([u'Lidl', u'Corte Inglés', u'Alcampo', u'Carrefour', u'Mercadona', u'Día%', u'Masymas']),
        u'ha recibido un paquete de ' + random.choice([u'Ebay', u'Amazon', u'PcComponentes', u'MediaMarkt']) + u' con',
        u'ha comprado por ' + random.choice([u'Wallapop']),
        u'ha ido al mercadillo y ha comprado',
        u'se ha llevado en una caja de cereales',
        u'se ha encontrado una caja misteriosa en la que había',
        u'ha recibido por su cumpleaños',
        u'se ha llevado por la puta cara',
        u'se ha llevado por su cara bonita',
        u'se ha llevado como premio en ' + random.choice([u'un concurso de talentos', u'una batalla de gallos', u'una concurso de baile', u'un show de belleza']),
        u'se ha llevado en un sorteo de ' + random.choice([u'HTCMania', u'PcComponentes', u'la ONCE', u'Forocoches']),
        u'llevaba mucho tiempo ahorrando para comprarse',
        u'iba andando por la calle cuando alguien le regaló',
        u'llevaba meses coleccionando tapas de yogurt para conseguir',
        u'ha ido coleccionando fascículos para montar',
        u'es tan manitas que se ha construido',
        u'vio a alguien desprevenido por la calle y le robó',
        u'se ha comprado en la deep web'
    ])

def start():
    return (u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Que empiece el juego.')

def winner(player):
    item_list = ''
    injury_list = ''
    kills = ''
    sufix = ''
    if player.kills == 0:
        kills = u'Lo ha conseguido sin llevarse por delante a nadie.'
    elif player.kills == 1:
        kills = u'Lo ha conseguido llevándose por delante a sólo 1 participante.'
    else:
        kills = u'Lo ha conseguido llevándose por delante a ' + str(player.kills) + ' participantes.'

    if len(player.item_list) > 0:
        list = ''
        for i, item in enumerate(player.item_list):
            if i == 0:
                list = item.name
            elif i == len(player.item_list) - 1:
                list = list + ' y ' + item.name
            else:
                list = list + ', ' + item.name

        item_list = u' Además, ha acabado teniendo ' + list + '.'
    if len(player.injury_list) > 0:
        list = ''
        for i, item in enumerate(player.injury_list):
            if i == 0:
                list = item.name
            elif i == len(player.item_list):
                list = list + ' y ' + item.name
            else:
                list = list + ', ' + item.name
        injury_list = ' Todo ello a pesar de padecer ' + list + '.'
    if player.infected:
        sufix = '¡Incluso ha sobrevivido al coronavirus!'
    return u' '.join((u'¡' + player.get_name(), u'ha ganado en ' + player.location.name + '! ' + kills + item_list, 'El ataque de', player.get_name(), u'llegó a ser de', str(player.get_attack()), u'y su defensa de', str(player.get_defense()) + '.', sufix))

def nobody_won():
    return (u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado... ¡otra vez será!')

def somebody_got_ill(player, illness):
    ill_verb = random.choice(['ha cogido', u'ha contraído', u'ha padecido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, illness.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(illness.attack), 'en ataque y', str(player.get_defense()) +  get_amount(illness.defense), 'en defensa.'))

def somebody_got_injured(player, injury):
    ill_verb = random.choice([u'ha recibido', u'ha cogido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, injury.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(injury.attack), 'en ataque y', str(player.get_defense()) +  get_amount(injury.defense), 'en defensa.'))

def somebody_found_item(player, item):
    action = get_find_action()

    if item.attack != 0:
        now_he_has = ' Ahora tiene ' + str(player.get_attack()) + get_amount(item.attack) + ' en ataque'
    if item.attack != 0 and item.defense != 0:
        now_he_has = u' '.join([now_he_has, 'y', str(player.get_defense()) + get_amount(item.defense), 'en defensa.'])
    elif item.defense != 0:
        now_he_has = ' Ahora tiene ' + str(player.get_defense()) + get_amount(item.defense) + ' en defensa.'
    elif item.attack == 0:
        now_he_has = ''
    else:
        now_he_has = now_he_has + '.'

    loot = ''
    if player.location.loot:
        loot = random.choice([
            u' Ha conseguido algo mejor de lo normal porque está en ' + player.location.name + u'.',
            u' Como ' + player.location.name + u' tiene mejor loot de lo normal, se ha llevado algo muy bueno.',
            u' Ha tenido suerte porque está en ' + player.location.name + u'.'
        ])

    return u' '.join((u'¡' + player.get_name(), action, item.name + '!' + now_he_has + loot))

def somebody_replaced_item(player, item_new, item_old):
    action = get_find_action()
    return u' '.join((u'¡' + player.get_name(), action, item_new.name + '!', 'Se lo queda y se deshace de', item_old.name + '.', 'Ahora tiene', str(player.get_attack()) + get_amount(item_new.attack - item_old.attack), 'en ataque y', str(player.get_defense()) + get_amount(item_new.defense - item_old.defense), 'en defensa.'))

def somebody_doesnt_want_item(player, item):
    action = get_find_action()

    return u' '.join((u'¡' + player.get_name(), action, item.name + '!', 'Pero no lo quiere porque ya tiene cosas mejores... (' + player.item_list[0].name,  'y', player.item_list[1].name + ').'))

def somebody_tied_and_became_friend(player_1, player_2):
    return random.choice([
    player_1.get_name() + ' y ' + player_2.get_name() + u' se han peleado, pero se han cansado antes de que nadie cayera en combate, así que se han hecho ' + get_x_or_y_plural([player_1, player_2],'amigos.', 'amigas.'),
    player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho una tregua y ahora son ' + get_x_or_y_plural([player_1, player_2],'amigos.', 'amigas.'),
    player_1.get_name() + ' ha formado una alianza con ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    'Aunque no se caigan muy bien, ' + player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho un pacto y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    'Una bonita amistad ha surgido entre ' + player_1.get_name() + ' y ' + player_2.get_name() + u'. A partir de ahora se ayudarán mutuamente.',
    player_1.get_name() + ' y ' + player_2.get_name() + u' iban tan ' + get_x_or_y_plural([player_1, player_2], 'ciegos.', 'ciegas.') + ' anoche que se habían olvidado de que eran ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    'Usando sus encantos, ' + player_1.get_name() + ' ha conquistado a ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
    ])

def somebody_tied_and_was_friend(player_1, player_2):
    return (random.choice([
    player_1.get_name() + ' y ' + player_2.get_name() + u' son tan ' + get_x_or_y_plural([player_1, player_2],
    'buenos amigos', 'buenas amigas') + ' que no han querido pelearse.',
    player_1.get_name() + u' iba a reventar a ' + player_2.get_name() + u', pero se dio cuenta de que en el fondo le cae bien.',
    u'La amistad ha impedido que ' + player_1.get_name() + u' se cargase a ' + player_2.get_name() + u'.',
    player_1.get_name() + u' contó un chiste tan malo que ' + player_2.get_name() + u' estuvo a punto de ' + get_x_or_y(player_1, 'matarlo', 'matarla') + u', pero cambió de opinión en el último momento porque son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    player_1.get_name() + ' se ha negado a pelearse con ' + player_2.get_name() + u' a pesar de que le tenga ganas, ya que son ' + get_x_or_y_plural([player_1, player_2], 'amigos', 'amigas') + '.'
    ]))

def somebody_escaped(player_1, player_2, unfriend = False):
    sufix = ''
    if unfriend:
        sufix = ' Han dejado de ser ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
    return (random.choice([
        player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_1.get_name() + u' ha salido por patas cual cobarde.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' han empezado a pelear, pero ' + player_2.get_name() + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.get_name() + u' en los ojos y salió corriendo.',
        player_1.get_name() + u' iba a asesinar a ' + player_2.get_name() + u' por la espalda, pero éste se dio cuenta en el último momento. ' + player_1.get_name() + u' ha salido por patas.',
        player_1.get_name() + u' se ha encarado con ' + player_2.get_name() + u', pero ' + player_2.get_name() + u' se ha achantado y salido corriendo.'
    ]) + sufix)

def somebody_killed(player_1, player_2, are_friends = False, new_item = None, old_item = None):
    kill_verb = random.choice([
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
        u'ha salido de su escondite y se ha agazapado sobre a',
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

    friend_message = ''

    kill_method = random.choice([
        u' con sus puños',
        u' por quitarle el último rollo de papel higiénico',
        u' a lo jíbiri',
        u' y le ha hecho tea-bag',
        u' a tortazo limpio',
        u' por la gloria de ESPAÑA',
        u' de un cabezazo',
        u' de un codazo en el esternón',
        u' y le ha hecho un dab',
        u' y le ha hecho un baile del fortnite',
        u' sin despeinarse',
        u' con una llave de kárate',
        u' y le ha cantado una canción triste',
        u' y ha hecho un perreo duro hasta el suelo',
        u' haciendo capoeira',
        u' y se ha puesto a bailar',
        u' a hostia limpia',
        u' y le ha cantado una bulería',
        u' y le ha cantado una balada',
        u' y le ha recitado un poema',
        u' y le ha quitado el trabajo',
        u' sin esforzarse',
        u' sin inmutarse',
        u' y ha seguido a lo suyo',
        u' y se ha acabado el bocata tranquilamente',
        u' con lágrimas en los ojos',
        u' con mirada de psicópata',
        u' y ha gritado SUUUUUUUUUUUUUUUUU',
        u' y ha gritado ' + get_x_or_y(player_1, u'ESTOY MAMADÍSIMO HIJO DE PUTA', u'ESTOY MAMADÍSIMA HIJO DE PUTA'),
        u' en una epic prank',
        u' en un abrir y cerrar de ojos',
        u' sin pestañear',
        u' por turras',
        u', lo ha grabado y lo ha subido a su instagram',
        u' y lo ha tuiteado',
        u' y le ha sacado una foto de recuerdo',
        u' y ha tirado su cadáver al contenedor de basura',
        u' y se ha ido de cañas',
        u' haciendo una buena escabechina con sus restos',
        u' sudando mogollón',
        u' y se ha fumado un cigarrito',
        u' mientras sus colegas le gritaban ACÁBALO',
        u' y se ha tirado un eructo',
        u' y se ha tirado un pedarro',
        u' y se ha tirado un cuesco',
        u' sin mucho esfuerzo',
        u' a duras penas',
        u'',
        u'',
        u''
    ])
    kills_count = '.'
    stole = ''
    fav = ''

    if are_friends:
        friend_message = random.choice([
        u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Parece que no se caían tan bien, ',
        u'Menudo judas, ',
        u'Vaya puñalada por la espalda, ',
        u'Menuda traición, ',
        u'Por lo visto no eran tan ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Premio ' + get_x_or_y(player_1, u'al mejor amigo', u'a la mejor amiga') + u' del año. ',
        ''
        ])
    if player_1.get_best_attack_item() != None:
        kill_method = u' con ' + player_1.get_best_attack_item().name
    if player_1.kills > 1:
        kills_count = u' y ya lleva ' + str(player_1.kills) + u' muertes. ' + random.choice([
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        u'Qué ' + get_x_or_y(player_1, u'tío.', u'tía.'),
        u'Vaya fiera.',
        u'Impresionante.',
        u'Es ' + get_x_or_y(player_1, u'un', u'una') + u' máquina.',
        u'Menudo monstruo.',
        u'Está ' + get_x_or_y(player_1, u'rocoso.', u'rocosa.'),
        u'Qué crack.',
        u'JO-DER.',
        u'Redios.',
        u'Es un tifón.',
        u'No hay quién ' + get_x_or_y(player_1, u'lo', u'la') + ' pare.',
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
        get_x_or_y(player_1, u'Esta mamadísimo.', u'Está mamadísima.')])
    if new_item != None and old_item != None:
        stole = u' Además, le ha robado ' + new_item.name + u' y se ha deshecho de ' + old_item.name + '.'
    elif new_item != None:
        stole = u' Además, le ha robado ' + new_item.name + '.'

    return u' '.join((friend_message + player_1.get_name(), kill_verb, player_2.get_name() + kill_method + kills_count + stole))

def somebody_revived(player, is_rebuilt):
    rebuilt = ''
    # if is_rebuilt:
    #     rebuilt = u'¡Además, ' + player.district.name + u' ha sido reconstruida y su equipo vuelve a la batalla!.'

    return u' '.join((player.get_name(), random.choice([
    u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!', u'la muerta. ¡Qué zooorrraaaaa! (sin trazas de patriarcado).'),
    u'ha vuelto a la vida bajo extrañas circunstancias.',
    u'ha vuelto en forma de chapa y ahora es un zombie.',
    u'ha resucitado en mitad de su funeral y ha vuelto a la batalla.',
    u'tiene enchufe y el creador del bot le ha resucitado.'
    u'ha vuelto del otro barrio.'
    ]), rebuilt))

def somebody_died(player):
    return u' '.join((player.get_name(), random.choice([
        u'ha sido víctima de un rayo y se ha muerto en el acto.',
        u'ha bebido un chupito de lejía.',
        u'ha bebido un chupito de cianuro.',
        u'se ha pegado un tiro.',
        u'se le olvidó cómo respirar.',
        u'se ha esnucado ' + get_x_or_y(player, 'él solito.', 'ella solita.'),
        u'se la ha pegado por conducir con unas copas de más.',
        u'tuvo un piñazo con un Seat Panda.',
        u'ha muerto repentinamente por un fallo cardíaco. ¡Hay que hacer más deporte!',
        u'ha empezado a toser, a toser y a toser y se ha acabado asfixiando. Estos chavalitos...',
        u'ha amochado de repente.',
        u'ha sido atropellado por una moto y se fue a la puta.'
    ])))

def somebody_moved(player, old_location, new_location):
    action = random.choice([
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
    u'ha llamado al taxi de ' + random.choice([u'Rebollo', u'Santi', u'Aquilino', u'Germán']) + u'para que le lleve de',
    u'ha llamado al taxi de ' + random.choice([u'Rebollo', u'Santi', u'Aquilino', u'Germán']) + u'para que le lleve de',
    u'ha ido en ' + random.choice([u'tractor', u'patinete', u'motorrabo', u'bici']) + u' de',
    u'ha ido en ' + random.choice([u'tractor', u'patinete', u'motorrabo', u'bici']) + u' de',
    u'ha ido en skate haciendo backflips de',
    u'ha cogido el coche y ha hecho un derrape de',
    u'ha cogido un Blabacar de'
    ])

    return u' '.join((player.get_name(), action, old_location.name, 'a', new_location.name + '.'))

def destroyed(place, dead_list, escaped_list, new_location):
    # prefix = random.choice([
    #     u'El equipo de ' + place.name + u' ha perdido, por lo que la ciudad ha sido reducida a cenizas'
    # ])
    prefix = random.choice([
       u'Un meteorito ha caído en ' + place.name + u' y lo ha destruido',
       place.name + u' ha colapsado',
       u'Un terrible incendio ha reducizo ' + place.name + u' a cenizas',
       u'Un terrorista ha dinamitado ' + place.name,
       u'Una riada ha inundado todo ' + place.name,
       u'Una bomba nuclear ha reducido ' + place.name + u' a pedazos',
       u'Un huracán ha arrasado todo ' + place.name,
       u'Una nube de gas tóxico ha llegado a ' + place.name + u' haciéndolo inhabitable',
       u'Una epidemia de listeriosis se ha extendido por ' + place.name + u'.',
       u'El mundo está mejor sin ' + place.name  + u', así que el creador de este bot ha decidido cargárselo sin más',
       place.name + u' se ha ido a la puta mierda',
       u'Una terrible sequía ha asolado ' + place.name
       ])

    if len(dead_list) == 0:
        sufix = '.'
    elif len(dead_list) == 1:
        sufix = random.choice([
        ' y ' + dead_list[0].get_name() + u' ha fallecido en un trágico accidente.',
        ' y ' + dead_list[0].get_name() + u' ha amochado.',
        ' y ' + dead_list[0].get_name() + u' ha muerto.',
        ' y ' + dead_list[0].get_name() + u' la ha palmado.',
        ' y ' + dead_list[0].get_name() + u' ha espichado.',
        '. DEP ' + dead_list[0].get_name() + u'.',
        ' y ' + dead_list[0].get_name() + u' se ha ido al otro barrio.',
        ' y ' + dead_list[0].get_name() + u' ya no está entre nosotros.',
        ' y se ha llevado por delante a ' + dead_list[0].get_name() + u'.'])
    else:
        dead = []
        dead_str = ''
        for i, d in enumerate(dead_list):
            dead.append(d.get_name())
        for i, d in enumerate(dead):
            if i == 0:
                dead_str = d
            elif i == len(dead) - 1:
                dead_str = dead_str + ' y ' + d
            else:
                dead_str = dead_str + ', ' + d
        sufix = random.choice([
            u' y ' + dead_str + u' han fallecido en un trágico accidente.',
            ' y ' + dead_str + u' han amochado.',
            ' y ' + dead_str + u' la han palmado.',
            ' y ' + dead_str + u' han muerto.',
            ' y ' + dead_str + u' no han sobrevivido.',
            ' y ' + dead_str + u' han espichado.',
            u' y hay un luto de 3 días por ' + dead_str + u'.',
            u' . DEP ' + dead_str + u'.'
        ])

    susufix = ''
    escaped = []

    if new_location and len(escaped_list) > 0:
        for i, d in enumerate(escaped_list):
            escaped.append(d.get_name())
        for i, d in enumerate(escaped):
            if i == 0:
                susufix_str = d
            elif i == len(escaped) - 1:
                susufix_str = susufix_str + ' y ' + d
            else:
                susufix_str = susufix_str + ', ' + d

        susufix = u' ' + susufix_str + get_sing_or_pl(escaped_list, u' se ha movido a ', u' se han movido a ') + new_location.name + u'.'

    return (prefix + sufix + susufix)

def somebody_couldnt_move(player):
    return u' '.join((player.get_name(), u'se ha terminado toda la comida de', player.location.name, u'y no ha podido acceder a otros lugares, por lo que ha muerto de hambre.'))

def trap(player, place):
    return u' '.join((player.get_name(), u'ha puesto una trampa en', player.location.name + '.'))

def trapped(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name, u'pero se ha comido la trampa que había puesto', trapped_by.get_name() + u'. ¡Qué torpe!'))

def dodged_trap(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name + u', ha visto la trampa que había puesto', trapped_by.get_name(), 'y la ha destruido.'))

def somebody_stole(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + '.'))

def somebody_stole_and_replaced(robber, robbed, item, old_item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + u'. Como es mejor, se ha deshecho de su' + old_item.name + '.'))

def somebody_stole_and_threw(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + u'. Como tiene cosas mejores, lo ha tirado a la basura.'))

def somebody_powerup(player, powerup):
    powerup_verb = random.choice(['ha cogido', u'ha encontrado'])
    return u' '.join((u'¡' + player.get_name(), powerup_verb, powerup.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(powerup.attack), 'en ataque y', str(player.get_defense()) +  get_amount(powerup.defense), 'en defensa.'))

def monster_appeared(place):
    return random.choice([
    u'Una patrulla de la guardia ha aparecido en ' + place.name + '.',
    u'Una patrulla de la guardia ha sido avistada en ' + place.name + '.',
    u'Control en ' + place.name + '.',
    u'¡Ojo! Alguien ha avistado una patrulla de la guardia en ' + place.name + '.',
    u'Se ha producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
    ])

def monster_moved(place, new_place):
    if new_place.name == u'Santa María':
        return (u'Ratonera sucia, la guardia se ha ido de ' + place.name + '.')
    if new_place.name == u'Bercianos':
        return (u'Como son las fiestas de Bercianos (#ProjectBercy) y todo el mundo está allí, la guardia se ha tenido que ir de ' + place.name + '.')

    return random.choice([
        u'Alguien se ha chivado de que hay un cultivo de maría en ' + new_place.name + u', por lo que la guardia se ha ido de ' + place.name + '.'
        u'¡La guardia se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
        u'Ha habido movida en ' + new_place.name + u', por lo que la guardia ha tenido que irse de ' + place.name + '.',
        u'La guardia se ha movido de ' + place.name + u' a ' + new_place.name + '.'
    ])

def monster_disappeared(place):
    return random.choice([
        u'¡La guardia se ha esfumado de ' + place.name + u'!',
        u'La guardia ya no está en ' + place.name + '.',
        u'Se acabó el turno de la guardia, por lo que se han ido de ' + place.name + u'.'
    ])

def monster_killed(player, place):
    return random.choice([
        player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado', 'arrestada') + u' por la guardia de ' + place.name + u'. Aquí acaba su aventura.',
         player.get_name() + ' tiene una pinta sospechosa y la guardia se lo ha llevado de ' + place.name + u' sólo por si acaso.',
        u'¡La guardia le ha pillado una bolsita a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(player, 'lo', 'la') + u' han llevado, hay que esconderla mejor!',
        u'La guardia ha desahuciado a palos a ' + player.get_name() + u' de ' + place.name + u'. ¡Game over!',
        u'La guardia ha detenido a ' + player.get_name() + u' por salir a correr en mitad de la cuarentena.',
        u'La guardia ha detenido a ' + player.get_name() + u' por salir a pasear a su perro en mitad de la cuarentena.',
        'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la guardia. Se ' + get_x_or_y(player, 'lo han llevado detenido', 'la han llevado detenida') + ' de ' + place.name + u' por apología al terrorismo.',
        player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso', u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la guardia en ' + place.name + u'.'
    ])

def somebody_died_of_infection(player):
    return random.choice([
        u'El coronavirus ha acabado con ' + player.get_name() + u'. Aquí acaba su aventura.',
        u'Los hospitales están colapsados y no quedan camas para ' + player.get_name() + u'. Ha muerto por una neumonía provocada por coronavirus.',
        player.get_name() + u' ha fallecido por coronavirus.',
        player.get_name() + u' ha tosido hasta ahogarse por culpa del coronavirus.'
    ])

def somebody_was_infected(player):
    return random.choice([
        player.get_name() + u' ha pillado el coronavirus.',
        u'Alguien ha infectado a ' + player.get_name() + u' con el coronavirus.',
        player.get_name() + u' no se ha lavado las manos lo suficiente y ha contraído el coronavirus.',
        player.get_name() + u' debería de haber seguido las recomendaciones para no pillar el coronavirus.',
        player.get_name() + u' ha contraído el coronavirus por ir al Mercadona a comprar papel higiénico.',
        player.get_name() + u' se saltó la cuarentena para fumarse uno y ha pillado el coronavirus.'
    ])
