#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, road connections, coordinates, district display name, water connections
raw_place_list = [
    # Islas
    [u'VillaTwitch', [], [690, 103], None, [u'Notre Dame',u'A Coruña',u'Karmaland']],
    [u'Karmaland', [], [218, 116], None, [u'VillaTwitch',u'Un instituto de Arizona']],
    [u'Un instituto de Arizona', [], [177, 454], None, [u'Karmaland',u'El zulo de Raúl',u'Rancho Relaxo']],
    [u'Rancho Relaxo', [], [149, 859], None, [u'Perú',u'Un instituto de Arizona']],
    [u'Perú', [], [181, 1189], None, [u'Rancho Relaxo',u'Kenia',u'Desalia']],
    [u'Kenia', [], [679, 1251], None, [u'Perú',u'Málaga']],
    [u'ElCapoLandia', [], [1377, 770], None, [u'Andorra',u"Popeye's"]],
    # Tierra
    [u'Desalia', [u'Las persianas de Darío',u'Málaga'], [586, 991], None, [u'Perú']],
    [u'Málaga', [u'Desalia',u'La tumba de Damián'], [809, 1031], None, [u'Kenia']],
    [u'La tumba de Damián', [u"Popeye's",u'Málaga'], [975, 901]],
    [u'El parque', [u"Popeye's",u'El zulo de Raúl',u'Andorra'], [955, 615]],
    [u'El zulo de Raúl', [u'El parque',u'Las persianas de Darío',u'A Coruña'], [653, 554], None, [u'Un instituto de Arizona']],
    [u'Las persianas de Darío', [u'El zulo de Raúl',u"Popeye's",u'Desalia'], [684, 784]],
    [u"Popeye's", [u'El parque',u'Las persianas de Darío',u'La tumba de Damián'], [996, 720], None, [u'ElCapoLandia']],
    [u'A Coruña', [u'El zulo de Raúl'], [541, 346], None, [u'VillaTwitch']],
    [u'Andorra', [u'Notre Dame',u'El parque'], [1297, 437], None, [u'ElCapoLandia']],
    [u'Notre Dame', [u'Andorra'], [1273, 158], None, [u'VillaTwitch']],
]
