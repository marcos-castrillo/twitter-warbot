#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont

from services.config import config
from services.store import get_alive_districts_count, get_alive_players_count, split_multiline_text
from models.enums import MatchType
from models.drawing import DrawingPlayer

current_dir = os.path.abspath(os.path.dirname(__file__))
font_path = os.path.join(current_dir, '../assets/fonts/Comic-Sans.ttf')


def draw_player(drawing_player):
    image = drawing_player.image
    coord_x = drawing_player.coord_x
    coord_y = drawing_player.coord_y
    player = drawing_player.player
    avatar_size = drawing_player.avatar_size
    icon_size = drawing_player.icon_size
    font_size = drawing_player.font_size
    show_icons = drawing_player.show_icons
    frame_color = drawing_player.frame_color
    if not frame_color:
        frame_color = '#FFFFFF'
    frame_width = config.map.frame_width_big if drawing_player.big_frame else config.map.frame_width

    draw = ImageDraw.Draw(image)
    paste_image(image, coord_x, coord_y, avatar_size, '', player.avatar_dir)
    draw.rectangle((coord_x - int(avatar_size / 2) - 1,
                    coord_y - int(avatar_size / 2) - 1,
                    coord_x + int(avatar_size / 2),
                    coord_y + int(avatar_size / 2)),
                   outline=frame_color, width=frame_width)

    if not player.is_alive:
        draw.text((coord_x - int(avatar_size / 3) - 4, coord_y - int(avatar_size / 3) * 2 - 4), 'X',
                  fill=config.map.colors.circle, font=ImageFont.truetype(font_path, size=avatar_size))

    if show_icons:
        skull_icon_size = int(icon_size * 3 / 4)
        skull_font_size = font_size if (len(str(player.kills)) == 1) else font_size - 3
        power_icon_size = icon_size
        power_font_size = font_size if (len(str(player.get_power())) == 1) else font_size - 3

        if player.kills > 0:
            draw.ellipse((coord_x - int(avatar_size / 3) - int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) - int(power_icon_size * 3 / 4),
                          coord_x - int(avatar_size / 3) + int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) + int(power_icon_size * 3 / 4)),
                         fill='#FFFFFF', outline=frame_color, width=2)
            paste_image(image, coord_x - int(avatar_size / 3) - int(avatar_size/15),
                        coord_y - avatar_size - int(avatar_size/15), skull_icon_size, 'skull')
            draw.text((coord_x - int(avatar_size / 3), coord_y - avatar_size - int(avatar_size/15)), str(player.kills),
                      fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=skull_font_size))

        if player.get_power() != 0:
            draw.ellipse((coord_x + int(avatar_size / 3) - int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) - int(power_icon_size * 3 / 4),
                          coord_x + int(avatar_size / 3) + int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) + int(power_icon_size * 3 / 4)),
                         fill='#FFFFFF', outline=frame_color, width=2)
            paste_image(image, coord_x + int(avatar_size / 3) - int(avatar_size/15),
                        coord_y - int(avatar_size) - int(avatar_size/15), power_icon_size, 'power')

            draw.text((coord_x + int(avatar_size / 3), coord_y - avatar_size - int(avatar_size/15)), str(player.get_power()),
                      fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=power_font_size))

        if len(player.item_list) == 1:
            paste_image(image, coord_x, coord_y - int((avatar_size + icon_size) / 2) + int(icon_size / 4), icon_size,
                        'item_' + str(player.item_list[0].get_rarity()))
        elif len(player.item_list) == 2:
            paste_image(image, coord_x - int(avatar_size / 3),
                        coord_y - int((avatar_size + icon_size) / 2) + int(icon_size / 4), icon_size,
                        'item_' + str(player.item_list[0].get_rarity()))
            paste_image(image, coord_x + int(avatar_size / 3),
                        coord_y - int((avatar_size + icon_size) / 2) + int(icon_size / 4), icon_size,
                        'item_' + str(player.item_list[1].get_rarity()))

        if player.infected:
            paste_image(image, coord_x + int(avatar_size / 2), coord_y, icon_size, 'infection')

        if player.monster_immunity:
            paste_image(image, coord_x - int(avatar_size / 2), coord_y - int(avatar_size / 4), icon_size,
                        'monster_immunity')
        if player.injure_immunity:
            paste_image(image, coord_x - int(avatar_size / 2), coord_y + int(avatar_size / 4), icon_size,
                        'injure_immunity')
        if player.infection_immunity:
            paste_image(image, coord_x + int(avatar_size / 2), coord_y, icon_size, 'infection_immunity')

        if player.is_alive and ((config.general.match_type == MatchType.districts and get_alive_districts_count() <= 1) or\
                (config.general.match_type == MatchType.standard and get_alive_players_count() <= 1)):
            paste_image(image, coord_x, coord_y - 2 * int(avatar_size / 4), icon_size * 2, 'crown')


def draw_multiple_players(drawing_players):
    image = drawing_players.image
    coord_x = drawing_players.coord_x
    coord_y = drawing_players.coord_y
    players = drawing_players.player_list
    delta_x = drawing_players.delta_x
    single_line = drawing_players.single_line
    font_size = drawing_players.font_size

    delta_y = config.map.height_between_players
    avatar_size = config.map.avatar_size
    players_length = len(players)

    if 0 < config.map.limit_small_avatars < len(players):
        delta_y = int(delta_y / 2)
        delta_x = int(delta_x / 2)
        avatar_size = int(avatar_size / 2)
    if 0 < config.map.max_players_in_line < len(players) and not single_line:
        players_length = config.map.max_players_in_line
    if players_length % 2 == 0:
        x_0 = coord_x - int(players_length / 2) * int(delta_x / 2)
    else:
        x_0 = coord_x - int((players_length - 1) / 2) * delta_x

    if len(players) > 0:
        x = x_0
        y = coord_y
        for i, player in enumerate(players):
            drawing_player = DrawingPlayer(image, x, y)
            drawing_player.player = players[i]
            drawing_player.avatar_size = avatar_size
            drawing_player.icon_size = config.map.icon_size
            drawing_player.show_icons = False
            drawing_player.font_size = font_size
            draw_player(drawing_player)
            x = x + delta_x
            if not single_line and (i - config.map.max_players_in_line + 1) % config.map.max_players_in_line == 0:
                x = x_0
                y = y + delta_y


def draw_items(drawing_items):
    image = drawing_items.image
    coord_x = drawing_items.coord_x
    coord_y = drawing_items.coord_y
    item_count = drawing_items.item_count
    transparent = drawing_items.transparent

    delta_y = int(config.map.small_icon_size / 2)
    item_img = 'item_transparent' if transparent else 'item'

    if item_count == 1:
        paste_image(image, coord_x, coord_y - int(config.map.icon_size / 2), config.map.small_icon_size, item_img)
    elif item_count == 2:
        paste_image(image, coord_x - 12, coord_y - delta_y, config.map.small_icon_size, item_img)
        paste_image(image, coord_x + 12, coord_y - delta_y, config.map.small_icon_size, item_img)
    else:
        while item_count > 0:
            if item_count <= 3:
                y = coord_y - delta_y
                paste_image(image, coord_x - config.map.small_icon_size * 2 + item_count * config.map.small_icon_size,
                            y, config.map.small_icon_size, item_img)
            else:
                y = coord_y - delta_y - 10
                paste_image(image,
                            coord_x - config.map.small_icon_size * 2 + (item_count - 3) * config.map.small_icon_size,
                            y, config.map.small_icon_size, item_img)
            item_count = item_count - 1


def draw_wrapped_text(drawing_text):
    image = drawing_text.image
    coord_x = drawing_text.coord_x
    coord_y = drawing_text.coord_y
    max_width = drawing_text.max_width
    max_height = drawing_text.max_height
    text = drawing_text.text
    initial_font_size = drawing_text.font_size
    text_color = drawing_text.color
    line_height = drawing_text.line_height
    center_horizontally = drawing_text.center_horizontally
    center_vertically = drawing_text.center_vertically

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=initial_font_size)
    lines = split_multiline_text(text, max_width, font)

    for i, line in enumerate(lines):
        y = coord_y + i * line_height

        font_size = initial_font_size + 1
        w, h = font.getsize(line)

        while w >= max_width:
            font_size = font_size - 1
            font = ImageFont.truetype(font_path, size=font_size)
            w, h = font.getsize(line)

        x = coord_x + (max_width - w) / 2 if center_horizontally else coord_x
        y = y + (int(max_height/len(lines)) - h) / 2 if max_height and center_vertically else y
        draw.text((x, y), line, fill=text_color, font=font)


def paste_image(image, x, y, dimension, image_name, image_dir=None):
    if image_dir is None and os.path.exists(
            os.path.join(current_dir, config.file_paths.icons + '/' + image_name + '.png')):
        image_dir = config.file_paths.icons + '/' + image_name
    elif image_dir is None:
        image_dir = config.file_paths.icons + '/../' + image_name
    else:
        image_dir = '../' + image_dir

    image_to_paste = Image.open(os.path.join(current_dir, image_dir + '.png'))
    image_to_paste.thumbnail([dimension, dimension])
    side = int(dimension / 2)
    image.paste(image_to_paste, (x - side, y - side, x + side, y + side), image_to_paste.convert('RGBA'))
