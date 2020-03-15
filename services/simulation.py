#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import urllib.request
from PIL import Image, ImageDraw, ImageFont

from data.literals import get_message
from models.tweet_type import Tweet_type

date = datetime.datetime.now()
time_stamp = u'-'.join([str(date.year), str(date.month), str(date.day), str(date.hour), str(date.minute)])
current_dir = os.path.abspath(os.path.dirname(__file__))
output_dir = os.path.join(current_dir, '../simulations', time_stamp)
filename = u'simulation'
line_number = 0

i = 1
temp_output_dir = output_dir
while os.path.exists(temp_output_dir):
    i = i + 1
    temp_output_dir = os.path.join(output_dir + '-' + str(i))

output_dir = temp_output_dir

os.makedirs(output_dir)

path = os.path.join(output_dir, filename + '.txt')

i = 1
while os.path.exists(path):
    i = i + 1
    path = os.path.join(output_dir, filename + '-' + str(i) + ".txt")

def initialize_avatars(player_list):
    path = 'assets/avatars'
    if not os.path.exists(path):
        os.makedirs(path)

    for i, player in enumerate(player_list):
        if len(player.username) > 0:
            filename = path + '/' + player.username
        else:
            filename = path + '/' + player.name
        if not (os.path.exists(filename + '.png')):
            urllib.request.urlretrieve('http://avatars.io/twitter/' + player.username + '/medium', filename + '.png')
        player.avatar_dir = filename

def write_tweet(type, player_list, place_list, location = None, args = None):
    global line_number
    if args == None:
        args = [player_list]
    write_line(get_message(type, args))
    line_number = line_number + 1
    draw_image(type, player_list, place_list, location, args)
    if type == Tweet_type.winner:
        with open(os.path.join(output_dir, '-1.txt'), "w") as file:
            file.write('todo ok')

def write_line(message):
    print(str(line_number) + u': ' + message.decode('utf-8'))

    with open(os.path.join(path), "a+", encoding="utf-8") as file:
        file.write(message.decode('utf8'))

def file_len():
    with open(os.path.join(path)) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_image(image_name, size = None):
    image = Image.open(os.path.join(current_dir, '../assets/' + image_name + '.png'))

    if size != None:
        return image.thumbnail(size)
    else:
        return image

def paste_image(image, x, y, dimension, image_name, image_dir = None):
    global current_dir

    if image_dir == None:
        image_dir = '../assets/' + image_name
    else:
        image_dir = '../' + image_dir

    image_to_paste = Image.open(os.path.join(current_dir, image_dir + '.png'))
    image_to_paste.thumbnail([dimension, dimension])
    side = int(dimension / 2)

    image.paste(image_to_paste, (x - side, y - side, x + side, y + side), image_to_paste.convert('RGBA'))

def draw_image(type, player_list, place_list, location = None, args = None):
    global line_number, current_dir
    image_1 = get_image('background')
    image_2 = get_image('background')

    alive_players_list = []
    dead_players_list = []
    for i, p in enumerate(player_list):
        if p.state == 1:
            alive_players_list.append(p)
        else:
            dead_players_list.append(p)

    if type == Tweet_type.start:
        image_2 = get_image('background_initial')
        summary_image = get_summary_image(type, image_2, alive_players_list, dead_players_list, place_list, location)
        summary_image.save(output_dir + '/' + str(line_number) + '.png')
    else:
        zoomed_image = get_zoomed_image(type, image_1, alive_players_list, dead_players_list, place_list, location, args)
        summary_image = get_summary_image(type, image_2, alive_players_list, dead_players_list, place_list, location)

        if type == Tweet_type.destroyed:
            zoomed_image.save(output_dir + '/' + str(line_number - 1) + 'bis.png')
            summary_image.save(output_dir + '/' + str(line_number - 1) + 'bisb.png')
        else:
            zoomed_image.save(output_dir + '/' + str(line_number) + '.png')
            summary_image.save(output_dir + '/' + str(line_number) + 'b.png')

def get_zoomed_image(type, image, alive_players_list, dead_players_list, place_list, location = None, args = None):
    draw = ImageDraw.Draw(image)
    font_path = os.path.join(current_dir, '../assets/Comic-Sans.ttf')
    image.putalpha(128)  # Half alpha; alpha argument must be an int

    for i, p in enumerate(place_list):
        if p.destroyed == True:
            paste_image(image, p.coord_x, p.coord_y, 60, 'destroyed')
        else:
            if p.loot:
                paste_image(image, p.coord_x - 16, p.coord_y, 32, 'loot')
            if p.trap_by != None:
                paste_image(image, location.coord_x, location.coord_y + 16, 32, 'trap')
            if p.monster:
                paste_image(image, location.coord_x, location.coord_y - 16, 32, 'monster')

    if type == Tweet_type.somebody_died or type == Tweet_type.monster_killed or type == Tweet_type.trapped or type == Tweet_type.somebody_died_of_infection:
        paste_image(image, args[0].location.coord_x, args[0].location.coord_y, 48, '', args[0].avatar_dir)
        draw.text((args[0].location.coord_x - 12, args[0].location.coord_y - 39), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
    elif type == Tweet_type.winner or type == Tweet_type.somebody_got_ill or type == Tweet_type.somebody_got_injured or type == Tweet_type.somebody_found_item or type == Tweet_type.somebody_replaced_item or type == Tweet_type.somebody_doesnt_want_item or type == Tweet_type.somebody_revived or type == Tweet_type.somebody_moved or type == Tweet_type.trap or type == Tweet_type.dodged_trap or type == Tweet_type.somebody_powerup or type == Tweet_type.somebody_was_infected:
        paste_image(image, location.coord_x, location.coord_y, 48, '', args[0].avatar_dir)
    elif type == Tweet_type.destroyed:
        for i, p in enumerate(args[1]):
            paste_image(image, location.coord_x + (i * 30) - 16, location.coord_y, 48, '', p.avatar_dir)
        if args[3] and len(args[2]) > 0:
            for i, p in enumerate(args[2]):
                paste_image(image, args[3].coord_x + (i * 30) - 16, args[3].coord_y, 48, '', p.avatar_dir)
    elif type == Tweet_type.somebody_tied_and_became_friend or type == Tweet_type.somebody_tied_and_was_friend or type == Tweet_type.somebody_escaped or type == Tweet_type.somebody_killed or type == Tweet_type.somebody_stole or type == Tweet_type.somebody_stole_and_threw or type == Tweet_type.somebody_stole_and_replaced:
        paste_image(image, location.coord_x - 26, location.coord_y, 48, '', args[0].avatar_dir)
        paste_image(image, location.coord_x + 26, location.coord_y, 48, '', args[1].avatar_dir)

        if args[0].state == 0:
            draw.text((location.coord_x + 8, location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
        if args[1].state == 0:
            draw.text((location.coord_x + 8, location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))

    w, h = image.size
    zoom = 3
    if location != None:
        x = location.coord_x
        y = location.coord_y
        zoom2 = zoom * 2
        image = image.crop((x - w / zoom2, y - h / zoom2, x + w / zoom2, y + h / zoom2))
        image.resize((w, h), Image.LANCZOS)
    return image

def get_summary_image(type, image, alive_players_list, dead_players_list, place_list, location):
    draw = ImageDraw.Draw(image)

    for i, place in enumerate(place_list):
        players_in_place = []
        for r, pp in enumerate(place.players):
            players_in_place.append(pp)
        for x, dp in enumerate(dead_players_list):
            if dp.location.name == place.name:
                players_in_place.append(dp)
        for j, player in enumerate(players_in_place):
            paste_image(image, place.coord_x + (j * 24), place.coord_y, 48, '', player.avatar_dir)

    if location != None:
        draw.ellipse((location.coord_x - 75, location.coord_y - 75, location.coord_x + 75, location.coord_y + 75), outline='rgb(255,0,0)', width=5)
        ellipse = Image.new('RGBA', image.size, (255,255,255,0))
        d = ImageDraw.Draw(ellipse)
        d.ellipse((location.coord_x - 2000, location.coord_y - 2000, location.coord_x + 2000, location.coord_y + 2000), outline=(255,255,255,100), width=1925)
        image = Image.alpha_composite(image, ellipse)

    for i, p in enumerate(place_list):
        if p.destroyed == True:
            paste_image(image, p.coord_x, p.coord_y, 60, 'destroyed')

        else:
            if p.loot:
                paste_image(image, p.coord_x - 16, p.coord_y, 32, 'loot')
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + 16, 32, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 16, 32, 'monster')

        if type == Tweet_type.winner:
            paste_image(image, p.coord_x, p.coord_y - 38, 72, 'crown')
            paste_image(image, 128, 128, 256, 'winner')
        elif type == Tweet_type.somebody_found_item or type == Tweet_type.somebody_replaced_item or type == Tweet_type.somebody_doesnt_want_item:
            paste_image(image, 128, 128, 256, 'item')
        elif type == Tweet_type.somebody_got_ill:
            paste_image(image, 128, 128, 256, 'illness')
        elif type == Tweet_type.somebody_got_injured:
            paste_image(image, 128, 128, 256, 'injure')
        elif type == Tweet_type.somebody_powerup:
            paste_image(image, 128, 128, 256, 'powerup')
        elif type == Tweet_type.somebody_tied_and_became_friend or type == Tweet_type.somebody_tied_and_was_friend:
            paste_image(image, 128, 128, 256, 'heart')
        elif type == Tweet_type.monster_moved or type == Tweet_type.monster_killed or type == Tweet_type.monster_appeared or type == Tweet_type.monster_disappeared:
            paste_image(image, 128, 128, 256, 'monster')
        elif type == Tweet_type.dodged_trap or type == Tweet_type.trapped or type == Tweet_type.trap:
            paste_image(image, 128, 128, 256, 'trap')
        elif type == Tweet_type.somebody_moved:
            paste_image(image, 128, 128, 256, 'move')
        elif type == Tweet_type.monster_killed or type == Tweet_type.somebody_killed or type == Tweet_type.somebody_died:
            paste_image(image, 128, 128, 256, 'skull')
        elif type == Tweet_type.somebody_revived:
            paste_image(image, 128, 128, 256, 'revive')
        elif type == Tweet_type.somebody_stole or type == Tweet_type.somebody_stole_and_threw or type == Tweet_type.somebody_stole_and_replaced:
            paste_image(image, 128, 128, 256, 'steal')
        elif type == Tweet_type.somebody_escaped:
            paste_image(image, 128, 128, 256, 'runaway')
        elif type == Tweet_type.destroyed:
            paste_image(image, 128, 128, 256, 'destroyed')
        elif type == Tweet_type.somebody_was_infected or type == Tweet_type.somebody_died_of_infection:
            paste_image(image, 128, 128, 256, 'infection')

    draw_ranking(image, alive_players_list, dead_players_list)
    return image

def draw_ranking(image, alive_players_list, dead_players_list):
    coord_x = 5
    coord_y = 1150

    for i, p in enumerate(alive_players_list):
        draw_player(image, coord_x, coord_y, alive_players_list[i])
        coord_x, coord_y = calculate_coords(coord_x, coord_y)

    for i, p in enumerate(dead_players_list):
        draw_player(image, coord_x, coord_y, dead_players_list[i])
        coord_x, coord_y = calculate_coords(coord_x, coord_y)


def draw_player(image, coord_x, coord_y, player):
    global current_dir
    draw = ImageDraw.Draw(image)

    font_path = os.path.join(current_dir, '../assets/Arial.ttf')
    font_path_2 = os.path.join(current_dir, '../assets/Comic-Sans.ttf')

    paste_image(image, coord_x + 24, coord_y + 24, 48, '', player.avatar_dir)
    draw.rectangle((coord_x, coord_y, coord_x + 48, coord_y + 48), outline='rgb(0,0,0)')

    if player.kills > 0:
        paste_image(image, coord_x + 7, coord_y - 17, 16, 'skull')
        draw.text((coord_x + 27, coord_y - 17), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_attack() != 0:
        paste_image(image, coord_x - 2, coord_y - 35, 16, 'attack')
        draw.text((coord_x + 14, coord_y - 35), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_defense() != 0:
        paste_image(image, coord_x + 26, coord_y - 35, 16, 'defense')
        draw.text((coord_x + 42, coord_y - 35), str(player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.state == 0:
        draw.text((coord_x + 3, coord_y - 11), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path_2, size=50))

def calculate_coords(coord_x, coord_y):
    img_width = 50
    imgs_per_row = 25
    space_between_rows = 100
    space_between_cols = 10
    first_column_x = 5

    coord_x = coord_x + (img_width + space_between_cols)
    if coord_x == first_column_x + imgs_per_row * (img_width + space_between_cols):
        coord_x = first_column_x
        coord_y = coord_y + space_between_rows

    return coord_x, coord_y

def wrap_text(text, width, font):
    text_lines = []
    text_line = []
    text = text.replace('\n', ' [br] ')
    words = text.split()
    font_size = font.getsize(text)

    for word in words:
        if word == '[br]':
            text_lines.append(' '.join(text_line))
            text_line = []
            continue
        text_line.append(word)
        w, h = font.getsize(' '.join(text_line))
        if w > width:
            text_line.pop()
            text_lines.append(' '.join(text_line))
            text_line = [word]

    if len(text_line) > 0:
        text_lines.append(' '.join(text_line))

    return text_lines

# def draw_big_player(image, draw, player, is_second_player = False):
#     global current_dir
#
#     font_path = os.path.join(current_dir, '../assets/Arial.ttf')
#     font_path_2 = os.path.join(current_dir, '../assets/Comic-Sans.ttf')
#
#     coord_x = 0
#     coord_y = 350
#     if is_second_player:
#         coord_x = 128
#
#     paste_image(image, coord_x, coord_y, 128, '', player.avatar_dir)
#     draw.rectangle((coord_x, coord_y, coord_x + 128, coord_y + 128), outline='rgb(0,0,0)')
#     paste_image(image, coord_x, coord_y, 76, 'skull')
#
#     draw.text((coord_x + 70, coord_y - 33), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=20))
#
#     paste_image(image, coord_x + 10, coord_y - 75, 16, 'attack')
#     draw.text((coord_x + 40, coord_y - 73), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=20))
#
#     paste_image(image, coord_x + 69, coord_y - 75, 16, 'defense')
#     draw.text((coord_x + 101, coord_y - 73), str(player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=20))
#
#     size_player = 17
#     size_location = 17
#     player_name = [0, 0]
#     location_name = [0, 0]
#
#     while len(player_name) > 1:
#         player_name = wrap_text(player.name, 128, ImageFont.truetype(font_path, size=size_player))
#         size_player = size_player - 1
#
#     while len(location_name) > 1:
#         location_name = wrap_text(player.location.name, 128, ImageFont.truetype(font_path, size=size_location))
#         size_location = size_location - 1
#
#     draw.text((coord_x + 2, coord_y + 130), player_name[0], fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=size_player))
#     draw.text((coord_x + 2, coord_y + 150), location_name[0], fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=size_location))
#
#     if player.state == 0:
#         draw.text((coord_x + 3, coord_y - 50), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path_2, size=150))
