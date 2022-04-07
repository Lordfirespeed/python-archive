from solution import Curling
import unittest


class CurlingTests(unittest.TestCase):

    def test1(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.6, -0.6, 1.4, 1.8), 2.09)

    def test2(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, 0.707), 4.74)

    def test3(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, -0.707), 4.74)

    def test4(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.8, 0, 1.75, 0.5), -1)

    def test5(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, 0), 1)

    def test6(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.45, 0), 0)


class ActualCurlingTests(unittest.TestCase):
    def test1(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.6, -0.6, 1.4, 1.8), 2.09)

    def test2(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, 0.707), 4.74)

    def test3(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.8, 0, 1.75, 0.5), -1)

    def test4(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.45, 0), 0)

    def test5(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, 0), 1)

    def test6(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, -0.707), 4.74)

    def test7(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0.5, 1.8, -0.5), 0.5)

    def test8(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0.6, 1.8, -0.6), 0.6)

    def test9(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.8, 0, 1.2, 2.5), -1)

    def test10(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.8, 0, 1.5, -1.5), 1.5)

    def test11(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.2, 0, 1.5, -0.3), 2.02)

    def test12(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.4, 0, 1.8, -0.6), 5.57)

    def test13(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.35, 0, 1.9, -0.9), 3.25)

    def test14(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.35, 0, 1.8, -0.4), 8.73)

    def test15(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.6, -0.5, 2, 0.3), -1)

    def test16(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, -0.5, 2, 0.3), 6.09)

    def test17(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, 0.2), 6.91)

    def test18(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.5, 0), 1.0)

    def test19(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.525, 0, 1.475, 0), 0.5)

    def test20(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.45, 0), 0)

    def test21(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.525, 0, 1.525, -1), 0.5)

    def test22(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.525, 0, 1.525, 0.6), 1.08)

    def test23(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.54, 0.9, 1.59, 0.6), 1.25)


class MyCurlingTests(unittest.TestCase):
    def test1(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(-1.2, 0, 1.5, 0.6), 0.6)


if __name__ == '__main__':
    unittest.main()
