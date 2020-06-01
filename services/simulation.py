#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.main_image import get_main_image
from services.map_image import get_map_image
from services.ranking_image import get_ranking_image
from services.images import *

output_dir = None
path = None
line_number = 0

def initialize():
    global output_dir, path
    date = datetime.datetime.now()
    time_stamp = u'-'.join([str(date.year), str(date.month), str(date.day), str(date.hour), str(date.minute)])
    output_dir = os.path.join(current_dir, '../simulations', time_stamp)

    filename = u'simulation'

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
    if output_dir == None:
        initialize()

    if tweet.type == Tweet_type.destroyed_district:
        line_number = line_number - 1

    write_line(get_message(tweet))
    draw_image(tweet)

    line_number = line_number + 1
    if tweet.type == Tweet_type.winner or tweet.type == Tweet_type.winner_districts:
        write_last_line()

def write_line(message):
    print(str(line_number) + u': ' + message.decode('utf-8'))

    with open(os.path.join(path), "a+", encoding="utf-8") as file:
        file.write(message.decode('utf-8'))

def write_last_line():
    with open(os.path.join(output_dir, '-1_image.txt'), "w") as file:
        file.write('ok')
    with open(os.path.join(output_dir, '-1_line.txt'), "w") as file:
        file.write('ok')

def draw_image(tweet):
    raw_map_img = draw_places(Image.open(os.path.join(current_dir, '../assets/maps/' + LOCALIZATION + '.png')))
    raw_map_img_2 = draw_places(Image.open(os.path.join(current_dir, '../assets/maps/' + LOCALIZATION + '.png')))

    if USE_DISTRICTS and MAX_TRIBUTES_PER_DISTRICT > 0:
        rows = math.ceil(len(get_alive_players()) / RANKING_IMGS_PER_ROW) + 2*(math.ceil(len(get_dead_players()) / RANKING_IMGS_PER_ROW))/3
    else:
        rows = math.ceil(len(player_list) / RANKING_IMGS_PER_ROW)

    RANKING_HEIGHT = int(rows * RANKING_SPACE_BETWEEN_ROWS + RANKING_PADDING * 2)
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
        map_image = get_main_image(raw_map_img_2, tweet)
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
        font = ImageFont.truetype(font_path_2, size=15)
        lines = get_multiline_wrapped_text(p.name, 70, font)
        for j, line in enumerate(lines):
            color = 'rgb(0,0,0)'
            if p.destroyed:
                color = 'rgb(255,0,0)'
            draw.text((p.coord_x + 15, p.coord_y + - 10 + j * 16), line, fill=color, font=font)
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 50, 'destroyed')
        else:
            paste_image(image, p.coord_x, p.coord_y, 50, 'place')
    return image
