import unittest
from kol1 import Plane


class MyTest(unittest.TestCase):
    def setUp(self):
        self.plane = Plane()

    def test_plane_instantiation(self):
        self.assertIsNotNone(self.plane)

    def test_get_random_current_orientation(self):
        self.plane2 = Plane()
        self.assertNotEqual(self.plane.get_current_orientation(), self.plane2.get_current_orientation())

    def test_get_current_orientation_lesser_than_360(self):
        self.assertLess(self.plane.get_current_orientation(), 360)

    def test_get_current_orientation_greater_than_0(self):
        self.assertGreater(self.plane.get_current_orientation(), 0)

    def test_correct_orientation(self):
        current_orientation = 200
        max_correction_step = 40
        self.assertEqual(self.plane.correct_orientation(current_orientation, max_correction_step), 180)

    def test_correct_orientation_step(self):
        current_orientation = 200
        max_correction_step = 10
        self.assertEqual(self.plane.correct_orientation(current_orientation, max_correction_step), 190)

    def test_correct_orientation_no_correction(self):
        current_orientation = 180
        max_correction_step = 20
        self.assertEqual(self.plane.correct_orientation(current_orientation, max_correction_step), 180)

    def test_correct_orientation_correction_direction_below(self):
        current_orientation = 100
        max_correction_step = 20
        self.assertLess(self.plane.correct_orientation(current_orientation, max_correction_step), 180)

    def test_correct_orientation_correction_direction_above(self):
        current_orientation = 230
        max_correction_step = 20
        self.assertGreater(self.plane.correct_orientation(current_orientation, max_correction_step), 180)

    def test_get_valid_orientation_after_n_steps(self):
        current_orientation = 130
        max_correction_step = 20
        step = 0
        while current_orientation != 180:
            current_orientation = self.plane.correct_orientation(current_orientation, max_correction_step)
            step += 1

        self.assertEqual(step, 3)

    def test_orientation_not_normalized_to_360(self):
        current_orientation = 480
        equivalent_orientation = 120
        max_correction_step = 20
        step_curr = step_eq = 0

        while current_orientation != 180:
            current_orientation = self.plane.correct_orientation(current_orientation, max_correction_step)
            step_curr += 1

        while equivalent_orientation != 180:
            equivalent_orientation = self.plane.correct_orientation(equivalent_orientation, max_correction_step)
            step_eq += 1

        self.assertNotEqual(step_curr, step_eq)
        # no normalization in implementation

    def test_get_valid_number_of_steps_for_different_max_correction(self):
        current_orientation1 = 130
        current_orientation2 = current_orientation1
        max_correction_step1 = 20
        max_correction_step2 = 40
        step1 = 0
        step2 = 0
        while current_orientation1 != 180:
            current_orientation1 = self.plane.correct_orientation(current_orientation1, max_correction_step1)
            step1 += 1

        while current_orientation2 != 180:
            current_orientation2 = self.plane.correct_orientation(current_orientation2, max_correction_step2)
            step2 += 1

        self.assertNotEqual(step1, step2)


if __name__ == '__main__':
    unittest.main()
