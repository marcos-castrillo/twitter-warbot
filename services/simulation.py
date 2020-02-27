#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import urllib
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
        if not (os.path.exists(filename + '.jpg') and os.path.exists(filename + '_medium.jpg')):
            urllib.urlretrieve('http://avatars.io/twitter/' + player.username + '/small', filename + '.jpg')
            urllib.urlretrieve('http://avatars.io/twitter/' + player.username + '/medium', filename + '_medium.jpg')
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

    if type == Tweet_type.somebody_died or type == Tweet_type.monster_killed or type == Tweet_type.trapped:
        avatar = Image.open(args[0].avatar_dir + '.jpg')
        image.paste(avatar, (args[0].location.coord_x - 24, args[0].location.coord_y - 24, args[0].location.coord_x + 24, args[0].location.coord_y + 24), avatar.convert('RGBA'))
        draw.text((args[0].location.coord_x - 12, args[0].location.coord_y - 39), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
        draw_big_player(image, draw, args[0])
    elif type == Tweet_type.winner or type == Tweet_type.somebody_got_ill or type == Tweet_type.somebody_got_injured or type == Tweet_type.somebody_found_item or type == Tweet_type.somebody_replaced_item or type == Tweet_type.somebody_doesnt_want_item or type == Tweet_type.somebody_revived or type == Tweet_type.somebody_moved or type == Tweet_type.trap or type == Tweet_type.dodged_trap or type == Tweet_type.somebody_powerup:
        avatar = Image.open(args[0].avatar_dir + '.jpg')
        image.paste(avatar, (location.coord_x - 24, location.coord_y - 24, location.coord_x + 24, location.coord_y + 24), avatar.convert('RGBA'))
        draw_big_player(image, draw, args[0])
    elif type == Tweet_type.somebody_tied_and_became_friend or type == Tweet_type.somebody_tied_and_was_friend or type == Tweet_type.somebody_escaped or type == Tweet_type.somebody_killed or type == Tweet_type.somebody_stole or type == Tweet_type.somebody_stole_and_threw or type == Tweet_type.somebody_stole_and_replaced:
        avatar_1 = Image.open(args[0].avatar_dir + '.jpg')
        avatar_2 = Image.open(args[1].avatar_dir + '.jpg')
        image.paste(avatar_1, (location.coord_x - 50, location.coord_y - 24, location.coord_x - 2, location.coord_y + 24), avatar_1.convert('RGBA'))
        draw_big_player(image, draw, args[0])
        image.paste(avatar_2, (location.coord_x + 2, location.coord_y - 24, location.coord_x + 50, location.coord_y + 24), avatar_2.convert('RGBA'))
        draw_big_player(image, draw, args[1], True)

        if args[0].state == 0:
            draw.text((location.coord_x + 8, location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
        if args[1].state == 0:
            draw.text((location.coord_x + 8, location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))

    if type == Tweet_type.destroyed:
        for i, p in enumerate(args[1]):
            avatar = Image.open(p.avatar_dir + '.jpg')
            image.paste(avatar, (location.coord_x - 40 + (i * 30), location.coord_y - 24, location.coord_x + 8 + (i * 30), location.coord_y + 24), avatar.convert('RGBA'))
        if args[3] and len(args[2]) > 0:
            for i, p in enumerate(args[2]):
                avatar = Image.open(p.avatar_dir + '.jpg')
                image.paste(avatar, (args[3].coord_x - 40 + (i * 30), args[3].coord_y - 24, args[3].coord_x + 8 + (i * 30), args[3].coord_y + 24), avatar.convert('RGBA'))

    for i, p in enumerate(place_list):
        if p.destroyed == True:
            image.paste(get_image('destroyed'), (p.coord_x - 30, p.coord_y - 30, p.coord_x + 30, p.coord_y + 30), get_image('destroyed').convert('RGBA'))
        else:
            if p.loot:
                image.paste(get_image('loot'), (p.coord_x - 30, p.coord_y - 20, p.coord_x, p.coord_y + 10), get_image('loot').convert('RGBA'))
            if p.trap_by != None:
                image.paste(get_image('trap'), (p.coord_x - 10, p.coord_y - 10, p.coord_x + 20, p.coord_y + 20), get_image('trap').convert('RGBA'))
            if p.monster:
                image.paste(get_image('monster'), (p.coord_x - 15, p.coord_y - 30, p.coord_x + 15, p.coord_y), get_image('monster').convert('RGBA'))

    w, h = image.size
    zoom = 3
    if location != None:
        x = location.coord_x
        y = location.coord_y
        zoom2 = zoom * 2
        image = image.crop((x - w / zoom2, y - h / zoom2,
                        x + w / zoom2, y + h / zoom2))
        image.resize((w, h), Image.LANCZOS)
    return image

def get_summary_image(type, image, alive_players_list, dead_players_list, place_list, location):
    draw = ImageDraw.Draw(image)

    for i, place in enumerate(place_list):
        for j, player in enumerate(place.players):
            avatar = Image.open(player.avatar_dir + '.jpg')
            image.paste(avatar, (place.coord_x - 24 + (j * 24), place.coord_y - 24, place.coord_x + 24 + (j * 24), place.coord_y + 24), avatar.convert('RGBA'))

    if location != None:
        draw.ellipse((location.coord_x - 75, location.coord_y - 75, location.coord_x + 75, location.coord_y + 75), outline='rgb(255,0,0)', width=5)

    for i, p in enumerate(place_list):
        if p.destroyed == True:
            image.paste(get_image('destroyed'), (p.coord_x - 30, p.coord_y - 30, p.coord_x + 30, p.coord_y + 30), get_image('destroyed').convert('RGBA'))
        else:
            if p.loot:
                image.paste(get_image('loot'), (p.coord_x - 30, p.coord_y - 20, p.coord_x, p.coord_y + 10), get_image('loot').convert('RGBA'))
            if p.trap_by != None:
                image.paste(get_image('trap'), (p.coord_x - 10, p.coord_y - 10, p.coord_x + 20, p.coord_y + 20), get_image('trap').convert('RGBA'))
            if p.monster:
                monster = Image.open(os.path.join(current_dir, '../assets/monster.png'))
                image.paste(monster, (p.coord_x - 15, p.coord_y - 30, p.coord_x + 15, p.coord_y), monster.convert('RGBA'))

        if type == Tweet_type.winner:
            image.paste(get_image('crown'), (location.coord_x - 36, location.coord_y - 76, location.coord_x + 36, location.coord_y - 20), get_image('crown').convert('RGBA'))
            image.paste(get_image('winner'), (0, 0), get_image('winner').convert('RGBA'))
        elif type == Tweet_type.somebody_found_item or type == Tweet_type.somebody_replaced_item or type == Tweet_type.somebody_doesnt_want_item:
            image.paste(get_image('item'), (location.coord_x - 256, location.coord_y - 256), get_image('item').convert('RGBA'))
        elif type == Tweet_type.somebody_got_ill:
            image.paste(get_image('illness'), (0, 0), get_image('illness').convert('RGBA'))
        elif type == Tweet_type.somebody_got_injured:
            image.paste(get_image('injure'), (0, 0), get_image('injure').convert('RGBA'))
        elif type == Tweet_type.somebody_powerup:
            image.paste(get_image('powerup'), (0, 0), get_image('powerup').convert('RGBA'))
        elif type == Tweet_type.somebody_tied_and_became_friend or type == Tweet_type.somebody_tied_and_was_friend:
            image.paste(get_image('heart'), (0, 0), get_image('heart').convert('RGBA'))
        elif type == Tweet_type.monster_moved or type == Tweet_type.monster_killed or type == Tweet_type.monster_appeared or type == Tweet_type.monster_disappeared:
            image.paste(get_image('monster_big'), (0, 0), get_image('monster_big').convert('RGBA'))
        elif type == Tweet_type.dodged_trap or type == Tweet_type.trapped or type == Tweet_type.trap:
            image.paste(get_image('trap_big'), (0, 0), get_image('trap_big').convert('RGBA'))
        elif type == Tweet_type.somebody_moved:
            image.paste(get_image('move'), (0, 0), get_image('move').convert('RGBA'))
        elif type == Tweet_type.monster_killed or type == Tweet_type.somebody_killed or type == Tweet_type.somebody_died:
            image.paste(get_image('skull_big'), (0, 0), get_image('skull_big').convert('RGBA'))
        elif type == Tweet_type.somebody_revived:
            image.paste(get_image('revive'), (0, 0), get_image('revive').convert('RGBA'))
        elif type == Tweet_type.somebody_stole or type == Tweet_type.somebody_stole_and_threw or type == Tweet_type.somebody_stole_and_replaced:
            image.paste(get_image('steal'), (0, 0), get_image('steal').convert('RGBA'))
        elif type == Tweet_type.somebody_escaped:
            image.paste(get_image('runaway'), (0, 0), get_image('runaway').convert('RGBA'))
        elif type == Tweet_type.destroyed:
            image.paste(get_image('destroyed_big'), (0, 0), get_image('destroyed_big').convert('RGBA'))

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

def draw_big_player(image, draw, player, is_second_player = False):
    global current_dir

    avatar = Image.open(os.path.join(current_dir, '../', player.avatar_dir + '.jpg'))
    font_path = os.path.join(current_dir, '../assets/Arial.ttf')
    font_path_2 = os.path.join(current_dir, '../assets/Comic-Sans.ttf')

    coord_x = 0
    coord_y = 350
    if is_second_player:
        coord_x = 128

    image.paste(avatar, (coord_x, coord_y), avatar.convert('RGBA'))
    draw.rectangle((coord_x, coord_y, coord_x + 128, coord_y + 128), outline='rgb(0,0,0)')

    image.paste(get_image('skull'), (coord_x + 38, coord_y - 38), get_image('skull').convert('RGBA'))
    draw.text((coord_x + 70, coord_y - 33), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=20))

    image.paste(get_image('attack'), (coord_x + 10, coord_y - 75), get_image('attack').convert('RGBA'))
    draw.text((coord_x + 40, coord_y - 73), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=20))

    image.paste(get_image('defense'), (coord_x + 69, coord_y - 75), get_image('defense').convert('RGBA'))
    draw.text((coord_x + 101, coord_y - 73), str(player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=20))

    size_player = 17
    size_location = 17
    player_name = [0, 0]
    location_name = [0, 0]

    while len(player_name) > 1:
        player_name = wrap_text(player.name, 128, ImageFont.truetype(font_path, size=size_player))
        size_player = size_player - 1

    while len(location_name) > 1:
        location_name = wrap_text(player.location.name, 128, ImageFont.truetype(font_path, size=size_location))
        size_location = size_location - 1

    draw.text((coord_x + 2, coord_y + 130), player_name[0], fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=size_player))
    draw.text((coord_x + 2, coord_y + 150), location_name[0], fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=size_location))

    if player.state == 0:
        draw.text((coord_x + 3, coord_y - 50), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path_2, size=150))

def draw_player(image, coord_x, coord_y, player):
    global current_dir
    draw = ImageDraw.Draw(image)

    avatar = Image.open(os.path.join(current_dir, '../', player.avatar_dir + '.jpg'))

    font_path = os.path.join(current_dir, '../assets/Arial.ttf')
    font_path_2 = os.path.join(current_dir, '../assets/Comic-Sans.ttf')

    image.paste(avatar, (coord_x, coord_y), avatar.convert('RGBA'))
    draw.rectangle((coord_x, coord_y, coord_x + 48, coord_y + 48), outline='rgb(0,0,0)')

    if player.kills > 0:
        image.paste(get_image('skull'), (coord_x + 7, coord_y - 17), get_image('skull').convert('RGBA'))
        draw.text((coord_x + 27, coord_y - 17), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_attack() != 0:
        image.paste(get_image('attack'), (coord_x - 2, coord_y - 35), get_image('attack').convert('RGBA'))
        draw.text((coord_x + 14, coord_y - 35), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_defense() != 0:
        image.paste(get_image('defense'), (coord_x + 26, coord_y - 35), get_image('defense').convert('RGBA'))
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
