#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.es.items import *

# Name, defense, attack
raw_weapon_list = [
    [1, u'una pulsera con la bandera de ESPAÑA', 1, 1],
    [1, u'un cenicero', 0, 2],
    [1, u'una rata de la peste', 0, 3],
    [2, u'una botella de lejía', 1, 2],
    [2, u'una silla de pressing catch', 0, 3],
    [2, u'un puño americano', 0, 3],
    [2, u'una navaja de Albacete', 1, 5],
    [2, u'la escena', 0, 3],
    [2, u'un arma con patas', 0, 3],
    [2, u'el queso del kebab', 0, 3],
    [2, u'el kebab', 0, 3],
    [2, u'el dinosaurio chavalito', 0, 3],
    [2, u'un alien fumeta', 0, 3],
    [2, u'un vaso de plástico con cerveza', 0, 3],
    [2, u'el cuchillo de Orslok', 0, 3],
    [2, u'la cabra de Cheeto', 0, 3],
    [2, u'la polla de Rasputin', 0, 3],
    [2, u'la constitución española', 0, 3],
    [2, u'el manifiesto', 0, 3],
    [2, u'el bocadillo de Damián', 0, 3],
    [2, u'un satisfyer', 0, 3],
    [2, u'un teclado de Coolermaster', 0, 3],
    [2, u'el Kuko', 0, 3],
    [2, u'unos pantaloncitos blancos', 0, 3],
    [2, u'una bola de papel', 0, 3],
    [2, u'un turbante', 0, 3],
    [2, u'la bandana de ricardo milos', 0, 3],
    [2, u'Ana Rosa', 0, 3],
]

raw_special_list = [
    [u'una placa de policía', True, False, False],
    [u'la corona de España', True, False, False],
    [u'la presa de Jah', False, True, False],
    [u'un ibuprofeno', False, True, False],
    [u'la vacuna del coronavirus', False, False, True],
    [u'una mascarilla', False, False, True]
]

raw_injury_list = [
    [u'un "y tan joven"', 0, 3],
    [u'un tumor en la mano', 0, 3],
    [u'un amarillo', 0, 3],
    [u'un coma etílico', 0, 3],
    [u'un esguince de tobillo', -1, -1],
    [u'una torta bien dada', -1, -1],
    [u'una colleja', -1, -1],
    [u'una hostia a mano abierta', -2, -2],
    [u'una patada en el pecho', -2, -2],
    [u'un dedo en el ojo', -2, -2],
    [u'un rodillazo en la boca del estómago', -3, -3],
    [u'un puñetazo en el estómago', -3, -3],
    [u'un dolor de espalda', -1, -1],
    [u'una caries', -1, -1],
    [u'un resfriado', -1, -1],
    [u'una diarrea aguda', -2, -2],
    [u'una apendicitis', -2, -2],
    [u'una piedra en el riñón', -2, -2],
    [u'una infección urinaria', -3, -3],
    [u'una diabetes', -3, -3],
    [u'una bronquitis', -3, -3],
    [u'una hernia discal', -4, -4],
    [u'la gripe española', -4, -4],
    [u'una malaria', -4, -4],
    [u'un sida', -5, -5],
    [u'un cáncer', -5, -5],
    [u'un infarto', -5, -5]
]

raw_powerup_list =[
    [2, u'una cerveza de marca no identificada', 0, 3],
    [2, u'unas perculaes', 0, 3],
    [2, u'un porro', 0, 3],
    [2, u'toda la puestada', 0, 3],
    [2, u'un footjob', 0, 3],
    [2, u'una clenca de amistad', 0, 3],
    [2, u'un ¡ALTO! Fúmese uno', 0, 3],
    [2, u'un GAMERS EN PIE', 0, 3],
    [1, u'un Monster', 0, 2],
    [1, u'un Red Bull', 0, 2],
    [1, u'un hummus de lentejas del Mercadona', 2, 0],
    [1, u'un Maxibon', 0, 2],
    [1, u'una lata de Steinburg', 2, 0],
    [1, u'unos Risketos', 1, 1],
    [1, u'unas Pringles', 1, 1],
    [1, u'una botella de agua (¡hay que hidratarse!)', 1, 1],
    [1, u'unos Doritos', 1, 1],
    [2, u'un paquete de cereales rellenos de leche del Mercadona', 2, 1],
    [2, u'un porrito', 2, 2],
    [2, u'unas patatas bravas del Mercadona', 3, 0],
    [2, u'un cacharro de kalimotxo', 2, 1],
    [3, u'un Knebep limón', 3, 3],
    [3, u'un Almirante cola', 3, 3],
    [3, u'un Cacique cola', 3, 3]
]