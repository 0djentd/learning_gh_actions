"""Unittests"""

import unittest
import game


class GameTests(unittest.TestCase):
    """Unittests"""

    def test_player(self):
        """Test player name."""
        player = game.Player('a')
        self.assertEqual(player.name, 'a')
