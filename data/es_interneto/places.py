#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, road connections, coordinates, district display name, water connections
raw_place_list = [
    # Islas
    [u'VillaTwitch', [], [674, 160], None, [u'Notre Dame', u'El parque', u'Karmaland']],
    [u'Karmaland', [], [244, 170], None, [u'VillaTwitch', u'Un instituto de Arizona', u'A Coruña']],
    [u'Un instituto de Arizona', [], [204, 476], None, [u'Karmaland', u'Rancho Relaxo']],
    [u'Rancho Relaxo', [], [178, 860], None, [u'Perú', u'Un instituto de Arizona']],
    [u'Perú', [], [196, 1152], None, [u'Rancho Relaxo', u'Kenia']],
    [u'Kenia', [], [658, 1214], None, [u'Perú', u'Málaga', u'El Desalia']],
    [u'ElCapoLandia', [], [1294, 770], None, [u'Andorra', u'La piscina de Teruel']],
    # Tierra
    [u'El Desalia', [u"Popeye's"], [566, 968], None, [u'Kenia']],
    [u'Málaga', [u'La tumba de Damián'], [774, 1020], None, [u'Kenia']],
    [u'La tumba de Damián', [u'El parque', u'Andorra', u'Un zulo elegante'], [994, 580]],
    [u'El parque', [u'A Coruña', u'Villapersiana', u'Villapersiana'], [847, 389], None, [u'VillaTwitch']],
    [u'Un zulo elegante', [u"Popeye's", u'Villapersiana', u'A Coruña'], [640, 572]],
    [u'La piscina de Teruel', [u'Málaga', u'Villapersiana'], [984, 856], None, [u'ElCapoLandia']],
    [u'Villapersiana', [u"Popeye's", u'La piscina de Teruel', u'La tumba de Damián'], [792, 722]],
    [u"Popeye's", [u'El Desalia', u'Un zulo elegante', u'La tumba de Damián'], [576, 773]],
    [u'A Coruña', [u'Un zulo elegante', u'El parque'], [552, 368], None, [u'Karmaland']],
    [u'Andorra', [u'Notre Dame', u'La tumba de Damián'], [1216, 460], None, [u'ElCapoLandia']],
    [u'Notre Dame', [u'Andorra'], [1206, 210], None, [u'VillaTwitch']]
]
