import unittest
import game


class GameTests(unittest.TestCase):
    def test_player(self):
        player = game.Player('a')
        self.assertEqual(player.name, 'a')
