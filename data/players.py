#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import LOCALIZATION

if LOCALIZATION == "es_paramo":
    from data.es_paramo.players import *
elif LOCALIZATION == "es_spain":
    from data.es_spain.players import *
