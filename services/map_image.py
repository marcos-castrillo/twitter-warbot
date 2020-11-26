#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.images import *
from services.store import place_list
from models.enums import MatchType
from models.drawing import DrawingItems, DrawingText, DrawingMultiplePlayer

draw = None
image = None
tweet = None


def get_map_image(image_map, tweet_map):
    global draw, image, tweet
    image = image_map
    tweet = tweet_map
    draw = ImageDraw.Draw(image)

    draw_map_places(image)
    draw_map_players()
    if config.map.show_circle:
        if tweet.place is not None:
            draw_ellipse(tweet.place, tweet.place_2)
    if config.map.watermark_coordinates is not None:
        drawing_image = DrawingFile(image, config.map.watermark_coordinates[0], config.map.watermark_coordinates[1])
        drawing_image.dimension = 150
        drawing_image.image_name = 'watermark'
        paste_image(drawing_image)

    return image


def draw_map_players():
    for i, p in enumerate(place_list):
        drawing_players = DrawingMultiplePlayer(image, p.coord_x, p.coord_y)
        drawing_players.player_list = p.players
        drawing_players.delta_x = config.map.width_between_players
        drawing_players.single_line = config.map.players_in_single_line
        drawing_players.font_size = config.map.font_size_icons
        draw_multiple_players(drawing_players)

        if config.general.match_type != MatchType.rumble:
            if p.trap_by is not None:
                drawing_image = DrawingFile(image, p.coord_x, p.coord_y + int(config.map.icon_size / 2))
                drawing_image.dimension = config.map.icon_size
                drawing_image.image_name = 'trap'
                paste_image(drawing_image)
            if p.monster:
                drawing_image = DrawingFile(image, p.coord_x, p.coord_y - int(config.map.icon_size / 4))
                drawing_image.dimension = config.map.icon_size
                drawing_image.image_name = 'monster'
                paste_image(drawing_image)


def draw_ellipse(place, place_2=None):
    global draw, image
    draw.ellipse((place.coord_x - int(config.map.circle_size / 2),
                  place.coord_y - int(config.map.circle_size / 2),
                  place.coord_x + int(config.map.circle_size / 2),
                  place.coord_y + int(config.map.circle_size / 2)), outline=config.map.colors.circle, width=5)
    if place_2 is not None:
        draw.ellipse((place_2.coord_x - int(config.map.circle_size / 2),
                      place_2.coord_y - int(config.map.circle_size / 2),
                      place_2.coord_x + int(config.map.circle_size / 2),
                      place_2.coord_y + int(config.map.circle_size / 2)), outline=config.map.colors.circle, width=5)

    ellipse = Image.new('RGBA', image.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(ellipse)
    d.ellipse((place.coord_x - 2000, place.coord_y - 2000, place.coord_x + 2000,
               place.coord_y + 2000), outline=(255, 255, 255, 100), width=2000 - int(config.map.circle_size / 2))
    image = Image.alpha_composite(image, ellipse)
    draw = ImageDraw.Draw(image)
