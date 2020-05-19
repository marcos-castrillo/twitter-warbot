#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import math
from PIL import Image, ImageDraw, ImageFont

from data.literals import get_message
from data.config import *

from models.tweet_type import Tweet_type
from store import place_list, player_list, get_alive_players, get_dead_players

date = datetime.datetime.now()
time_stamp = u'-'.join([str(date.year), str(date.month), str(date.day), str(date.hour), str(date.minute)])
current_dir = os.path.abspath(os.path.dirname(__file__))
output_dir = os.path.join(current_dir, '../simulations', time_stamp)
font_path = os.path.join(current_dir, '../assets/fonts/Comic-Sans.ttf')
font_path_2 = os.path.join(current_dir, '../assets/fonts/Arial.ttf')

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

def write_tweet(tweet):
    global line_number

    if tweet.type == Tweet_type.destroyed_district:
        line_number = line_number - 1

    write_line(get_message(tweet))
    draw_image(tweet)

    line_number = line_number + 1
    if tweet.type == Tweet_type.winner or tweet.type == Tweet_type.winner_districts:
        with open(os.path.join(output_dir, '-1_image.txt'), "w") as file:
            file.write('todo ok')
        with open(os.path.join(output_dir, '-1_line.txt'), "w") as file:
            file.write('todo ok')

def write_line(message):
    print(str(line_number) + u': ' + message.decode('utf-8'))

    with open(os.path.join(path), "a+", encoding="utf-8") as file:
        file.write(message.decode('utf-8'))

def file_len():
    with open(os.path.join(path)) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def paste_image(image, x, y, dimension, image_name, image_dir = None):
    if image_dir == None and os.path.exists(os.path.join(current_dir, '../assets/img/' + LOCALIZATION + '/' + image_name + '.png')):
        image_dir = '../assets/img/' + LOCALIZATION + '/' + image_name
    elif image_dir == None:
        image_dir = '../assets/img/' + image_name
    else:
        image_dir = '../' + image_dir

    image_to_paste = Image.open(os.path.join(current_dir, image_dir + '.png'))
    image_to_paste.thumbnail([dimension, dimension])
    side = int(dimension / 2)

    image.paste(image_to_paste, (x - side, y - side, x + side, y + side), image_to_paste.convert('RGBA'))

def draw_image(tweet):
    global line_number, current_dir
    raw_map_img = draw_places(Image.open(os.path.join(current_dir, '../assets/img/maps/' + LOCALIZATION + '.png')))
    raw_map_img_2 = draw_places(Image.open(os.path.join(current_dir, '../assets/img/maps/' + LOCALIZATION + '.png')))
    rows = math.ceil(len(player_list) / RANKING_IMGS_PER_ROW)
    RANKING_HEIGHT = 2*(rows * RANKING_SPACE_BETWEEN_ROWS + RANKING_PADDING * 2)
    blank_img = Image.new('RGB', (RANKING_WIDTH, RANKING_HEIGHT), color = BG_COLOR)

    main_image = None
    map_image = None
    ranking_image = None

    if tweet.type == Tweet_type.start:
        map_image = get_map_image(raw_map_img_2, tweet)
        ranking_image = get_ranking_image(blank_img, tweet)

        map_image.save(output_dir + '/' + str(line_number) + '_map.png')
        ranking_image.save(output_dir + '/' + str(line_number) + '_ranking.png')
    elif tweet.type == Tweet_type.introduce_players:
        map_image = get_map_image(raw_map_img_2, tweet)
        map_image.save(output_dir + '/' + str(line_number) + '_map.png')
    elif tweet.type == Tweet_type.destroyed_district:
        main_image = get_main_image(raw_map_img, tweet)
        map_image = get_map_image(raw_map_img_2, tweet)
        ranking_image = get_ranking_image(blank_img, tweet)

        main_image.save(output_dir + '/' + str(line_number) + '_bis.png')
        map_image.save(output_dir + '/' + str(line_number) + '_map_bis.png')
        ranking_image.save(output_dir + '/' + str(line_number) + '_ranking_bis.png')
    else:
        main_image = get_main_image(raw_map_img, tweet)
        map_image = get_map_image(raw_map_img_2, tweet)
        ranking_image = get_ranking_image(blank_img, tweet)

        main_image.save(output_dir + '/' + str(line_number) + '.png')
        map_image.save(output_dir + '/' + str(line_number) + '_map.png')
        ranking_image.save(output_dir + '/' + str(line_number) + '_ranking.png')

def draw_places(image):
    for i, p in enumerate(place_list):
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path_2, size=10)
        lines = get_multiline_wrapped_text(p.name, 50, font)
        for j, line in enumerate(lines):
            color = 'rgb(0,0,0)'
            if p.destroyed:
                color = 'rgb(255,0,0)'
            draw.text((p.coord_x + 25, p.coord_y + - 10 + j * 10), line, fill=color, font=font)
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 60, 'destroyed')
        else:
            paste_image(image, p.coord_x, p.coord_y, 38, 'place')
    return image

def get_main_image(image, tweet):
    draw = ImageDraw.Draw(image)
    image.putalpha(128)  # Half alpha; alpha argument must be an int

    for i, p in enumerate(place_list):
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 60, 'destroyed')
        else:
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + 24, 48, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 12, 48, 'monster')
            if p.infected:
                paste_image(image, p.coord_x + 12, p.coord_y, 48, 'infection')

            draw_items(len(p.items), p.coord_x, p.coord_y, image, True)

    if USE_DISTRICTS and (tweet.type == Tweet_type.introduce_players or tweet.type == Tweet_type.destroyed_district or tweet.type == Tweet_type.winner_districts or tweet.type == Tweet_type.atraction):
        if USE_FLAGS:
            dimension_1 = 424
            dimension_2 = 286
            image_to_paste = Image.open(os.path.join(current_dir, '../assets/img/flags/' + LOCALIZATION + '/' + tweet.place.district_display_name + '.jpg'))
            image_to_paste.thumbnail([dimension_1/2, dimension_2/2])
            image.paste(image_to_paste, (tweet.place.coord_x - 100, tweet.place.coord_y - 130), image_to_paste.convert('RGBA'))

        draw_items(len(tweet.place.items), tweet.place.coord_x, tweet.place.coord_y, image)

    if tweet.type == Tweet_type.somebody_suicided or tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.trapped or tweet.type == Tweet_type.somebody_died_of_infection:
        paste_image(image, tweet.place.coord_x, tweet.place.coord_y, 48, '', tweet.player.avatar_dir)
        draw.text((tweet.place.coord_x - 6, tweet.place.coord_y - 39), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
    elif tweet.type == Tweet_type.winner or tweet.type == Tweet_type.somebody_got_injured or tweet.type == Tweet_type.somebody_got_special or tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item or tweet.type == Tweet_type.somebody_revived or tweet.type == Tweet_type.somebody_moved or tweet.type == Tweet_type.trap or tweet.type == Tweet_type.trap_dodged or tweet.type == Tweet_type.somebody_powerup or tweet.type == Tweet_type.somebody_was_infected:
        paste_image(image, tweet.place.coord_x, tweet.place.coord_y, 48, '', tweet.player.avatar_dir)
        if tweet.player.infected:
            paste_image(image, tweet.place.coord_x + 24, tweet.place.coord_y + 12, 36, 'infection')
    elif tweet.type == Tweet_type.destroyed or tweet.type == Tweet_type.destroyed_district or tweet.type == Tweet_type.winner_districts:
        draw_multiple_players(tweet, tweet.player_list, tweet.place.coord_x, tweet.place.coord_y, image, 50)
        if tweet.place_2 != None:
            draw_multiple_players(tweet, tweet.player_list_2, tweet.place_2.coord_x, tweet.place_2.coord_y, image, 50)
    elif tweet.type == Tweet_type.introduce_players:
        if len(tweet.player_list) == 1:
            paste_image(image, tweet.place.coord_x, tweet.place.coord_y, 48, '', tweet.player_list[0].avatar_dir)
        elif len(tweet.player_list) == 2:
            paste_image(image, tweet.place.coord_x - 25, tweet.place.coord_y, 48, '', tweet.player_list[0].avatar_dir)
            paste_image(image, tweet.place.coord_x + 25, tweet.place.coord_y, 48, '', tweet.player_list[1].avatar_dir)
        elif len(tweet.player_list) == 3:
                paste_image(image, tweet.place.coord_x - 50, tweet.place.coord_y, 48, '', tweet.player_list[0].avatar_dir)
                paste_image(image, tweet.place.coord_x, tweet.place.coord_y, 48, '', tweet.player_list[1].avatar_dir)
                paste_image(image, tweet.place.coord_x + 50, tweet.place.coord_y, 48, '', tweet.player_list[2].avatar_dir)

        if len(tweet.player_list_2) > 0:
            draw_multiple_players(tweet, tweet.player_list_2, tweet.place.coord_x, tweet.place.coord_y + 140, image, 50)

            if tweet.inverse:
                paste_image(image, tweet.place.coord_x, tweet.place.coord_y + 70, 128, 'merge')
            else:
                paste_image(image, tweet.place.coord_x, tweet.place.coord_y + 70, 128, 'split')

    elif tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_escaped or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.somebody_stole or tweet.type == Tweet_type.somebody_stole_and_threw or tweet.type == Tweet_type.somebody_stole_and_replaced:
        if tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_escaped or tweet.type == Tweet_type.somebody_killed:
            color_1 = 'rgb(255,0,0)'
            color_2 = 'rgb(0,0,255)'
            color_tie = 'rgb(127,0,127)'
            color_tie_1 = 'rgb(192,0,64)'
            color_tie_2 = 'rgb(64,0,192)'
            color_arrow = 'rgb(59,249,0)'

            if not tweet.type == Tweet_type.somebody_escaped:
                tweet.place_2 = tweet.place

            if tweet.new_item != None:
                # Stole
                if tweet.inverse:
                    att_player_1 = tweet.player.get_attack() + tweet.new_item.attack
                    def_player_1 = tweet.player.get_defense() + tweet.new_item.defense
                    att_player_2 = tweet.player_2.get_attack() - tweet.new_item.attack
                    def_player_2 = tweet.player_2.get_defense() - tweet.new_item.defense
                else:
                    att_player_1 = tweet.player.get_attack() - tweet.new_item.attack
                    def_player_1 = tweet.player.get_defense() - tweet.new_item.defense
                    att_player_2 = tweet.player_2.get_attack() + tweet.new_item.attack
                    def_player_2 = tweet.player_2.get_defense() + tweet.new_item.defense

                if tweet.old_item != None:
                    # Throw away
                    if tweet.inverse:
                        att_player_2 = att_player_2 + tweet.old_item.attack
                        def_player_2 = def_player_2 + tweet.old_item.defense
                    else:
                        att_player_1 = att_player_1 + tweet.old_item.attack
                        def_player_1 = def_player_1 + tweet.old_item.defense
            else:
                att_player_1 = tweet.player.get_attack()
                def_player_1 = tweet.player.get_defense()
                att_player_2 = tweet.player_2.get_attack()
                def_player_2 = tweet.player_2.get_defense()

            #avatar player_1
            paste_image(image, tweet.player.location.coord_x - 28, tweet.player.location.coord_y, 48, '', tweet.player.avatar_dir)
            draw.rectangle((tweet.player.location.coord_x - 55, tweet.player.location.coord_y - 28, tweet.player.location.coord_x - 1, tweet.player.location.coord_y + 27), outline=color_1, width=4)
            #avatar player_2
            paste_image(image, tweet.player_2.location.coord_x + 28, tweet.player_2.location.coord_y, 48, '', tweet.player_2.avatar_dir)
            draw.rectangle((tweet.player_2.location.coord_x, tweet.player_2.location.coord_y - 28, tweet.player_2.location.coord_x + 55, tweet.player_2.location.coord_y + 27), outline=color_2, width=4)
            #stats player_1
            draw.rectangle((tweet.player.location.coord_x - 110, tweet.player.location.coord_y - 25, tweet.player.location.coord_x - 60, tweet.player.location.coord_y + 25), fill='rgb(255,255,255)')
            paste_image(image, tweet.player.location.coord_x - 98, tweet.player.location.coord_y - 10, 32, 'attack')
            paste_image(image, tweet.player.location.coord_x - 98, tweet.player.location.coord_y + 12, 32, 'defense')
            draw.text((tweet.player.location.coord_x - 85, tweet.player.location.coord_y - 22), str(att_player_1), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
            draw.text((tweet.player.location.coord_x - 85, tweet.player.location.coord_y), str(def_player_1), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
            #stats player_2
            draw.rectangle((tweet.player_2.location.coord_x + 110, tweet.player_2.location.coord_y - 25, tweet.player_2.location.coord_x + 60, tweet.player_2.location.coord_y + 25), fill='rgb(255,255,255)')
            paste_image(image, tweet.player_2.location.coord_x + 72, tweet.player_2.location.coord_y - 10, 32, 'attack')
            paste_image(image, tweet.player_2.location.coord_x + 72, tweet.player_2.location.coord_y + 12, 32, 'defense')
            draw.text((tweet.player_2.location.coord_x + 85, tweet.player_2.location.coord_y - 22), str(att_player_2), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
            draw.text((tweet.player_2.location.coord_x + 85, tweet.player_2.location.coord_y), str(def_player_2), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
        elif tweet.type == Tweet_type.somebody_stole or tweet.type == Tweet_type.somebody_stole_and_threw or tweet.type == Tweet_type.somebody_stole_and_replaced:
            paste_image(image, tweet.player.location.coord_x - 28, tweet.player.location.coord_y, 48, '', tweet.player.avatar_dir)
            paste_image(image, tweet.player_2.location.coord_x + 28, tweet.player_2.location.coord_y, 48, '', tweet.player_2.avatar_dir)

        if tweet.player.infected:
            paste_image(image, tweet.player.location.coord_x - 28 + 24, tweet.player.location.coord_y + 12, 36, 'infection')
        if tweet.player_2.infected:
            paste_image(image, tweet.player_2.location.coord_x + 28 + 24, tweet.player_2.location.coord_y + 12, 36, 'infection')
        if tweet.player.state == 0:
            draw.text((tweet.player.location.coord_x - 56, tweet.player.location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
        if tweet.player_2.state == 0:
            draw.text((tweet.player_2.location.coord_x + 8, tweet.player_2.location.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
    elif tweet.type == Tweet_type.atraction:
        draw_multiple_players(tweet, tweet.player_list, tweet.place.coord_x, tweet.place.coord_y, image, 50)

    if tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.somebody_escaped:
        min = tweet.place.coord_x - 100
        max = tweet.place.coord_x + 100
        action_number = min + tweet.action_number * 2

        tie = min + 2*(tweet.factor)

        min_tie = min + 2*(tweet.factor - PROBAB_TIE)
        if min_tie < min:
            min_tie = min
        elif min_tie > max:
            min_tie = max

        max_tie = min_tie + 4*PROBAB_TIE
        if max_tie < min:
            max_tie = min
        elif max_tie > max:
            max_tie = max
        #progress bar
        draw.rectangle((min - 2, tweet.place.coord_y - 77, max + 2, tweet.place.coord_y - 48), outline='rgb(255,255,255)', width=4)
        draw.rectangle((min, tweet.place.coord_y - 75, min_tie, tweet.place.coord_y - 50), fill=color_1)
        draw.rectangle((max_tie, tweet.place.coord_y - 75, max, tweet.place.coord_y - 50), fill=color_2)
        draw.rectangle((min_tie, tweet.place.coord_y - 75, tie, tweet.place.coord_y - 50), fill=color_tie_1)
        draw.rectangle((tie, tweet.place.coord_y - 75, max_tie, tweet.place.coord_y - 50), fill=color_tie_2)
        draw.rectangle((tie - 1, tweet.place.coord_y - 75, tie + 1, tweet.place.coord_y - 50), fill=color_tie)

        #action_number
        draw.rectangle((action_number - 1, tweet.place.coord_y - 75, action_number + 1, tweet.place.coord_y - 50), fill=color_arrow)
        paste_image(image, action_number, tweet.place.coord_y - 100, 72, 'arrow')

    w, h = image.size
    zoom = 3

    if tweet.place != None:
        if tweet.type == Tweet_type.winner:
            paste_image(image, tweet.place.coord_x, tweet.place.coord_y - 48, 72, 'crown')

        if tweet.type == Tweet_type.winner or tweet.type == Tweet_type.winner_districts:
            paste_image(image, tweet.place.coord_x, tweet.place.coord_y + 130, 248, 'winner')

        x = tweet.place.coord_x
        y = tweet.place.coord_y
        zoom2 = zoom * 2

        x_1 = x - w / zoom2
        x_2 = x + w / zoom2
        y_1 = y - h / zoom2
        y_2 = y + h / zoom2

        if x_1 < 0:
            x_2 = x_2 - x_1
            x_1 = 0
        if y_1 < 0:
            y_2 = y_2 - y_1
            y_1 = 0
        if x_2 > WIDTH_MAP:
            x_1 = x_1 - x_2 + WIDTH_MAP
            x_2 = WIDTH_MAP

        image = image.crop((x_1, y_1, x_2, y_2))
        image.resize((w, h), Image.LANCZOS)

    if tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item:
        if tweet.item.get_rarity() == 1:
            paste_image(image, 80, 80, 256, 'weapon_1')
        elif tweet.item.get_rarity() == 2:
            paste_image(image, 80, 80, 256, 'weapon_2')
        elif tweet.item.get_rarity() == 3:
            paste_image(image, 80, 80, 256, 'weapon_3')
    elif tweet.type == Tweet_type.somebody_got_injured:
        paste_image(image, 80, 80, 256, 'injure')
    elif tweet.type == Tweet_type.somebody_got_special:
        if tweet.item.get_rarity() == 1:
            paste_image(image, 80, 80, 256, 'special_1')
        elif tweet.item.get_rarity() == 2:
            paste_image(image, 80, 80, 256, 'special_2')
        elif tweet.item.get_rarity() == 3:
            paste_image(image, 80, 80, 256, 'special_3')
    elif tweet.type == Tweet_type.somebody_powerup:
        if tweet.item.get_rarity() == 1:
            paste_image(image, 80, 80, 256, 'powerup_1')
        elif tweet.item.get_rarity() == 2:
            paste_image(image, 80, 80, 256, 'powerup_2')
        elif tweet.item.get_rarity() == 3:
            paste_image(image, 80, 80, 256, 'powerup_3')
    elif tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend:
        paste_image(image, 80, 80, 256, 'heart')
    elif tweet.type == Tweet_type.monster_moved or tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.monster_appeared or tweet.type == Tweet_type.monster_disappeared:
        paste_image(image, 80, 80, 256, 'monster')
    elif tweet.type == Tweet_type.trap_dodged or tweet.type == Tweet_type.trapped or tweet.type == Tweet_type.trap:
        paste_image(image, 80, 80, 256, 'trap')
    elif tweet.type == Tweet_type.somebody_moved:
        paste_image(image, 80, 80, 256, 'move')
    elif tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.somebody_suicided:
        paste_image(image, 80, 80, 256, 'skull')
    elif tweet.type == Tweet_type.somebody_revived:
        paste_image(image, 80, 80, 256, 'revive')
    elif tweet.type == Tweet_type.somebody_stole or tweet.type == Tweet_type.somebody_stole_and_threw or tweet.type == Tweet_type.somebody_stole_and_replaced:
        paste_image(image, 80, 80, 256, 'steal')
    elif tweet.type == Tweet_type.somebody_escaped:
        paste_image(image, 80, 80, 256, 'runaway')
    elif tweet.type == Tweet_type.destroyed or tweet.type == Tweet_type.destroyed_district:
        paste_image(image, 80, 80, 256, 'destroyed')
    elif tweet.type == Tweet_type.somebody_was_infected or tweet.type == Tweet_type.somebody_died_of_infection:
        paste_image(image, 80, 80, 256, 'infection')
    elif tweet.type == Tweet_type.atraction:
        paste_image(image, 80, 80, 256, 'atraction')

    return image

def get_map_image(image, tweet):
    draw = ImageDraw.Draw(image)

    for i, p in enumerate(place_list):
        if not p.destroyed:
            draw_items(len(p.items), p.coord_x, p.coord_y, image)

    for i, place in enumerate(place_list):
        draw_multiple_players(tweet, place.players, place.coord_x, place.coord_y, image, WIDTH_BETWEEN_PLAYERS, PLAYERS_IN_SINGLE_LINE)

    if tweet.place != None:
        draw.ellipse((tweet.place.coord_x - 75, tweet.place.coord_y - 75, tweet.place.coord_x + 75, tweet.place.coord_y + 75), outline='rgb(255,0,0)', width=5)
        ellipse = Image.new('RGBA', image.size, (255,255,255,0))
        d = ImageDraw.Draw(ellipse)
        d.ellipse((tweet.place.coord_x - 2000, tweet.place.coord_y - 2000, tweet.place.coord_x + 2000, tweet.place.coord_y + 2000), outline=(255,255,255,100), width=1925)
        image = Image.alpha_composite(image, ellipse)
        draw = ImageDraw.Draw(image)

    for i, p in enumerate(place_list):
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 100, 'destroyed')
        else:
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + 24, 48, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 12, 48, 'monster')

    return image

def get_ranking_image(image, tweet):
    limitless_districts = MAX_TRIBUTES_PER_DISTRICT == 0
    row_index = 0
    col_index = 0

    def draw_player_ranking(player, row_index, col_index):
        draw = ImageDraw.Draw(image)

        coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index)
        coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index)

        paste_image(image, coord_x + 24, coord_y + 24, 48, '', player.avatar_dir)
        draw_wrapped_text(image, coord_x, coord_y + 50, RANKING_IMG_SIZE, player.name, font_path, 10, 'rgb(0,0,0)')
        draw.rectangle((coord_x, coord_y, coord_x + 48, coord_y + 48), outline='rgb(0,0,0)')

        if player.kills > 0:
            paste_image(image, coord_x + 20, coord_y - 10, 32, 'skull')
            draw.text((coord_x + 27, coord_y - 17), str(player.kills), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

        if player.get_attack() != 0:
            paste_image(image, coord_x + 8, coord_y - 30, 32, 'attack')
            draw.text((coord_x + 14, coord_y - 35), str(player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

        if player.get_defense() != 0:
            paste_image(image, coord_x + 34, coord_y - 30, 32, 'defense')
            draw.text((coord_x + 42, coord_y - 35), str(player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path, size=10))

        if player.state == 0:
            draw.text((coord_x - 7, coord_y - 35), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=70))
        else:
            if player.infected:
                paste_image(image, coord_x + 24 + 24, coord_y + 24 + 12, 36, 'infection')
            if len(player.item_list) == 2:
                paste_image(image, coord_x + 5, coord_y + 5, 32, get_item_rarity(player.item_list[1]))
            if len(player.item_list) > 0:
                paste_image(image, coord_x + 5, coord_y + 5, 32, get_item_rarity(player.item_list[0]))
            if player.injure_immunity:
                paste_image(image, coord_x, coord_y + 48, 32, 'special')
            if player.monster_immunity:
                paste_image(image, coord_x, coord_y + 36, 32, 'special')
            if player.infection_immunity:
                paste_image(image, coord_x, coord_y + 24, 32, 'special')

    def draw_ranking_rectangle(players_count, row_index, col_index, index):
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
            y_0 = y_0 - (RANKING_PADDING / 2)
            draw.rectangle((x_0, y_0 + 1, x_1, y_1), outline='rgb(0,0,0)', fill=fill_color, width=1)
            draw.rectangle((x_0 + 1, y_0, x_1 - 1, y_0 + 1), fill=fill_color)
        else:
            draw.rectangle((x_0, y_0, x_1, y_1), outline='rgb(0,0,0)', fill=fill_color, width=1)

    def draw_district_name(name, row_index, col_index, cols_width):
        draw = ImageDraw.Draw(image)
        coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index) - RANKING_SPACE_BETWEEN_DISTRICTS / 2
        coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index) - RANKING_IMG_SIZE
        font = ImageFont.truetype(font_path, size=10)

        lines = get_multiline_wrapped_text(name.upper(), RANKING_DELTA_X - 4, font)
        for j, line in enumerate(lines):
            draw_wrapped_text(image, coord_x + 1, coord_y + 1 + j*10, RANKING_IMG_SIZE - 4, line, font_path, 10, 'rgb(0,0,0)')

    def draw_player_list_ranking(list, row_index, col_index, draw_rectangles = False):
        for i, player in enumerate(list):
            if draw_rectangles and i % RANKING_IMGS_PER_ROW == 0:
                draw_ranking_rectangle(len(list), row_index, col_index, i)
                if i == 0:
                    cols_width = len(list)
                    if cols_width > RANKING_IMGS_PER_ROW:
                        cols_width = RANKING_IMGS_PER_ROW
                    draw_district_name(player.district.district_display_name, row_index, col_index, cols_width)
            draw_player_ranking(player, row_index, col_index)
            col_index = col_index + 1

            if col_index + 1 > RANKING_IMGS_PER_ROW:
                col_index = 0
                row_index = row_index + 1

        return row_index, col_index

    def circle_players(image, players_to_circle):
        draw = ImageDraw.Draw(image)
        col_index = 0
        row_index = 0

        for i, player in enumerate(players_to_circle):
            if (tweet.player != None and player.get_name() == tweet.player.get_name()) or (tweet.player_2 != None and player.get_name() == tweet.player_2.get_name()):
                coord_x = RANKING_FIRST_COLUMN_X + (RANKING_DELTA_X * col_index)
                coord_y = RANKING_FIRST_ROW_Y + (RANKING_SPACE_BETWEEN_ROWS * row_index)
                draw.ellipse((coord_x - 50, coord_y - 50, coord_x + 100, coord_y + 100), outline='rgb(255,0,0)', width=5)

            col_index = col_index + 1

            if col_index + 1 > RANKING_IMGS_PER_ROW:
                col_index = 0
                row_index = row_index + 1

    if USE_DISTRICTS:
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

        def get_fill_color(players_in_district):
            alive_count = sum(1 for y in players_in_district if y != '' and y.state == 1)
            if alive_count == 0:
                return 'rgb(255, 196, 176)'
            elif alive_count == 1:
                return 'rgb(255, 225, 176)'
            elif alive_count == 2:
                return 'rgb(248, 255, 176)'
            else:
                return 'rgb(206, 255, 176)'

        def cross_district_if_needed(tributes):
            count = 0
            for j, tribute in enumerate(tributes):
                if tribute == '' or tribute.state == 0:
                    count = count + 1
            if count == len(tributes):
                draw.line((coord_x - 205, coord_y - 40, coord_x, coord_y + 60), fill='rgb(255,0,0)', width=5)

        district_list = get_district_list()
        drawn_player_list = []

        while len(district_list) > 0:
            players_in_district = choose_fitting_district(district_list, row_index, col_index)
            players_count = len(players_in_district)
            fill_color = get_fill_color(players_in_district)

            row_index, col_index = draw_player_list_ranking(players_in_district, row_index, col_index, True)

            if not limitless_districts:
                cross_district_if_needed(players_in_district)

            drawn_player_list = drawn_player_list + players_in_district
            district_list.pop(district_list.index(players_in_district))

        # Breakline
        col_index = 0
        row_index = row_index + 1
        dead_players = get_dead_players()
        row_index, col_index = draw_player_list_ranking(dead_players, row_index, col_index)
        drawn_player_list = drawn_player_list + dead_players

    else:
        alive_players_list = get_alive_players()
        dead_players_list = get_dead_players()
        drawn_player_list = alive_players_list + dead_players_list

        row_index, col_index = draw_player_list_ranking(alive_players_list, row_index, col_index)
        row_index, col_index = draw_player_list_ranking(dead_players_list, row_index, col_index)

    circle_players(image, drawn_player_list)

    return image

def calculate_coords(coord_x, coord_y, dead = False):
    delta_x = RANKING_IMG_SIZE + RANKING_SPACE_BETWEEN_COLS
    limit_x = RANKING_FIRST_COLUMN_X + RANKING_IMGS_PER_ROW * delta_x
    if coord_x + delta_x >= limit_x:
        #breakline
        coord_x = RANKING_FIRST_COLUMN_X
        if dead:
            coord_y = coord_y + RANKING_SPACE_BETWEEN_ROWS - (RANKING_PADDING + int(RANKING_PADDING/2))
        else:
            coord_y = coord_y + RANKING_SPACE_BETWEEN_ROWS
    else:
        coord_x = coord_x + delta_x

    return coord_x, coord_y

def draw_items(items_count, coord_x, coord_y, image, transparent = False):
    if transparent:
        item_img = 'item_transparent'
    else:
        item_img = 'item'

    if items_count == 1:
        paste_image(image, coord_x, coord_y - 26, 48, item_img)
    elif items_count == 2:
        paste_image(image, coord_x - 12, coord_y - 26, 48, item_img)
        paste_image(image, coord_x + 12, coord_y - 26, 48, item_img)
    else:
        while items_count > 0:
            if items_count <= 3:
                y = coord_y - 26
                paste_image(image, coord_x - 48 + items_count * 24, y, 48, item_img)
            else:
                y = coord_y - 26 - 10
                paste_image(image, coord_x - 48 + (items_count - 3) * 24, y, 48, item_img)
            items_count = items_count - 1

def draw_multiple_players(tweet, players, coord_x, coord_y, image, delta_x, single_line = False):
    draw = ImageDraw.Draw(image)
    if len(players) > 0:
        if len(players) == 1:
            paste_image(image, coord_x, coord_y, 48, '', players[0].avatar_dir)
            if players[0].state == 0:
                draw.text((coord_x - 30, coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
            elif players[0].infected:
                paste_image(image, coord_x + 24, coord_y + 12, 36, 'infection')
            if tweet.type == Tweet_type.winner_districts:
                paste_image(image, coord_x, coord_y - 48, 72, 'crown')
        elif len(players) == 2:
            paste_image(image, coord_x - int(delta_x/2), coord_y, 48, '', players[0].avatar_dir)
            if players[0].state == 0:
                draw.text((coord_x - 30 - int(delta_x/2), coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
            elif players[0].infected:
                paste_image(image, coord_x - int(delta_x/2) + 24, coord_y + 12, 36, 'infection')
            if tweet.type == Tweet_type.winner_districts:
                paste_image(image, coord_x - int(delta_x/2), coord_y - 48, 72, 'crown')

            paste_image(image, coord_x + int(delta_x/2), coord_y, 48, '', players[1].avatar_dir)
            if players[1].state == 0:
                draw.text((coord_x - 30 + int(delta_x/2), coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
            elif players[1].infected:
                paste_image(image, coord_x + int(delta_x/2) + 24, coord_y + 12, 36, 'infection')
            if tweet.type == Tweet_type.winner_districts:
                paste_image(image, coord_x + int(delta_x/2), coord_y - 48, 72, 'crown')

        elif single_line:
            x = coord_x - int(len(players)/2)*delta_x
            y = coord_y
            for i, player in enumerate(players):
                paste_image(image, x, y, 48, '', players[i].avatar_dir)
                if players[i].state == 0:
                    draw.text((x - 30, y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
                elif players[i].infected:
                    paste_image(image, x + 24, y + 12, 36, 'infection')
                if tweet.type == Tweet_type.winner_districts:
                    paste_image(image, x, y - 48, 72, 'crown')

                x = x + delta_x

        elif len(players) <= 12:
            x = coord_x - delta_x
            y = coord_y
            for i, player in enumerate(players):
                paste_image(image, x, y, 48, '', players[i].avatar_dir)
                if players[i].state == 0:
                    draw.text((x - 30, y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
                elif players[i].infected:
                    paste_image(image, x + 24, y + 12, 36, 'infection')
                if tweet.type == Tweet_type.winner_districts:
                    paste_image(image, x, y - 48, 72, 'crown')

                x = x + delta_x
                if (i-4)%5 == 0:
                    x = coord_x - delta_x
                    y = y + HEIGHT_BETWEEN_PLAYERS
        else:
            x = coord_x - int(delta_x/2)*4
            y = coord_y
            for i, player in enumerate(players):
                paste_image(image, x, y, 24, '', players[i].avatar_dir)
                if players[i].state == 0:
                    draw.text((x - 30, y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
                elif players[i].infected:
                    paste_image(image, x + 24, y + 12, 36, 'infection')
                if tweet.type == Tweet_type.winner_districts:
                    paste_image(image, x, y - 48, 72, 'crown')

                x = x + int(delta_x/2)
                if (i-8)%9 == 0:
                    x = coord_x - int(delta_x/2)*4
                    y = y + int(HEIGHT_BETWEEN_PLAYERS / 2)

def draw_wrapped_text(image, coord_x, coord_y, max_width, text, font_path, initial_font_size, fill):
    draw = ImageDraw.Draw(image)
    font_size = initial_font_size
    font = ImageFont.truetype(font_path, size=font_size)
    w, h = font.getsize(text)

    while w >= max_width:
        font = ImageFont.truetype(font_path, size=font_size)
        w, h = font.getsize(text)
        font_size = font_size - 1
        coord_x = coord_x + 1
        coord_y = coord_y + 1

    new_font = ImageFont.truetype(font_path, size=font_size)
    draw.text((coord_x, coord_y), text, fill=fill, font=new_font)

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
