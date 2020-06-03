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
    if MAP_WATERMARK_COORDINATES != None:
        paste_image(image, MAP_WATERMARK_COORDINATES[0], MAP_WATERMARK_COORDINATES[1], 150, 'watermark')

    return image

def draw_map_places():
    for i, p in enumerate(place_list):
        if p.destroyed:
            paste_image(image, p.coord_x, p.coord_y, 40, 'destroyed')
        else:
            draw_items(len(p.items), p.coord_x, p.coord_y, image)
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + int(AVATAR_SIZE / 2), 48, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - int(AVATAR_SIZE / 4), 48, 'monster')
        draw_multiple_players(tweet, p.players, p.coord_x, p.coord_y, image, MAP_WIDTH_BETWEEN_PLAYERS, MAP_PLAYERS_IN_SINGLE_LINE)

def draw_ellipse():
    global draw, image
    draw.ellipse((tweet.place.coord_x - int(MAP_CIRCLE_SIZE/2), tweet.place.coord_y - int(MAP_CIRCLE_SIZE/2), tweet.place.coord_x + int(MAP_CIRCLE_SIZE/2), tweet.place.coord_y + int(MAP_CIRCLE_SIZE/2)), outline='rgb(255,0,0)', width=5)
    ellipse = Image.new('RGBA', image.size, (255,255,255,0))
    d = ImageDraw.Draw(ellipse)
    d.ellipse((tweet.place.coord_x - 2000, tweet.place.coord_y - 2000, tweet.place.coord_x + 2000, tweet.place.coord_y + 2000), outline=(255,255,255,100), width=1925)
    image = Image.alpha_composite(image, ellipse)
    draw = ImageDraw.Draw(image)
