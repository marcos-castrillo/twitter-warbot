#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.config import LOCALIZATION

if LOCALIZATION == "es_paramo":
    from data.es_paramo.items import *
elif LOCALIZATION == "es_spain":
    from data.es_spain.items import *
