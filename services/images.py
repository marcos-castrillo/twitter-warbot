#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import math
from PIL import Image, ImageDraw, ImageFont

from data.literals import get_message
from data.config import *
from store import place_list, player_list, get_alive_players, get_dead_players
from models.tweet_type import Tweet_type
from models.item_type import Item_type

current_dir = os.path.abspath(os.path.dirname(__file__))
font_path = os.path.join(current_dir, '../assets/fonts/Comic-Sans.ttf')
font_path_2 = os.path.join(current_dir, '../assets/fonts/Arial.ttf')

def draw_player(image, tweet, player, coord_x, coord_y, simple = False):
    draw = ImageDraw.Draw(image)
    paste_image(image, coord_x, coord_y, AVATAR_SIZE, '', player.avatar_dir)

    if player.state == 0:
        draw.text((coord_x - 28, coord_y - 50), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=70))
    else:
        if player.infected:
            paste_image(image, coord_x + int(AVATAR_SIZE / 2), coord_y + 12, 36, 'infection')
        if not simple:
            if len(player.item_list) == 2:
                paste_image(image, coord_x + int(AVATAR_SIZE / 2), coord_y - int(AVATAR_SIZE / 2), 32, get_item_rarity(player.item_list[1]))
            if len(player.item_list) > 0:
                paste_image(image, coord_x - int(AVATAR_SIZE / 2), coord_y - int(AVATAR_SIZE / 2), 32, get_item_rarity(player.item_list[0]))
            if player.monster_immunity:
                paste_image(image, coord_x - int(AVATAR_SIZE / 2), coord_y + int(AVATAR_SIZE / 4), 32, 'special')
            if player.injure_immunity:
                paste_image(image, coord_x - int(AVATAR_SIZE / 2), coord_y + 2*int(AVATAR_SIZE / 4), 32, 'special')
            if player.infection_immunity:
                paste_image(image, coord_x - int(AVATAR_SIZE / 2), coord_y + 3*int(AVATAR_SIZE / 4), 32, 'special')
        if tweet.type == Tweet_type.winner or tweet.type == Tweet_type.winner_districts:
            paste_image(image, coord_x, coord_y - AVATAR_SIZE, 72, 'crown')

def draw_items(items_count, coord_x, coord_y, image, transparent = False):
    delta_y = int(AVATAR_SIZE / 2)
    if transparent:
        item_img = 'item_transparent'
    else:
        item_img = 'item'

    if items_count == 1:
        paste_image(image, coord_x, coord_y - int(AVATAR_SIZE / 2), 48, item_img)
    elif items_count == 2:
        paste_image(image, coord_x - 12, coord_y - delta_y, 48, item_img)
        paste_image(image, coord_x + 12, coord_y - delta_y, 48, item_img)
    else:
        while items_count > 0:
            if items_count <= 3:
                y = coord_y - delta_y
                paste_image(image, coord_x - 48 + items_count * 24, y, 48, item_img)
            else:
                y = coord_y - delta_y - 10
                paste_image(image, coord_x - 48 + (items_count - 3) * 24, y, 48, item_img)
            items_count = items_count - 1

def draw_multiple_players(tweet, players, coord_x, coord_y, image, delta_x, single_line = False):
    draw = ImageDraw.Draw(image)
    delta_y = HEIGHT_BETWEEN_PLAYERS

    if len(players) > 12:
        delta_y = int(delta_y / 2)
        delta_x = int(delta_x / 2)
    players_length = len(players)
    if MAX_PLAYERS_IN_LINE > 0 and not single_line and len(players) > MAX_PLAYERS_IN_LINE:
        players_length = MAX_PLAYERS_IN_LINE
    if players_length % 2 == 0:
        x_0 = coord_x - int(players_length / 2) * int(delta_x/2)
    else:
        x_0 = coord_x - int((players_length - 1) / 2) * delta_x

    if len(players) > 0:
        if single_line:
            x = x_0
            y = coord_y
            for i, player in enumerate(players):
                draw_player(image, tweet, players[i], x, y, True)
                x = x + delta_x
        else:
            x = x_0
            y = coord_y
            for i, player in enumerate(players):
                draw_player(image, tweet, players[i], x, y, True)
                x = x + delta_x
                if (i - MAX_PLAYERS_IN_LINE + 1) % MAX_PLAYERS_IN_LINE == 0:
                    x = x_0
                    y = y + delta_y

def draw_wrapped_text(image, coord_x, coord_y, max_width, max_height, text, font_path, initial_font_size, fill):
    draw = ImageDraw.Draw(image)
    font_size = initial_font_size + 1
    font = ImageFont.truetype(font_path, size=font_size)
    w, h = font.getsize(text)

    while w >= max_width:
        font_size = font_size - 1
        font = ImageFont.truetype(font_path, size=font_size)
        w, h = font.getsize(text)

    coord_x = coord_x + (max_width - w) / 2
    coord_y = coord_y + (max_height - h) / 2
    draw.text((coord_x, coord_y), text, fill=fill, font=font)

def get_multiline_wrapped_text(text, width, font):
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

def get_item_rarity(item):
    if item.get_rarity() == 1:
        return 'item_1'
    elif item.get_rarity() == 2:
        return 'item_2'
    elif item.get_rarity() == 3:
        return 'item_3'

def paste_image(image, x, y, dimension, image_name, image_dir = None):
    if image_dir == None and os.path.exists(os.path.join(current_dir, '../assets/icons/' + LOCALIZATION + '/' + image_name + '.png')):
        image_dir = '../assets/icons/' + LOCALIZATION + '/' + image_name
    elif image_dir == None:
        image_dir = '../assets/icons/' + image_name
    else:
        image_dir = '../' + image_dir

    image_to_paste = Image.open(os.path.join(current_dir, image_dir + '.png'))
    image_to_paste.thumbnail([dimension, dimension])
    side = int(dimension / 2)
    image.paste(image_to_paste, (x - side, y - side, x + side, y + side), image_to_paste.convert('RGBA'))
