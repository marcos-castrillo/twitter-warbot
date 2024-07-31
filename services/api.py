#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import os
import random
import urllib
import sys

from data.secrets import *
from data.literals import SLEEP
from data.config import config
from services.store import player_list
from PIL import Image
from shutil import copyfile

def get_api():
    auth = tweepy.OAuth1UserHandler(consumer_key=api_key,
                       consumer_secret=api_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)
    return tweepy.API(auth)

def get_client():
    return tweepy.Client(consumer_key=api_key,
                       consumer_secret=api_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

def tweet_line_from_file(file_path, line_number, image_path_list=[]):
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
    message = config.literals.default_sleep
    image_path = None
    image_dir = os.path.join(image_dir, config.general.language)

    if action_number <= config.sleep.probabilities.text:
        message = SLEEP()
    else:
        image_path = [os.path.join(image_dir, random.choice(os.listdir(image_dir)))]

    return tweet(message, image_path)


def tweet(message, image_path_list):
    media_ids  = []
    api = get_api()
    client = get_client()

    if image_path_list is not None:
        for i, path in enumerate(image_path_list):
            if path is not None and os.path.exists(path):
                media = api.chunked_upload(path)
                media_ids.append(media.media_id_string)

    return client.create_tweet(text=message, media_ids=media_ids)



def initialize_avatars():
    path = 'assets/avatars'
    icons_path = 'assets/icons'

    if not os.path.exists(path):
        os.makedirs(path)
    for i, player in enumerate(player_list):
        if len(player.username) > 0:
            filename = path + '/' + player.username
        else:
            filename = path + '/' + player.name

        if not (os.path.exists(filename + '.jpg')):
            if True:
                sys.exit("Error: avatar does not exist: " + player.username);
            else:
                # Disable downloading avatars
                api = get_api()

                print('Downloading ' + player.get_name() + '\'s avatar...')
                profile_image_url = api.GetUser(screen_name=player.username).profile_image_url
                profile_image_url = profile_image_url.replace('_normal', '')
                try:
                    urllib.request.urlretrieve(profile_image_url, filename + '.jpg')
                except urllib.error.HTTPError as te:
                    copyfile(icons_path + '/default.jpg', filename + '.jpg')

                old_im = Image.open(filename + '.jpg')
                (old_size_x, old_size_y) = old_im.size

                if old_size_x / old_size_y != 1.0 or old_size_x != 400 or old_size_y != 400:
                    # make image square
                    new_size = (400, 400)
                    new_im = Image.new(mode="RGB", size=new_size, color='#FFFFFF')
                    if old_size_x % 2 != 0:
                        old_size_x = old_size_x - 1
                    if old_size_y % 2 != 0:
                        old_size_y = old_size_y - 1
                    x = int((new_size[0] - old_size_x) / 2)
                    y = int((new_size[1] - old_size_y) / 2)
                    new_im.paste(old_im, (x, y))
                    new_im.save(filename + '.jpg')
        player.avatar_dir = filename

