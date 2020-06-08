#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.images import *

limitless_districts = MAX_TRIBUTES_PER_DISTRICT == 0
image = None
tweet = None

def get_ranking_image(ranking_image, ranking_tweet):
    global image, tweet
    image = ranking_image
    tweet = ranking_tweet
    row_index = 0
    col_index = 0

    if MATCH_TYPE == Match_type.districts:
        district_list = get_district_list()
        drawn_player_list = []

        while len(district_list) > 0:
            players_in_district = choose_fitting_district(district_list, row_index, col_index)
            players_count = len(players_in_district)

            row_index, col_index = draw_player_list_ranking(players_in_district, row_index, col_index, True)

            if not limitless_districts:
                cross_district_if_needed(players_in_district)

            drawn_player_list = drawn_player_list + players_in_district
            district_list.pop(district_list.index(players_in_district))

        # Breakline
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

def draw_player_ranking(player, row_index, col_index, is_dead = False):
    draw = ImageDraw.Draw(image)

    coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index)
    coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index)
    if is_dead:
        alive_rows = math.ceil(len(get_alive_players()) / RANKING_IMGS_PER_ROW)
        dead_rows = row_index + 1 - alive_rows
        coord_y = coord_y - dead_rows * int(RANKING_SPACE_BETWEEN_ROWS/3)

    y = coord_y + RANKING_IMG_SIZE
    font = ImageFont.truetype(font_path, size=10)
    lines = get_multiline_wrapped_text(player.name, RANKING_IMG_SIZE, font)
    for j, line in enumerate(lines):
        y = y + j*12
        draw_wrapped_text(image, coord_x, y, RANKING_IMG_SIZE, 12, line, font_path, 10, 'rgb(0,0,0)')

    draw.rectangle((coord_x, coord_y, coord_x + RANKING_AVATAR_SIZE, coord_y + RANKING_AVATAR_SIZE), outline='rgb(0,0,0)')
    draw_player(image, tweet, player, coord_x + int(RANKING_AVATAR_SIZE / 2), coord_y + int(RANKING_AVATAR_SIZE / 2), False, True)

    if player.kills > 0:
        paste_image(image, coord_x + int(RANKING_AVATAR_SIZE / 2) - 4, coord_y - 10, 32, 'skull')
        draw.text((coord_x + int(RANKING_AVATAR_SIZE / 2) + 4, coord_y - 17), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_attack() != 0:
        paste_image(image, coord_x + int(RANKING_AVATAR_SIZE / 5), coord_y - 30, 32, 'attack')
        draw.text((coord_x + int(RANKING_AVATAR_SIZE / 5) + 6, coord_y - 35), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

    if player.get_defense() != 0:
        paste_image(image, coord_x + 2 * int(RANKING_AVATAR_SIZE / 3), coord_y - 30, 32, 'defense')
        draw.text((coord_x + 2 * int(RANKING_AVATAR_SIZE / 3) + 10, coord_y - 35), str(player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

def draw_ranking_rectangle(fill_color, fill_color_dark, players_count, row_index, col_index, index):
    draw = ImageDraw.Draw(image)

    players_in_rectangle = players_count - index

    if players_in_rectangle > RANKING_IMGS_PER_ROW:
        players_in_rectangle = RANKING_IMGS_PER_ROW

    x_0 = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index) - RANKING_SPACE_BETWEEN_DISTRICTS / 2
    x_1 = x_0 + (RANKING_DELTA_X * players_in_rectangle) - RANKING_SPACE_BETWEEN_DISTRICTS
    y_0 = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index) - RANKING_IMG_SIZE
    y_1 = y_0 + RANKING_IMG_SIZE + (RANKING_IMG_SIZE * 4 / 3)

    if index >= RANKING_IMGS_PER_ROW:
        # multirow
        y_0 = y_0 - (RANKING_PADDING / 2) - RANKING_DISTRICT_NAME_HEIGHT
        draw.rectangle((x_0, y_0 + 1, x_1, y_1), outline='rgb(0,0,0)', fill=fill_color, width=1)
        draw.rectangle((x_0 + 1, y_0, x_1 - 1, y_0 + 1), fill=fill_color)
    else:
        draw.rectangle((x_0, y_0, x_1, y_1), outline='rgb(0,0,0)', fill=fill_color, width=1)
        draw.rectangle((x_0, y_0 - RANKING_DISTRICT_NAME_HEIGHT, x_1, y_0), outline='rgb(0,0,0)', fill=fill_color_dark, width=1)

def draw_place_name(name, row_index, col_index, cols_width, current_index):
    draw = ImageDraw.Draw(image)
    coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index) - int(RANKING_SPACE_BETWEEN_DISTRICTS / 2)
    coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index) - RANKING_IMG_SIZE - RANKING_DISTRICT_NAME_HEIGHT
    font = ImageFont.truetype(font_path, size=10)

    lines = get_multiline_wrapped_text(name, RANKING_DELTA_X, font)
    for j, line in enumerate(lines):
        y = coord_y + j*12
        draw_wrapped_text(image, coord_x, y, RANKING_IMG_SIZE + RANKING_SPACE_BETWEEN_DISTRICTS, int((RANKING_DISTRICT_NAME_HEIGHT-2)/len(lines)), line, font_path, 10, 'rgb(0,0,0)')

    if current_index > 0:
        # dots
        x_0 = coord_x - RANKING_PADDING/2 + 3
        x_1 = coord_x - RANKING_PADDING/2 + 5
        y_0 = coord_y + RANKING_DISTRICT_NAME_HEIGHT / 2 - 1
        y_1 = coord_y + RANKING_DISTRICT_NAME_HEIGHT / 2 + 1
        draw.ellipse((x_0, y_0, x_1, y_1), fill='rgb(0,0,0)')

def draw_player_list_ranking(players_in_district, row_index, col_index, draw_rectangles = False, dead_area = False):
    first_line = True
    fill_color, fill_color_dark = get_fill_colors(players_in_district)

    for i, player in enumerate(players_in_district):
        if draw_rectangles:
            if i % RANKING_IMGS_PER_ROW == 0:
                draw_ranking_rectangle(fill_color, fill_color_dark, len(players_in_district), row_index, col_index, i)
                if i == 0:
                    cols_width = len(players_in_district)
                    if cols_width > RANKING_IMGS_PER_ROW:
                        cols_width = RANKING_IMGS_PER_ROW
            if first_line:
                draw_place_name(player.district.district_display_name, row_index, col_index, cols_width, i)

        draw_player_ranking(player, row_index, col_index, dead_area)
        col_index = col_index + 1

        if col_index + 1 > RANKING_IMGS_PER_ROW:
            first_line = False
            col_index = 0
            row_index = row_index + 1

    return row_index, col_index

def circle_players(players_to_circle):
    draw = ImageDraw.Draw(image)
    col_index = 0
    row_index = 0
    dead_area = False

    for i, player in enumerate(players_to_circle):
        if MATCH_TYPE == Match_type.districts and MAX_TRIBUTES_PER_DISTRICT > 0 and not dead_area and player.state == 0:
            col_index = 0
            row_index = row_index + 1
            dead_area = True

        if (tweet.player != None and player.get_name() == tweet.player.get_name()) or (tweet.player_2 != None and player.get_name() == tweet.player_2.get_name()) or (tweet.type == Tweet_type.atraction and any(x for x in tweet.player_list if x.get_name() == player.get_name())):
            coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index)
            coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index)
            if dead_area:
                alive_rows = math.ceil(len(get_alive_players()) / RANKING_IMGS_PER_ROW)
                dead_rows = row_index + 1 - alive_rows
                coord_y = coord_y - dead_rows * int(RANKING_SPACE_BETWEEN_ROWS/3)
            else:
                coord_y = coord_y - RANKING_DISTRICT_NAME_HEIGHT

            draw.ellipse((coord_x - RANKING_IMG_SIZE, coord_y - RANKING_IMG_SIZE, coord_x + RANKING_IMG_SIZE * 2, coord_y + RANKING_IMG_SIZE * 2), outline='rgb(255,0,0)', width=5)

        col_index = col_index + 1

        if col_index + 1 > RANKING_IMGS_PER_ROW:
            col_index = 0
            row_index = row_index + 1

def cross_district_if_needed(tributes):
    count = 0
    for j, tribute in enumerate(tributes):
        if tribute == '' or tribute.state == 0:
            count = count + 1
    if count == len(tributes):
        draw.line((coord_x - 205, coord_y - 40, coord_x, coord_y + 60), fill='rgb(255,0,0)', width=5)

def get_district_list():
    player_list_by_district = sorted(player_list, key=lambda x: x.district.name, reverse=False)

    if not limitless_districts:
        return [player_list_by_district[x:x+MAX_TRIBUTES_PER_DISTRICT] for x in range(0, len(player_list_by_district), MAX_TRIBUTES_PER_DISTRICT)]
    else:
        # dead players are shown below the rest
        district_list = []

        for i,loc in enumerate(place_list):
            temp_list = []
            for j,pl in enumerate(player_list_by_district):
                if pl.district.name == loc.name and pl.state == 1:
                    temp_list.append(pl)
            if len(temp_list) > 0:
                district_list.append(temp_list)

        return sorted(district_list, key=lambda x: sum(1 for y in x if y != '' and y.state == 1), reverse=True)

def choose_fitting_district(district_list, row_index, col_index):
    for i, d in enumerate(district_list):
        if (col_index == 0 and len(d) > RANKING_IMGS_PER_ROW) or (len(d) <= RANKING_IMGS_PER_ROW - col_index):
            return d
    return district_list[0]

def get_fill_colors(players_in_district):
    alive_count = sum(1 for y in players_in_district if y != '' and y.state == 1)
    if alive_count == 0:
        return 'rgb(255, 196, 176)', 'rgb(191, 124, 101)'
    elif alive_count == 1:
        return 'rgb(255, 225, 176)', 'rgb(219, 178, 112)'
    elif alive_count == 2:
        return 'rgb(248, 255, 176)', 'rgb(195, 204, 100)'
    else:
        return 'rgb(206, 255, 176)', 'rgb(142, 204, 104)'
