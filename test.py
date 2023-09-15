import unittest
from craft_control import move

class Testing(unittest.TestCase):
    def test_movement(self):
        coordinates, direction = move([0, 0, 0], 'W', 'b')
        self.assertEqual(coordinates, [1, 0, 0])
        self.assertEqual(direction,'W')