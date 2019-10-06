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
            filename = path + '/' + player.username + '.jpg'
        else:
            filename = path + '/' + player.name + '.jpg'
        if not os.path.exists(filename):
            urllib.urlretrieve('http://avatars.io/twitter/' + player.username + '/small', filename)
        player.avatar_dir = filename

def write_tweet(type, player_list, place_list, location = None, args = None):
    global line_number
    if args == None:
        args = [player_list]
    write_line(get_message(type, args))
    line_number = file_len() - 1
    draw_image(type, player_list, place_list, location, args)
    if type == Tweet_type.winner:
        with open(os.path.join(output_dir, '-1.txt'), "w") as file:
            file.write('todo ok')

def write_line(message):
    with open(os.path.join(path), "a+") as file:
        print(str(line_number + 1) + ': ' + message)
        file.write(message + '\n')

def file_len():
    with open(os.path.join(path)) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def draw_image(type, player_list, place_list, location = None, args = None):
    global line_number, current_dir

    image = Image.open(os.path.join(current_dir, '../assets/background.png'))
    destroyed = Image.open(os.path.join(current_dir, '../assets/destroyed.png'))
    destroyed_big = Image.open(os.path.join(current_dir, '../assets/destroyed_big.png'))
    trap = Image.open(os.path.join(current_dir, '../assets/trap.png'))
    trap_big = Image.open(os.path.join(current_dir, '../assets/trap_big.png'))
    loot = Image.open(os.path.join(current_dir, '../assets/loot.png'))
    item = Image.open(os.path.join(current_dir, '../assets/item.png'))
    monster = Image.open(os.path.join(current_dir, '../assets/monster.png'))
    monster_big = Image.open(os.path.join(current_dir, '../assets/monster_big.png'))
    illness = Image.open(os.path.join(current_dir, '../assets/illness.png'))
    powerup = Image.open(os.path.join(current_dir, '../assets/powerup.png'))
    skull = Image.open(os.path.join(current_dir, '../assets/skull.png'))
    skull_big = Image.open(os.path.join(current_dir, '../assets/skull_big.png'))
    heart = Image.open(os.path.join(current_dir, '../assets/heart.png'))
    crown = Image.open(os.path.join(current_dir, '../assets/crown.png'))
    injure = Image.open(os.path.join(current_dir, '../assets/injure.png'))
    move = Image.open(os.path.join(current_dir, '../assets/move.png'))
    revive = Image.open(os.path.join(current_dir, '../assets/revive.png'))
    start = Image.open(os.path.join(current_dir, '../assets/start.png'))
    steal = Image.open(os.path.join(current_dir, '../assets/steal.png'))
    runaway = Image.open(os.path.join(current_dir, '../assets/runaway.png'))
    winner = Image.open(os.path.join(current_dir, '../assets/winner.png'))

    font_path = os.path.join(current_dir, '../assets/Comic-Sans.ttf')

    draw = ImageDraw.Draw(image)

    alive_players_list = []
    dead_players_list = []
    for i, p in enumerate(player_list):
        if p.state == 1:
            alive_players_list.append(p)
        else:
            dead_players_list.append(p)
    if type == Tweet_type.start:
        for i, place in enumerate(place_list):
            for j, player in enumerate(place.players):
                avatar = Image.open(player.avatar_dir)
                image.paste(avatar, (place.coord_x - 24 + (j * 24), place.coord_y - 24, place.coord_x + 24 + (j * 24), place.coord_y + 24), avatar.convert('RGBA'))
    elif type == Tweet_type.somebody_died or type == Tweet_type.monster_killed or type == Tweet_type.trapped:
        avatar = Image.open(args[0].avatar_dir)
        image.paste(avatar, (args[0].location.coord_x - 24, args[0].location.coord_y - 24, args[0].location.coord_x + 24, args[0].location.coord_y + 24), avatar.convert('RGBA'))
        draw.text((args[0].location.coord_x - 12, args[0].location.coord_y - 39), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
    elif type == Tweet_type.winner or type == Tweet_type.somebody_got_ill or type == Tweet_type.somebody_got_injured or type == Tweet_type.somebody_found_item or type == Tweet_type.somebody_replaced_item or type == Tweet_type.somebody_doesnt_want_item or type == Tweet_type.somebody_revived or type == Tweet_type.somebody_moved or type == Tweet_type.trap or type == Tweet_type.dodged_trap or type == Tweet_type.somebody_powerup:
        avatar = Image.open(args[0].avatar_dir)
        image.paste(avatar, (location.coord_x - 24, location.coord_y - 24, location.coord_x + 24, location.coord_y + 24), avatar.convert('RGBA'))
    elif type == Tweet_type.somebody_tied_and_became_friend or type == Tweet_type.somebody_tied_and_was_friend or type == Tweet_type.somebody_escaped or type == Tweet_type.somebody_killed or type == Tweet_type.somebody_stole or type == Tweet_type.somebody_stole_and_threw or type == Tweet_type.somebody_stole_and_replaced:
        avatar_1 = Image.open(args[0].avatar_dir)
        avatar_2 = Image.open(args[1].avatar_dir)
        image.paste(avatar_1, (location.coord_x - 50, location.coord_y - 24, location.coord_x - 2, location.coord_y + 24), avatar_1.convert('RGBA'))
        image.paste(avatar_2, (location.coord_x + 2, location.coord_y - 24, location.coord_x + 50, location.coord_y + 24), avatar_2.convert('RGBA'))

        if args[0].state == 0:
            draw.text((location.coord_x + 8, location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
        if args[1].state == 0:
            draw.text((location.coord_x + 8, location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))

    if location != None:
        draw.ellipse((location.coord_x - 75, location.coord_y - 75, location.coord_x + 75, location.coord_y + 75), outline='rgb(255,0,0)', width=3)
    if type == Tweet_type.destroyed:
        for i, p in enumerate(args[1]):
            avatar = Image.open(p.avatar_dir)
            image.paste(avatar, (location.coord_x - 40 + (i * 30), location.coord_y - 24, location.coord_x + 8 + (i * 30), location.coord_y + 24), avatar.convert('RGBA'))
        if args[3] and len(args[2]) > 0:
            for i, p in enumerate(args[2]):
                avatar = Image.open(p.avatar_dir)
                image.paste(avatar, (args[3].coord_x - 40 + (i * 30), args[3].coord_y - 24, args[3].coord_x + 8 + (i * 30), args[3].coord_y + 24), avatar.convert('RGBA'))

    if type == Tweet_type.winner:
        image.paste(crown, (location.coord_x - 36, location.coord_y - 76, location.coord_x + 36, location.coord_y - 20), crown.convert('RGBA'))
        image.paste(winner, (0, 0), winner.convert('RGBA'))
    elif type == Tweet_type.somebody_found_item or type == Tweet_type.somebody_replaced_item or type == Tweet_type.somebody_doesnt_want_item:
        image.paste(item, (0, 0), item.convert('RGBA'))
    elif type == Tweet_type.start:
        image.paste(start, (0, 0), start.convert('RGBA'))
    elif type == Tweet_type.somebody_got_ill:
        image.paste(illness, (0, 0), illness.convert('RGBA'))
    elif type == Tweet_type.somebody_got_injured:
        image.paste(injure, (0, 0), injure.convert('RGBA'))
    elif type == Tweet_type.somebody_powerup:
        image.paste(powerup, (0, 0), powerup.convert('RGBA'))
    elif type == Tweet_type.somebody_tied_and_became_friend or type == Tweet_type.somebody_tied_and_was_friend:
        image.paste(heart, (0, 0), heart.convert('RGBA'))
    elif type == Tweet_type.monster_moved or type == Tweet_type.monster_killed or type == Tweet_type.monster_appeared or type == Tweet_type.monster_disappeared:
        image.paste(monster_big, (0, 0), monster_big.convert('RGBA'))
    elif type == Tweet_type.dodged_trap or type == Tweet_type.trapped or type == Tweet_type.trap:
        image.paste(trap_big, (0, 0), trap_big.convert('RGBA'))
    elif type == Tweet_type.somebody_moved:
        image.paste(move, (0, 0), move.convert('RGBA'))
    elif type == Tweet_type.monster_killed or type == Tweet_type.somebody_killed or type == Tweet_type.somebody_died:
        image.paste(skull_big, (0, 0), skull_big.convert('RGBA'))
    elif type == Tweet_type.somebody_revived:
        image.paste(revive, (0, 0), revive.convert('RGBA'))
    elif type == Tweet_type.somebody_stole or type == Tweet_type.somebody_stole_and_threw or type == Tweet_type.somebody_stole_and_replaced:
        image.paste(steal, (0, 0), steal.convert('RGBA'))
    elif type == Tweet_type.somebody_escaped:
        image.paste(runaway, (0, 0), runaway.convert('RGBA'))
    elif type == Tweet_type.destroyed:
        image.paste(destroyed_big, (0, 0), destroyed_big.convert('RGBA'))

    for i, p in enumerate(place_list):
        if p.destroyed == True:
            image.paste(destroyed, (p.coord_x - 15, p.coord_y - 15, p.coord_x + 15, p.coord_y + 15), destroyed.convert('RGBA'))
        else:
            if p.loot:
                image.paste(loot, (p.coord_x - 30, p.coord_y - 20, p.coord_x, p.coord_y + 10), loot.convert('RGBA'))
            if p.trap_by != None:
                image.paste(trap, (p.coord_x - 10, p.coord_y - 10, p.coord_x + 20, p.coord_y + 20), trap.convert('RGBA'))
            if p.monster:
                image.paste(monster, (p.coord_x - 15, p.coord_y - 30, p.coord_x + 15, p.coord_y), monster.convert('RGBA'))

    draw_ranking(image, draw, alive_players_list, dead_players_list)

    image.save(output_dir + '/' + str(line_number) + '.png')

def draw_ranking(image, draw, alive_players_list, dead_players_list):
    coord_x = 5
    coord_y = 1145

    for i, p in enumerate(alive_players_list):
        draw_player(image, draw, coord_x, coord_y, alive_players_list[i], True)
        coord_x, coord_y = calculate_coords(coord_x, coord_y)

    for i, p in enumerate(dead_players_list):
        draw_player(image, draw, coord_x, coord_y, dead_players_list[i], False)
        coord_x, coord_y = calculate_coords(coord_x, coord_y)

def draw_player(image, draw, coord_x, coord_y, player, is_alive):
    global current_dir

    avatar = Image.open(os.path.join(current_dir, '../', player.avatar_dir))
    skull = Image.open(os.path.join(current_dir, '../assets/skull.png'))
    attack = Image.open(os.path.join(current_dir, '../assets/attack.png'))
    defense = Image.open(os.path.join(current_dir, '../assets/defense.png'))

    font_path = os.path.join(current_dir, '../assets/Comic-Sans.ttf')

    image.paste(avatar, (coord_x, coord_y), avatar.convert('RGBA'))
    draw.rectangle((coord_x, coord_y, coord_x + 48, coord_y + 48), outline='rgb(0,0,0)')


    if player.kills > 0:
        image.paste(skull, (coord_x + 7, coord_y - 17), skull.convert('RGBA'))
        draw.text((coord_x + 27, coord_y - 17), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_attack() != 0:
        image.paste(attack, (coord_x - 2, coord_y - 35), attack.convert('RGBA'))
        draw.text((coord_x + 14, coord_y - 35), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_defense() != 0:
        image.paste(defense, (coord_x + 26, coord_y - 35), defense.convert('RGBA'))
        draw.text((coord_x + 42, coord_y - 35), str(player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if not is_alive:
        draw.text((coord_x + 3, coord_y - 11), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))

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
