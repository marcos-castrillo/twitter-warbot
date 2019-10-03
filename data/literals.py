#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from models.tweet_type import Tweet_type

def get_message(type, args = None):
    if type == Tweet_type.start:
        return start()
    # if type == Tweet_type.hour_threshold:
    #     return hour_threshold(args[0])
    if type == Tweet_type.winner:
        return winner(args[0])
    if type == Tweet_type.nobody_won:
        return nobody_won()
    if type == Tweet_type.somebody_got_ill:
        return somebody_got_ill(args[0], args[1])
    if type == Tweet_type.somebody_got_injured:
        return somebody_got_injured(args[0], args[1])
    if type == Tweet_type.somebody_found_item:
        return somebody_found_item(args[0], args[1])
    if type == Tweet_type.somebody_replaced_item:
        return somebody_replaced_item(args[0], args[1], args[2])
    if type == Tweet_type.somebody_doesnt_want_item:
        return somebody_doesnt_want_item(args[0], args[1])
    if type == Tweet_type.somebody_tied_and_became_friend:
        return somebody_tied_and_became_friend(args[0], args[1])
    if type == Tweet_type.somebody_tied_and_was_friend:
        return somebody_tied_and_was_friend(args[0], args[1])
    if type == Tweet_type.somebody_escaped:
        if len(args) == 3:
            return somebody_escaped(args[0], args[1], args[2])
        if len(args) == 2:
            return somebody_escaped(args[0], args[1])
    if type == Tweet_type.somebody_killed:
        if len(args) == 5:
            return somebody_killed(args[0], args[1], args[2], args[3], args[4])
        if len(args) == 4:
            return somebody_killed(args[0], args[1], args[2], args[3])
        if len(args) == 3:
            return somebody_killed(args[0], args[1], args[2])
    if type == Tweet_type.somebody_revived:
        return somebody_revived(args[0])
    if type == Tweet_type.somebody_died:
        return somebody_died(args[0])
    if type == Tweet_type.somebody_moved:
        return somebody_moved(args[0], args[1], args[2])
    if type == Tweet_type.destroyed:
        return destroyed(args[0], args[1], args[2], args[3])
    if type == Tweet_type.somebody_couldnt_move:
        return somebody_couldnt_move(args[0])
    if type == Tweet_type.trap:
        return trap(args[0], args[1])
    if type == Tweet_type.trapped:
        return trapped(args[0], args[1], args[2])
    if type == Tweet_type.dodged_trap:
        return dodged_trap(args[0], args[1], args[2])
    if type == Tweet_type.somebody_stole:
        return somebody_stole(args[0], args[1], args[2])
    if type == Tweet_type.somebody_stole_and_replaced:
        return somebody_stole_and_replaced(args[0], args[1], args[2], args[3])
    if type == Tweet_type.somebody_stole_and_threw:
        return somebody_stole_and_threw(args[0], args[1], args[2])
    if type == Tweet_type.somebody_powerup:
        return somebody_powerup(args[0], args[1])
    if type == Tweet_type.monster_appeared:
        return monster_appeared(args[0])
    if type == Tweet_type.monster_moved:
        return monster_moved(args[0], args[1])
    if type == Tweet_type.monster_dissappeared:
        return monster_dissappeared(args[0])
    if monster_killed(args[0], args[1]):
        return monster_killed(args[0], args[1])

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

def start():
    return (u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Esto está a punto de arrancar.').encode('utf-8')

def winner(player):
    item_list = ''
    injury_list = ''
    kills = ''
    if player.kills == 0:
        kills = u'Lo ha conseguido sin llevarse por delante a nadie.'
    if player.kills == 1:
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
            elif i == len(player.item_list) - 1:
                list = list + ' y ' + item.name
            else:
                list = list + ', ' + item.name
        injury_list = ' Todo ello a pesar de padecer ' + list + '.'
    return u' '.join((u'¡' + player.get_name(), u'ha ganado! ' + kills + item_list + injury_list, 'El ataque de', player.get_name(), u'llegó a ser de', str(player.get_attack()), u'y su defensa de', str(player.get_defense()) + '.')).encode('utf-8')

def nobody_won():
    return (u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado... ¡otra vez será!').encode('utf-8')

def somebody_got_ill(player, illness):
    ill_verb = random.choice(['ha cogido', u'ha contraído', u'ha padecido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, illness.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(illness.attack), 'en ataque y', str(player.get_defense()) +  get_amount(illness.defense), 'en defensa.')).encode('utf-8')

def somebody_got_injured(player, injury):
    ill_verb = random.choice(['ha padecido', u'ha recibido', u'ha cogido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, injury.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(injury.attack), 'en ataque y', str(player.get_defense()) +  get_amount(injury.defense), 'en defensa.')).encode('utf-8')

def somebody_found_item(player, item):
    action = random.choice([
    u'se ha encontrado',
    u'ha cogido',
    u'ha entrado en una casa y ha robado',
    u'ha recogido',
    u'le ha suplicado al creador de este bot que le diera algo. Tras mucho intentarlo, se ha llevado',
    u'ha abierto un contenedor. Rebuscando entre la basura, ha encontrado',
    u'se ha llevado en la tómbola',
    u'ha intercambiado ' + random.choice([u'dos gramos', u'un gramo', u'dos cigarros', u'medio porro', u'un porro', u'una chusta', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por',
    u'ha ganado en una apuesta',
    u'se ha comprado en un estanco',
    u'se ha comprado clandestinamente en un kiosko',
    u'ha comprado en el supermercado',
    u'ha recibido un paquete de Amazon con',
    u'ha ido al mercadillo y ha comprado',
    u'se ha llevado en una caja de cereales',
    u'se ha encontrado una caja llena de papel de periódico. Al abrirla había',
    u'ha recibido por su cumpleaños',
    u'llevaba mucho tiempo ahorrando para comprarse',
    u'iba tranquilamente por la calle cuando un desconocido le regaló',
    u'llevaba meses coleccionando tapas de yogurt para conseguir',
    u'ha ido coleccionando fascículos para montar',
    u'es tan manitas que se ha construido',
    u'vio a alguien desprevenido por la calle y le robó'
    ])
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
    if player.fav_place == player.location:
        loot = u' Como ' + player.location.name + u' es su ciudad, ha conseguido algo mejor de lo normal.'
    elif player.location.loot:
        loot = u' Ha conseguido algo mejor de lo normal porque está en ' + player.location.name + u'.'

    return u' '.join((u'¡' + player.get_name(), action, item.name + '!' + now_he_has + loot)).encode('utf-8')

def somebody_replaced_item(player, item_new, item_old):
    action = random.choice([
    u'se ha encontrado',
    u'ha cogido',
    u'ha entrado en una casa y ha robado',
    u'ha recogido',
    u'le ha suplicado al creador de este bot que le diera algo. Tras mucho intentarlo, se ha llevado',
    u'ha abierto un contenedor. Rebuscando entre la basura, ha encontrado',
    u'se ha llevado en la tómbola',
    u'ha intercambiado ' + random.choice([u'dos gramos', u'un gramo', u'dos cigarros', u'medio porro', u'un porro', u'una chusta', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por',
    u'ha ganado en una apuesta',
    u'se ha comprado en un estanco',
    u'se ha comprado clandestinamente en un kiosko',
    u'ha comprado en el supermercado',
    u'ha recibido un paquete de Amazon con',
    u'ha ido al mercadillo y ha comprado',
    u'se ha llevado en una caja de cereales',
    u'se ha encontrado una caja llena de papel de periódico. Al abrirla había',
    u'ha recibido por su cumpleaños',
    u'llevaba mucho tiempo ahorrando para comprarse',
    u'iba tranquilamente por la calle cuando un desconocido le regaló',
    u'llevaba meses coleccionando tapas de yogurt para conseguir',
    u'ha ido coleccionando fascículos para montar',
    u'es tan manitas que se ha construido',
    u'vio a alguien desprevenido por la calle y le robó'
    ])

    return u' '.join((u'¡' + player.get_name(), action, item_new.name + '!', 'Se lo queda y se deshace de', item_old.name + '.', 'Ahora tiene', str(player.get_attack()) + get_amount(item_new.attack - item_old.attack), 'en ataque y', str(player.get_defense()) + get_amount(item_new.defense - item_old.defense), 'en defensa.')).encode('utf-8')

def somebody_doesnt_want_item(player, item):
    action = random.choice([
    u'se ha encontrado',
    u'ha cogido',
    u'ha entrado en una casa y ha robado',
    u'ha recogido',
    u'le ha suplicado al creador de este bot que le diera algo. Tras mucho intentarlo, se ha llevado',
    u'ha abierto un contenedor. Rebuscando entre la basura, ha encontrado',
    u'se ha llevado en la tómbola',
    u'ha intercambiado ' + random.choice([u'dos gramos', u'un gramo', u'dos cigarros', u'medio porro', u'un porro', u'una chusta', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por',
    u'ha ganado en una apuesta',
    u'se ha comprado en un estanco',
    u'se ha comprado clandestinamente en un kiosko',
    u'ha comprado en el supermercado',
    u'ha recibido un paquete de Amazon con',
    u'ha ido al mercadillo y ha comprado',
    u'se ha llevado en una caja de cereales',
    u'se ha encontrado una caja llena de papel de periódico. Al abrirla había',
    u'ha recibido por su cumpleaños',
    u'llevaba mucho tiempo ahorrando para comprarse',
    u'iba tranquilamente por la calle cuando un desconocido le regaló',
    u'llevaba meses coleccionando tapas de yogurt para conseguir',
    u'ha ido coleccionando fascículos para montar',
    u'es tan manitas que se ha construido',
    u'vio a alguien desprevenido por la calle y le robó'
    ])

    return u' '.join((u'¡' + player.get_name(), action, item.name + '!', 'Pero no lo quiere porque ya tiene cosas mejores... (' + player.item_list[0].name,  'y', player.item_list[1].name + ').')).encode('utf-8')

def somebody_tied_and_became_friend(player_1, player_2):
    return random.choice([
    player_1.get_name() + ' y ' + player_2.get_name() + u' se han peleado, pero se han cansado antes de que nadie cayera en combate, así que se han hecho ' + get_x_or_y_plural([player_1, player_2],'amigos.', 'amigas.'),
    player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho una tregua y ahora son ' + get_x_or_y_plural([player_1, player_2],'amigos.', 'amigas.'),
    player_1.get_name() + ' ha formado una alianza con ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    'Aunque no se caigan muy bien, ' + player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho un pacto y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    player_1.get_name() + ' y ' + player_2.get_name() + u' iban tan ciegos anoche que se habían olvidado de que eran ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    'Usando sus encantos, ' + player_1.get_name() + ' ha conquistado a ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
    ]).encode('utf-8')

def somebody_tied_and_was_friend(player_1, player_2):
    return (random.choice([
    player_1.get_name() + ' y ' + player_2.get_name() + u' son tan ' + get_x_or_y_plural([player_1, player_2],
    'buenos amigos', 'buenas amigas') + ' que no han querido pelearse.',
    player_1.get_name() + u' iba a reventar a ' + player_2.get_name() + u', pero se dio cuenta de que en el fondo le cae bien.',
    player_1.get_name() + u' contó un chiste tan malo que ' + player_2.get_name() + u' estuvo a punto de ' + get_x_or_y(player_1, 'matarlo', 'matarla') + u', pero cambió de opinión en el último momento porque son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
    player_1.get_name() + ' se ha negado a pelearse con ' + player_2.get_name() + u' a pesar de que le tenga ganas, ya que son ' + get_x_or_y_plural([player_1, player_2], 'amigos', 'amigas') + '.'
    ])).encode('utf-8')

def somebody_escaped(player_1, player_2, unfriend = False):
    sufix = ''
    if unfriend:
        sufix = ' Han dejado de ser ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
    return random.choice([
    player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_1.get_name() + u' ha salido por patas cual cobarde.',
    player_1.get_name() + u' y ' + player_2.get_name() + u' han empezado a pelear, pero ' + player_2.get_name() + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.get_name() + u' en los ojos y salió corriendo.',
    player_1.get_name() + u' iba a asesinar a ' + player_2.get_name() + u' por la espalda, pero se dio cuenta en el último momento, por lo que' + player_1.get_name() + u' salió por patas.',
    player_1.get_name() + u' se ha encarado con ' + player_2.get_name() + u', pero ' + player_2.get_name() + u' se ha achantado y salido corriendo.'
    ]).encode('utf-8') + sufix

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
    u'ha asesinado a sangre fría a',
    u'se ha quitado de en medio a',
    u'se ha cepillado a',
    u'ha degollado a',
    u'ha asfixiado a',
    u'ha lapidado a',
    u'ha desnucado a'])

    friend_message = ''

    kill_method = random.choice([
    u' con sus puños',
    u' a lo jíbiri',
    u' a tortazo limpio',
    u' de un cabezazo',
    u' de un codazo en el esternón',
    u', le ha pisoteado, escupido y ha meado un ojo',
    u' y le ha hecho un dab',
    u' y le ha hecho un baile del fortnite',
    u' sin despeinarse',
    u' con una llave de kárate',
    u' haciendo capoeira',
    u' de una hostia limpia',
    u' sin esforzarse',
    u' y ha seguido a lo suyo',
    u' y se ha acabado el bocata tranquilamente',
    u' con lágrimas en los ojos',
    u' con mirada de psicópata',
    u' y ha gritado SUUUUUUUUUUUUUUUUU',
    u' y ha gritado ' + get_x_or_y(player_1, u'ESTOY MAMADÍSIMO HIJO DE PUTA', u'ESTOY MAMADÍSIMA HIJO DE PUTA'),
    u' y ha gritado PRANK ÉPICA',
    u', lo ha grabado y lo ha subido a su instagram',
    u' y lo ha tuiteado',
    u' y le ha sacado una foto de recuerdo',
    u' y ha tirado su cadáver al contenedor de basura'
    ])
    kills_count = '.'
    stole = ''
    fav = ''

    if are_friends:
        friend_message = random.choice([
        u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Parece que no se caían tan bien, ',
        u'Parece que alguien es un judas, ',
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
        u'Qué ' + get_x_or_y(player_1, u'tío.', u'tía.'),
        u'Vaya fiera.',
        u'Es una máquina.',
        u'Menudo monstruo.',
        u'Qué crack.',
        u'No hay quién ' + get_x_or_y(player_1, u'lo.', u'la.') + ' pare.',
        u'A por la MOAB.',
        u'Tra tra.',
        u'Campear tanto da sus frutos.',
        get_x_or_y(player_1, u'Esta mamadísimo.', u'Está mamadísima.')])
    if new_item != None and old_item != None:
        stole = u' Además, le ha robado ' + new_item.name + u' y se ha deshecho de ' + old_item.name + '.'
    elif new_item != None:
        stole = u' Además, le ha robado ' + new_item.name + '.'

    if player_1.location == player_1.fav_place:
        fav = random.choice([
        ' ' + player_1.get_name() + u' estaba peleando en su lugar preferido(' + player_1.location.name + u'), lo que le dio ventaja.',
        u' Se nota que ' + player_1.get_name() + u' estaba en su lugar de nacimiento, ' + player_1.location.name + '.',
        ' ' + player_1.get_name() + u' ha podido ganar gracias a que juega en casa (' + player_1.location.name + ').'])
    return u' '.join((friend_message + player_1.get_name(), kill_verb, player_2.get_name() + kill_method + kills_count + stole + fav)).encode('utf-8')

def somebody_revived(player):
    return u' '.join((player.get_name(), random.choice([
    u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!.', u'la muerta. ¡Qué zooorrraaaaa! (sin trazas de patriarcado).'),
    u'ha vuelto a la vida bajo extrañas circunstancias.',
    u'ha vuelto en forma de chapa y ahora es un zombie.',
    u'ha resucitado en mitad de su funeral y ha vuelto a la batalla.',
    u'tiene enchufe y el creador del bot le ha resucitado.'
    ]))).encode('utf-8')

def somebody_died(player):
    return u' '.join((player.get_name(), random.choice([
    u'debería de haber mirado antes de cruzar la carretera. Quizás así hubiera visto el camión que se lo ha llevado por delante.',
    u'ha sido víctima de un rayo y se ha muerto en el acto.',
    u'ha muerto repentinamente por un fallo cardíaco. ¡Hay que hacer más deporte!',
    u'ha empezado a toser, a toser y a toser y se ha acabado asfixiando. Puede que fumarse 5 paquetes al día no fuera la decisión más sabia. Estos chavalitos...',
    u'ha amochado de repente.',
    u'ha sido atropellado por una moto y se fue a la puta.'
    ]))).encode('utf-8')

def somebody_moved(player, old_location, new_location):
    road = False

    for i, c in enumerate(old_location.road_connections):
        if c.encode('utf-8') == new_location.name.encode('utf-8'):
            road = True

    if road:
        action = random.choice([
        u'ha llamado a un taxi para que le lleve de',
        u'ha llamado a un Uber para que le lleve de',
        u'ha llamado a un Cabify para que le lleve de',
        u'está tan en forma que ha ido en bici de',
        u'ha hecho dedo desde',
        u'ha hecho autostop desde',
        u'ha robado un coche descapotable a lo GTA y se ha ido de',
        u'ha ido en moto de',
        u'ha ido en su scooter de',
        u'ha ido en AVE de',
        u'ha ido en mochillo de',
        u'ha ido en patinete eléctrico de',
        u'ha ido en tren regional de',
        u'ha encontrado billetes de avión baratos para ir de',
        u'ha ido en avión en primera clase para ir de',
        u'ha cogido un Blablacar de'
        ])
    else:
        action = random.choice([
        u'ha ido en su barquito velero de',
        u'ha ido en un crucero de cinco plantas de',
        u'ha ido en lancha motora de',
        u'se ha colado de polizón en un barco de',
        u'ha ido en patera de'
        ])

    return u' '.join((player.get_name(), action, old_location.name, 'a', new_location.name + '.')).encode('utf-8')

def destroyed(place, dead_list, escaped_list, new_location):
    prefix = random.choice([
    u'Un meteorito ha caído en ' + place.name + u' y lo ha destruido',
    place.name + u' ha colapsado',
    u'Alguien se dejó una vela encendida, lo que incendió su casa y rápidamente todo ' + place.name + u' fue reducido a cenizas',
    u'Un terrorista ha dinamitado ' + place.name,
    u'Una riada ha inundado todo ' + place.name,
    u'Una bomba nuclear ha reducido ' + place.name + u' a pedazos',
    u'Un huracán ha arrasado todo ' + place.name,
    u'Una nube de gas tóxico ha llegado a ' + place.name + u' haciéndolo inhabitable',
    u'Una epidemia de listeriosis se ha extendido por ' + place.name + u'.',
    u'En medio de una gran tormenta, un rayo ha caído en ' + place.name  + u', provocando un incendio que lo ha quemado todo',
    u'El mundo está mejor sin ' + place.name  + u', así que el creador de este bot ha decidido cargárselo sin más',
    u'Unos alienígenas han estado observando ' + place.name + u' durante meses para llegar a la conclusión de que no merece existir, así que lo han destruido con un láser tocho',
    u'Un avión ' + random.choice([u'portugués', u'inglés', u'francés', u'estadounidense', u'italiano', u'alemán', u'ruso', u'chino']) + u' ha bombardeado ' + place.name,
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
            elif i == len(dead) - 1:
                susufix_str = susufix_str + ' y ' + d
            else:
                susufix_str = susufix_str + ', ' + d

        susufix = random.choice([
        u' Por suerte, ' + susufix_str + get_sing_or_pl(escaped_list, u' ha conseguido escapar a ', u' han conseguido escapar a ') + new_location.name + u'.',
        u' ' + susufix_str + get_sing_or_pl(escaped_list, u' ha sido rápido y ha huido a ', u' han sido rápidos y han huido a ') + new_location.name + u'.',
        u' ' + susufix_str + get_sing_or_pl(escaped_list, u' se ha librado a duras penas y se ha movido a ', u' se han librado a duras penas y se han movido a ') + new_location.name + u'.'
        ])

    return (prefix + sufix + susufix).encode('utf-8')

def somebody_couldnt_move(player):
    return u' '.join((player.get_name(), u'se ha terminado toda la comida de', player.location.name, u'y no ha podido acceder a otros lugares, por lo que ha muerto de hambre.')).encode('utf-8')

def trap(player, place):
    return u' '.join((player.get_name(), u'ha puesto una trampa en', player.location.name + '.')).encode('utf-8')

def trapped(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name, u'pero se ha comido la trampa que había puesto', trapped_by.get_name() + u'. ¡Qué torpe!')).encode('utf-8')

def dodged_trap(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name + u', ha visto la trampa que había puesto', trapped_by.get_name(), 'y la ha destruido.')).encode('utf-8')

def somebody_stole(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + '.')).encode('utf-8')

def somebody_stole_and_replaced(robber, robbed, item, old_item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + u'. Como es mejor, se ha deshecho de su' + old_item.name + '.')).encode('utf-8')

def somebody_stole_and_threw(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + u'. Como tiene cosas mejores, lo ha tirado a la basura.')).encode('utf-8')

def somebody_powerup(player, powerup):
    powerup_verb = random.choice(['ha cogido', u'ha encontrado'])
    return u' '.join((u'¡' + player.get_name(), powerup_verb, powerup.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(powerup.attack), 'en ataque y', str(player.get_defense()) +  get_amount(powerup.defense), 'en defensa.')).encode('utf-8')

def monster_appeared(place):
    return random.choice([
    u'¡Ojo! Alguien ha avistado una patrulla de la guardia en ' + place.name + '.',
    u'Se han producido una serie de altercados en ' + place.name + u', por lo que la policía se ha visto obligada a desplazarse allí.',
    ]).encode('utf-8')

def monster_moved(place, new_place):
    return random.choice([
    u'¡La policía se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.',
    u'Ha habido movida en ' + new_place.name + u', por lo que la policía ha tenido que irse de ' + place.name + '.',
    u'Alguien se ha chivado de que hay una manifestación en ' + new_place.name + u', así que la policía se ha ido de ' + place.name + '.',
    u'La policía se ha movido de ' + place.name + u' a ' + new_place.name + '.',
    u'¡La policía se ha ido a un desahucio a ' + new_place.name + '!.',
    ]).encode('utf-8')

def monster_disappeared(place):
    return random.choice([
    u'¡La policía se ha esfumado de ' + place.name + u'!',
    u'La policía ya no está en ' + place.name + '.',
    u'Se acabó el turno de la policía, por lo que se han ido de ' + new_place.name + u'.'
    ]).encode('utf-8')

def monster_killed(player, place):
    return random.choice([
    player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado', 'arrestada') + u' por la policía de ' + place.name + u'. Aquí acaba su aventura.',
    u'¡La guardia le ha pillado una bolsita a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(player, 'lo', 'la') + u' han llevado, hay que esconderla mejor!',
    u'La policía ha desahuciado a palos a ' + player.get_name() + u' de ' + place.name + u'. ¡Game over!',
    player.get_name() + u' creía que no iba a pasar nada por meter su voto en una urna, hasta que los antidisturbios de ' + place.name + ' cargaron contra ' + get_x_or_y(player, u'él', 'ella') + u'. ¡Mala suerte!',
    'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la policía. Se ' + get_x_or_y(player, 'lo han llevado detenido', 'la han llevado detenida') + ' de ' + place.name + u' por apología al terrorismo.',
    player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso', u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la policía en ' + place.name + u'.'
    ]).encode('utf-8')
