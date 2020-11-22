#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, road connections, coordinates, district display name, water connections
raw_place_list = [
    [u'Andalucía', [u'Castilla-La Mancha', u'Murcia'], [703, 1090], None, [u'Ceuta']],
    [u'Aragón', [u'Navarra', u'Cataluña', u'Madrid', u'Valencia'], [1133, 509]],
    [u'Asturias', [u'Cantabria', u'Galicia', u'Castilla y León'], [598, 232]],
    [u'Islas Baleares', [], [1518, 739], None, [u'Cataluña', u'Valencia']],
    [u'Canarias', [], [253, 1458], None, [u'Ceuta']],
    [u'Cantabria', [u'Asturias', u'País Vasco'], [768, 249]],
    [u'Castilla y León', [u'Madrid', u'Asturias', u'Galicia'], [696, 482]],
    [u'Castilla-La Mancha', [u'Madrid', u'Valencia', u'Murcia', u'Andalucía'], [896, 794]],
    [u'Cataluña', [u'Aragón'], [1356, 456], None, [u'Islas Baleares']],
    [u'Valencia', [u'Aragón', u'Murcia', u'Castilla-La Mancha'], [1155, 783], None, [u'Islas Baleares']],
    [u'Extremadura', [u'Madrid'], [537, 829]],
    [u'Galicia', [u'Castilla y León', u'Asturias'], [372, 307]],
    [u'Madrid', [u'Castilla y León', u'Castilla-La Mancha', u'Extremadura', u'Aragón'], [811, 639]],
    [u'Murcia', [u'Valencia', u'Andalucía', u'Castilla-La Mancha'], [1084, 990]],
    [u'Navarra', [u'País Vasco', u'Aragón'], [1052, 313]],
    [u'País Vasco', [u'La Rioja', u'Navarra', u'Cantabria'], [927, 278]],
    [u'La Rioja', [u'País Vasco'], [933, 403]],
    [u'Ceuta', [], [611, 1303], None, [u'Melilla', u'Andalucía', u'Canarias']],
    [u'Melilla', [], [887, 1379], None, [u'Ceuta']],
]
