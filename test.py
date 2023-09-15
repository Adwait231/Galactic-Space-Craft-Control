import unittest
from craft_control import move
from command import execute

class Testing(unittest.TestCase):
    def test_movement(self):
        coordinates, direction = move([0, 0, 0], 'W', 'b')
        self.assertEqual(coordinates, [1, 0, 0])
        self.assertEqual(direction,'W')

    def test_execution(self):
        coordinates, direction = execute([0,0,0], 'N', 'frubl')
        self.assertEqual(coordinates, [0, 1, -1])
        self.assertEqual(direction,'N')