#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import datetime
import os
import random

from data.secrets import *
from data.config import *

def tweet_line_from_file(file_path, line_number, image_path = None, image_2_path = None, last_tweet_id = None):
    with open(image_path, 'rb') as image:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if int(i) == int(line_number):
                    print(line)
                    return tweet(line, image_path, image_2_path, last_tweet_id)

def tweet_sleep(image_dir):
    action_number = random.randint(0, 100)
    message = u''
    image_path = None

    if action_number > 65:
        message = random.choice([
            u'Los participantes se han ido a dormir tras un largo día.',
            u'Los participantes se han ido a dormir tras un largo día.',
            u'Los participantes se han ido a dormir tras un largo día.',
            u'Todo el mundo está durmiendo. Mañana será otro día.',
            u'Todo el mundo está durmiendo. Mañana será otro día.',
            u'Todo el mundo está durmiendo. Mañana será otro día.',
            u'Buenas noches hasta mañana, los lunnis y los niños, nos vamos a la cama.',
            u'Te diría que sueñes con los angelitos, pero creo que ya me has visto bastante el día de hoy.',
            u'Antes de dormir mira bien debajo de tu cama. No sea que a medianoche algo intente jalarte los pies.',
            u'¡Buenas noches y ten cuidado con las chinches!',
            u'Te deseo que tengas dulces sueños y que en cada uno de ellos, me veas para que puedas dormir bien.',
            u'Duerme bien y aseguráte de cerrar el armario, no sea que el coco vaya a venir por ti.',
            u'Hasta los tontos como tú deben descansar, ¡así que a la cama! Mañana habrá tiempo de que hagas más tonterías.',
            u'Hello darkness, my old friend. I´ve come to talk with you again.',
            u'Me voy a dormir, cualquier emergencia me avisan que yo al medio día les respondo.',
            u'Buenas noches, que pasen una linda y bendecida noche. Dulces sueños hasta mañana amigos ya amigas.',
            u'Se me acabaron las pilas. Buenas noches. Chistes cortos buenos, graciosos y divertidos para pasar un momento genial para compartir con las amistades y familiares.',
            u'Hello darkness, my old friend. I´ve come to talk with you again.',
            u'Hello darkness, my old friend. I´ve come to talk with you again.',
            u'Hello darkness, my old friend. I´ve come to talk with you again.',
        ])
    else:
        image_path = os.path.join(image_dir, random.choice(os.listdir(image_dir)))
    return tweet(message, image_path)

def tweet(message, image_path = None, image_2_path = None, last_tweet_id = None):
    global consumer_key, consumer_secret, access_token, access_token_secret

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    image_list = []
    if image_path != None and os.path.exists(image_path):
        image_list.append(image_path)
    if image_2_path != None and os.path.exists(image_2_path):
        image_list.append(image_2_path)

    tweet = api.PostUpdate(status = message.decode("utf8"), in_reply_to_status_id=last_tweet_id, media=image_list)
    return tweet.id_str
