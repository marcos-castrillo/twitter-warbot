#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.config import LOCALIZATION

if LOCALIZATION == "es_paramo":
    from data.es_paramo.places import *
elif LOCALIZATION == "es_spain":
    from data.es_spain.places import *
elif LOCALIZATION == "es_interneto":
    from data.es_interneto.places import *
