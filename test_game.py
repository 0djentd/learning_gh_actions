"""Unittests"""

import unittest
import copy

from src import game


class GameTests(unittest.TestCase):
    """Unittests"""

    def setUp(self):
        """Test player name."""
        self.names = ['player 1', 'player 2']

    def tearDown(self):
        """Test player name."""
        del self.names

    def test_names(self):
        """Test player name."""
        for x in self.names:
            if not isinstance(x, str):
                raise TypeError

    def test_names_2(self):
        """Test player name."""
        for x in self.names:
            player = game.Player(copy.deepcopy(x))
            with self.subTest():
                self.assertEqual(player.check_name(), None)
