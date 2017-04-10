import unittest
from kol1 import Simulation
from kol1 import Plane
import random

class MyTest(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_correct_orientaion(self):
       current_orientation = 200
       max_correction_step = 40
       self.assertEqual(self.plane.correct_orientation(current_orientation, max_correction_step), 180)

    def test_correct_orientaion_step(self):
        current_orientation = 200
        max_correction_step = 10
        self.assertEqual(self.plane.correct_orientation(current_orientation, max_correction_step), 190)

    def test_correct_orientaion__no_correction(self):
        current_orientation = 180
        max_correction_step = 20
        self.assertEqual(self.plane.correct_orientation(current_orientation, max_correction_step), 180)

    def test_get_current_orientation(self):
            self.assertNotEqual(self.plane.get_current_orientation(), random.randint(0, 360))
