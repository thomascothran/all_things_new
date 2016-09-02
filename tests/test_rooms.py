import unittest

try:
    from utils import rooms
except Exception as e:
    print('Error: %s' % e)


class WallTests(unittest.TestCase):
    """This class tests the descriptions of a wall."""

    def setUp(self):
        # self.test_walls = Walls()
        pass

    def tearDown(self):
        pass

    def test_color(self):
        wall = rooms.Walls()
        self.assertIn(wall.color, rooms.wall_colors)

    def test_condition(self):
        wall = rooms.Walls()
        self.assertIn(wall.condition, rooms.wall_conditions)


class RoomTests(unittest.TestCase):
    """This tests our Room class."""
    def setUp(self):
        self.test_room = rooms.Room()

    def tearDown(self):
        pass

    def test_whether_room_has_walls(self):
        print(self.test_room.walls)
        self.assertTrue(self.test_room.walls is not None)


if __name__ == "__main__":
    unittest.main()
