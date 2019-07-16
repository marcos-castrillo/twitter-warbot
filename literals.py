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

def start():
    return (u'¡Los participantes están listos! Bienvenidos a los juegos de Q, dónde sólo uno de ellos se alzará con el título. Esto está a punto de arrancar.').encode('utf-8')

def sleep(wake_up_time):
    return (u'Se está haciendo de noche y los participantes que aún están vivos se han ido a dormir. ' + random.choice([u'El amanecer será sobre las ', u'Empezará a clarear a las ']) + str(wake_up_time) + '.').encode('utf-8')

def hour_threshold(hour_count):
    return (u'¡Ya han pasado ' + str(hour_count) + ' horas! A partir de ahora incrementan las posibilidades de batalla y las de encontrarse mejores objetos.').encode('utf-8')

def winner(player):
    return u' '.join((u'¡' + player.name, 'ha ganado!')).encode('utf-8')

def nobody_won():
    return (u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado...').encode('utf-8')

def somebody_found_item(player, item):
    if item.attack != 0:
        now_he_has = ' Ahora tiene ' + str(player.get_attack()) + get_amount(item.attack) + ' en ataque'
    if item.attack != 0 and item.defense != 0:
        now_he_has = u' '.join([now_he_has, 'y', str(player.get_defense()) + get_amount(item.defense), 'en defensa.'])
    elif item.defense != 0:
        now_he_has = ' Ahora tiene ' + str(player.get_defense()) + get_amount(item.defense) + ' en defensa.'
    else:
        now_he_has = ''

    return u' '.join((u'¡' + player.name, 'se ha encontrado', item.name + '!' + now_he_has)).encode('utf-8')

def somebody_replaced_item(player, item_new, item_old):
    return u' '.join((u'¡' + player.name, 'se ha encontrado', item_new.name + '!', 'Se lo queda y se deshace de', item_old.name + '.', 'Ahora tiene', str(player.get_attack()) + get_amount(item_new.attack - item_old.attack), 'en ataque y', str(player.get_defense()) +  get_amount(item_new.defense - item_old.defense), 'en defensa.')).encode('utf-8')

def somebody_doesnt_want_item(player, item):
    return u' '.join((u'¡' + player.name, 'se ha encontrado', item.name + '!', 'Pero no lo quiere porque ya tiene cosas mejores... (' + player.item_list[0].name,  'y', player.item_list[1].name + ').')).encode('utf-8')

def somebody_tied_and_became_friend(player_1, player_2):
    return random.choice([player_1.name + ' y ' + player_2.name + u' se han peleado, pero se han cansado antes de que nadie cayera en combate, así que se han hecho amigos.', player_1.name + ' y ' + player_2.name + u' han hecho una tregua y ahora son amigos.', player_1.name + ' ha formado una alianza con ' + player_2.name + u' y ahora son amigos.', 'Aunque no se caigan muy bien, ' + player_1.name + ' y ' + player_2.name + u' han hecho un pacto y ahora son amigos.']).encode('utf-8')

def somebody_tied_and_was_friend(player_1, player_2):
    return (random.choice([player_1.name + ' y ' + player_2.name + u'son tan buenos amigos que no han querido pelearse.', player_1.name + u' iba a reventar a ' + player_2.name + u', pero se dio cuenta de que en el fondo le cae bien.', player_1.name + u' contó un chiste tan malo que ' + player_2.name + u' estuvo a punto de matarlo, pero cambió de opinión en el último momento porque son amigos.'])).encode('utf-8')

def somebody_escaped(player_1, player_2, unfriend = False):
    sufix = ''
    if unfriend:
        sufix = ' Han dejado de ser amigos.'
    return random.choice([player_1.name + ' ha visto a lo lejos a ' + player_2.name + u', pero no ha sido tan rápido y le ha perdido la pista.', player_1.name + ' y ' + player_2.name + ' se han encontrado, pero ' + player_1.name + ' ha salido por patas cual cobarde.', player_1.name + ' y ' + player_2.name + ' han empezado a pelear, pero ' + player_2.name + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.name + u' en los ojos y salió corriendo.'] ).encode('utf-8') + sufix

def somebody_killed(player_1, player_2, are_friends = False, new_item = None, old_item = None):
    kill_verb = random.choice(['se ha cargado a', 'ha matado a', 'se ha llevado por delante a', 'le ha cruzado la cara a'])
    friend_message = ''
    kill_method = ''
    kills_count = '.'
    stole = ''

    if are_friends:
        friend_message = random.choice([u'Aunque eran amigos, ', u'Parece que no se caían tan bien, ', u'Premio al mejor amigo del año. ', ''])
    if player_1.get_best_attack_item() != None:
        kill_method = u' con ' + player_1.get_best_attack_item().name
    if player_1.kills > 1:
        kills_count = u' y ya lleva ' + str(player_1.kills) + u' muertes. ' + random.choice(['', u'Qué tío.', u'Vaya fiera.', u'Es una máquina.', u'Menudo monstruo.', u'Qué crack.', u'No hay quién l@ pare.', u'A por la MOAB.', u'Ni Willyrex.', u'Campear tanto da sus frutos.'])
    if new_item != None and old_item != None:
        stole = u' Además, le ha robado ' + new_item.name + u' y se ha deshecho de ' + old_item.name
    elif new_item != None:
        stole = u' Además, le ha robado ' + new_item.name + '.'

    return u' '.join((friend_message + player_1.name, kill_verb, player_2.name + kill_method + kills_count + stole)).encode('utf-8')

def somebody_revived(player):
    return u' '.join((player.name, random.choice([u' sólo se estaba haciendo el muerto. ¡Qué zooorrrooooo!.', u'ha vuelto a la vida bajo extrañas circunstancias.', u'ha vuelto en forma de chapa y ahora es un zombie.', u'tiene enchufe y el creador de Q le ha resucitado.']))).encode('utf-8')

def somebody_died(player):
    return u' '.join((player.name, random.choice([u'ha metido la pierna en una trampa para osos y se ha muerto desangrado. ¡Qué mala pata!', u'se ha caído por un barranco y se ha muerto. ¡Qué torpe!', u'ha sido víctima de un rayo y se ha muerto en el acto.', u'ha muerto repentinamente por un fallo cardíaco. ¡Hay que hacer más deporte!', u'se estaba dando un baño en un lago sin darse cuenta de que había pirañas. Nunca fue la persona más avispada.', u'ha empezado a toser, a toser y a toser y se ha acabado asfixiando. Puede que fumarse 5 paquetes al día no fuera la decisión más sabia.', u'ha amochado de repente.', u'se petateó y ahora le está dando de comer a los gusanos.']))).encode('utf-8')