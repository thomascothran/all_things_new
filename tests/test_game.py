import unittest
from utils import game, rooms


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.test_door = rooms.Door()
        self.test_door2 = rooms.Door()

    def tearDown(self):
        pass

    def test_that_select_item_returns_correct_item_from_list(self):
        menu = game.Menu()
        test_list = [self.test_door, self.test_door2]
        returned_item = menu.select_item(
            test_list,
            get_user_input=lambda: '1',  # Select first item from list
        )
        self.assertEqual(returned_item, self.test_door)
        # TO DO: Figure out how to test user input.