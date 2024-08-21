#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.images import *
from models.enums import TweetType
from models.drawing import DrawingMultiplePlayer

draw = None
image = None
tweet = None


def get_main_image(main_image, main_tweet, map_preview=False):
    global draw, image, tweet
    image = main_image
    tweet = main_tweet

    offset_horizontal = config.map.zoomed_avatar_size + config.map.frame_width * 2 + config.map.width_between_players_battle
    offset_vertical = int(config.map.zoomed_avatar_size / 2) + \
                      int(config.map.zoomed_avatar_size / 3) + int(config.map.zoomed_icon_size * 3 / 2)

    place_x, place_y = adjust_coordinates(tweet, offset_horizontal, offset_vertical)

    draw_map_places(image, tweet.place, map_preview=map_preview)

    if tweet.type not in [TweetType.monster_appeared, TweetType.monster_moved,TweetType.zombie_appeared,
                          TweetType.zombie_moved, TweetType.doctor_appeared, TweetType.doctor_moved]:
        # No player actions
        blurred_area = Image.new('RGBA', image.size, color=(255, 255, 255, 100))
        image = Image.alpha_composite(image, blurred_area)

    draw = ImageDraw.Draw(image)

    if tweet.type in [TweetType.winner, TweetType.somebody_got_special, TweetType.somebody_found_item,
                      TweetType.somebody_replaced_item, TweetType.somebody_revived, TweetType.somebody_moved, TweetType.somebody_moved_together_with,
                      TweetType.trap, TweetType.trap_dodged, TweetType.somebody_was_infected,
                      TweetType.somebody_suicided, TweetType.monster_took, TweetType.zombie_killed, TweetType.zombie_was_defeated,
                      TweetType.trapped, TweetType.somebody_died_of_infection, TweetType.somebody_got_cured, TweetType.doctor_cured]:

        # Individual actions
        drawing_player = DrawingPlayer(image, place_x, place_y)
        drawing_player.player = tweet.player
        drawing_player.avatar_size = config.map.zoomed_avatar_size
        drawing_player.icon_size = config.map.zoomed_icon_size
        drawing_player.font_size = config.map.font_size_icons
        if tweet.type == TweetType.somebody_moved_together_with:
            drawing_player.player_2 = tweet.player_2
        draw_player(drawing_player)
        if tweet.type == TweetType.winner:
            drawing_image = DrawingFile(image, place_x, place_y - int(2*config.map.zoomed_avatar_size / 3))
            drawing_image.dimension = config.map.zoomed_avatar_size * 3
            drawing_image.image_name = 'winner'
            paste_image(drawing_image)
    elif tweet.type in [TweetType.somebody_tied_and_became_friend, TweetType.somebody_tied_and_was_friend,
                        TweetType.somebody_escaped, TweetType.somebody_hurt, TweetType.somebody_killed, TweetType.somebody_stole,
                        TweetType.somebody_stole_and_threw, TweetType.somebody_stole_and_replaced]:
        # Pair actions
        if tweet.type in [TweetType.somebody_tied_and_became_friend, TweetType.somebody_tied_and_was_friend,
                          TweetType.somebody_escaped, TweetType.somebody_hurt, TweetType.somebody_killed]:
            draw_battle(place_x, place_y)

        # player_1
        drawing_player = DrawingPlayer(image, place_x - int(offset_horizontal / 2), place_y)
        drawing_player.player = tweet.player
        drawing_player.avatar_size = config.map.zoomed_avatar_size
        drawing_player.icon_size = config.map.zoomed_icon_size
        drawing_player.font_size = config.map.font_size_icons
        drawing_player.frame_color = config.battle.colors.player_1
        drawing_player.big_frame = True
        drawing_player.previous_power = tweet.player.previous_power
        draw_player(drawing_player)

        # player_2
        drawing_player_2 = DrawingPlayer(image, place_x + int(offset_horizontal / 2), place_y)
        drawing_player_2.player = tweet.player_2
        drawing_player_2.avatar_size = config.map.zoomed_avatar_size
        drawing_player_2.icon_size = config.map.zoomed_icon_size
        drawing_player_2.font_size = config.map.font_size_icons
        drawing_player_2.frame_color = config.battle.colors.player_2
        drawing_player_2.big_frame = True
        drawing_player_2.previous_power = tweet.player_2.previous_power
        draw_player(drawing_player_2)

        if tweet.type in [TweetType.somebody_tied_and_became_friend, TweetType.somebody_tied_and_was_friend]:
            drawing_image = DrawingFile(image, place_x, place_y)
            drawing_image.dimension = 128
            drawing_image.image_name = 'heart'
            paste_image(drawing_image)

    elif tweet.type in [TweetType.destroyed, TweetType.destroyed_district, TweetType.winner_districts,
                        TweetType.attraction, TweetType.introduce_players]:
        # Multi actions
        drawing_players = DrawingMultiplePlayer(image, place_x, place_y)
        drawing_players.player_list = tweet.player_list
        drawing_players.delta_x = config.map.avatar_size + 2
        drawing_players.font_size = config.map.font_size_icons
        draw_multiple_players(drawing_players)

        if tweet.type == TweetType.introduce_players:
            if len(tweet.player_list_2) > 0:
                drawing_players = DrawingMultiplePlayer(image, place_x, place_y + config.map.circle_size)
                drawing_players.player_list = tweet.player_list_2
                drawing_players.delta_x = config.map.avatar_size + 2
                drawing_players.font_size = config.map.font_size_icons
                draw_multiple_players(drawing_players)

                if tweet.inverse:
                    drawing_image = DrawingFile(image, place_x, place_y + 70)
                    drawing_image.dimension = 128
                    drawing_image.image_name = 'merge'''
                    paste_image(drawing_image)
                else:
                    drawing_image = DrawingFile(image, place_x, place_y + 70)
                    drawing_image.dimension = 128
                    drawing_image.image_name = 'split'
                    paste_image(drawing_image)
        elif tweet.type == TweetType.winner_districts:
            player_list_2 = tweet.place.tributes
            drawing_players = DrawingMultiplePlayer(image, place_x, place_y)
            drawing_players.player_list = player_list_2
            drawing_players.delta_x = config.map.avatar_size + 2
            drawing_players.font_size = config.map.font_size_icons
            draw_multiple_players(drawing_players)

            drawing_image = DrawingFile(image, place_x, place_y - int(2*config.map.zoomed_avatar_size / 3))
            drawing_image.dimension = config.map.zoomed_icon_size * 3
            drawing_image.image_name = 'winner'
            paste_image(drawing_image)
        elif tweet.place_2 is not None:
            drawing_players = DrawingMultiplePlayer(image, tweet.place_2.coord_x,
                                                    tweet.place_2.coord_y)
            drawing_players.player_list = tweet.player_list_2
            drawing_players.delta_x = config.map.avatar_size + 2
            drawing_players.font_size = config.map.font_size_icons
            draw_multiple_players(drawing_players)

    resize_image()
    return image


def adjust_coordinates(tweet_object, offset_horizontal, offset_vertical):
    coord_x = tweet_object.place.coord_x
    coord_y = tweet_object.place.coord_y

    if tweet.type == TweetType.introduce_players:
        return coord_x, coord_y

    if coord_x - offset_horizontal < 0:
        coord_x = offset_horizontal + config.map.width_between_players_battle
    elif coord_x + offset_horizontal > image.width:
        coord_x = image.width - offset_horizontal - config.map.width_between_players_battle

    if coord_y - offset_vertical < 0:
        coord_y = offset_vertical
    #elif coord_y + offset_vertical > image.height:
        # coord_y = image.height - offset_vertical

    return coord_x, coord_y


def draw_battle(coord_x, coord_y):
    if not tweet.type == TweetType.somebody_escaped:
        tweet.place_2 = tweet.place

    min_x = coord_x - config.map.zoomed_avatar_size
    max_x = coord_x + config.map.zoomed_avatar_size

    action_number_x = min_x + tweet.action_number * int(config.map.zoomed_avatar_size/50)
    tie = min_x + int(config.map.zoomed_avatar_size / 50) * tweet.factor
    min_tie = min_x + int(config.map.zoomed_avatar_size / 50) * (tweet.factor - config.battle.probabilities.neutral)
    max_tie = min_tie + 2 * int(config.map.zoomed_avatar_size / 50) * config.battle.probabilities.neutral

    if min_tie < min_x:
        min_tie = min_x
    elif min_tie > max_x:
        min_tie = max_x

    if max_tie < min_x:
        max_tie = min_x
    elif max_tie > max_x:
        max_tie = max_x

    # progress bar
    y_0 = coord_y + int(3 * config.map.zoomed_avatar_size / 4)
    y_1 = y_0 + 30

    draw.rectangle((min_x - 2, y_0 - 2, max_x + 2, y_1 + 2), outline='rgb(0,0,0)', width=4)
    draw.rectangle((min_x, y_0, min_tie, y_1), fill=config.battle.colors.player_1)
    draw.rectangle((max_tie, y_0, max_x, y_1), fill=config.battle.colors.player_2)
    draw.rectangle((min_tie, y_0, tie, y_1), fill=config.battle.colors.tie_player_1)
    draw.rectangle((tie, y_0, max_tie, y_1), fill=config.battle.colors.tie_player_2)
    draw.rectangle((tie - 2 * int((config.battle.probabilities.tie - 1) / 2), y_0,
                    tie + 2 * int((config.battle.probabilities.tie - 1) / 2), y_1), fill=config.battle.colors.tie)

    draw.text((min_x - 15, y_0 - 30), "0%", fill='rgb(255,255,255)', font=ImageFont.truetype(font_path, size=20),
              stroke_width=2,
              stroke_fill='rgb(0,0,0)')
    draw.text((max_x - 23, y_0 - 30), "100%", fill='rgb(255,255,255)', font=ImageFont.truetype(font_path, size=20),
              stroke_width=2,
              stroke_fill='rgb(0,0,0)')

    # action_number
    draw.rectangle((action_number_x - 1, y_0, action_number_x + 1, y_1), fill=config.battle.colors.arrow)
    drawing_image = DrawingFile(image, action_number_x, y_0 + 60)
    drawing_image.dimension = 72
    drawing_image.image_name = 'arrow'
    paste_image(drawing_image)

    draw.text((action_number_x + 23, y_0 + 35), str(tweet.action_number) + "%", fill='rgb(255,255,255)',
              font=ImageFont.truetype(font_path, size=20), stroke_width=2, stroke_fill='rgb(0,0,0)')


def resize_image():
    global image
    w, h = image.size
    x = tweet.place.coord_x
    y = tweet.place.coord_y
    zoom = 2
    zoom2 = zoom * 2

    x_1 = x - w / zoom2
    x_2 = x + w / zoom2
    y_1 = y - h / zoom2
    y_2 = y + h / zoom2

    if x_1 < 0:
        x_2 = x_2 - x_1
        x_1 = 0
    if y_1 < 0:
        y_2 = y_2 - y_1
        y_1 = 0
    if x_2 > w:
        x_1 = x_1 - x_2 + w
        x_2 = w

    image = image.crop((x_1, y_1, x_2, y_2))
    image.resize((w, h), Image.LANCZOS)

    if y_2 > h:
        # make image square
        new_im = Image.new(mode="RGB", size=image.size, color=config.map.colors.background)
        new_im.paste(image)
        image = new_im
