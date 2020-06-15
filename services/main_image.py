#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.images import *

draw = None
image = None
tweet = None

def get_main_image(main_image, main_tweet):
    global draw, image, tweet
    image = main_image
    tweet = main_tweet
    draw = ImageDraw.Draw(image)

    image.putalpha(128)  # Half alpha; alpha argument must be an int

    for i, p in enumerate(place_list):
        if not p.destroyed:
            if p.trap_by != None:
                paste_image(image, p.coord_x, p.coord_y + int(MAP_AVATAR_SIZE / 2), 48, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - int(MAP_AVATAR_SIZE / 4), 48, 'monster')

            if tweet.type != Tweet_type.introduce_players and MATCH_TYPE != Match_type.rumble:
                draw_items(len(p.items), p.coord_x, p.coord_y, image, True)

    if MATCH_TYPE == Match_type.districts and (tweet.type == Tweet_type.introduce_players or tweet.type == Tweet_type.destroyed_district or tweet.type == Tweet_type.winner_districts or tweet.type == Tweet_type.atraction):
        if USE_FLAGS:
            draw_flag()
        draw_items(len(tweet.place.items), tweet.place.coord_x, tweet.place.coord_y, image)

    if tweet.type == Tweet_type.winner or tweet.type == Tweet_type.somebody_got_special or tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item or tweet.type == Tweet_type.somebody_revived or tweet.type == Tweet_type.somebody_moved or tweet.type == Tweet_type.trap or tweet.type == Tweet_type.trap_dodged or tweet.type == Tweet_type.somebody_was_infected or tweet.type == Tweet_type.somebody_suicided or tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.trapped or tweet.type == Tweet_type.somebody_died_of_infection or tweet.type == Tweet_type.somebody_got_cured:
        # Individual actions
        draw_player(image, tweet, tweet.player, tweet.place.coord_x, tweet.place.coord_y)
    elif tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_escaped or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.somebody_stole or tweet.type == Tweet_type.somebody_stole_and_threw or tweet.type == Tweet_type.somebody_stole_and_replaced or tweet.type == Tweet_type.soft_attack:
        # Pair actions
        if tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_escaped or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.soft_attack:
            draw_battle()

        frame_width = 4
        draw_player(image, tweet, tweet.player, tweet.player.location.coord_x - int(MAP_AVATAR_SIZE / 2) - frame_width - 10, tweet.player.location.coord_y)
        draw_player(image, tweet, tweet.player_2, tweet.player_2.location.coord_x + int(MAP_AVATAR_SIZE / 2) + frame_width + 10 + 1, tweet.player_2.location.coord_y)
    elif tweet.type == Tweet_type.destroyed or tweet.type == Tweet_type.destroyed_district or tweet.type == Tweet_type.winner_districts or tweet.type == Tweet_type.atraction or tweet.type == Tweet_type.introduce_players:
        # Multi actions
        draw_multiple_players(tweet, tweet.player_list, tweet.place.coord_x, tweet.place.coord_y, image, 50)
        if tweet.type == Tweet_type.introduce_players:
            if len(tweet.player_list_2) > 0:
                draw_multiple_players(tweet, tweet.player_list_2, tweet.place.coord_x, tweet.place.coord_y + 140, image, 50)

                if tweet.inverse:
                    paste_image(image, tweet.place.coord_x, tweet.place.coord_y + 70, 128, 'merge')
                else:
                    paste_image(image, tweet.place.coord_x, tweet.place.coord_y + 70, 128, 'split')
        elif tweet.place_2 != None:
            draw_multiple_players(tweet, tweet.player_list_2, tweet.place_2.coord_x, tweet.place_2.coord_y, image, 50)

    resize_image()
    draw_big_image()
    return image

def draw_big_image():
    if tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item:
        if tweet.item.get_rarity() == 1:
            paste_image(image, 80, 80, 256, 'weapon_1')
        elif tweet.item.get_rarity() == 2:
            paste_image(image, 80, 80, 256, 'weapon_2')
        elif tweet.item.get_rarity() == 3:
            paste_image(image, 80, 80, 256, 'weapon_3')
    elif tweet.type == Tweet_type.somebody_got_special:
        if tweet.item.get_rarity() == 1:
            paste_image(image, 80, 80, 256, 'special_1')
        elif tweet.item.get_rarity() == 2:
            paste_image(image, 80, 80, 256, 'special_2')
        elif tweet.item.get_rarity() == 3:
            paste_image(image, 80, 80, 256, 'special_3')
    elif tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend:
        paste_image(image, 80, 80, 256, 'tie')
    elif tweet.type == Tweet_type.monster_moved or tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.monster_appeared:
        paste_image(image, 80, 80, 256, 'monster')
    elif tweet.type == Tweet_type.trap_dodged or tweet.type == Tweet_type.trapped or tweet.type == Tweet_type.trap:
        paste_image(image, 80, 80, 256, 'trap')
    elif tweet.type == Tweet_type.somebody_moved:
        if tweet.double:
            paste_image(image, 80, 80, 256, 'strong')
        elif tweet.item != None:
            if tweet.item.type == Item_type.powerup:
                if tweet.item.get_rarity() == 1:
                    paste_image(image, 80, 80, 256, 'powerup_1')
                elif tweet.item.get_rarity() == 2:
                    paste_image(image, 80, 80, 256, 'powerup_2')
                elif tweet.item.get_rarity() == 3:
                    paste_image(image, 80, 80, 256, 'powerup_3')
            elif tweet.item.type == Item_type.injury:
                paste_image(image, 80, 80, 256, 'injure')
        else:
            paste_image(image, 80, 80, 256, 'move')
    elif tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.somebody_suicided:
        paste_image(image, 80, 80, 256, 'skull')
    elif tweet.type == Tweet_type.soft_attack:
        paste_image(image, 80, 80, 256, 'soft_attack')
    elif tweet.type == Tweet_type.somebody_revived:
        paste_image(image, 80, 80, 256, 'revive')
    elif tweet.type == Tweet_type.somebody_stole or tweet.type == Tweet_type.somebody_stole_and_threw or tweet.type == Tweet_type.somebody_stole_and_replaced:
        paste_image(image, 80, 80, 256, 'steal')
    elif tweet.type == Tweet_type.somebody_escaped:
        paste_image(image, 80, 80, 256, 'runaway')
    elif tweet.type == Tweet_type.destroyed or tweet.type == Tweet_type.destroyed_district:
        paste_image(image, 80, 80, 256, 'destroyed')
    elif tweet.type == Tweet_type.somebody_was_infected or tweet.type == Tweet_type.somebody_died_of_infection:
        paste_image(image, 80, 80, 256, 'infection')
    elif tweet.type == Tweet_type.atraction:
        paste_image(image, 80, 80, 256, 'atraction')
    elif tweet.type == Tweet_type.somebody_got_cured:
        paste_image(image, 80, 80, 256, 'cure')
    elif tweet.type == Tweet_type.winner or tweet.type == Tweet_type.winner_districts:
        paste_image(image, 80, 100, 248, 'winner')

def draw_battle():
    color_1 = 'rgb(255,0,0)'
    color_2 = 'rgb(0,0,255)'
    color_tie = 'rgb(127,0,127)'
    color_tie_1 = 'rgb(192,0,64)'
    color_tie_2 = 'rgb(64,0,192)'
    color_arrow = 'rgb(59,249,0)'

    if not tweet.type == Tweet_type.somebody_escaped:
        tweet.place_2 = tweet.place

    if tweet.new_item != None:
        # Stole
        if tweet.inverse:
            att_player_1 = tweet.player.get_attack() + tweet.new_item.attack
            def_player_1 = tweet.player.get_defense() + tweet.new_item.defense
            att_player_2 = tweet.player_2.get_attack() - tweet.new_item.attack
            def_player_2 = tweet.player_2.get_defense() - tweet.new_item.defense
        else:
            att_player_1 = tweet.player.get_attack() - tweet.new_item.attack
            def_player_1 = tweet.player.get_defense() - tweet.new_item.defense
            att_player_2 = tweet.player_2.get_attack() + tweet.new_item.attack
            def_player_2 = tweet.player_2.get_defense() + tweet.new_item.defense

        if tweet.old_item != None:
            # Throw away
            if tweet.inverse:
                att_player_2 = att_player_2 + tweet.old_item.attack
                def_player_2 = def_player_2 + tweet.old_item.defense
            else:
                att_player_1 = att_player_1 + tweet.old_item.attack
                def_player_1 = def_player_1 + tweet.old_item.defense
    else:
        att_player_1 = tweet.player.get_attack()
        def_player_1 = tweet.player.get_defense()
        att_player_2 = tweet.player_2.get_attack()
        def_player_2 = tweet.player_2.get_defense()

    frame_width = 4
    #frame player_1
    draw.rectangle((tweet.player.location.coord_x - MAP_AVATAR_SIZE - frame_width * 2 - 10, tweet.player.location.coord_y - int(MAP_AVATAR_SIZE / 2) - frame_width, tweet.player.location.coord_x - 10 - 1, tweet.player.location.coord_y + int(MAP_AVATAR_SIZE / 2) + frame_width - 1), outline=color_1, width=4)
    #frame player_2
    draw.rectangle((tweet.player_2.location.coord_x + 10 + 1, tweet.player_2.location.coord_y - int(MAP_AVATAR_SIZE / 2) - frame_width, tweet.player_2.location.coord_x + MAP_AVATAR_SIZE + frame_width * 2 + 10, tweet.player_2.location.coord_y + int(MAP_AVATAR_SIZE / 2) + frame_width - 1), outline=color_2, width=4)
    #stats
    delta_x = MAP_AVATAR_SIZE + 10
    square_size = 50
    unit = int(square_size / 10)
    #stats player_1
    x_0 = tweet.player.location.coord_x - MAP_AVATAR_SIZE - 10
    draw.ellipse((x_0 - square_size - unit * 2, tweet.player.location.coord_y - unit * 5, x_0 - unit * 2, tweet.player.location.coord_y + 25), fill='rgb(255,255,255)')
    draw.ellipse((x_0 - square_size - unit * 2, tweet.player.location.coord_y - unit * 5, x_0 - unit * 2, tweet.player.location.coord_y + 25), outline=color_1, width=2)
    paste_image(image, x_0 - unit * 9, tweet.player.location.coord_y - unit * 2, 32, 'attack')
    paste_image(image, x_0 - unit * 9, tweet.player.location.coord_y + unit * 2, 32, 'defense')
    draw.text((x_0 - unit * 6 - 4, tweet.player.location.coord_y - unit * 4 + 2), str(att_player_1), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
    draw.text((x_0 - unit * 6 - 4, tweet.player.location.coord_y + unit - 2), str(def_player_1), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
    #stats player_2
    x_0 = tweet.player_2.location.coord_x + MAP_AVATAR_SIZE + 10
    draw.ellipse((x_0 + unit * 2, tweet.player_2.location.coord_y - unit * 5, x_0 + square_size + unit * 2, tweet.player_2.location.coord_y + 25), fill='rgb(255,255,255)')
    draw.ellipse((x_0 + unit * 2, tweet.player_2.location.coord_y - unit * 5, x_0 + square_size + unit * 2, tweet.player_2.location.coord_y + 25), outline=color_2, width=2)
    paste_image(image, x_0 + unit * 5, tweet.player_2.location.coord_y - unit * 2, 32, 'attack')
    paste_image(image, x_0 + unit * 5, tweet.player_2.location.coord_y + unit * 2, 32, 'defense')
    draw.text((x_0 + unit * 8 - 4, tweet.player_2.location.coord_y - unit * 4 + 2), str(att_player_2), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
    draw.text((x_0 + unit * 8 - 4, tweet.player_2.location.coord_y + unit - 2), str(def_player_2), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))

    # Config progress bar
    min = tweet.place.coord_x - 100
    max = tweet.place.coord_x + 100
    action_number = min + tweet.action_number * 2

    tie = min + 2*(tweet.factor)

    min_tie = min + 2*(tweet.factor - PROBAB_NEUTRAL)
    if min_tie < min:
        min_tie = min
    elif min_tie > max:
        min_tie = max

    max_tie = min_tie + 4*PROBAB_NEUTRAL
    if max_tie < min:
        max_tie = min
    elif max_tie > max:
        max_tie = max

    # progress bar
    y_0 = tweet.place.coord_y - MAP_AVATAR_SIZE
    y_1 = y_0 + 25
    draw.rectangle((min - 2, y_0 - 2, max + 2, y_1 + 2), outline='rgb(255,255,255)', width=4)
    draw.rectangle((min, y_0, min_tie, y_1), fill=color_1)
    draw.rectangle((max_tie, y_0, max, y_1), fill=color_2)
    draw.rectangle((min_tie, y_0, tie, y_1), fill=color_tie_1)
    draw.rectangle((tie, y_0, max_tie, y_1), fill=color_tie_2)
    draw.rectangle((tie - 2*int((PROBAB_TIE - 1) / 2), y_0, tie + 2*int((PROBAB_TIE - 1) / 2), y_1), fill=color_tie)

    # action_number
    draw.rectangle((action_number - 1, y_0, action_number + 1, y_1), fill=color_arrow)
    paste_image(image, action_number, y_0 - 25, 72, 'arrow')

def draw_flag():
    dimension_1 = 424
    dimension_2 = 286
    image_to_paste = Image.open(os.path.join(current_dir, '../assets/flags/' + LOCALIZATION + '/' + tweet.place.district_display_name + '.jpg'))
    image_to_paste.thumbnail([dimension_1/2, dimension_2/2])
    image.paste(image_to_paste, (tweet.place.coord_x - 100, tweet.place.coord_y - 130), image_to_paste.convert('RGBA'))

def resize_image():
    global image
    w, h = image.size
    x = tweet.place.coord_x
    y = tweet.place.coord_y
    zoom = 2.5
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
