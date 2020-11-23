#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys

from services.main_image import get_main_image
from services.map_image import get_map_image
from services.ranking_image import get_ranking_image, get_ranking_height, RANKING_WIDTH
from services.images import *
from services.store import get_players_in_place, place_list
from data.literals import get_message
from models.enums import MatchType, TweetType

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

    with open(os.path.join(output_dir, 'events.txt'), "w") as file:
        file.write('')


def write_tweet(tweet):
    global line_number
    if output_dir is None:
        initialize()

    if tweet.type == TweetType.destroyed_district:
        line_number = line_number - 1
    elif tweet.is_event:
        with open(os.path.join(output_dir, 'events.txt'), "a+") as file:
            file.write(str(line_number) + '\n')

    write_line(get_message(tweet))
    draw_image(tweet)

    line_number = line_number + 1
    if tweet.type == TweetType.winner or tweet.type == TweetType.winner_districts:
        write_last_line()


def write_line(message):
    print(str(line_number) + u': ' + message.decode("utf-8"))

    with open(os.path.join(path), "a+", encoding="utf-8") as file:
        file.write(message.decode('utf-8'))


def write_last_line():
    with open(os.path.join(output_dir, '-1_image.txt'), "w") as file:
        file.write('ok')
    with open(os.path.join(output_dir, '-1_line.txt'), "w") as file:
        file.write('ok')
    sanitize_lines(os.path.join(output_dir, 'simulation.txt'))


def draw_image(tweet):
    raw_map_img = Image.open(os.path.join(current_dir, config.file_paths.map, config.general.run_name + '.png'))
    raw_map_img_2 = Image.open(os.path.join(current_dir, config.file_paths.map, config.general.run_name + '.png'))
    blank_img = Image.new('RGB', (RANKING_WIDTH, get_ranking_height()), color=config.ranking.colors.background)

    main_image = None
    map_image = None
    ranking_image = None

    if tweet.is_event:
        if tweet.type == TweetType.start or tweet.type == TweetType.start_2:
            return
        main_image = Image.open(os.path.join(current_dir, config.file_paths.icons, 'event_' + tweet.type + '.png'))
        main_image.save(output_dir + '/' + str(line_number) + '.png')
    elif tweet.type == TweetType.introduce_players:
        map_image = get_main_image(raw_map_img_2, tweet)
        map_image.save(output_dir + '/' + str(line_number) + '_map.png')
    elif tweet.type == TweetType.destroyed_district:
        map_image = get_map_image(raw_map_img_2, tweet)
        map_image.save(output_dir + '/' + str(line_number) + '_bis.png')
    elif config.general.match_type == MatchType.rumble:
        if tweet.type == TweetType.next_entrance:
            main_image = Image.open(tweet.player.avatar_dir + '.png')
            map_image = get_map_image(raw_map_img_2, tweet)
        else:
            main_image = get_main_image(raw_map_img, tweet)
            if len(get_players_in_place(place_list[0])) > 2:
                map_image = get_map_image(raw_map_img_2, tweet)

        main_image.save(output_dir + '/' + str(line_number) + '.png')
        if map_image is not None:
            map_image.save(output_dir + '/' + str(line_number) + '_map.png')
    else:
        main_image = get_main_image(raw_map_img, tweet)
        map_image = get_map_image(raw_map_img_2, tweet)

        main_image.save(output_dir + '/' + str(line_number) + '.png')
        map_image.save(output_dir + '/' + str(line_number) + '_map.png')

        if tweet.type in [TweetType.monster_killed, TweetType.trapped, TweetType.somebody_died_of_infection,
                          TweetType.somebody_killed, TweetType.somebody_revived, TweetType.somebody_suicided,
                          TweetType.somebody_was_infected, TweetType.winner, TweetType.winner_districts]:
            ranking_image = get_ranking_image(blank_img, tweet)
            ranking_image.save(output_dir + '/' + str(line_number) + '_ranking.png')


def sanitize_lines(path):
    # Lines no longer than 280 chars
    longest_line = max(open(path, 'r', encoding='utf-8'), key=len)
    if len(longest_line) > 280:
        sys.exit('File error: line its too long: (' + str(len(longest_line)) + ' characters)\n' + longest_line)

    # Add . at the beginning of the lines if there's an @
    lines = {}
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    for i, l in enumerate(lines):
        if l[0] == '@':
            temp_str = ''
            for j in l:
                temp_str += j
            temp_str = '.' + temp_str
            lines[i] = temp_str

    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    with open(path, encoding='utf-8') as f:
        for i, l in enumerate(f):
            if l[0] == '@':
                sys.exit('File error: theres an @ as the first character of the line: ' + str(i))