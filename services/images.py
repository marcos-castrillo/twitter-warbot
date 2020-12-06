#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont

from services.config import config
from services.store import get_alive_districts_count, get_alive_players_count,\
    split_multiline_text, place_list, any_players_around
from models.enums import MatchType
from models.drawing import DrawingPlayer, DrawingFile, DrawingItems, DrawingText

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
    drawing_image = DrawingFile(image, coord_x, coord_y)
    drawing_image.dimension = avatar_size
    drawing_image.image_name = ''
    drawing_image.image_dir = player.avatar_dir
    paste_image(drawing_image)

    draw.rectangle((coord_x - int(avatar_size / 2) - 1,
                    coord_y - int(avatar_size / 2) - 1,
                    coord_x + int(avatar_size / 2),
                    coord_y + int(avatar_size / 2)),
                   outline=frame_color, width=frame_width)

    if not player.is_alive:
        draw.text((coord_x - int(3 * avatar_size / 8), coord_y - int(9 * avatar_size / 12)), 'X',
                  fill=config.map.colors.circle, font=ImageFont.truetype(font_path, size=avatar_size))

    if show_icons:
        skull_icon_size = int(icon_size * 3 / 4)
        skull_font_size = font_size if (len(str(player.kills)) == 1) else font_size - 3
        skull_text_delta_x = int(avatar_size / 3) if (len(str(player.get_power())) == 1) else int(3 * avatar_size / 12)
        power_icon_size = icon_size
        power_font_size = font_size if (len(str(player.get_power())) == 1) else font_size - 3

        if player.kills > 0:
            draw.ellipse((coord_x - int(avatar_size / 3) - int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) - int(power_icon_size * 3 / 4),
                          coord_x - int(avatar_size / 3) + int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) + int(power_icon_size * 3 / 4)),
                         fill='#FFFFFF', outline=frame_color, width=2)

            draw = ImageDraw.Draw(image)
            drawing_image = \
                DrawingFile(image, coord_x - int(avatar_size / 3) - int(avatar_size/15), coord_y - avatar_size - int(avatar_size/15))
            drawing_image.dimension = skull_icon_size
            drawing_image.image_name = 'skull'
            paste_image(drawing_image)

            draw.text((coord_x - skull_text_delta_x, coord_y - avatar_size - int(avatar_size/15)), str(player.kills),
                      fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=skull_font_size))

        if player.get_power() != 0:
            draw.ellipse((coord_x + int(avatar_size / 3) - int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) - int(power_icon_size * 3 / 4),
                          coord_x + int(avatar_size / 3) + int(power_icon_size * 3 / 4),
                          coord_y - int(avatar_size) + int(power_icon_size * 3 / 4)),
                         fill='#FFFFFF', outline=frame_color, width=2)

            drawing_image = \
                DrawingFile(image, coord_x + int(avatar_size / 3) - int(avatar_size/15), coord_y - int(avatar_size) - int(avatar_size/15))
            drawing_image.dimension = power_icon_size
            drawing_image.image_name = 'power'
            paste_image(drawing_image)

            draw.text((coord_x + int(avatar_size / 3), coord_y - avatar_size - int(avatar_size/15)), str(player.get_power()),
                      fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=power_font_size))

        if len(player.item_list) == 1:
            drawing_image = \
                DrawingFile(image, coord_x, coord_y - int((avatar_size + icon_size) / 2) + int(icon_size / 4))
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'item_' + str(player.item_list[0].get_rarity())
            paste_image(drawing_image)
        elif len(player.item_list) == 2:
            drawing_image = DrawingFile(image, coord_x - int(avatar_size / 3),
                                        coord_y - int((avatar_size + icon_size) / 2) + int(icon_size / 4))
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'item_' + str(player.item_list[0].get_rarity())
            paste_image(drawing_image)

            drawing_image = DrawingFile(image, coord_x + int(avatar_size / 3),
                                        coord_y - int((avatar_size + icon_size) / 2) + int(icon_size / 4))
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'item_' + str(player.item_list[1].get_rarity())
            paste_image(drawing_image)

        delta_x = int(avatar_size / 2) - int(avatar_size / 10)
        delta_y = int(avatar_size / 4)

        if player.infected:
            drawing_image = DrawingFile(image, coord_x + delta_x, coord_y + delta_y)
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'infection'
            paste_image(drawing_image)

        if player.monster_immunity:
            drawing_image = DrawingFile(image, coord_x - delta_x, coord_y - delta_y)
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'monster_immunity'
            paste_image(drawing_image)

        if player.injure_immunity:
            drawing_image = DrawingFile(image, coord_x - delta_x, coord_y + delta_y)
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'injure_immunity'
            paste_image(drawing_image)

        if player.infection_immunity:
            drawing_image = DrawingFile(image, coord_x + delta_x, coord_y + delta_y)
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'infection_immunity'
            paste_image(drawing_image)

        if player.movement_boost:
            drawing_image = DrawingFile(image, coord_x + delta_x, coord_y - delta_y)
            drawing_image.dimension = icon_size
            drawing_image.image_name = 'movement_boost'
            paste_image(drawing_image)

        if player.is_alive and ((config.general.match_type == MatchType.districts and get_alive_districts_count() <= 1) or\
                (config.general.match_type == MatchType.standard and get_alive_players_count() <= 1)):
            drawing_image = DrawingFile(image, coord_x, coord_y - 2 * int(avatar_size / 4))
            drawing_image.dimension = icon_size * 2
            drawing_image.image_name = 'crown'
            paste_image(drawing_image)


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

    if players_length == 0:
        return

    if any_players_around(players[0].location):
        delta_y = int(delta_y / 2)
        delta_x = int(delta_x / 2)
        avatar_size = int(avatar_size / 2)
    if 0 < config.map.max_players_in_line < players_length and not single_line:
        players_length = config.map.max_players_in_line
    if players_length % 2 == 0:
        x_0 = coord_x - int(players_length / 2) * int(delta_x / 2)
    else:
        x_0 = coord_x - int((players_length - 1) / 2) * delta_x

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
    offset_y = drawing_items.offset_y
    gray_style = drawing_items.gray_style

    delta_x = int(config.map.icon_size / 2)
    delta_y = offset_y if offset_y is not None else config.map.icon_size

    if item_count == 1:
        drawing_image = DrawingFile(image, coord_x, coord_y - delta_y)
        drawing_image.dimension = config.map.icon_size
        drawing_image.image_name = 'item'
        drawing_image.gray_style = gray_style
        paste_image(drawing_image)
    elif item_count == 2:
        drawing_image = DrawingFile(image, coord_x - delta_x, coord_y - delta_y)
        drawing_image.dimension = config.map.icon_size
        drawing_image.image_name = 'item'
        drawing_image.gray_style = gray_style
        paste_image(drawing_image)

        drawing_image = DrawingFile(image, coord_x + delta_x, coord_y - delta_y)
        drawing_image.dimension = config.map.icon_size
        drawing_image.image_name = 'item'
        drawing_image.gray_style = gray_style
        paste_image(drawing_image)
    else:
        while item_count > 0:
            if item_count <= 3:
                y = coord_y - delta_y
                drawing_image =\
                    DrawingFile(image, coord_x - config.map.icon_size * 2 + item_count * config.map.icon_size, y)
                drawing_image.dimension = config.map.icon_size
                drawing_image.image_name = 'item'
                drawing_image.gray_style = gray_style
                paste_image(drawing_image)
            else:
                y = coord_y - delta_y - 10
                drawing_image = \
                    DrawingFile(image, coord_x - config.map.icon_size * 2 + (item_count - 3) * config.map.icon_size, y)
                drawing_image.dimension = config.map.icon_size
                drawing_image.image_name = 'item'
                drawing_image.gray_style = gray_style
                paste_image(drawing_image)
            item_count = item_count - 1


def draw_map_places(image, main_place=None):
    for i, p in enumerate(place_list):
        gray_style = main_place is not None and p.name != main_place.name
        color = config.map.colors.text if not gray_style else config.map.colors.text_subtle
        icon_name = 'place'
        if p.destroyed:
            color = config.map.colors.text_destroyed
            icon_name = 'destroyed'
        drawing_text = DrawingText(image, p.coord_x + int(config.map.avatar_size / 4) + 4,
                                   p.coord_y - int(config.map.line_height / 2))
        drawing_text.color = color
        drawing_text.font_size = config.map.font_size
        drawing_text.max_width = config.map.avatar_size * 2
        drawing_text.line_height = config.map.line_height
        drawing_text.text = p.name
        drawing_text.center_horizontally = True
        draw_wrapped_text(drawing_text)

        drawing_image = DrawingFile(image, p.coord_x, p.coord_y)
        drawing_image.dimension = config.map.icon_size
        drawing_image.image_name = icon_name
        drawing_image.gray_style = gray_style
        paste_image(drawing_image)

        if config.general.match_type != MatchType.rumble:
            item_y = p.coord_y if len(p.players) == 0 else p.coord_y - int(config.map.avatar_size / 3)
            drawing_items = DrawingItems(image, p.coord_x, item_y)
            drawing_items.item_count = len(p.items)
            drawing_items.offset_y = int(config.map.icon_size / 2)
            drawing_items.gray_style = gray_style
            draw_items(drawing_items)

        if p.trap_by is not None:
            drawing_image = DrawingFile(image, p.coord_x, p.coord_y + int(config.map.icon_size / 2))
            drawing_image.dimension = config.map.icon_size
            drawing_image.image_name = 'trap'
            drawing_image.gray_style = gray_style
            paste_image(drawing_image)
        if p.monster:
            drawing_image = DrawingFile(image, p.coord_x, p.coord_y - int(config.map.icon_size / 4))
            drawing_image.dimension = config.map.icon_size
            drawing_image.image_name = 'monster'
            drawing_image.gray_style = gray_style
            paste_image(drawing_image)


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


def paste_image(drawing_image):
    image = drawing_image.image
    x = drawing_image.coord_x
    y = drawing_image.coord_y
    dimension = drawing_image.dimension
    image_name = drawing_image.image_name
    image_dir = drawing_image.image_dir
    gray_style = drawing_image.gray_style

    if image_dir is None and os.path.exists(
            os.path.join(current_dir, config.file_paths.icons, config.general.run_name + '/' + image_name + '.png')):
        image_dir = os.path.join(config.file_paths.icons, config.general.run_name, image_name)
    elif image_dir is None:
        image_dir = os.path.join(config.file_paths.icons, image_name)
    else:
        image_dir = '../' + image_dir

    image_to_paste = Image.open(os.path.join(current_dir, image_dir + '.png'))
    image_to_paste.thumbnail([dimension, dimension])
    side = int(dimension / 2)
    if gray_style:
        image_to_paste = image_to_paste.convert('L')
        image_to_paste.putalpha(128)
    image.paste(image_to_paste, (x - side, y - side, x + side, y + side), image_to_paste.convert('RGBA'))
