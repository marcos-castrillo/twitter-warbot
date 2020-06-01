#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, road connections, coordinates, district display name, water connections
raw_place_list = [
    [u'Andalucía', [u'Aragón', u'Melilla'], [409, 133]],
    [u'Aragón', [u'Asturias',u'Andalucía'], [955, 615]],
    [u'Asturias', [u'Islas Baleares', u'Aragón'], [1066, 675]],
    [u'Islas Baleares', [u'Canarias', u'Asturias'], [900, 844]],
    [u'Canarias', [u'Cantabria',u'Islas Baleares'], [714, 430]],
    [u'Cantabria', [u'Castilla y León', u'Canarias'], [511, 621]],
    [u'Castilla y León', [u'Castilla-La Mancha', u'Cantabria'], [1281, 322]],
    [u'Castilla-La Mancha', [u'Cataluña', u'Castilla y León'], [864, 142]],
    [u'Cataluña', [u'Comunidad Valenciana', u'Castilla-La Mancha'], [798, 238]],
    [u'Comunidad Valenciana', [u'Extremadura',u'Cataluña'], [570, 558]],
    [u'Extremadura', [u'Galicia',u'Comunidad Valenciana'], [579, 877]],
    [u'Galicia', [u'Comunidad de Madrid', u'Extremadura'], [1098, 501]],
    [u'Comunidad de Madrid', [u'Región de Murcia',u'Galicia'], [627, 985]],
    [u'Región de Murcia', [u'Comunidad Foral de Navarra', u'Comunidad de Madrid'], [777, 613]],
    [u'Comunidad Foral de Navarra', [u'País Vasco', u'Región de Murcia'], [699, 736]],
    [u'País Vasco', [u'La Rioja', u'Comunidad Foral de Navarra'], [930, 493]],
    [u'La Rioja', [u'Ceuta',u'País Vasco'], [1342, 264]],
    [u'Ceuta', [u'Melilla', u'La Rioja'], [804, 817]],
    [u'Melilla', [u'Andalucía', u'Ceuta'], [846, 430]],
]
