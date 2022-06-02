#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

from services.images import *
from services.store import *
from models.drawing import DrawingText

draw = None
image = None
tweet = None
font = ImageFont.truetype(font_path, size=config.ranking.font_size)

limitless_districts = config.general.max_tributes_per_district == 0
RANKING_IMG_SIZE = config.ranking.avatar_size + 2
RANKING_SPACE_BETWEEN_COLS = config.ranking.padding
RANKING_FIRST_COLUMN_X = config.ranking.padding
RANKING_FIRST_ROW_Y = RANKING_IMG_SIZE + config.ranking.padding + config.ranking.district_name_height
RANKING_SPACE_BETWEEN_DISTRICTS = config.ranking.padding / 2
RANKING_SPACE_BETWEEN_ROWS = int(RANKING_IMG_SIZE * 7 / 4) + config.ranking.padding + int(
    RANKING_SPACE_BETWEEN_DISTRICTS / 4) + config.ranking.district_name_height
RANKING_WIDTH = config.ranking.images_per_row * RANKING_IMG_SIZE + \
                (config.ranking.images_per_row - 1) * RANKING_SPACE_BETWEEN_COLS + config.ranking.padding * 2
RANKING_DELTA_X = RANKING_IMG_SIZE + RANKING_SPACE_BETWEEN_COLS


def get_ranking_image(ranking_image, ranking_tweet):
    global image, tweet, draw
    image = ranking_image
    tweet = ranking_tweet
    draw = ImageDraw.Draw(image)
    row_index = 0
    col_index = 0

    if config.general.match_type == MatchType.districts:
        district_list = get_district_list()
        drawn_player_list = []

        while len(district_list) > 0:
            players_in_district = choose_fitting_district(district_list, row_index, col_index)
            row_index, col_index = draw_player_list_ranking(players_in_district, row_index, col_index, True)

            if not limitless_districts:
                cross_district_if_needed(players_in_district)

            drawn_player_list = drawn_player_list + players_in_district
            district_list.pop(district_list.index(players_in_district))

        # Linebreak
        dead_players = get_dead_players()
        if len(dead_players) > 0:
            if col_index > 0:
                col_index = 0
                row_index = row_index + 1
            row_index, col_index = draw_player_list_ranking(dead_players, row_index, col_index, False, True)
        drawn_player_list = drawn_player_list + dead_players
    else:
        alive_players_list = get_alive_players()
        dead_players_list = get_dead_players()
        drawn_player_list = alive_players_list + dead_players_list

        row_index, col_index = draw_player_list_ranking(alive_players_list, row_index, col_index)
        row_index, col_index = draw_player_list_ranking(dead_players_list, row_index, col_index)

    circle_players(drawn_player_list)

    return image


def get_ranking_height():
    alive_rows = math.ceil(len(get_alive_players()) / config.ranking.images_per_row)
    dead_rows = 0

    if config.general.match_type == MatchType.districts:
        dead_rows = math.ceil(len(get_dead_players()) / config.ranking.images_per_row)

    return int(alive_rows * RANKING_SPACE_BETWEEN_ROWS +
               dead_rows * int(7 * RANKING_SPACE_BETWEEN_ROWS / 12) + config.ranking.padding * 2)


def draw_player_ranking(player, row_index, col_index, is_dead=False):
    coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index)
    coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index)
    text_color = config.ranking.colors.text

    if is_dead:
        alive_rows = math.ceil(len(get_alive_players()) / config.ranking.images_per_row)
        dead_rows = row_index + 1 - alive_rows
        coord_y = coord_y - dead_rows * int(2 * RANKING_SPACE_BETWEEN_ROWS / 5)

    y = coord_y + int(2 * RANKING_IMG_SIZE / 4) - 2
    lines = split_multiline_text(player.name, RANKING_IMG_SIZE, font)

    for j, line in enumerate(lines):
        drawing_text = DrawingText(image, coord_x - 6, y)
        drawing_text.color = text_color
        drawing_text.font_size = config.ranking.font_size
        drawing_text.max_width = RANKING_IMG_SIZE + 10
        drawing_text.max_height = config.ranking.line_height
        drawing_text.line_height = config.ranking.line_height
        drawing_text.text = line
        drawing_text.center_horizontally = True
        drawing_text.center_vertically = False
        draw_wrapped_text(drawing_text)
        y = y + config.ranking.line_height

    drawing_player = DrawingPlayer(image, coord_x + int(config.ranking.avatar_size / 2),
                                   coord_y)
    drawing_player.player = player
    drawing_player.avatar_size = config.ranking.avatar_size
    drawing_player.icon_size = config.ranking.small_icon_size
    drawing_player.font_size = config.ranking.font_size_icons
    drawing_player.show_icons = player.is_alive

    draw_player(drawing_player)


def draw_ranking_rectangle(fill_color, fill_color_dark, players_count, row_index, col_index, index):
    players_in_rectangle = players_count - index

    if players_in_rectangle > config.ranking.images_per_row:
        players_in_rectangle = config.ranking.images_per_row

    x_0 = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index) - RANKING_SPACE_BETWEEN_DISTRICTS / 2
    x_1 = x_0 + (RANKING_DELTA_X * players_in_rectangle) - RANKING_SPACE_BETWEEN_DISTRICTS
    y_0 = RANKING_FIRST_ROW_Y + RANKING_SPACE_BETWEEN_ROWS * row_index - RANKING_IMG_SIZE
    y_1 = y_0 + RANKING_IMG_SIZE + RANKING_IMG_SIZE

    if index >= config.ranking.images_per_row:
        # multirow
        y_0 = y_0 - (config.ranking.padding / 2) - config.ranking.district_name_height
        draw.rectangle((x_0, y_0 + 1, x_1, y_1), outline='rgb(0,0,0)', fill=fill_color, width=1)
        draw.rectangle((x_0 + 1, y_0, x_1 - 1, y_0 + 1), fill=fill_color)
    else:
        draw.rectangle((x_0, y_0, x_1, y_1), outline='rgb(0,0,0)', fill=fill_color, width=1)
        draw.rectangle((x_0, y_0 - config.ranking.district_name_height, x_1, y_0), outline='rgb(0,0,0)',
                       fill=fill_color_dark, width=1)


def draw_place_name(name, row_index, col_index, current_index):
    coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index) - int(RANKING_SPACE_BETWEEN_DISTRICTS / 2)
    coord_y = RANKING_FIRST_ROW_Y + (
            RANKING_SPACE_BETWEEN_ROWS * row_index) - RANKING_IMG_SIZE - config.ranking.district_name_height

    drawing_text = DrawingText(image, coord_x, coord_y)
    drawing_text.color = config.ranking.colors.text
    drawing_text.font_size = config.ranking.font_size
    drawing_text.max_width = RANKING_IMG_SIZE + RANKING_SPACE_BETWEEN_DISTRICTS
    drawing_text.max_height = config.ranking.district_name_height - 2
    drawing_text.line_height = config.ranking.line_height
    drawing_text.text = name
    drawing_text.center_horizontally = True
    draw_wrapped_text(drawing_text)

    if current_index > 0:
        # dots
        x_0 = coord_x - config.ranking.padding / 2 + 3
        x_1 = coord_x - config.ranking.padding / 2 + 5
        y_0 = coord_y + config.ranking.district_name_height / 2 - 1
        y_1 = coord_y + config.ranking.district_name_height / 2 + 1
        draw.ellipse((x_0, y_0, x_1, y_1), fill='rgb(0,0,0)')


def draw_player_list_ranking(players_in_district, row_index, col_index, draw_rectangles=False, dead_area=False):
    first_line = True
    fill_color, fill_color_dark = get_fill_colors(players_in_district)

    for i, player in enumerate(players_in_district):
        if draw_rectangles:
            if i % config.ranking.images_per_row == 0:
                draw_ranking_rectangle(fill_color, fill_color_dark, len(players_in_district), row_index, col_index, i)
                if i == 0:
                    cols_width = len(players_in_district)
                    if cols_width > config.ranking.images_per_row:
                        cols_width = config.ranking.images_per_row
            if first_line:
                draw_place_name(player.district.district_display_name, row_index, col_index, i)

        draw_player_ranking(player, row_index, col_index, dead_area)
        col_index = col_index + 1

        if col_index + 1 > config.ranking.images_per_row:
            first_line = False
            col_index = 0
            row_index = row_index + 1

    return row_index, col_index


def circle_players(players_to_circle):
    col_index = 0
    row_index = 0
    dead_area = False

    for i, player in enumerate(players_to_circle):
        if config.general.match_type == MatchType.districts and not dead_area and not player.is_alive:
            col_index = 0
            row_index = row_index + 1
            dead_area = True

        if (tweet.player is not None and player.get_name() == tweet.player.get_name()) or \
                (tweet.player_2 is not None and player.get_name() == tweet.player_2.get_name()) or \
                (tweet.type == TweetType.attraction and any(
                    x for x in tweet.player_list if x.get_name() == player.get_name())):
            coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index)
            coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index)
            if dead_area:
                alive_rows = math.ceil(len(get_alive_players()) / config.ranking.images_per_row)
                dead_rows = row_index + 1 - alive_rows
                coord_y = coord_y - dead_rows * int(2 * RANKING_SPACE_BETWEEN_ROWS / 5)

                draw.ellipse((coord_x - int(RANKING_IMG_SIZE / 2), coord_y - RANKING_IMG_SIZE,
                              coord_x + 3 * int(RANKING_IMG_SIZE / 2), coord_y + RANKING_IMG_SIZE),
                             outline=config.map.colors.circle, width=6)
                draw.ellipse((coord_x - int(RANKING_IMG_SIZE / 2), coord_y - RANKING_IMG_SIZE, coord_x + 3 * int(
                    RANKING_IMG_SIZE / 2), coord_y + RANKING_IMG_SIZE),
                             outline='rgb(0,0,0)', width=2)
                draw.ellipse((coord_x - int(RANKING_IMG_SIZE / 2) + 5, coord_y - RANKING_IMG_SIZE + 5, coord_x + 3 * int(
                    RANKING_IMG_SIZE / 2) - 5, coord_y + RANKING_IMG_SIZE - 5),
                             outline='rgb(0,0,0)', width=2)
            else:
                coord_y = coord_y - config.ranking.district_name_height

                draw.ellipse((coord_x - RANKING_IMG_SIZE, coord_y - RANKING_IMG_SIZE - int(RANKING_IMG_SIZE/4), coord_x + RANKING_IMG_SIZE * 2,
                              coord_y + RANKING_IMG_SIZE * 2 - int(RANKING_IMG_SIZE / 4)),
                             outline=config.map.colors.circle, width=6)
                draw.ellipse((coord_x - RANKING_IMG_SIZE, coord_y - RANKING_IMG_SIZE - int(RANKING_IMG_SIZE / 4), coord_x + RANKING_IMG_SIZE * 2,
                              coord_y + RANKING_IMG_SIZE * 2 - int(RANKING_IMG_SIZE / 4)),
                             outline='rgb(0,0,0)', width=2)
                draw.ellipse((coord_x - RANKING_IMG_SIZE + 5, coord_y - RANKING_IMG_SIZE - int(RANKING_IMG_SIZE / 4) + 5,
                              coord_x + RANKING_IMG_SIZE * 2 - 5, coord_y + RANKING_IMG_SIZE * 2 - int(
                    RANKING_IMG_SIZE / 4) - 5),
                             outline='rgb(0,0,0)', width=2)

        col_index = col_index + 1

        if col_index + 1 > config.ranking.images_per_row:
            col_index = 0
            row_index = row_index + 1


def cross_district_if_needed(tributes, coord_x, coord_y):
    count = 0
    for j, tribute in enumerate(tributes):
        if tribute == '' or not tribute.is_alive:
            count = count + 1
    if count == len(tributes):
        draw.line((coord_x - 205, coord_y - 40, coord_x, coord_y + 60), fill=config.map.colors.circle, width=5)


def get_district_list():
    player_list_by_district = sorted(player_list, key=lambda x: x.district.name, reverse=False)

    if not limitless_districts:
        return [player_list_by_district[x:x + config.general.max_tributes_per_district] for x in
                range(0, len(player_list_by_district), config.general.max_tributes_per_district)]
    else:
        # dead players are shown below the rest
        district_list = []

        for i, loc in enumerate(place_list):
            temp_list = []
            for j, pl in enumerate(player_list_by_district):
                if pl.district.name == loc.name and pl.is_alive:
                    temp_list.append(pl)
            if len(temp_list) > 0:
                district_list.append(temp_list)

        return sorted(district_list, key=lambda x: sum(1 for y in x if y != '' and y.is_alive), reverse=True)


def choose_fitting_district(district_list, row_index, col_index):
    for i, d in enumerate(district_list):
        if (col_index == 0 and len(d) > config.ranking.images_per_row) or (
                len(d) <= config.ranking.images_per_row - col_index):
            return d
    return district_list[0]


def get_fill_colors(players_in_district):
    alive_count = sum(1 for y in players_in_district if y != '' and y.is_alive)
    if alive_count == 0:
        return config.ranking.colors.dead_color_2, config.ranking.colors.dead_color_1
    elif alive_count == 1:
        return config.ranking.colors.error_color_2, config.ranking.colors.error_color_1
    elif alive_count == 2:
        return config.ranking.colors.warning_color_2, config.ranking.colors.warning_color_1
    else:
        return config.ranking.colors.success_color_2, config.ranking.colors.success_color_1
