#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import datetime
import os
import random

from data.secrets import *
from data.config import *
from data.literals import SLEEP

def tweet_line_from_file(file_path, line_number, image_path = None, image_2_path = None, last_tweet_id = None):
    with open(image_path, 'rb') as image:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if int(i) == int(line_number):
                    print(line)
                    return tweet(line.decode("utf-8"), image_path, image_2_path, last_tweet_id)

def tweet_sleep(image_dir):
    action_number = random.randint(0, 100)
    message = u''
    image_path = None

    if action_number > 60:
        message = SLEEP()
    else:
        image_path = os.path.join(image_dir, random.choice(os.listdir(image_dir)))

    print(message, image_path)
    return tweet(message, image_path)

def tweet(message, image_path = None, image_2_path = None, last_tweet_id = None):
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    image_list = []
    if image_path != None and os.path.exists(image_path):
        image_list.append(image_path)
    if image_2_path != None and os.path.exists(image_2_path):
        image_list.append(image_2_path)

    tweet = api.PostUpdate(status = message, in_reply_to_status_id=last_tweet_id, media=image_list)
    return tweet.id_str
