#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, defense, attack
raw_weapon_list = [
    [u'un vaso rojo de plástico con cerveza no identificada', 0, 1],
    [u'la bandana de Ricardo Milos', 1, 0],
    [u'una pulsera con la bandera de ESPAÑA', 2, 0],
    [u'unos pantaloncitos blancos', 2, 0],
    [u'la camiseta de Perculaes Social Club', 2, 0],
    [u'un cable RJ45', 0, 2],
    [u'la escena', 0, 2],
    [u'Ana Rosa', 0, 2],
    [u'un cenicero', 0, 3],
    [u'una silla de pressing catch', 0, 3],
    [u'el arma con patas', 0, 3],
    [u'el chupo', 1, 2],
    [u'el dinosaurio chavalito', 1, 2],
    [u'un alien fumeta', 2, 1],
    [u'la Constitución española', 3, 0],
    [u'el manifiesto', 3, 0],
    [u'la polla de Rasputin', 0, 3],
    [u'un teclado de Coolermaster', 1, 2],
    [u'el cuchillo de Orslok', 0, 4],
    [u'la cabra de Cheeto', 3, 1],
    [u'un satisfyer', 2, 2],
    [u'una botella de lejía', 2, 3],
    [u'el Kuko', 3, 2],
    [u'el espíritu de las plantas', 3, 2],
    [u'un puño americano', 0, 5],
    [u'una rata con la peste', 0, 5],
    [u'una navaja de Albacete', 1, 4]
]

raw_special_list = [
    [u'una placa de policía', True, False, False],
    [u'el m-word pass', True, False, False],
    [u'la presa de Jah', False, True, False],
    [u'un ibuprofeno', False, True, False],
    [u'la vacuna del coronavirus', False, False, True],
    [u'una mascarilla', False, False, True]
]

raw_injury_list = [
    [u'una colleja', -1, -1],
    [u'un puñetazo en el estómago', -1, -2],
    [u'una diarrea aguda', -2, -1],
    [u'una piedra en el riñón', -2, -3],
    [u'una diabetes', -3, -2],
    [u'un amarillo', -3, -3],
    [u'la gripe española', -4, -4],
    [u'una malaria', -4, -4],
    [u'un tumor en la muñeca', -5, -4],
    [u'un cáncer', -4, -5],
    [u'un sida', -5, -5],
    [u'un stroke', -5, -5],
    [u'un "y tan joven"', -5, -5],
    [u'un coma etílico', -5, -5]
]

raw_powerup_list = [
    [u'una botella de agua (¡hay que hidratarse!)', 1, 1],
    [u'un Monster', 0, 2],
    [u'un Red Bull', 0, 2],
    [u'un paquete de cereales rellenos de leche del Mercadona', 2, 0],
    [u'unas patatas bravas del Mercadona', 3, 0],
    [u'toda la puestada', 0, 3],
    [u'el bocadillo de Damián', 0, 3],
    [u'un kebab', 0, 2],
    [u'el queso del kebab', 0, 3],
    [u'la changa', 0, 3],
    [u'una lata de Steinburg', 2, 0],
    [u'un porrito', 3, 0],
    [u'un rebujito', 2, 2],
    [u'un licor café', 2, 2],
    [u'unas perculaes', 0, 4],
    [u'una clenca de amistad', 3, 2],
    [u'un ¡ALTO! Fúmese uno', 2, 3],
    [u'un GAMERS EN PIE', 0, 5],
    [u'un footjob', 5, 0]
]
