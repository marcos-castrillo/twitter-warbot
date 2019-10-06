#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Id, name, coordinates, connections
raw_place_list = [
    [u'A Coruña', [u'Lugo', u'Pontevedra'], [409, 133]],
    [u'Albacete', [u'Alicante', u'Cuenca', u'Murcia', u'Valencia'], [955, 615]],
    [u'Alicante', [u'Albacete', u'Murcia', u'Valencia'], [1066, 675]],
    [u'Almería', [u'Granada', u'Murcia'], [900, 844]],
    [u'Ávila', [u'Segovia'], [714, 430]],
    [u'Badajoz', [u'Cáceres', u'Madrid', u'Sevilla'], [511, 621]],
    [u'Barcelona', [u'Lleida', u'Girona', u'Tarragona'], [1281, 322], [u'Palma de Mallorca']],
    [u'Bilbao', [u'San Sebastián', u'Santander', u'Vitoria'], [864, 142]],
    [u'Burgos', [u'Madrid', u'Palencia', u'Vitoria'], [798, 238]],
    [u'Cáceres', [u'Badajoz'], [570, 558]],
    [u'Cádiz', [u'Sevilla'], [579, 877], [u'Ceuta', u'Las Palmas de Gran Canaria']],
    [u'Castellón de la Plana', [u'Tarragona', u'Teruel', u'Valencia'], [1098, 501]],
    [u'Ceuta', [], [627, 985], [u'Cádiz', u'Melilla']],
    [u'Ciudad Real', [u'Jaén', u'Madrid'], [777, 613]],
    [u'Córdoba', [u'Jaén', u'Granada', u'Málaga', u'Sevilla'], [699, 736]],
    [u'Cuenca', [u'Albacete', u'Madrid'], [930, 493]],
    [u'Girona', [u'Barcelona'], [1342, 264]],
    [u'Granada', [u'Almería', u'Córdoba', u'Jaén', u'Málaga'], [804, 817]],
    [u'Guadalajara', [u'Soria', u'Madrid'], [846, 430]],
    [u'Huelva', [u'Sevilla'], [508, 795]],
    [u'Huesca', [u'Zaragoza'], [1074, 253]],
    [u'Jaén', [u'Ciudad Real', u'Córdoba', u'Granada', u'Madrid'], [802, 717]],
    [u'Las Palmas de Gran Canaria', [], [262, 1027], [u'Cádiz', u'Santa Cruz de Tenerife']],
    [u'León', [u'Lugo', u'Ourense', u'Oviedo', u'Valladolid', u'Zamora'], [642, 210]],
    [u'Lleida', [u'Barcelona', u'Tarragona', u'Zaragoza'], [1164, 312]],
    [u'Logroño', [u'Pamplona', u'Vitoria', u'Zaragoza'], [901, 229]],
    [u'Lugo', [u'A Coruña', u'León'], [472, 153]],
    [u'Madrid', [u'Badajoz', u'Burgos', u'Cáceres', u'Ciudad Real', u'Cuenca', u'Guadalajara', u'Jaén', u'Segovia', u'Sevilla', u'Toledo'], [792, 450]],
    [u'Málaga', [u'Córdoba', u'Granada'], [712, 862]],
    [u'Melilla', [], [854, 1054], [u'Ceuta']],
    [u'Murcia', [u'Albacete', u'Alicante', u'Almería'], [1022, 727]],
    [u'Ourense', [u'León', u'Pontevedra', u'Zamora'], [456, 226]],
    [u'Oviedo', [u'León', u'Santander'], [618, 120]],
    [u'Palencia', [u'Burgos', u'Valladolid'], [729, 274]],
    [u'Palma de Mallorca', [], [1356, 526], [u'Barcelona', u'Valencia']],
    [u'Pamplona', [u'Logroño', u'San Sebastián', u'Zaragoza'], [966, 186]],
    [u'Pontevedra', [u'A Coruña', u'Ourense'], [397, 235]],
    [u'Salamanca', [u'Valladolid'], [633, 387]],
    [u'San Sebastián', [u'Bilbao', u'Pamplona'], [922, 148]],
    [u'Santa Cruz de Tenerife', [], [163, 991], [u'Las Palmas de Gran Canaria']],
    [u'Santander', [u'Bilbao', u'Oviedo'], [794, 130]],
    [u'Segovia', [u'Ávila', u'Madrid', u'Valladolid'], [764, 385]],
    [u'Sevilla', [u'Badajoz', u'Cádiz', u'Córdoba', u'Huelva', u'Madrid'], [590, 792]],
    [u'Soria', [u'Guadalajara', u'Zaragoza'], [902, 304]],
    [u'Tarragona', [u'Barcelona', u'Castellón de la Plana', u'Lleida'], [1204, 360]],
    [u'Teruel', [u'Castellón de la Plana', u'Zaragoza'], [1020, 456]],
    [u'Toledo', [u'Madrid'], [768, 517]],
    [u'Valencia', [u'Albacete', u'Alicante', u'Castellón de la Plana'], [1070, 562], [u'Palma de Mallorca']],
    [u'Valladolid', [u'León', u'Palencia', u'Salamanca', u'Segovia', u'Zamora'], [714, 318]],
    [u'Vitoria', [u'Bilbao', u'Logroño', u'Burgos'], [885, 184]],
    [u'Zamora', [u'León', u'Ourense', u'Valladolid'], [628, 324]],
    [u'Zaragoza', [u'Huesca', u'Lleida', u'Logroño', u'Pamplona', u'Soria', u'Teruel'], [1034, 312]]
]
