#!/usr/bin/env python
# -*- coding: utf-8 -*-
from services.config import config


class DrawingBase(object):
    coord_x = None
    coord_y = None
    image = None

    def __init__(self, image, coord_x, coord_y):
        self.image = image
        self.coord_x = coord_x
        self.coord_y = coord_y


class DrawingPlayer(DrawingBase):
    player = None
    avatar_size = None
    icon_size = None
    font_size = None
    frame_color = None
    show_icons = True
    big_frame = False
    previous_power = None


class DrawingMultiplePlayer(DrawingBase):
    player_list = None
    delta_x = None
    single_line = False
    font_size = None


class DrawingItems(DrawingBase):
    item_count = 0
    gray_style = False
    offset_y = None


class DrawingText(DrawingBase):
    color = None
    font_size = None
    max_height = None
    max_width = None
    line_height = None
    text = None
    center_horizontally = False
    center_vertically = True


class DrawingFile(DrawingBase):
    image_name = None
    image_dir = None
    dimension = None
    gray_style = False

