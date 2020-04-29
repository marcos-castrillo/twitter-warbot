#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, road connections, coordinates, district display name, water connections
raw_place_list = [
    [u'VillaTwitch', [u'Notre Dame',u'A Coruña',u'Karmaland'], [690, 103]],
    [u'Karmaland', [u'VillaTwitch',u'un Instituto de Arizona'], [218, 116]],
    [u'un Instituto de Arizona', [u'Karmaland',u'el zulo de Raúl',u'Rancho Relaxo'], [177, 454]],
    [u'Rancho Relaxo', [u'Perú',u'un Instituto de Arizona'], [149, 859]],
    [u'Perú', [u'Rancho Relaxo',u'Kenia',u'Desalia'], [181, 1189]],
    [u'Kenia', [u'Perú',u'Málaga'], [679, 1327]],
    [u'ElCapoLandia', [u'Andorra',u"Popeye's"], [1377, 770]],
    [u'Desalia', [u'Perú',u'las persianas de Darío',u'Málaga'], [586, 991]],
    [u'Málaga', [u'Kenia',u'Desalia',u'la tumba de Damián'], [809, 1031]],
    [u'la tumba de Damián', [u"Popeye's",u'Málaga'], [975, 901]],
    [u'el parque', [u"Popeye's",u'el zulo de Raúl',u'Andorra'], [955, 615]],
    [u'el zulo de Raúl', [u'el parque',u'las persianas de Darío',u'A Coruña',u'un Instituto de Arizona'], [942, 500]],
    [u'las persianas de Darío', [u'el zulo de Raúl',u"Popeye's",u'Desalia'], [684, 784]],
    [u"Popeye's", [u'el parque',u'las persianas de Darío',u'la tumba de Damián',u'ElCapoLandia'], [996, 720]],
    [u'A Coruña', [u'VillaTwitch',u'el zulo de Raúl'], [541, 346]],
    [u'Andorra', [u'Notre Dame',u'el parque',u'ElCapoLandia'], [1297, 437]],
    [u'Notre Dame', [u'Andorra',u'VillaTwitch'], [1273, 158]],
]
