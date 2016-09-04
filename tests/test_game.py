import unittest
from utils import game


class MenuTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_that_select_item_returns_correct_item_from_list(self):
        menu = game.Menu()
        test_list = ['a dog', 'a cat', 'a tree']
        returned_item = menu.select_item(test_list)
        # TO DO: Figure out how to test user input.