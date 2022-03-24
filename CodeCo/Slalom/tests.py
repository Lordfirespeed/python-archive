from solution import Slalom
import unittest


class SlalomTests(unittest.TestCase):

    def test1(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([10, -10, 10, -10, 10], 2), 81)

    def test2(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([-10, 5, -15, 0, -10, 10, -5], 3), 85.5)

    def test3(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([-9.7, 10.8, -5, 0, -21, 0, 5.1], 3.7421133), 77.5184)


if __name__ == '__main__':
    unittest.main()
