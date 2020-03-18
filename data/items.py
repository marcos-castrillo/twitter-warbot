#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, defense, attack
raw_item_list_1 = [
    [u'un gato chino que mueve el brazo', 1, 0],
    [u'el cartel de Project Bercy', 1, 0],
    [u'una pistola sin balas', 1, 0],
    [u'unas chinchetas', 0, 1],
    [u'unas tijeras', 0, 1],
    [u'una lata de atún del Día', 0, 1],
    [u'una bandera de Moderdonia', 0, 1],
    [u'una monda de plátano', 0, 1],
    [u'un libro tocho', 1, 0],
    [u'una botella de horchata', 0, 1],
    [u'una botella de agua de Madrid', 0, 1],
    [u'una percha de Zara', 1, 0],
    [u'el tiesto de una petunia', 0, 1],
    [u'un periódico enrollado', 0, 1],
    [u'una lata de sardinas', 0, 1],
    [u'una lata de melocotones en almíbar', 0, 1],
    [u'un palo', 0, 1],
    [u'una barra de pan de hace una semana', 0, 1],
    [u'una espada de plástico de los chinos', 0, 1],
    [u'un puntero láser', 1, 1],
    [u'una escoba', 0, 1],
    [u'un saco de pienso', 1, 0],
    [u'un saco de patatas', 1, 0],
    [u'un picahielos', 0, 2],
    [u'una gorro de cocinero', 1, 0],
    [u'una lata de anchoas', 1, 0],
    [u'una sudadera guapa', 2, 0],
    [u'un tirachinas', 0, 2],
    [u'un trozo de espejo roto', 0, 2],
    [u'un micrófono', 0, 2],
    [u'una llave inglesa', 0, 2],
    [u'un destornillador', 0, 2],
    [u'una cacha', 0, 1],
    [u'una chancla', 0, 2],
    [u'una vara de hierro', 2, 0],
    [u'una zapatilla de andar por casa', 1, 1],
    [u'una pistola de agua', 0, 1],
    [u'una camiseta de The Skalzos', 1, 1],
    [u'una espada de madera', 0, 2],
    [u'unos zuecos', 1, 0],
    [u'un escudo de madera', 2, 0],
    [u'un rodillo de amasar', 0, 2],
    [u'un manojo de llaves', 1, 1],
    [u'un calcetín sudado', 0, 1],
    [u'un pajarito', 0, 2],
    [u'un tubo de regar', 0, 2],
    [u'una pulsera con la bandera de ESPAÑA', 1, 1]
]

raw_item_list_2 = [
    [u'unos tirantes con la bandera de ESPAÑA', 0, 3],
    [u'una raqueta de frontenis', 0, 3],
    [u'un cenicero', 0, 2],
    [u'una cuchilla de afeitar', 0, 3],
    [u'una escopeta de balines', 0, 3],
    [u'unos shurikens', 0, 3],
    [u'una botella de lejía', 1, 2],
    [u'un palo muy largo', 1, 2],
    [u'una silla del Ikea', 1, 2],
    [u'un bate de béisbol', 0, 3],
    [u'una hoz y un martillo', 0, 3],
    [u'un tomahawk', 0, 3],
    [u'una ballesta', 0, 3],
    [u'unos guantes de boxeo', 1, 2],
    [u'una botella de vodka rota', 0, 3],
    [u'un puño americano', 0, 3],
    [u'un balón medicinal', -1, 3],
    [u'una merluza grasienta', -1, 3],
    [u'una sandía gorda gorda gorda', -1, 3],
    [u'una lanza', 0, 3],
    [u'un martillo', 1, 2],
    [u'un pico del Minecraft', 0, 3],
    [u'un Nokia 6300', 0, 3],
    [u'un escudo de hierro', 4, 0],
    [u'un hacha', 0, 4],
    [u'el casco de Fernando Alonso', 4, 0],
    [u'los guantes de Casillas', 3, 0],
    [u'unas botas de regar', 4, 0],
    [u'un azadón', 0, 4]
]

raw_item_list_3 = [
    [u'un bazooka', -3, 10],
    [u'un cinturón con la bandera de ESPAÑA', 3, 5],
    [u'una escopeta de caza', 0, 7],
    [u'un francotirador', -1, 9],
    [u'un escudo antidisturbios', 10, -3],
    [u'un chaleco antibalas', 10, 0],
    [u'el peluquín de Cepeda', 10, 0],
    [u'la silla de Echenique', 10, 0],
    [u'el puño de Thanos', 0, 9],
    [u'el perro Excálibur', 2, 8],
    [u'la cabra de la Legión', 2, 8]
]

raw_item_list = raw_item_list_1 + raw_item_list_2 + raw_item_list_3

raw_illness_list = [
    [u'un dolor de espalda', -1, -1],
    [u'una caries', -1, -1],
    [u'una sinusitis', -1, -1],
    [u'un resfriado', -1, -1],
    [u'una tos mucal', -1, -1],
    [u'una tos seca', -1, -1],
    [u'un reuma', -2, -2],
    [u'un dolor de oído', -2, -2],
    [u'una diarrea aguda', -2, -2],
    [u'una gripe', -2, -2],
    [u'una apendicitis', -2, -2],
    [u'una piedra en el riñón', -2, -2],
    [u'una trombosis', -2, -2],
    [u'un dolor de riñones', -2, -2],
    [u'una infección urinaria', -3, -3],
    [u'una otitis', -3, -3],
    [u'una diabetes', -3, -3],
    [u'una varicela', -3, -3],
    [u'una faringitis', -3, -3],
    [u'una bronquitis', -3, -3],
    [u'una hernia discal', -4, -4],
    [u'una gripe española', -4, -4],
    [u'una listeriosis', -4, -4],
    [u'una malaria', -4, -4],
    [u'una gripe porcina', -4, -4],
    [u'una epilepsia', -4, -4],
    [u'un sida', -5, -5],
    [u'un cáncer', -5, -5],
    [u'un infarto', -5, -5]
]

raw_injury_list = [
    [u'una cagada de pájaro', -1, -1],
    [u'un esguince de tobillo', -1, -1],
    [u'una torta bien dada', -1, -1],
    [u'una colleja', -1, -1],
    [u'una hostia a mano abierta', -2, -2],
    [u'una seta venenosa', -2, -2],
    [u'un corte leve en el brazo derecho', -2, -2],
    [u'una picadura de cobra', -2, -2],
    [u'una patada en el pecho', -2, -2],
    [u'una ensalada de codazos', -2, -2],
    [u'un dedo en el ojo', -2, -2],
    [u'un rodillazo en la boca del estómago', -3, -3],
    [u'un puñetazo en el estómago', -3, -3],
    [u'un corte profundo en el pecho', -3, -3],
    [u'una patada en sus partes', -4, -4],
    [u'una puñetazo en la nariz', -4, -4],
    [u'una necrosis en el brazo', -5, -5]
]

raw_powerup_list = [
    [u'una bolsa de magdalenas', 2, 0],
    [u'un botiquín', 3, 0],
    [u'una bocata de calamares', 2, 1],
    [u'un Knebep limón', 3, 3],
    [u'un Larios limón', 3, 3],
    [u'un Almirante cola', 3, 3],
    [u'un Cacique cola', 3, 3],
    [u'un Brugal cola', 3, 3],
    [u'una botella de sidra', 3, 3],
    [u'un JB cola', 3, 3],
    [u'un porrito', 2, 2],
    [u'un Monster', 0, 2],
    [u'un Red Bull', 0, 2],
    [u'un café con leche', 1, 1],
    [u'un cacharro de kalimotxo', 2, 1],
    [u'un hummus de lentejas del Mercadona', 2, 0],
    [u'unas patatas bravas del Mercadona', 2, 0],
    [u'un Maxibon', 0, 2],
    [u'un Calippo', 0, 2],
    [u'un Negritón', 2, 0],
    [u'un Frigopie', 2, 0],
    [u'una lata de Steinburg', 2, 0],
    [u'un paquete de cereales rellenos de leche del Mercadona', 2, 1],
    [u'unos Risketos', 1, 1],
    [u'unas Lays', 1, 1],
    [u'una caja de Fresón de Palos', 1, 1],
    [u'un jamón de Jabugo', 1, 1],
    [u'una morcilla de León', 1, 1],
    [u'una morcilla de Burgos', 1, 1],
    [u'unas Pringles', 1, 1],
    [u'una botella de agua (¡hay que hidratarse!)', 1, 1],
    [u'unos Doritos', 1, 1],
    [u'unas Papadeltas', 1, 1]
]
