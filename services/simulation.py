#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
from data.literals import get_message

# Text files
date = datetime.datetime.now()
time_stamp = u'-'.join([str(date.year), str(date.month), str(date.day), str(date.hour) ,str(date.minute)])

output_dir = u'/'.join(['.', 'simulations', time_stamp])
filename = u'simulation'
line_number = 0


i = 1
while os.path.exists(output_dir):
    i = i + 1
    output_dir = os.path.join(output_dir + ' (' + str(i) + ')' + ".txt")
os.makedirs(output_dir)

path = os.path.join(output_dir, filename + '.txt')

i = 1
while os.path.exists(path):
    i = i + 1
    path = os.path.join(output_dir, filename + ' (' + str(i) + ')' + ".txt")

def write_tweet(type, player_list, args = None):
    global line_number
    if args == None:
        args = player_list
    write_line(get_message(type, args))
    line_number = file_len()
    draw_image(type, player_list, args)

def write_line(message):
    with open(os.path.join(path), "a+") as file:
        print(message)
        file.write(message + '\n')

def file_len():
    with open(os.path.join(path)) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Image files
from PIL import Image, ImageDraw, ImageFont

image = Image.open('assets/background.jpg')
draw = ImageDraw.Draw(image)

def draw_image(type, player_list, args = None):
    global line_number

    alive_players_list = []
    dead_players_list = []
    for i, p in enumerate(player_list):
        if p.state == 1:
            alive_players_list.append(p)
        else:
            dead_players_list.append(p)

    font = ImageFont.truetype('assets/Comic-Sans.ttf', size=15)

    (x, y) = (50, 50)
    message = alive_players_list[0].name
    color = 'rgb(0, 0, 0)'
    draw.text((x, y), message, fill=color, font=font)

    image.save(output_dir + '/' + str(line_number) + '.png')
