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
        self.assertTrue(self.test_room.walls is not None)

    def test_whether_things_in_room_returns_dict(self):
        # TO DO: Implemeent
        pass
        # self.assertEqual(dict, type(self.test_room.things_in_room()))

    def test_whether_flat_object_returns_list(self):
        self.assertEqual(list, type(self.test_room.things_inside(flat=True)))


class CabinetTests(unittest.TestCase):
    """Tests our cabinet objects."""
    def setUp(self):
        self.test_cabinet = rooms.Cabinet()

    def tearDown(self):
        pass

    def test_inspecting_cabinet(self):
        """inspect() method should return str"""
        self.assertEqual(str, type(self.test_cabinet.inspect()))

    def test_material(self):
        self.assertIn(self.test_cabinet.material, rooms.cabinet_material)


class DoorTests(unittest.TestCase):
    """Test our door objects"""
    def setUp(self):
        self.test_door = rooms.Door()

    def tearDown(self):
        pass

    def test_inspection_method(self):
        self.test_door.locked = True
        self.test_door.deadbolt = True
        message = self.test_door.inspect()
        self.assertEqual(
            'The door has a deadbolt. You try the door. It is locked. ',
            message
        )


if __name__ == "__main__":
    unittest.main()
