#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from models.tweet_type import Tweet_type

def get_message(type, args = None):
    if type == Tweet_type.start:
        return start()
    if type == Tweet_type.sleep:
        return sleep(args[0])
    if type == Tweet_type.hour_threshold:
        return hour_threshold(args[0])
    if type == Tweet_type.final:
        return final()
    if type == Tweet_type.winner:
        return winner(args[0])
    if type == Tweet_type.nobody_won:
        return nobody_won()
    if type == Tweet_type.final_statistics_1:
        return final_statistics_1(args[0])
    if type == Tweet_type.final_statistics_2:
        return final_statistics_2(args[0])
    if type == Tweet_type.final_statistics_3:
        return final_statistics_3(args[0])
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
        return destroyed(args[0], args[1])
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

def get_amount(number):
    if number == 0:
        return ''
    elif number > 0:
        return '(+' + str(number) + ')'
    else:
        return '(' + str(number) + ')'

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
    return (u'¡Los participantes están listos! Bienvenidos a los juegos de Q, dónde sólo uno de ellos se alzará con el título. Esto está a punto de arrancar.').encode('utf-8')

def sleep(wake_up_time):
    return (u'Se está haciendo de noche y los participantes que aún están vivos se han ido a dormir. ' + random.choice([u'El amanecer será sobre las ', u'Empezará a clarear a las ']) + str(wake_up_time) + '.').encode('utf-8')

def hour_threshold(hour_count):
    return (u'¡Ya han pasado ' + str(hour_count) + ' horas! A partir de ahora incrementan las posibilidades de batalla y las de encontrarse mejores objetos.').encode('utf-8')

def final():
    return (u'¡Se acabó! Los participantes han peleado con valor, pero sólo podía quedar uno. A continuación, las estadísticas destacadas de este torneo.').encode('utf-8')

def winner(player):
    item_list = ''
    injury_list = ''
    if len(player.item_list) > 0:
        list = []
        for i, item in enumerate(player.item_list):
            list.append(item.name)
        item_list = u' Además, ha acabado teniendo ' + u', '.join(list) + '.'
    if len(player.injury_list) > 0:
        list = []
        for i, item in enumerate(player.injury_list):
            list.append(item.name)
        injury_list = ' Todo ello a pesar de tener ' + u', '.join(list) + '.'
    return u' '.join((u'¡' + player.get_name(), u'ha ganado! Lo ha conseguido llevándose por delante a', str(player.kills), 'participantes.' + item_list + injury_list, 'El ataque de', player.get_name(), u'llegó a ser de', str(player.get_attack()), u'y su defensa de', str(player.get_defense()) + '.')).encode('utf-8')

def nobody_won():
    return (u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado...').encode('utf-8')

def final_statistics_1(player_list):
    more_kills = None
    more_injuries = None
    list = []

    for i, player in enumerate(player_list):
        list.append(player)
        if more_kills == None or player.kills > more_kills.kills:
            more_kills = player
        if more_injuries == None or len(player.injury_list) > len(more_injuries.injury_list):
            more_injuries = player

    stat_kills = more_kills.get_name() + u' es ' + get_x_or_y(more_kills, 'el jugador', 'la jugadora') + u' que ha conseguido más bajas con un total de ' + str(more_kills.kills) + '.'
    stat_injuries = more_injuries.get_name() + u' es ' + get_x_or_y(more_injuries, 'el pupas', 'la pupas') + u' del torneo, con ' + str(len(more_injuries.injury_list)) + ' enfermedades o desventajas.'
    return u' '.join([stat_kills, stat_injuries]).encode('utf-8')

def final_statistics_2(player_list):
    more_defense = None
    more_attack = None
    list = []

    for i, player in enumerate(player_list):
        list.append(player)
        if more_defense == None or player.get_defense() > more_defense.get_defense():
            more_defense = player
        if more_attack == None or player.get_attack() > more_attack.get_attack():
            more_attack = player

    stat_defense = get_x_or_y(more_defense, u'El jugador más defensivo', u'La jugadora más defensiva') + u' ha sido ' + more_defense.get_name() + ' con un total de ' + str(more_defense.get_defense()) + '.'
    stat_attack = u'En cambio, ' + get_x_or_y(more_attack, u'el más ofensivo', u'la más ofensiva') + 'ha sido ' + more_attack.get_name() + ' con ' +  str(more_attack.get_attack()) + ' de ataque.'
    return u' '.join([stat_defense, stat_attack]).encode('utf-8')

def final_statistics_3(player_list):
    more_friends = None
    list = []

    for i, player in enumerate(player_list):
        list.append(player)
        if more_friends == None or len(player.friend_list) > len(more_friends.friend_list):
            more_friends = player

    list = []
    for i, friend in enumerate(more_friends.friend_list):
        list.append(friend.get_name())

    stat_friends = more_friends.get_name() + u' es ' + get_x_or_y(more_friends, 'el jugador', 'la jugadora') + u' más popular. Tiene nada más y nada menos que ' + str(len(list)) + ' amigos: (' + u', '.join(list) + ').'
    return u' '.join([stat_friends]).encode('utf-8')

def somebody_got_ill(player, illness):
    ill_verb = random.choice(['ha cogido', u'ha contraído', u'ha padecido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, illness.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(illness.attack), 'en ataque y', str(player.get_defense()) +  get_amount(illness.defense), 'en defensa.')).encode('utf-8')

def somebody_got_injured(player, injury):
    ill_verb = random.choice(['ha padecido', u'ha recibido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, injury.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(injury.attack), 'en ataque y', str(player.get_defense()) +  get_amount(injury.defense), 'en defensa.')).encode('utf-8')

def somebody_found_item(player, item):
    if item.attack != 0:
        now_he_has = ' Ahora tiene ' + str(player.get_attack()) + get_amount(item.attack) + ' en ataque'
    if item.attack != 0 and item.defense != 0:
        now_he_has = u' '.join([now_he_has, 'y', str(player.get_defense()) + get_amount(item.defense), 'en defensa.'])
    elif item.defense != 0:
        now_he_has = ' Ahora tiene ' + str(player.get_defense()) + get_amount(item.defense) + ' en defensa.'
    elif item.attack == 0:
        now_he_has = ''

    return u' '.join((u'¡' + player.get_name(), random.choice([u'se ha encontrado', u'ha cogido', u'ha encontrado un cadáver. Rebuscando entre sus restos, ha cogido', u'ha entrado en una cabaña y ha robado', u'ha abierto un cofre. Dentro había', u'ha recogido', u'ha encontrado', u'ha entrado en una cueva y ha encontrado']), item.name + '!' + now_he_has)).encode('utf-8')

def somebody_replaced_item(player, item_new, item_old):
    return u' '.join((u'¡' + player.get_name(), random.choice([u'se ha encontrado', u'ha cogido', u'ha encontrado un cadáver. Rebuscando entre sus restos, ha cogido', u'ha entrado en una cabaña y ha robado', u'ha abierto un cofre. Dentro había', u'ha recogido', u'ha encontrado', u'ha entrado en una cueva y ha encontrado']), item_new.name + '!', 'Se lo queda y se deshace de', item_old.name + '.', 'Ahora tiene', str(player.get_attack()) + get_amount(item_new.attack - item_old.attack), 'en ataque y', str(player.get_defense()) +  get_amount(item_new.defense - item_old.defense), 'en defensa.')).encode('utf-8')

def somebody_doesnt_want_item(player, item):
    return u' '.join((u'¡' + player.get_name(), random.choice([u'se ha encontrado', u'ha cogido', u'ha encontrado un cadáver. Rebuscando entre sus restos, ha cogido', u'ha entrado en una cabaña y ha robado', u'ha abierto un cofre. Dentro había', u'ha recogido', u'ha encontrado', u'ha entrado en una cueva y ha encontrado']), item.name + '!', 'Pero no lo quiere porque ya tiene cosas mejores... (' + player.item_list[0].name,  'y', player.item_list[1].name + ').')).encode('utf-8')

def somebody_tied_and_became_friend(player_1, player_2):
    return random.choice([player_1.get_name() + ' y ' + player_2.get_name() + u' se han peleado, pero se han cansado antes de que nadie cayera en combate, así que se han hecho' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho una tregua y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), player_1.get_name() + ' ha formado una alianza con ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), 'Aunque no se caigan muy bien, ' + player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho un pacto y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')]).encode('utf-8')

def somebody_tied_and_was_friend(player_1, player_2):
    return (random.choice([player_1.get_name() + ' y ' + player_2.get_name() + u'son tan ' + get_x_or_y_plural([player_1, player_2], 'buenos amigos', 'buenas amigas') + 'que no han querido pelearse.', player_1.get_name() + u' iba a reventar a ' + player_2.get_name() + u', pero se dio cuenta de que en el fondo le cae bien.', player_1.get_name() + u' contó un chiste tan malo que ' + player_2.get_name() + u' estuvo a punto de ' + get_x_or_y(player_1, 'matarlo', 'matarla') + u', pero cambió de opinión en el último momento porque son ' + get_x_or_y_plural([player_1, player_2], 'amigos', 'amigas')])).encode('utf-8')

def somebody_escaped(player_1, player_2, unfriend = False):
    sufix = ''
    if unfriend:
        sufix = ' Han dejado de ser ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
    return random.choice([player_1.get_name() + ' ha visto a lo lejos a ' + player_2.get_name() + u', pero no ha sido tan ' + get_x_or_y(player_1, u'rápido', u'rápida') + ' y le ha perdido la pista.', player_1.get_name() + ' y ' + player_2.get_name() + ' se han encontrado, pero ' + player_1.get_name() + ' ha salido por patas cual cobarde.', player_1.get_name() + ' y ' + player_2.get_name() + ' han empezado a pelear, pero ' + player_2.get_name() + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.get_name() + u' en los ojos y salió corriendo.'] ).encode('utf-8') + sufix

def somebody_killed(player_1, player_2, are_friends = False, new_item = None, old_item = None):
    kill_verb = random.choice(['se ha cargado a', 'ha matado a', 'se ha llevado por delante a', 'le ha cruzado la cara a'])
    friend_message = ''
    kill_method = random.choice([u' con sus puños', u' con sus puños', u' a tortazo limpio', u' de un cabezazo', u' de un codazo en el esternón', u' le ha pisoteado, escupido y ha meado un ojo', u' y le ha hecho un dab', u' y le ha hecho un baile del fortnite'])
    kills_count = '.'
    stole = ''

    if are_friends:
        friend_message = random.choice([u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos', u'amigas'), u'Parece que no se caían tan bien, ', u'Premio ' + get_x_or_y(player_1, u'al mejor amigo', u'a la mejor amiga') + u' del año. ', ''])
    if player_1.get_best_attack_item() != None:
        kill_method = u' con ' + player_1.get_best_attack_item().name
    if player_1.kills > 1:
        kills_count = u' y ya lleva ' + str(player_1.kills) + u' muertes. ' + random.choice(['', u'Qué ' + get_x_or_y(player_1, u'tío.', u'tía.'), u'Vaya fiera.', u'Es una máquina.', u'Menudo monstruo.', u'Qué crack.', u'No hay quién le pare.', u'A por la MOAB.', u'Ni Willyrex.', u'Campear tanto da sus frutos.'])
    if new_item != None and old_item != None:
        stole = u' Además, le ha robado ' + new_item.name + u' y se ha deshecho de ' + old_item.name
    elif new_item != None:
        stole = u' Además, le ha robado ' + new_item.name + '.'

    return u' '.join((friend_message + player_1.get_name(), kill_verb, player_2.get_name() + kill_method + kills_count + stole)).encode('utf-8')

def somebody_revived(player):
    return u' '.join((player.get_name(), random.choice([u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!.', u'la muerta. ¡Qué zooorrraaaaa!..'), u'ha vuelto a la vida bajo extrañas circunstancias.', u'ha vuelto en forma de chapa y ahora es un zombie.', u'tiene enchufe y el creador de Q le ha resucitado.']))).encode('utf-8')

def somebody_died(player):
    return u' '.join((player.get_name(), random.choice([u'ha metido la pierna en una trampa para osos y se ha muerto ' + get_x_or_y(player, u'desangrado', u'desangrada') + u'.¡Qué mala pata!', u'se ha caído por un barranco y se ha muerto. ¡Qué torpe!', u'ha sido víctima de un rayo y se ha muerto en el acto.', u'ha muerto repentinamente por un fallo cardíaco. ¡Hay que hacer más deporte!', u'se estaba dando un baño en un lago sin darse cuenta de que había pirañas. Nunca fue la persona más avispada.', u'ha empezado a toser, a toser y a toser y se ha acabado asfixiando. Puede que fumarse 5 paquetes al día no fuera la decisión más sabia.', u'ha amochado de repente.', u'se petateó y ahora le está dando de comer a los gusanos.']))).encode('utf-8')

def somebody_moved(player, old_location, new_location):
    return u' '.join((player.get_name(), 'ha caminado desde', old_location.name, 'a', new_location.name + '.')).encode('utf-8')

def destroyed(place, dead_list):
    prefix = random.choice([u'Un meterito ha caído en ' + place.name, u'Una riada ha inundado ' + place.name, u'Una bomba nuclear ha reducido ' + place.name + u' a pedazos', u'Alguien ha prendido el polen de ' + place.name + u' provocando un gran incendio', u'La caseta de ' + place.name + u' se ha derrumbado', u'Un huracán ha arrasado todo ' + place.name])

    if len(dead_list) == 0:
        sufix = '.'
    elif len(dead_list) == 1:
        sufix = random.choice([' y ' + dead_list[0].get_name() + u' ha fallecido en un trágico accidente.'])
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
        sufix = random.choice([' y ' + dead_str + u' han fallecido en un trágico accidente.'])

    return (prefix + sufix).encode('utf-8')

def somebody_couldnt_move(player):
    return u' '.join((player.get_name(), u'se ha terminado toda la comida de', player.location.name, u'y no ha podido acceder a otros lugares, por lo que ha muerto de hambre.')).encode('utf-8')

def trap(player, place):
    return u' '.join((player.get_name(), u'ha puesto una trampa en', player.location.name + '.')).encode('utf-8')

def trapped(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name, u'pero se ha comido la trampa que había puesto', trapped_by.get_name())).encode('utf-8')

def dodged_trap(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name, u', ha visto la trampa que había puesto', trapped_by.get_name(), 'y la ha destruido.')).encode('utf-8')

def somebody_stole(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + '.')).encode('utf-8')

def somebody_stole_and_replaced(robber, robbed, item, old_item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + u'. Como es mejor, se ha deshecho de su' + old_item.name + '.')).encode('utf-8')

def somebody_stole(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + u'. Como tiene cosas mejores, lo ha tirado a la basura.')).encode('utf-8')
