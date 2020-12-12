#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from services.api import tweet_line_from_file

dir_name = 'simulations'

img_file_extension = '.png'
text_file_extension = '.txt'

line_filename_suffix = '_line' + text_file_extension
image_filename_suffix = '_image' + text_file_extension

simulation_filename = 'simulation' + text_file_extension
events_filename = 'events' + text_file_extension


def get_file_path(filename):
    return os.path.join(current_dir, dir_name, dir_files[-1], filename)


# Get all files in dir
current_dir = os.path.abspath(os.path.dirname(__file__))
unsorted_dir_files = os.listdir(os.path.join(current_dir, dir_name))
dir_files = sorted(unsorted_dir_files, key=lambda d: list(map(int, d.split('-'))))
# Get file paths
next_line_path = get_file_path('-1' + line_filename_suffix)
next_image_path = get_file_path('-1' + image_filename_suffix)
simulation_path = get_file_path(simulation_filename)
events_path = get_file_path(events_filename)
# Get number of total lines
total_lines = 0
with open(simulation_path, encoding='utf-8') as f:
    for i, l in enumerate(f):
        total_lines = total_lines + 1
        pass
# Get next line to tweet
next_line = 0
while not os.path.isfile(next_line_path):
    if next_line > total_lines:
        exit(0)
    next_line_path = get_file_path(str(next_line) + line_filename_suffix)
    next_line = next_line + 1
# Check if the next line is an event
is_event = False
with open(events_path, encoding='utf-8') as f:
    for i, line in enumerate(f):
        if int(line) == next_line:
            is_event = True

if is_event:
    # Get next image to tweet
    next_image = 0
    while not os.path.isfile(next_image_path):
        next_image_path = get_file_path(str(next_image) + image_filename_suffix)
        next_image = next_image + 1
    # Tweet line
    main_image_path = get_file_path(str(next_image) + img_file_extension)
    image_path_list = [main_image_path]
    tweet_line_from_file(simulation_path, next_line, image_path_list)
    # Rename next_line and next_image files
    new_line_path = get_file_path(str(next_line) + line_filename_suffix)
    new_image_path = get_file_path(str(next_image) + image_filename_suffix)
    os.rename(next_line_path, new_line_path)
    os.rename(next_image_path, new_image_path)

