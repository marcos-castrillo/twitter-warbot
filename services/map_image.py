#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.images import *

draw = None
image = None
tweet = None

def get_map_image(image_map, tweet_map):
    global draw, image, tweet
    image = image_map
    tweet = tweet_map
    draw = ImageDraw.Draw(image)

    draw_map_places()
    if tweet.place != None:
        draw_ellipse()
    paste_image(image, 125, 1275, 150, 'watermark')

    return image

def draw_map_places():
    for i, p in enumerate(place_list):
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 40, 'destroyed')
        else:
            draw_items(len(p.items), p.coord_x, p.coord_y, image)
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + 24, 48, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 12, 48, 'monster')
        draw_multiple_players(tweet, p.players, p.coord_x, p.coord_y, image, WIDTH_BETWEEN_PLAYERS, PLAYERS_IN_SINGLE_LINE)

def draw_ellipse():
    global draw, image
    draw.ellipse((tweet.place.coord_x - 75, tweet.place.coord_y - 75, tweet.place.coord_x + 75, tweet.place.coord_y + 75), outline='rgb(255,0,0)', width=5)
    ellipse = Image.new('RGBA', image.size, (255,255,255,0))
    d = ImageDraw.Draw(ellipse)
    d.ellipse((tweet.place.coord_x - 2000, tweet.place.coord_y - 2000, tweet.place.coord_x + 2000, tweet.place.coord_y + 2000), outline=(255,255,255,100), width=1925)
    image = Image.alpha_composite(image, ellipse)
    draw = ImageDraw.Draw(image)
