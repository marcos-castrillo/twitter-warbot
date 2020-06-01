#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import datetime
import os
import random
import urllib.request

from data.secrets import *
from data.config import *
from data.literals import SLEEP
from store import player_list

def get_api():
    return twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

def tweet_line_from_file(file_path, line_number, image_path_list):
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if int(i) == int(line_number):
                linebreaks = line.count('//n')
                if linebreaks > 0:
                    line = line.replace('//n', '\n')
                print(line)
                return tweet(line, image_path_list)

def tweet_sleep(image_dir):
    action_number = random.randint(0, 100)
    message = DEFAULT_SLEEP_MESSAGE
    image_path = None
    image_dir = os.path.join(image_dir, LOCALIZATION)

    if action_number > SLEEP_ACTION_NUMBER_LIMIT:
        message = SLEEP().decode("utf-8")
    else:
        image_path = [os.path.join(image_dir, random.choice(os.listdir(image_dir)))]

    return tweet(message, image_path)

def tweet(message, image_path_list):
    image_list = []

    if image_path_list != None:
        for i, path in enumerate(image_path_list):
            if path != None and os.path.exists(path):
                image_list.append(path)

    api = get_api()
    tweet = api.PostUpdate(status = message, media=image_list)
    return tweet.id_str

def initialize_avatars():
    path = 'assets/avatars'
    if not os.path.exists(path):
        os.makedirs(path)
    for i, player in enumerate(player_list):
        if len(player.username) > 0:
            filename = path + '/' + player.username
        else:
            filename = path + '/' + player.name

        if not (os.path.exists(filename + '.png')):
            api = get_api()

            print('Downloading ' + player.get_name() + '\'s avatar...')
            profile_image_url = api.GetUser(screen_name=player.username).profile_image_url
            urllib.request.urlretrieve(profile_image_url, filename + '.png')
        player.avatar_dir = filename
