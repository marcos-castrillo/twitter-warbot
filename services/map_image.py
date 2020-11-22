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

    draw_map_places()
    draw_map_players()
    if tweet.place is not None and config.map.show_circle:
        draw_ellipse()
    if config.map.watermark_coordinates is not None:
        paste_image(image, config.map.watermark_coordinates[0], config.map.watermark_coordinates[1], 150, 'watermark')

    return image


def draw_map_places():
    for i, p in enumerate(place_list):
        color = config.map.colors.text
        icon_name = 'place'
        if p.destroyed:
            color = config.map.colors.text_destroyed
            icon_name = 'destroyed'

        drawing_text = DrawingText(image, p.coord_x + int(config.map.avatar_size / 4) + 4, p.coord_y - int(config.map.line_height / 2))
        drawing_text.color = color
        drawing_text.font_size = config.map.font_size
        drawing_text.max_width = config.map.avatar_size * 2
        drawing_text.line_height = config.map.line_height
        drawing_text.text = p.name
        drawing_text.center_horizontally = True
        draw_wrapped_text(drawing_text)

        paste_image(image, p.coord_x, p.coord_y, config.map.icon_size, icon_name)


def draw_map_players():
    for i, p in enumerate(place_list):
        drawing_players = DrawingMultiplePlayer(image, p.coord_x, p.coord_y)
        drawing_players.player_list = p.players
        drawing_players.delta_x = config.map.width_between_players
        drawing_players.single_line = config.map.players_in_single_line
        drawing_players.font_size = config.map.font_size_icons
        draw_multiple_players(drawing_players)

        if config.general.match_type != MatchType.rumble:
            drawing_items = DrawingItems(image, p.coord_x, p.coord_y)
            drawing_items.item_count = len(p.items)
            draw_items(drawing_items)

            if p.trap_by is not None:
                paste_image(image, p.coord_x, p.coord_y + int(config.map.icon_size / 2), config.map.small_icon_size,
                            'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - int(config.map.icon_size / 4), config.map.small_icon_size,
                            'monster')


def draw_ellipse():
    global draw, image
    draw.ellipse((tweet.place.coord_x - int(config.map.circle_size / 2),
                  tweet.place.coord_y - int(config.map.circle_size / 2),
                  tweet.place.coord_x + int(config.map.circle_size / 2),
                  tweet.place.coord_y + int(config.map.circle_size / 2)), outline=config.map.colors.circle, width=5)
    ellipse = Image.new('RGBA', image.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(ellipse)
    d.ellipse((tweet.place.coord_x - 2000, tweet.place.coord_y - 2000, tweet.place.coord_x + 2000,
               tweet.place.coord_y + 2000), outline=(255, 255, 255, 100), width=2000 - int(config.map.circle_size / 2))
    image = Image.alpha_composite(image, ellipse)
    draw = ImageDraw.Draw(image)
