import unittest
from utils import objects, game

class KeyTests(unittest.TestCase):
    def setUp(self):
        self.test_key = objects.Key()
        self.test_player = game.Player()

    def tearDown(self):
        pass

    def test_that_player_can_pick_up_key(self):
        self.test_key.take(self.test_player)
        self.assertIn(self.test_key, self.test_player.inventory)
