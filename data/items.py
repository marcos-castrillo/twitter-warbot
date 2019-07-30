#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, defense, attack
raw_item_list_1 = [
    [u'un gato chino de esos que mueven el brazo', 0, 0],
    [u'una trucha', 0, 0],
    [u'un mero', 0, 0],
    [u'una pistola sin balas', 0, 0],
    [u'unas chinchetas', 0, 1],
    [u'una cáscara de plátano', 0, 1],
    [u'un libro tocho', 1, 0],
    [u'un tiesto', 0, 1],
    [u'una lata de sardinas', 0, 1],
    [u'una lata de melocotones en almíbar', 0, 1],
    [u'un palo', 0, 1],
    [u'un pedrolo', 0, 1],
    [u'un abrigo feo', 1, 0],
    [u'una remolacha', 0, 1],
    [u'un huevo podrido', 1, 0],
    [u'una barra de pan de hace una semana', 0, 1],
    [u'una espada de plástico de los chinos', 0, 1],
    [u'una cuchilla de afeitar', 1, 1],
    [u'un perrito faldero', 1, 1],
    [u'un cepo', 0, 2],
    [u'una sudadera guapa', 2, 0],
    [u'un tirachinas', 0, 2],
    [u'un tomahawk', 0, 2],
    [u'una pistola de agua', 0, 1],
    [u'una espada de madera', 0, 2],
    [u'un escudo de madera', 2, 0],
    [u'un pallet', 2, 0],
    [u'unas llaves', 1, 1],
    [u'un cartel de Jose de Rico #ProjectBercy', 2, 0],
    [u'una piedra con forma de Q', 2, 0],
    [u'la foto de la orla de Juan Pérez Trujillo', 2, 0]
]

raw_item_list_2 = [
    [u'una escopeta de balines', 0, 3],
    [u'unos shurikens', 0, 3],
    [u'un palo muy largo', 1, 2],
    [u'una ballesta', 0, 3],
    [u'un arco', 0, 3],
    [u'una botella de vodka', 0, 3],
    [u'un puño americano', 0, 3],
    [u'una lanza', 0, 3],
    [u'un Nokia 6300', 0, 3],
    [u'una jeringuilla con sida', -2, -1],
    [u'un cuchillo con forma de Q', 3, 0],
    [u'un perro agresivo pero muy obediente', 2, 2],
    [u'un escudo de hierro', 4, 0],
    [u'un hacha', 0, 4],
    [u'unas granadas', 0, 4],
    [u'unos restos del avión estrellado de Juan Pérez Trujillo', 3, 0]
]

raw_item_list_3 = [
    [u'un bazooka', -3, 10],
    [u'una escopeta de caza', 0, 7],
    [u'una pistola silenciada', 2, 6],
    [u'un rifle de caza', 0, 8],
    [u'un francotirador', -1, 9],
    [u'un subfusil', 0, 7],
    [u'una ametralladora pesada', -2, 9],
    [u'un escudo antidisturbios', 10, -3],
    [u'un chaleco antibalas', 10, 0],
    [u'una espada con forma de Q', 6, 0],
    [u'un javelin', -2, 10]
]

raw_item_list = raw_item_list_1 + raw_item_list_2 + raw_item_list_3

raw_illness_list = [
    [u'un resfriado', -1, -1],
    [u'una tos mucal', -1, -1],
    [u'una diarrea aguda', -2, -2],
    [u'una apendicitis', -2, -2],
    [u'una otitis', -3, -3],
    [u'una faringitis', -3, -3],
    [u'una bronquitis', -3, -3],
    [u'una malaria', -4, -4],
    [u'un sida', -5, -5],
    [u'un cáncer', -5, -5],
    [u'un infarto', -5, -5]
]

raw_injury_list = [
    [u'un esguince de tobillo', -1, -1],
    [u'una torta bien dada', -1, -1],
    [u'una hostia a mano abierta', -1, -1],
    [u'una colleja', -2, -2],
    [u'una seta venenosa', -2, -2],
    [u'un corte leve en el brazo derecho', -2, -2],
    [u'una picadura de cobra', -2, -2],
    [u'una patada en el pecho', -2, -2],
    [u'una ensalada de codazos', -2, -2],
    [u'un puñetazo en el estómago', -3, -3],
    [u'un corte profundo en el pecho', -3, -3],
    [u'una patada en sus partes', -4, -4],
    [u'una necrosis en el brazo izquierdo', -5, -5]
]

raw_powerup_list = [
    [u'un cubata bien cargado', 3, 3]
]
