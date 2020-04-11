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

ALSO_STOLE = u'Además, le ha robado'
AND = 'y'

def ATRACTION_NOBODY():
    return random.choice([
        u' pero por desgracia nadie ha ido...',
        u' pero no ha ido ni dios...',
        u' pero a nadie le interesan...'
    ])

def CROSSING():
    return random.choice([u'atravesando', u'cruzando'])

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
       u'Una epidemia de listeriosis se ha extendido por ' + place + u'.',
       u'El mundo está mejor sin ' + place  + u', así que el creador de este bot ha decidido cargárselo sin más',
       place + u' se ha ido a la puta mierda',
       u'Una terrible sequía ha asolado ' + place
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

def ESCAPED(player_1, player_2):
    return random.choice([
        player_1.get_name() + u' y ' + player_2.get_name() + u' se han encontrado, pero ' + player_1.get_name() + u' ha salido por patas cual cobarde.',
        player_1.get_name() + u' y ' + player_2.get_name() + u' han empezado a pelear, pero ' + player_2.get_name() + u' sabía que tenía las de perder. Cogió un puñado de arena, se lo echó a ' + player_1.get_name() + u' en los ojos y salió corriendo.',
        player_1.get_name() + u' iba a asesinar a ' + player_2.get_name() + u' por la espalda, pero éste se dio cuenta en el último momento. ' + player_1.get_name() + u' ha salido por patas.',
        player_1.get_name() + u' se ha encarado con ' + player_2.get_name() + u', pero ' + player_2.get_name() + u' se ha achantado y salido corriendo.'
    ])

def FIND_ACTION():
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
        u'tiene enchufe con el programador de esto y se ha llevado',
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
    return u' '.join((u'y ya lleva', kills_count, u'muertes.'))

def I_COMPOSED(player, action, event, has_now):
    return u' '.join((u'¡' + player.get_name(), action, event.name + '!', has_now))

def ILLNESS_ACTION():
    return random.choice([U'ha cogido', u'ha contraído', u'ha padecido'])

IN_ATTACK = u'en ataque'
IN_DEFENSE = u'en defensa'

def INJURE_ACTION():
    return random.choice([u'ha recibido', u'ha cogido'])

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
        u'de un codazo en el esternón',
        u'y le ha hecho un dab',
        u'y le ha hecho un baile del fortnite',
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
        u', lo ha grabado y lo ha subido a su instagram',
        u'y lo ha tuiteado',
        u'y le ha sacado una foto de recuerdo',
        u'y ha tirado su cadáver al contenedor de basura',
        u'y se ha ido de cañas',
        u'haciendo una buena escabechina con sus restos',
        u'sudando mogollón',
        u'y se ha fumado un cigarrito',
        u'mientras sus colegas le gritaban ACÁBALO',
        u'y se ha tirado un eructo',
        u'y se ha tirado un pedarro',
        u'y se ha tirado un cuesco',
        u'sin mucho esfuerzo',
        u'a duras penas',
        u'',
        u'',
        u''
    ])

NOBODY_WON = u'Por algún motivo, todos los jugadores están muertos. Nadie ha ganado... ¡otra vez será!'
HAS_NOW = u'Ahora tiene'

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
        u'Redios.',
        u'Es un tifón.',
        u'No hay quién ' + get_x_or_y(player, u'lo', u'la') + ' pare.',
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
        get_x_or_y(player, u'Esta mamadísimo.', u'Está mamadísima.')
    ])

REPLACED = u'Se lo queda y se deshace de'

def REVIVED(player):
    return u' '.join((player.get_name(), random.choice([
        u'sólo se estaba haciendo ' + get_x_or_y(player, u'el muerto. ¡Qué zooorrrooooo!', u'la muerta. ¡Qué zooorrraaaaa! (sin trazas de patriarcado).'),
        u'ha vuelto a la vida bajo extrañas circunstancias.',
        u'ha vuelto en forma de chapa y ahora es un zombie.',
        u'ha resucitado en mitad de su funeral y ha vuelto a la batalla.',
        u'tiene enchufe y el creador del bot le ha resucitado.',
        u'ha vuelto del otro barrio.'
    ])))

def INFECTED(player):
    return random.choice([
        player.get_name() + u' ha pillado el coronavirus.',
        u'Alguien ha infectado a ' + player.get_name() + u' con el coronavirus.',
        player.get_name() + u' no se ha lavado las manos lo suficiente y ha contraído el coronavirus.',
        player.get_name() + u' debería de haber seguido las recomendaciones para no pillar el coronavirus.',
        player.get_name() + u' ha contraído el coronavirus por ir al Mercadona a comprar papel higiénico.',
        player.get_name() + u' se saltó la cuarentena para fumarse uno y ha pillado el coronavirus.'
    ])

def INFECTED_DIED(player):
    return random.choice([
        u'El coronavirus ha acabado con ' + player.get_name() + u'. Aquí acaba su aventura.',
        u'Los hospitales están colapsados y no quedan camas para ' + player.get_name() + u'. Ha muerto por una neumonía provocada por coronavirus.',
        player.get_name() + u' ha fallecido por coronavirus.',
        player.get_name() + u' ha tosido hasta ahogarse por culpa del coronavirus.'
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

def MOVED_ATRACTION_SING():
    return random.choice([
        u' se ha acercado a ver qué se cuece.',
        u' ha llamado a un taxi para ir.',
        u' ha ido en coche.',
        u' ha ido a bailar.'
    ])

def MOVED_ATRACTION_PL():
    return random.choice([
        u' se han acercado a ver qué se cuece.',
        u' han llamado a un taxi para ir.',
        u' han ido en coche.',
        u' han ido a bailar.'
    ])

def POWERUP_ACTION():
    return random.choice([
        'ha cogido',
        u'ha encontrado'
    ])

START = u'¡Los participantes están listos! Ya conocemos la ubicación de cada uno de ellos. Que empiece el juego.'

def STOLE(robber, robbed, item):
    return u' '.join((robber.get_name(), u'le ha robado', item.name, u'a', robbed.get_name() + '.'))

def STOLE_AND_REPLACED(robber, robbed, item, old_item):
    return u' '.join((STOLE(robber, robbed, item) + u'.', 'Como es mejor, se ha deshecho de su' + old_item.name + '.'))

def STOLE_AND_THREW(robber, robbed, item):
    return u' '.join((STOLE(robber, robbed, item) + u'. Como tiene cosas mejores, lo ha tirado a la basura.'))

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

def TIED_AND_BEFRIEND(player_1, player_2):
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

def TRAP(player):
    return u' '.join((player.get_name(), u'ha puesto una trampa en', player.location.name + '.'))

def TRAP_DODGED(player, trapped_by, location):
    return u' '.join((player.get_name(), MOVED_SING(), location.name + u', ha visto la trampa que había puesto', trapped_by.get_name(), 'y la ha destruido.'))

def TRAPPED(player, trapped_by, location):
    return u' '.join((player.get_name(), MOVED_SING(), location.name, u'pero se ha comido la trampa que había puesto', trapped_by.get_name() + u'. ¡Qué torpe!'))

def TREASON(player_1, player_2):
    return random.choice([
        u'Aunque eran ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Parece que no se caían tan bien, ',
        u'Menudo judas, ',
        u'Vaya puñalada por la espalda, ',
        u'Menuda traición, ',
        u'Por lo visto no eran tan ' + get_x_or_y_plural([player_1, player_2], u'amigos, ', u'amigas, '),
        u'Premio ' + get_x_or_y(player_1, u'al mejor amigo', u'a la mejor amiga') + u' del año. ',
        ''
    ])

def UNFRIEND():
    return random.choice([
        'Ya no son ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.'),
        'Han dejado de ser ' + get_x_or_y_plural([player_1, player_2], 'amigos.', 'amigas.')
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

WITH = u'con'
