#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.api import tweet_sleep
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(current_dir, 'assets/img/sleep')

tweet_sleep(image_path)
