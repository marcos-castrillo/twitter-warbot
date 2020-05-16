#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import datetime
import os
import random

from data.secrets import *
from data.config import *
from data.literals import SLEEP

def tweet_line_from_file(file_path, line_number, image_path_list):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if int(i) == int(line_number):
                print(line)
                return tweet(line.decode("utf-8"), image_path_list)

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
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    image_list = []

    if image_path_list != None:
        print(image_path_list)

        for i, path in enumerate(image_path_list):
            if path != None and os.path.exists(path):
                image_list.append(path)

    tweet = api.PostUpdate(status = message, media=image_list)
    return tweet.id_str
