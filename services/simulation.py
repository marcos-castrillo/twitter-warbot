#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime

from data.constants import output_dir

date = datetime.datetime.now()
filename = u'-'.join(['tournament', str(date.year), str(date.month), str(date.day), str(date.hour) ,str(date.minute)])
path = os.path.join(output_dir, filename + ".txt")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

i = 1
while os.path.exists(path):
    i = i + 1
    path = os.path.join(output_dir, filename + ' (' + str(i) + ')' + ".txt")


def write_tweet(message):
    with open(os.path.join(path), "a+") as file:
        print message
        file.write(message + '\n')
