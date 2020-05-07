#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import exit
from services.api import tweet_line_from_file
from subprocess import call

current_dir = os.path.abspath(os.path.dirname(__file__))

unsorted_dir_files = os.listdir(os.path.join(current_dir, 'simulations'))
dir_files = sorted(unsorted_dir_files, key=lambda d: map(int, d.split('-')))

next_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], '-1_line.txt')
next_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], '-1_image.txt')
simulation_path = os.path.join(current_dir, 'simulations', dir_files[-1], 'simulation.txt')

total_lines = 0
with open(simulation_path) as f:
    for i, l in enumerate(f):
        total_lines = total_lines + 1
        pass

next_line = 0
next_image = 0

while not os.path.isfile(next_line_path):
    if next_line > total_lines:
        exit(0)
    next_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
    next_line = next_line + 1

while not os.path.isfile(next_image_path):
    next_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_image.txt')
    next_image = next_image + 1

image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '.png')
image_2_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + 'b.png')
tweet_line_from_file(simulation_path, next_line, image_path, image_2_path)

new_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
new_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_image.txt')
os.rename(next_line_path, new_line_path)
os.rename(next_image_path, new_image_path)

second_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_bis.png')
if os.path.exists(second_image_path):
    second_image_bis_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + 'b_bis.png')
    previous_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
    next_line = next_line + 1

    tweet_line_from_file(simulation_path, next_line, second_image_path, second_image_bis_path)

    new_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
    os.rename(previous_line_path, new_line_path)
