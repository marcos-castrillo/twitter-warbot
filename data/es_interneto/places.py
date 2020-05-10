#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, road connections, coordinates, district display name, water connections
raw_place_list = [
    # Islas
    [u'VillaTwitch', [], [674, 160], None, [u'Notre Dame',u'A Coruña',u'Karmaland']],
    [u'Karmaland', [], [244, 170], None, [u'VillaTwitch',u'Un instituto de Arizona']],
    [u'Un instituto de Arizona', [], [204, 476], None, [u'Karmaland',u'El zulo de Raúl',u'Rancho Relaxo']],
    [u'Rancho Relaxo', [], [178, 860], None, [u'Perú',u'Un instituto de Arizona']],
    [u'Perú', [], [196, 1152], None, [u'Rancho Relaxo',u'Kenia',u'El Desalia']],
    [u'Kenia', [], [658, 1214], None, [u'Perú',u'Málaga']],
    [u'ElCapoLandia', [], [1294, 770], None, [u'Andorra',u"Popeye's"]],
    # Tierra
    [u'El Desalia', [u'Las persianas de Darío',u'Málaga'], [566, 968], None, [u'Perú']],
    [u'Málaga', [u'El Desalia',u'La tumba de Damián'], [774, 1020], None, [u'Kenia']],
    [u'La tumba de Damián', [u"Popeye's",u'Málaga'], [946, 890]],
    [u'El parque', [u"Popeye's",u'El zulo de Raúl',u'Andorra'], [898, 512]],
    [u'El zulo de Raúl', [u'El parque',u'Las persianas de Darío',u'A Coruña'], [634, 572], None, [u'Un instituto de Arizona']],
    [u'Las persianas de Darío', [u'El zulo de Raúl',u"Popeye's",u'El Desalia'], [666, 780]],
    [u"Popeye's", [u'El parque',u'Las persianas de Darío',u'La tumba de Damián'], [954, 720], None, [u'ElCapoLandia']],
    [u'A Coruña', [u'El zulo de Raúl'], [552, 368], None, [u'VillaTwitch']],
    [u'Andorra', [u'Notre Dame',u'El parque'], [1216, 460], None, [u'ElCapoLandia']],
    [u'Notre Dame', [u'Andorra'], [1206, 210], None, [u'VillaTwitch']],
]
