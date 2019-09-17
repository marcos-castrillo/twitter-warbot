#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from models.tweet_type import Tweet_type

def get_message(type, args = None):
    if type == Tweet_type.start:
        return start()
    if type == Tweet_type.hour_threshold:
        return hour_threshold(args[0])
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
    return (u'¡Los participantes están listos! Bienvenidos a la Páramo War, dónde sólo uno de ellos se alzará con el título. Esto está a punto de arrancar.').encode('utf-8')

def hour_threshold(hour_count):
    return (u'¡Ya han pasado ' + str(hour_count) + ' horas! A partir de ahora incrementan las posibilidades de batalla y las de encontrarse mejores objetos.').encode('utf-8')

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
    return (u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado... ¡otra vez será!').encode('utf-8')

def somebody_got_ill(player, illness):
    ill_verb = random.choice(['ha cogido', u'ha contraído', u'ha padecido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, illness.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(illness.attack), 'en ataque y', str(player.get_defense()) +  get_amount(illness.defense), 'en defensa.')).encode('utf-8')

def somebody_got_injured(player, injury):
    ill_verb = random.choice(['ha padecido', u'ha recibido', u'ha cogido'])
    return u' '.join((u'¡' + player.get_name(), ill_verb, injury.name + '!', 'Ahora tiene', str(player.get_attack()) + get_amount(injury.attack), 'en ataque y', str(player.get_defense()) +  get_amount(injury.defense), 'en defensa.')).encode('utf-8')

def somebody_found_item(player, item):
    action = random.choice([u'se ha encontrado', u'le ha suplicado al creador de este bot que le diera algo. Tras mucho intentarlo, se ha llevado', u'ha cogido', u'ha entrado en una casa y ha robado', u'ha recogido', u'ha abierto un contenedor. Rebuscando entre la basura, ha encontrado', u'se ha llevado en la tómbola', u'ha intercambiado ' + random.choice([u'dos gramos', u'tres gramos', u'un gramo', u'dos cigarros', u'medio porro', u'un porro', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por', u'lleva unas pintas que alguien lo confundió con ' + get_x_or_y(player, u'un vagabundo', u'una vagabunda') + u' y le regaló', u'ha ganado en el bingo de #ProjectBercy', u'ha ganado en una apuesta', u'se ha comprado en el estanco', u'se ha comprado en el kiosko', u'ha comprado en el supermercado', u'ha recibido un paquete de Amazon con', u'ha ido al mercadillo y ha comprado', u'se ha llevado en una caja de cereales', u'se ha encontrado una caja llena de papel de periódico. Al abrirla había', u'ha recibido por su cumpleaños', u'llevaba mucho tiempo ahorrando para comprarse', u'iba tranquilamente por la calle cuando un desconocido le regaló', u'llevaba meses coleccionando tapas de yogurt para conseguir', u'ha ido coleccionando fascículos para montar', u'es tan manitas que se ha construido', u'vio a alguien por la calle, le metió una hostia y le robó'])
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
        loot = u' Como ' + player.location.name + u' es su lugar favorito, ha conseguido algo mejor de lo normal.'
    elif player.location.loot:
        loot = u' Ha conseguido algo mejor de lo normal porque está en ' + player.location.name + u'.'

    return u' '.join((u'¡' + player.get_name(), action, item.name + '!' + now_he_has + loot)).encode('utf-8')

def somebody_replaced_item(player, item_new, item_old):
    action = random.choice([u'se ha encontrado', u'ha cogido', u'ha entrado en una casa y ha robado', u'ha recogido', u'ha abierto un contenedor. Rebuscando entre la basura, ha encontrado', u'se ha llevado en la tómbola', u'ha intercambiado ' + random.choice([u'dos gramos', u'tres gramos', u'un gramo', u'dos cigarros', u'medio porro', u'un porro', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por', u'lleva unas pintas que alguien lo confundió con ' + get_x_or_y(player, u'un vagabundo', u'una vagabunda') + u' y le regaló', u'ha ganado en un bingo', u'ha ganado en una apuesta', u'se ha comprado en el estanco', u'se ha comprado en el kiosko', u'ha comprado en el supermercado', u'ha recibido un paquete de Amazon con', u'ha ido al mercadillo y ha comprado', u'se ha llevado en una caja de cereales', u'se ha encontrado una caja llena de papel de periódico. Al abrirla había', u'ha recibido por su cumpleaños', u'llevaba mucho tiempo ahorrando para comprarse', u'iba tranquilamnente por la calle cuando un desconocido le regaló', u'llevaba meses coleccionando tapas de yogurt para conseguir', u'ha ido coleccionando fascículos para montar', u'es tan manitas que se ha construido', u'vio a alguien por la calle, le metió una hostia y le robó'])

    return u' '.join((u'¡' + player.get_name(), action, item_new.name + '!', 'Se lo queda y se deshace de', item_old.name + '.', 'Ahora tiene', str(player.get_attack()) + get_amount(item_new.attack - item_old.attack), 'en ataque y', str(player.get_defense()) + get_amount(item_new.defense - item_old.defense), 'en defensa.')).encode('utf-8')

def somebody_doesnt_want_item(player, item):
    action = random.choice([u'se ha encontrado', u'ha cogido', u'ha entrado en una casa y ha robado', u'ha recogido', u'ha abierto un contenedor. Rebuscando entre la basura, ha encontrado', u'se ha llevado en la tómbola', u'ha intercambiado ' + random.choice([u'dos gramos', u'tres gramos', u'un gramo', u'dos cigarros', u'medio porro', u'un porro', u'cuatro cigarros', u'tres cigarros', 'una calada']) + ' por', u'lleva unas pintas que alguien lo confundió con ' + get_x_or_y(player, u'un vagabundo', u'una vagabunda') + u' y le regaló', u'ha ganado en un bingo', u'ha ganado en una apuesta', u'se ha comprado en el estanco', u'se ha comprado en el kiosko', u'ha comprado en el supermercado', u'ha recibido un paquete de Amazon con', u'ha ido al mercadillo y ha comprado', u'se ha llevado en una caja de cereales', u'se ha encontrado una caja llena de papel de periódico. Al abrirla había', u'ha recibido por su cumpleaños', u'llevaba mucho tiempo ahorrando para comprarse', u'iba tranquilamnente por la calle cuando un desconocido le regaló', u'llevaba meses coleccionando tapas de yogurt para conseguir', u'ha ido coleccionando fascículos para montar', u'es tan manitas que se ha construido', u'vio a alguien por la calle, le metió una hostia y le robó'])

    return u' '.join((u'¡' + player.get_name(), action, item.name + '!', 'Pero no lo quiere porque ya tiene cosas mejores... (' + player.item_list[0].name,  'y', player.item_list[1].name + ').')).encode('utf-8')

def somebody_tied_and_became_friend(player_1, player_2):
    return random.choice([player_1.get_name() + ' y ' + player_2.get_name() + u' se han peleado, pero se han cansado antes de que nadie cayera en combate, así que se han hecho ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho una tregua y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), player_1.get_name() + ' ha formado una alianza con ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), 'Aunque no se caigan muy bien, ' + player_1.get_name() + ' y ' + player_2.get_name() + u' han hecho un pacto y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), player_1.get_name() + ' y ' + player_2.get_name() + u' iban tan ciegos anoche que se habían olvidado de que eran ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), 'Usando sus encantos, ' + player_1.get_name() + ' ha conquistado a ' + player_2.get_name() + u' y ahora son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')]).encode('utf-8')

def somebody_tied_and_was_friend(player_1, player_2):
    return (random.choice([player_1.get_name() + ' y ' + player_2.get_name() + u' son tan ' + get_x_or_y_plural([player_1, player_2], 'buenos amigos', 'buenas amigas') + ' que no han querido pelearse.', player_1.get_name() + u' iba a reventar a ' + player_2.get_name() + u', pero se dio cuenta de que en el fondo le cae bien.', player_1.get_name() + u' contó un chiste tan malo que ' + player_2.get_name() + u' estuvo a punto de ' + get_x_or_y(player_1, 'matarlo', 'matarla') + u', pero cambió de opinión en el último momento porque son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'), player_1.get_name() + ' se ha negado a pelearse con ' + player_2.get_name() + u' a pesar de que sea tan ' + get_x_or_y(player_2, 'tonto', 'tonta') + ', ya que son ' + get_x_or_y_plural([player_1, player_2], 'buenos amigos', 'buenas amigas') + '.'])).encode('utf-8')

def somebody_escaped(player_1, player_2, unfriend = False):
    sufix = ''
    if unfriend:
        sufix = ' Han dejado de ser ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
    return random.choice([player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_1.get_name() + u' ha salido por patas cual cobarde.', player_1.get_name() + u' y ' + player_2.get_name() + u' han empezado a pelear, pero ' + player_2.get_name() + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.get_name() + u' en los ojos y salió corriendo.', player_1.get_name() + u' iba a asesinar a ' + player_2.get_name() + u' por la espalda, pero se dio cuenta en el último momento, por lo que' + player_1.get_name() + u' salió por patas.', player_1.get_name() + u' se ha encarado con ' + player_2.get_name() + u', pero ' + player_2.get_name() + u' se ha achantado y salido corriendo.'] ).encode('utf-8') + sufix

def somebody_killed(player_1, player_2, are_friends = False, new_item = None, old_item = None):
    kill_verb = random.choice([u'se ha cargado a', u'ha matado a', u'se ha llevado por delante a', u'ha destrozado a', u'ha desintegrado a', u'ha dejado KO a', u'ha ejecutado a', u'ha despachado a', u'ha asesinado a sangre fría a', u'se ha quitado de en medio a', u'se ha cepillado a', u'ha degollado a', u'ha asfixiado a', u'ha lapidado a', u'ha desnucado a'])
    friend_message = ''
    kill_method = random.choice([u' con sus puños', u' a tortazo limpio', u' de un cabezazo', u' de un codazo en el esternón', u', le ha pisoteado, escupido y ha meado un ojo', u' y le ha hecho un dab', u' y le ha hecho un baile del fortnite', u' sin despeinarse', u' de un buco', u' con una llave de kárate', u' haciendo capoeira', u' de una hostia limpia', u' sin esforzarse', u' y ha seguido a lo suyo', u' y se ha acabado el bocata tranquilamente', u' con lágrimas en los ojos', u' con mirada de psicópata', u' y ha gritado SUUUUUUUUUUUUUUUUU', u' y ha gritado ' + get_x_or_y(player_1, u'ESTOY MAMADISIMO HIJO DE PUTA', u'ESTOY MAMADISIMA HIJO DE PUTA'), u' y ha gritado PRANK ÉPICA', u', lo ha grabado y lo ha subido a su instagram', u' y lo ha tuiteado', u' y le ha sacado una foto de recuerdo', u' y ha tirado su cadáver al contenedor de basura', u' y ha tirado su cadáver al contenedor de basura'])
    kills_count = '.'
    stole = ''
    fav = ''

    if are_friends:
        friend_message = random.choice([u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '), u'Parece que no se caían tan bien, ', u'Premio ' + get_x_or_y(player_1, u'al mejor amigo', u'a la mejor amiga') + u' del año. ', ''])
    if player_1.get_best_attack_item() != None:
        kill_method = u' con ' + player_1.get_best_attack_item().name
    if player_1.kills > 1:
        kills_count = u' y ya lleva ' + str(player_1.kills) + u' muertes. ' + random.choice(['', u'Qué ' + get_x_or_y(player_1, u'tío.', u'tía.'), u'Vaya fiera.', u'Es una máquina.', u'Menudo monstruo.', u'Qué crack.', u'No hay quién le pare.', u'A por la MOAB.', u'Ni Willyrex.', u'Campear tanto da sus frutos.', u'Campear tanto da sus frutos.', get_x_or_y(player_1, u'Esta mamadísimo.', u'Está mamadísima.')])
    if new_item != None and old_item != None:
        stole = u' Además, le ha robado ' + new_item.name + u' y se ha deshecho de ' + old_item.name + '.'
    elif new_item != None:
        stole = u' Además, le ha robado ' + new_item.name + '.'

    if player_1.location == player_1.fav_place:
        fav = random.choice([' ' + player_1.get_name() + u' estaba peleando en su lugar preferido(' + player_1.location.name + u'), lo que le dio ventaja.', u' Se nota que ' + player_1.get_name() + u' estaba en su sitio favorito, ' + player_1.location.name + '.', ' ' + player_1.get_name() + u' ha podido ganar gracias a que le encanta ' + player_1.location.name + '.'])
    return u' '.join((friend_message + player_1.get_name(), kill_verb, player_2.get_name() + kill_method + kills_count + stole + fav)).encode('utf-8')

def somebody_revived(player):
    return u' '.join((player.get_name(), random.choice([u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!.', u'la muerta. ¡Qué peeerrraaaaa!..'), u'ha vuelto a la vida bajo extrañas circunstancias.', u'ha vuelto en forma de chapa y ahora es un zombie.', u'tiene enchufe y el creador del bot le ha resucitado.']))).encode('utf-8')

def somebody_died(player):
    return u' '.join((player.get_name(), random.choice([u'ha metido la pierna en una trampa para osos y se ha muerto ' + get_x_or_y(player, u'desangrado', u'desangrada') + u'.¡Qué mala pata!', u'se ha caído por un barranco y se ha muerto. ¡Qué torpe!', u'ha sido víctima de un rayo y se ha muerto en el acto.', u'ha muerto repentinamente por un fallo cardíaco. ¡Hay que hacer más deporte!', u'se estaba dando un baño en un lago sin darse cuenta de que había pirañas. Nunca fue la persona más avispada.', u'ha empezado a toser, a toser y a toser y se ha acabado asfixiando. Puede que fumarse 5 paquetes al día no fuera la decisión más sabia.', u'ha amochado de repente.', u'se fue a la puta.', u'se petateó y ahora le está dando de comer a los gusanos.']))).encode('utf-8')

def somebody_moved(player, old_location, new_location):
    action = random.choice([u'ha caminado desde', u'ha ido en bici de', u'ha ido en motorrabo de', u'ha hecho dedo desde', u'está tan en forma que ha hecho un sprint de', u'se aburría y ha ido a la pata coja desde', u'ha llamado al taxi de Rebollo para que le lleve de', u'ha llamado al taxi de Santi para que le lleve de', u'ha llamado al taxi de Aquilino para que le lleve de', u'ha llamado al taxi de Germán para que le lleve de', u'ha ido en tractor de', u'ha ido en patinete de', u'ha ido en skate haciendo backflips de', u'ha cogido el coche y ha hecho un derrape de', u'ha cogido un Blablacar de'])
    return u' '.join((player.get_name(), action, old_location.name, 'a', new_location.name + '.')).encode('utf-8')

def destroyed(place, dead_list, escaped_list, new_location):
    prefix = random.choice([u'Un meteorito ha caído en ' + place.name + u' y lo ha destruido', place.name + u' ha colapsado', u'Alguien se dejó una vela encendida, lo que incendió su casa y rápidamente todo ' + place.name + u' fue reducido a cenizas', u'Un terrorista islámico ha dinamitado ' + place.name, u'Una riada ha inundado todo ' + place.name, u'Una bomba nuclear ha reducido ' + place.name + u' a pedazos', u'Alguien ha prendido el polen de ' + place.name + u' incendiando todo el pueblo', u'Un huracán ha arrasado todo ' + place.name, u'Una nube de gas tóxico ha llegado a ' + place.name + u' haciéndolo inhabitable', u'En medio de una gran tormenta, un rayo ha caído en ' + place.name  + u', provocando un incendio que ha quemado todo el pueblo', u'El mundo está mejor sin ' + place.name  + u', así que el creador de este bot ha decidido cargárselo sin más', u'Unos alienígenas han estado observando ' + place.name + u' durante meses para llegar a la conclusión de que no merece existir, así que lo han destruido con un láser tocho', u'Un avión portugués ha bombardeado ' + place.name, u'Un bombardero británico se ha cargado todo ' + place.name, place.name + u' se ha ido a la puta mierda', u'Una terrible sequía ha asolado ' + place.name])

    if len(dead_list) == 0:
        sufix = '.'
    elif len(dead_list) == 1:
        sufix = random.choice([' y ' + dead_list[0].get_name() + u' ha fallecido en un trágico accidente.', ' y ' + dead_list[0].get_name() + u' ha amochado.', ' y ' + dead_list[0].get_name() + u' ha muerto.', ' y ' + dead_list[0].get_name() + u' la ha palmado.', ' y ' + dead_list[0].get_name() + u' ha espichado.', ' y ' + dead_list[0].get_name() + u' se ha ido al otro barrio.', ' y ' + dead_list[0].get_name() + u' ya no está entre nosotros.', ' y se ha llevado por delante a ' + dead_list[0].get_name() + u'.'])
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
        sufix = random.choice([u' y ' + dead_str + u' han fallecido en un trágico accidente.', ' y ' + dead_str + u' han amochado.', ' y ' + dead_str + u' la han palmado.', ' y ' + dead_str + u' han muerto.', ' y ' + dead_str + u' no han sobrevivido.', u' y hay un luto de 3 días por ' + dead_str + u'.', u' y no ha habido supervivientes. RIP ' + dead_str + u'.'])

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
        susufix = random.choice([u' Por suerte, ' + susufix_str + get_sing_or_pl(escaped_list, u' ha conseguido escapar a ', u' ha conseguido escapar a ')]) + new_location.name

    return (prefix + sufix + susufix).encode('utf-8')

def somebody_couldnt_move(player):
    return u' '.join((player.get_name(), u'se ha terminado toda la comida de', player.location.name, u'y no ha podido acceder a otros lugares, por lo que ha muerto de hambre.')).encode('utf-8')

def trap(player, place):
    return u' '.join((player.get_name(), u'ha puesto una trampa en', player.location.name + '.')).encode('utf-8')

def trapped(player, trapped_by, location):
    return u' '.join((player.get_name(), u'ha ido a', location.name, u'pero se ha comido la trampa que había puesto', trapped_by.get_name() + '.')).encode('utf-8')

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
    if place.name == u'Santa María':
        return (u'Ratonera sucia.').encode('utf-8')
    if place.name == u'Bercianos':
        return (u'Como son las fiestas de Bercianos (#ProjectBercy) y todo el mundo está allí, la guardia se ha puesto a la salida de Santa María.').encode('utf-8')
    return random.choice([u'¡Ha aparecido un control de la guardia en ' + place.name + u'! Habrá que ir con cuidado.', u'¡Ojo! Alguien ha avistado un coche de la guardia civil en ' + place.name + '.', u'Están haciendo la prueba del palito en ' + place.name + '.', u'Ya está la guardia otra vez a la entrada de ' + place.name + '.']).encode('utf-8')

def monster_moved(place, new_place):
    if new_place.name == u'Santa María':
        return (u'Ratonera sucia, la guardia se ha ido de ' + place.name + '.').encode('utf-8')
    if new_place.name == u'Bercianos':
        return (u'Como son las fiestas de Bercianos (#ProjectBercy) y todo el mundo está allí, la guardia se ha tenido que ir de ' + place.name + '.').encode('utf-8')

    return random.choice([u'¡El control de la guardia se ha movido de ' + place.name + ' a ' + new_place.name + u'! Habrá que ir con cuidado.', u'Ha habido movida en ' + new_place.name + u', por lo que la guardia ha tenido que irse de ' + place.name + '.', u'El control se ha movido de ' + place.name + u' a ' + new_place.name + '.', u'Alguien se ha chivado de que hay un cultivo de maría en ' + new_place.name + u', por lo que la guardia se ha ido de ' + place.name + '.', u'La guardia se ha movido de ' + place.name + u' a ' + new_place.name + '.']).encode('utf-8')

def monster_disappeared(place):
    return random.choice([u'¡El control de la guardia ha desaparecido de ' + place.name + u'!', u'La guardia ya no está en ' + place.name + '.', u'Se acabó el turno de los guardias, por lo que se han ido de ' + new_place.name + u'.']).encode('utf-8')

def monster_killed(player, place):
    return random.choice([player.get_name() + u' ha pasado a 200 km/h al lado del control de la guardia en ' + place.name + u' y se lo han llevado a comisaría. ¡Mal jugado!', player.get_name() + u' ha sido ' + get_x_or_y(player, 'arrestado', 'arrestada') + ' por la guardia de ' + place.name + u'.', u'¡La guardia le ha pillado una bolsa a ' + player.get_name() + ' en ' + place.name + u' y se ' + get_x_or_y(player, 'lo', 'la') + u' han llevado, hay que esconderla mejor!', u'La policía ha desahuciado a palos a ' + player.get_name() + u' de ' + place.name + '.', 'A ' + player.get_name() + u' se le ocurrió que era gracioso gritar GORA *** al lado de la policía. Se lo han llevado detenido de ' + place.name + u' por apología al terrorismo.', player.get_name() + u' creía que era ' + get_x_or_y(player, u'el más gracioso', u'la más graciosa') + u' haciendo humor negro en Twitter, hasta que se encontró a la policía en ' + place.name + u'. ¡Game over!']).encode('utf-8')
