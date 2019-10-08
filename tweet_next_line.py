#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import exit
from services.api import tweet_line_from_file
from subprocess import call

current_dir = os.path.abspath(os.path.dirname(__file__))

unsorted_dir_files = os.listdir(os.path.join(current_dir, 'simulations'))
dir_files = sorted(unsorted_dir_files, key=lambda d: map(int, d.split('-')))

line_path = os.path.join(current_dir, 'simulations', dir_files[-1], '-1.txt')
simulation_path = os.path.join(current_dir, 'simulations', dir_files[-1], 'simulation.txt')

total_lines = 0
with open(simulation_path) as f:
    for i, l in enumerate(f):
        total_lines = total_lines + 1
        pass

line = 0

while not os.path.isfile(line_path):
    if line > total_lines:
        exit(0)
    line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(line) + '.txt')
    line = line + 1

last_tweet_id = None
with open(line_path) as f:
    for i, l in enumerate(f):
        last_tweet_id = l

image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(line) + '.png')

# last_tweet_id = tweet_line_from_file(simulation_path, line, image_path, last_tweet_id)
tweet_line_from_file(simulation_path, line, image_path)

with open(line_path, "w") as f:
    f.write(str(last_tweet_id))

new_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(line) + '.txt')
os.rename(line_path, new_path)
