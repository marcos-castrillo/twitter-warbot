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
                paste_image(image, p.coord_x, p.coord_y + 24, 48, 'trap')
            if p.monster:
                paste_image(image, p.coord_x, p.coord_y - 12, 48, 'monster')

            if tweet.type != Tweet_type.introduce_players:
                draw_items(len(p.items), p.coord_x, p.coord_y, image, True)

    if USE_DISTRICTS and (tweet.type == Tweet_type.introduce_players or tweet.type == Tweet_type.destroyed_district or tweet.type == Tweet_type.winner_districts or tweet.type == Tweet_type.atraction):
        if USE_FLAGS:
            draw_flag()
        draw_items(len(tweet.place.items), tweet.place.coord_x, tweet.place.coord_y, image)

    if tweet.type == Tweet_type.winner or tweet.type == Tweet_type.somebody_got_special or tweet.type == Tweet_type.somebody_found_item or tweet.type == Tweet_type.somebody_replaced_item or tweet.type == Tweet_type.somebody_revived or tweet.type == Tweet_type.somebody_moved or tweet.type == Tweet_type.trap or tweet.type == Tweet_type.trap_dodged or tweet.type == Tweet_type.somebody_was_infected or tweet.type == Tweet_type.somebody_suicided or tweet.type == Tweet_type.monster_killed or tweet.type == Tweet_type.trapped or tweet.type == Tweet_type.somebody_died_of_infection:
        # Individual actions
        draw_player(image, tweet, tweet.player, tweet.place.coord_x, tweet.place.coord_y)
    elif tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_escaped or tweet.type == Tweet_type.somebody_killed or tweet.type == Tweet_type.somebody_stole or tweet.type == Tweet_type.somebody_stole_and_threw or tweet.type == Tweet_type.somebody_stole_and_replaced:
        # Pair actions
        if tweet.type == Tweet_type.somebody_tied_and_became_friend or tweet.type == Tweet_type.somebody_tied_and_was_friend or tweet.type == Tweet_type.somebody_escaped or tweet.type == Tweet_type.somebody_killed:
            draw_battle()

        draw_player(image, tweet, tweet.player, tweet.player.location.coord_x - 28, tweet.player.location.coord_y)
        draw_player(image, tweet, tweet.player_2, tweet.player_2.location.coord_x + 28, tweet.player_2.location.coord_y)
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
        paste_image(image, 80, 80, 256, 'heart')
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

    #avatar player_1
    draw.rectangle((tweet.player.location.coord_x - 55, tweet.player.location.coord_y - 28, tweet.player.location.coord_x - 1, tweet.player.location.coord_y + 27), outline=color_1, width=4)
    #avatar player_2
    draw.rectangle((tweet.player_2.location.coord_x, tweet.player_2.location.coord_y - 28, tweet.player_2.location.coord_x + 55, tweet.player_2.location.coord_y + 27), outline=color_2, width=4)
    #stats player_1
    draw.rectangle((tweet.player.location.coord_x - 110, tweet.player.location.coord_y - 25, tweet.player.location.coord_x - 60, tweet.player.location.coord_y + 25), fill='rgb(255,255,255)')
    paste_image(image, tweet.player.location.coord_x - 98, tweet.player.location.coord_y - 10, 32, 'attack')
    paste_image(image, tweet.player.location.coord_x - 98, tweet.player.location.coord_y + 12, 32, 'defense')
    draw.text((tweet.player.location.coord_x - 85, tweet.player.location.coord_y - 22), str(att_player_1), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
    draw.text((tweet.player.location.coord_x - 85, tweet.player.location.coord_y), str(def_player_1), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
    #stats player_2
    draw.rectangle((tweet.player_2.location.coord_x + 110, tweet.player_2.location.coord_y - 25, tweet.player_2.location.coord_x + 60, tweet.player_2.location.coord_y + 25), fill='rgb(255,255,255)')
    paste_image(image, tweet.player_2.location.coord_x + 72, tweet.player_2.location.coord_y - 10, 32, 'attack')
    paste_image(image, tweet.player_2.location.coord_x + 72, tweet.player_2.location.coord_y + 12, 32, 'defense')
    draw.text((tweet.player_2.location.coord_x + 85, tweet.player_2.location.coord_y - 22), str(att_player_2), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))
    draw.text((tweet.player_2.location.coord_x + 85, tweet.player_2.location.coord_y), str(def_player_2), fill='rgb(0,0,0)', font=ImageFont.truetype(font_path_2, size=15))

    # Config progress bar
    min = tweet.place.coord_x - 100
    max = tweet.place.coord_x + 100
    action_number = min + tweet.action_number * 2

    tie = min + 2*(tweet.factor)

    min_tie = min + 2*(tweet.factor - PROBAB_TIE)
    if min_tie < min:
        min_tie = min
    elif min_tie > max:
        min_tie = max

    max_tie = min_tie + 4*PROBAB_TIE
    if max_tie < min:
        max_tie = min
    elif max_tie > max:
        max_tie = max
    # progress bar
    draw.rectangle((min - 2, tweet.place.coord_y - 77, max + 2, tweet.place.coord_y - 48), outline='rgb(255,255,255)', width=4)
    draw.rectangle((min, tweet.place.coord_y - 75, min_tie, tweet.place.coord_y - 50), fill=color_1)
    draw.rectangle((max_tie, tweet.place.coord_y - 75, max, tweet.place.coord_y - 50), fill=color_2)
    draw.rectangle((min_tie, tweet.place.coord_y - 75, tie, tweet.place.coord_y - 50), fill=color_tie_1)
    draw.rectangle((tie, tweet.place.coord_y - 75, max_tie, tweet.place.coord_y - 50), fill=color_tie_2)
    draw.rectangle((tie - 1, tweet.place.coord_y - 75, tie + 1, tweet.place.coord_y - 50), fill=color_tie)

    # action_number
    draw.rectangle((action_number - 1, tweet.place.coord_y - 75, action_number + 1, tweet.place.coord_y - 50), fill=color_arrow)
    paste_image(image, action_number, tweet.place.coord_y - 100, 72, 'arrow')

def draw_flag():
    dimension_1 = 424
    dimension_2 = 286
    image_to_paste = Image.open(os.path.join(current_dir, '../assets/img/flags/' + LOCALIZATION + '/' + tweet.place.district_display_name + '.jpg'))
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
    if x_2 > WIDTH_MAP:
        x_1 = x_1 - x_2 + WIDTH_MAP
        x_2 = WIDTH_MAP

    image = image.crop((x_1, y_1, x_2, y_2))
    image.resize((w, h), Image.LANCZOS)
