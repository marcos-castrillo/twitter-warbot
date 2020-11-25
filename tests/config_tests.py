#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest
from types import SimpleNamespace


class TestConfig(unittest.TestCase):
    config = None
    place_list = []
    player_list = []
    event_list = []

    def setUp(self):
        with open('../data/config.json', 'r', encoding="utf-8") as configFile:
            data = configFile.read()
        self.config = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        self.place_list = self.config.data.place_list
        self.event_list = self.config.event_list
        for i, place in enumerate(self.place_list):
            self.player_list = self.player_list + place.player_list
        pass

    # Returns True if battle probabilities are uneven.
    def test_battle_probabilities(self):
        probabilities = self.config.battle.probabilities
        self.assertNotEqual((probabilities.neutral + probabilities.tie) % 2, 0)

    # Returns True if item probabilities sum up 100.
    def test_items_probabilities(self):
        probabilities = self.config.items.probabilities
        self.assertEqual(probabilities.rarity_1 + probabilities.rarity_2 + probabilities.rarity_3, 100)

    # Returns True if item probabilities sum up 100.
    def test_actions_probabilities(self):
        actions = self.config.action_list

        self.assertEqual(sum(a.probability for a in actions), 100)

    # Returns True if all the connections are in place_list and area mutually connected.
    def test_connection_list(self):
        for i, place in enumerate(self.place_list):
            for j, connection in enumerate(place.road_connection_list):
                connection_place = next((i for i in self.config.data.place_list if i.name == connection), None)
                self.assertIsNotNone(connection_place, connection + u' not in place_list.')
                self.assertTrue(any(c for c in connection_place.road_connection_list if c == place.name),
                                place.name + u' not mutually connected in ' + connection_place.name)

            if hasattr(place, 'water_connection_list'):
                for j, connection in enumerate(place.water_connection_list):
                    connection_place = next((i for i in self.config.data.place_list if i.name == connection), None)
                    self.assertIsNotNone(connection_place, connection + u' not in place_list.')
                    self.assertTrue(any(c for c in connection_place.water_connection_list if c == place.name),
                                    place.name + u' not mutually connected in ' + connection_place.name)

    # Returns True if all the assigned weapons are in weapon_list.
    def test_assigned_weapon_list(self):
        place_list = self.config.data.place_list
        weapon_list = self.config.data.weapon_list
        for i, place in enumerate(place_list):
            for j, player in enumerate(place.player_list):
                if hasattr(player, 'weapon_list'):
                    for k, item in enumerate(player.weapon_list):
                        self.assertTrue(any(i for i in weapon_list if i == item), item + u' not in weapon_list.')

    # Returns True the number of participants is higher than 1.
    def test_min_number_participants(self):
        self.assertTrue(len(self.player_list) > 1)

    # Returns True the number of tributes per district is not higher than max_tributes_per_district.
    def test_max_tributes_per_district(self):
        if self.config.general.match_type == 2 and self.config.general.max_tributes_per_district > 0:
            place_list = self.config.data.place_list
            for i, place in enumerate(place_list):
                self.assertFalse(len(place.player_list) > self.config.general.max_tributes_per_district)

    # Returns True if the participants have the required attrs (name and gender).
    def test_required_attrs_participants(self):
        self.assertEqual(len([p for p in self.player_list if p.name is None or p.is_female is None]), 0)

    # Returns True if the events have the required images.
    def test_required_images_events(self):
        for i, event in enumerate(self.event_list):
            self.assertTrue(os.path.exists('../assets/icons/events/' + event.name + '.png'))
