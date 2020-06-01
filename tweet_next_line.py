#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from services.api import tweet_line_from_file
from subprocess import call

current_dir = os.path.abspath(os.path.dirname(__file__))

unsorted_dir_files = os.listdir(os.path.join(current_dir, 'simulations'))
dir_files = sorted(unsorted_dir_files, key=lambda d: list(map(int, d.split('-'))))

next_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], '-1_line.txt')
next_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], '-1_image.txt')
simulation_path = os.path.join(current_dir, 'simulations', dir_files[-1], 'simulation.txt')

def sanitize_lines(simulation_path):
    # Lines no longer than 240 chars
    longest_line = max(open(simulation_path, 'r', encoding='utf-8'), key=len)
    if len(longest_line) > 240:
        sys.exit('File error: line its too long: (' + str(len(longest_line)) +  ' characters)\n' +  longest_line)

    # Add . at the beginning of the lines if there's an @
    lines = {}
    with open(simulation_path, encoding='utf-8') as f:
        lines = f.readlines()

    for i, l in enumerate(lines):
        if l[0] == '@':
            temp_str = ''
            for j in l:
                temp_str += j
            temp_str = '.' + temp_str
            lines[i] = temp_str

    with open(simulation_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    with open(simulation_path, encoding='utf-8') as f:
        for i, l in enumerate(f):
            if l[0] == '@':
                sys.exit('File error: theres an @ as the first character of the line: ' + str(i))

sanitize_lines(simulation_path)

total_lines = 0
with open(simulation_path, encoding='utf-8') as f:
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

main_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '.png')
map_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_map.png')
ranking_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_ranking.png')
image_path_list = [main_image_path, map_image_path, ranking_image_path]
tweet_line_from_file(simulation_path, next_line, image_path_list)

new_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
new_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_image.txt')
os.rename(next_line_path, new_line_path)
os.rename(next_image_path, new_image_path)

main_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_bis.png')
if os.path.exists(main_image_path):
    map_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_map_bis.png')
    ranking_image_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_image) + '_ranking_bis.png')

    previous_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
    next_line = next_line + 1
    image_path_list = [main_image_path, map_image_path, ranking_image_path]
    tweet_line_from_file(simulation_path, next_line, image_path_list)

    new_line_path = os.path.join(current_dir, 'simulations', dir_files[-1], str(next_line) + '_line.txt')
    os.rename(previous_line_path, new_line_path)
