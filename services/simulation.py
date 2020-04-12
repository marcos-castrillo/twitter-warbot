#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import urllib.request
from PIL import Image, ImageDraw, ImageFont

from data.literals import get_message
from config import LOCALIZATION, PROBAB_TIE
from models.tweet_type import Tweet_type
from store import place_list, player_list, get_alive_players, get_dead_players

date = datetime.datetime.now()
time_stamp = u'-'.join([str(date.year), str(date.month), str(date.day), str(date.hour), str(date.minute)])
current_dir = os.path.abspath(os.path.dirname(__file__))
output_dir = os.path.join(current_dir, '../simulations', time_stamp)
font_path = os.path.join(current_dir, '../assets/fonts/Comic-Sans.ttf')
font_path_2 = os.path.join(current_dir, '../assets/fonts/Comic-Sans.ttf')

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

def initialize_avatars():
    path = 'assets/img/avatars'
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

def write_tweet(tweet):
    global line_number

    write_line(get_message(tweet))
    draw_image(tweet)

    line_number = line_number + 1
    if tweet.type == Tweet_type.winner:
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
    image = Image.open(os.path.join(current_dir, '../assets/img/' + image_name + '.png'))

    if size != None:
        return image.thumbnail(size)
    else:
        return image

def paste_image(image, x, y, dimension, image_name, image_dir = None):
    global current_dir

    if image_dir == None:
        image_dir = '../assets/img/' + image_name
    else:
        image_dir = '../' + image_dir

    image_to_paste = Image.open(os.path.join(current_dir, image_dir + '.png'))
    image_to_paste.thumbnail([dimension, dimension])
    side = int(dimension / 2)

    image.paste(image_to_paste, (x - side, y - side, x + side, y + side), image_to_paste.convert('RGBA'))

def draw_image(tweet):
    global line_number, current_dir
    image_1 = get_image('maps/' + LOCALIZATION)
    image_2 = get_image('maps/' + LOCALIZATION)

    if tweet.type == Tweet_type.start:
        summary_image = get_summary_image(image_2, tweet)
        summary_image.save(output_dir + '/' + str(line_number) + '.png')
    else:
        zoomed_image = get_zoomed_image(image_1, tweet)
        summary_image = get_summary_image(image_2, tweet)

        zoomed_image.save(output_dir + '/' + str(line_number) + '.png')
        summary_image.save(output_dir + '/' + str(line_number) + 'b.png')

def get_zoomed_image(image, tweet):
    draw = ImageDraw.Draw(image)
    image.putalpha(128)  # Half alpha; alpha argument must be an int

    for i, p in enumerate(place_list):
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 60, 'destroyed')
        else:
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + 16, 32, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 16, 32, 'monster')
            if p.infected:
                paste_image(image, p.coord_x + 16, p.coord_y, 32, 'infection')

    if tweet.type == Tweet_type.somebody_suicided or tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.trapped or tweet.type == Tweet_type.somebody_died_of_infection:
        paste_image(image, tweet.place.coord_x, tweet.place.coord_y, 48, '', tweet.player.avatar_dir)
        draw.text((tweet.place.coord_x - 12, tweet.place.coord_y - 39), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
    elif tweet.type == Tweet_type.winner or tweet.type == Tweet_type.somebody_got_injured or tweet.type == Tweet_type.somebody_got_special or tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item or tweet.type == Tweet_type.somebody_revived or tweet.type == Tweet_type.somebody_moved or tweet.type == Tweet_type.trap or tweet.type == Tweet_type.trap_dodged or tweet.type == Tweet_type.somebody_powerup or tweet.type == Tweet_type.somebody_was_infected:
        paste_image(image, tweet.place.coord_x, tweet.place.coord_y, 48, '', tweet.player.avatar_dir)
        if tweet.player.infected:
            paste_image(image, tweet.place.coord_x + 24, tweet.place.coord_y + 12, 36, 'infection')
    elif tweet.type == Tweet_type.destroyed:
        for i, p in enumerate(tweet.player_list):
            paste_image(image, tweet.place.coord_x + (i * 30) - 16, tweet.place.coord_y, 48, '', p.avatar_dir)
            if p.infected:
                paste_image(image, tweet.place.coord_x + (i * 30) - 16 + 24, tweet.place.coord_y + 12, 36, 'infection')
        if tweet.place_2 != None:
            for i, p in enumerate(tweet.player_list_2):
                paste_image(image, tweet.place_2.coord_x + (i * 30) - 16, tweet.place_2.coord_y, 48, '', p.avatar_dir)
                if p.infected:
                    paste_image(image, tweet.place_2.coord_x + (i * 30) - 16 + 24, tweet.place_2.coord_y + 12, 36, 'infection')
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
            elif tweet.inverse:
                a = tweet.place_2
                tweet.place_2 = tweet.place
                tweet.place = a

            #avatar player_1
            paste_image(image, tweet.place.coord_x - 28, tweet.place.coord_y, 48, '', tweet.player.avatar_dir)
            draw.rectangle((tweet.place.coord_x - 55, tweet.place.coord_y - 28, tweet.place.coord_x - 1, tweet.place.coord_y + 27), outline=color_1, width=4)
            #avatar player_2
            paste_image(image, tweet.place_2.coord_x + 28, tweet.place_2.coord_y, 48, '', tweet.player_2.avatar_dir)
            draw.rectangle((tweet.place_2.coord_x, tweet.place_2.coord_y - 28, tweet.place_2.coord_x + 55, tweet.place_2.coord_y + 27), outline=color_2, width=4)
            #stats player_1
            draw.rectangle((tweet.place.coord_x - 110, tweet.place.coord_y - 25, tweet.place.coord_x - 60, tweet.place.coord_y + 25), fill='rgb(255,255,255)')
            paste_image(image, tweet.place.coord_x - 98, tweet.place.coord_y - 10, 32, 'attack')
            paste_image(image, tweet.place.coord_x - 98, tweet.place.coord_y + 12, 32, 'defense')
            draw.text((tweet.place.coord_x - 85, tweet.place.coord_y - 22), str(tweet.player.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
            draw.text((tweet.place.coord_x - 85, tweet.place.coord_y), str(tweet.player.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
            #stats player_2
            draw.rectangle((tweet.place.coord_x + 110, tweet.place.coord_y - 25, tweet.place.coord_x + 60, tweet.place.coord_y + 25), fill='rgb(255,255,255)')
            paste_image(image, tweet.place.coord_x + 72, tweet.place.coord_y - 10, 32, 'attack')
            paste_image(image, tweet.place.coord_x + 72, tweet.place.coord_y + 12, 32, 'defense')
            draw.text((tweet.place.coord_x + 85, tweet.place.coord_y - 22), str(tweet.player_2.get_attack()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
            draw.text((tweet.place.coord_x + 85, tweet.place.coord_y), str(tweet.player_2.get_defense()), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))

        if tweet.player.infected:
            paste_image(image, tweet.place_2.coord_x - 28 + 24, tweet.place_2.coord_y + 12, 36, 'infection')
        if tweet.player_2.infected:
            paste_image(image, tweet.place.coord_x + 28 + 24, tweet.place.coord_y + 12, 36, 'infection')
        if tweet.player.state == 0:
            draw.text((tweet.place.coord_x - 56, tweet.place.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
        if tweet.player_2.state == 0:
            draw.text((tweet.place.coord_x + 8, tweet.place.coord_y - 36), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path, size=50))
    elif tweet.type == Tweet_type.atraction:
        for j, player in enumerate(tweet.player_list):
            paste_image(image, tweet.place.coord_x + (j * 24), tweet.place.coord_y, 48, '', player.avatar_dir)
            if player.infected:
                paste_image(image, tweet.place.coord_x + (j * 24) + 24, tweet.place.coord_y + 12, 36, 'infection')

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

        x = tweet.place.coord_x
        y = tweet.place.coord_y
        zoom2 = zoom * 2
        image = image.crop((x - w / zoom2, y - h / zoom2, x + w / zoom2, y + h / zoom2))
        image.resize((w, h), Image.LANCZOS)

    if tweet.type == Tweet_type.winner:
        paste_image(image, 80, 80, 256, 'winner')
    if tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item:
        if tweet.item.rarity == 1:
            paste_image(image, 80, 80, 256, 'weapon_1')
        elif tweet.item.rarity == 2:
            paste_image(image, 80, 80, 256, 'weapon_2')
        elif tweet.item.rarity == 3:
            paste_image(image, 80, 80, 256, 'weapon_3')
    elif tweet.type == Tweet_type.somebody_got_injured:
        paste_image(image, 80, 80, 256, 'injure')
    elif tweet.type == Tweet_type.somebody_got_special:
        if tweet.item.rarity == 1:
            paste_image(image, 80, 80, 256, 'special_1')
        elif tweet.item.rarity == 2:
            paste_image(image, 80, 80, 256, 'special_2')
        elif tweet.item.rarity == 3:
            paste_image(image, 80, 80, 256, 'special_3')
    elif tweet.type == Tweet_type.somebody_powerup:
        if tweet.item.rarity == 1:
            paste_image(image, 80, 80, 256, 'powerup_1')
        elif tweet.item.rarity == 2:
            paste_image(image, 80, 80, 256, 'powerup_2')
        elif tweet.item.rarity == 3:
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
    elif tweet.type == Tweet_type.destroyed:
        paste_image(image, 80, 80, 256, 'destroyed')
    elif tweet.type == Tweet_type.somebody_was_infected or tweet.type == Tweet_type.somebody_died_of_infection:
        paste_image(image, 80, 80, 256, 'infection')
    elif tweet.type == Tweet_type.atraction:
        paste_image(image, 80, 80, 256, 'atraction')

    return image

def get_summary_image(image, tweet):
    draw = ImageDraw.Draw(image)

    for i, place in enumerate(place_list):
        for j, player in enumerate(place.players):
            paste_image(image, place.coord_x + (j * 24), place.coord_y, 48, '', player.avatar_dir)

    if tweet.place != None:
        draw.ellipse((tweet.place.coord_x - 75, tweet.place.coord_y - 75, tweet.place.coord_x + 75, tweet.place.coord_y + 75), outline='rgb(255,0,0)', width=5)
        ellipse = Image.new('RGBA', image.size, (255,255,255,0))
        d = ImageDraw.Draw(ellipse)
        d.ellipse((tweet.place.coord_x - 2000, tweet.place.coord_y - 2000, tweet.place.coord_x + 2000, tweet.place.coord_y + 2000), outline=(255,255,255,100), width=1925)
        image = Image.alpha_composite(image, ellipse)

    for i, p in enumerate(place_list):
        if p.destroyed == True:
            paste_image(image, p.coord_x, p.coord_y, 60, 'destroyed')

        else:
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + 16, 32, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 16, 32, 'monster')
            if p.infected:
                paste_image(image, p.coord_x + 16, p.coord_y, 32, 'infection')
            if len(p.items) > 0:
                for i, item in enumerate(p.items):
                    paste_image(image, p.coord_x - 16 + i*5, p.coord_y, 32, get_item_rarity(item))

    draw_ranking(image)
    return image

def draw_ranking(image):
    coord_x = 5
    coord_y = 1150

    alive_players_list = get_alive_players()
    dead_players_list = get_dead_players()

    for i, p in enumerate(alive_players_list):
        draw_player(image, coord_x, coord_y, alive_players_list[i])
        coord_x, coord_y = calculate_coords(coord_x, coord_y)

    for i, p in enumerate(dead_players_list):
        draw_player(image, coord_x, coord_y, dead_players_list[i])
        coord_x, coord_y = calculate_coords(coord_x, coord_y)

def draw_player(image, coord_x, coord_y, player):
    global current_dir
    draw = ImageDraw.Draw(image)

    paste_image(image, coord_x + 24, coord_y + 24, 48, '', player.avatar_dir)
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
        draw.text((coord_x + 3, coord_y - 11), 'X', fill='rgb(255,0,0)', font=ImageFont.truetype(font_path_2, size=50))
    else:
        if player.infected:
            paste_image(image, coord_x + 24 + 24, coord_y + 24 + 12, 36, 'infection')
        if len(player.item_list) == 2:
            paste_image(image, coord_x + 45, coord_y + 5, 32, get_item_rarity(player.item_list[1]))
        if len(player.item_list) > 0:
            paste_image(image, coord_x + 5, coord_y + 5, 32, get_item_rarity(player.item_list[0]))

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

def get_item_rarity(item):
    if item.rarity == 1:
        return 'item_1'
    elif item.rarity == 2:
        return 'item_2'
    elif item.rarity == 3:
        return 'item_3'
