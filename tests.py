#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest
from types import SimpleNamespace
from data.config import config


class TestConfig(unittest.TestCase):
    config = None
    place_list = []
    player_list = []
    event_list = []

    def setUp(self):
        self.place_list = config.place_list
        self.event_list = config.event_list
        for i, place in enumerate(self.place_list):
            self.player_list = self.player_list + place.player_list
        pass

    # Returns True if battle probabilities are uneven.
    def test_battle_probabilities(self):
        probabilities = config.battle.probabilities
        self.assertNotEqual((probabilities.neutral + probabilities.tie) % 2, 0)

    # Returns True if item probabilities sum up 100.
    def test_items_probabilities(self):
        probabilities = config.items.probabilities
        self.assertEqual(probabilities.rarity_1 + probabilities.rarity_2 + probabilities.rarity_3, 100)

    # Returns True if item probabilities sum up 100.
    def test_actions_probabilities(self):
        actions = config.action_list

        self.assertEqual(sum(a.probability for a in actions), 100)

    # Returns True if all the connections are in place_list and area mutually connected.
    def test_connection_list(self):
        for i, place in enumerate(self.place_list):
            self.assertTrue(hasattr(place, 'road_connection_list') or hasattr(place, 'water_connection_list'))

            if hasattr(place, 'road_connection_list'):
                self.assertGreater(len(place.road_connection_list), 0, place.name + u' has no road connections.')
                for j, connection in enumerate(place.road_connection_list):
                    connection_place = next((i for i in config.place_list if i.name == connection), None)
                    self.assertIsNotNone(connection_place, connection + u' not in place_list.')
                    self.assertTrue(any(c for c in connection_place.road_connection_list if c == place.name),
                                    place.name + u' not mutually connected in ' + connection_place.name)

            if hasattr(place, 'water_connection_list'):
                self.assertGreater(len(place.water_connection_list), 0, place.name + u' has no water connections.')
                for j, connection in enumerate(place.water_connection_list):
                    connection_place = next((i for i in config.place_list if i.name == connection), None)
                    self.assertIsNotNone(connection_place, connection + u' not in place_list.')
                    self.assertTrue(any(c for c in connection_place.water_connection_list if c == place.name),
                                    place.name + u' not mutually connected in ' + connection_place.name)

    # Returns True if all the connections have coordinates.
    def test_places_coordinates(self):
        for i, place in enumerate(self.place_list):
            self.assertEqual(len(place.coordinates), 2, place.name + u' has no coordinates.')

    # Returns True if all the assigned weapons are in weapon list.
    def test_assigned_weapon_list(self):
        all_suffixes = []
        for k, weapon_group in enumerate(config.weapon_list):
            all_suffixes = all_suffixes + weapon_group.suffix_list

        for i, player in enumerate(self.player_list):
            if hasattr(player, 'weapon_list'):
                for j, item in enumerate(player.weapon_list):
                    self.assertTrue(any(i for i in all_suffixes if i == item), item + u' not in weapon_list.')

    # Returns True if all the assigned powerups are in powerups list.
    def test_assigned_powerup_list(self):
        all_suffixes = []
        for k, powerup_group in enumerate(config.powerup_list):
            all_suffixes = all_suffixes + powerup_group.suffix_list

        for i, player in enumerate(self.player_list):
            if hasattr(player, 'powerup_list'):
                for j, item in enumerate(player.powerup_list):
                    self.assertTrue(any(i for i in all_suffixes if i == item), item + u' not in powerup_list.')

    # Returns True the number of participants is higher than 1.
    def test_min_number_participants(self):
        self.assertTrue(len(self.player_list) > 1, u'Not enough participants.')

    # Returns True the number of tributes per district is not higher than max_tributes_per_district.
    def test_max_tributes_per_district(self):
        if config.general.match_type == 2 and config.general.max_tributes_per_district > 0:
            place_list = config.place_list
            for i, place in enumerate(place_list):
                self.assertFalse(len(place.player_list) > config.general.max_tributes_per_district,
                                 u'Too many participants in ' + place.name +
                                 ' . The limit is ' + config.general.max_tributes_per_district)

    # Returns True if the participants have the required attrs (name and gender).
    def test_required_attrs_participants(self):
        self.assertFalse(any([p for p in self.player_list if p.name is None or p.is_female is None]),
                         'There are participants with no name or gender')

    # Returns True if the participants are not duplicated.
    def test_required_attrs_participants(self):
        for i, player in enumerate(self.player_list):
            same_name = [p for p in self.player_list if p.username == player.username]
            self.assertEqual(1, len(same_name),
                             same_name[0].username + ' is duplicated.')

    # Returns True if the events have the required images.
    def test_required_images_events(self):
        for i, event in enumerate(self.event_list):
            self.assertTrue(os.path.exists('./assets/icons/events/' + event.name + '.png'),
                             'The event ' + event.name + ' does not have an image.')

if __name__ == '__main__':
    unittest.main()