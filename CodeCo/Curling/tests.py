from solution import Curling
import unittest


class BriefCurlingTests(unittest.TestCase):

    def test1(self):
        solution = Curling()
        self.assertEqual(2.09, solution.push_stones(1.6, -0.6, 1.4, 1.8))

    def test2(self):
        solution = Curling()
        self.assertEqual(4.74, solution.push_stones(1.5, 0, 1.8, 0.707))

    def test4(self):
        solution = Curling()
        self.assertEqual(-1, solution.push_stones(1.8, 0, 1.75, 0.5))


class MarkingCurlingTests(unittest.TestCase):
    def test1(self):
        solution = Curling()
        self.assertEqual(2.09, solution.push_stones(1.6, -0.6, 1.4, 1.8))

    def test2(self):
        solution = Curling()
        self.assertEqual(4.74, solution.push_stones(1.5, 0, 1.8, 0.707))

    def test3(self):
        solution = Curling()
        self.assertEqual(-1, solution.push_stones(1.8, 0, 1.75, 0.5))

    def test4(self):
        solution = Curling()
        self.assertEqual(0, solution.push_stones(1.5, 0, 1.45, 0))

    def test5(self):
        solution = Curling()
        self.assertEqual(1, solution.push_stones(1.5, 0, 1.8, 0))

    def test6(self):
        solution = Curling()
        self.assertEqual(4.74, solution.push_stones(1.5, 0, 1.8, -0.707))

    def test7(self):
        solution = Curling()
        self.assertEqual(0.5, solution.push_stones(1.5, 0.5, 1.8, -0.5))

    def test8(self):
        solution = Curling()
        self.assertEqual(0.6, solution.push_stones(1.5, 0.6, 1.8, -0.6))

    def test9(self):
        solution = Curling()
        self.assertEqual(-1, solution.push_stones(1.8, 0, 1.2, 2.5))

    def test10(self):
        solution = Curling()
        self.assertEqual(1.5, solution.push_stones(1.8, 0, 1.5, -1.5))

    def test11(self):
        solution = Curling()
        self.assertEqual(2.02, solution.push_stones(1.2, 0, 1.5, -0.3))

    def test12(self):
        solution = Curling()
        self.assertEqual(5.57, solution.push_stones(1.4, 0, 1.8, -0.6))

    def test13(self):
        solution = Curling()
        self.assertEqual(4.56, solution.push_stones(1.35, 0, 1.9, -0.9))

    def test14(self):
        solution = Curling()
        self.assertEqual(4.66, solution.push_stones(1.35, 0, 1.8, -0.4))

    def test15(self):
        solution = Curling()
        self.assertEqual(-1, solution.push_stones(1.6, -0.5, 2, 0.3))

    def test16(self):
        solution = Curling()
        self.assertEqual(-1, solution.push_stones(1.5, -0.5, 2, 0.3))

    def test17(self):
        solution = Curling()
        self.assertEqual(1.72, solution.push_stones(1.5, 0, 1.8, 0.2))

    def test18(self):
        solution = Curling()
        self.assertEqual(1.0, solution.push_stones(1.5, 0, 1.5, 0))

    def test19(self):
        solution = Curling()
        self.assertEqual(0.5, solution.push_stones(1.525, 0, 1.475, 0))

    def test20(self):
        solution = Curling()
        self.assertEqual(0, solution.push_stones(1.5, 0, 1.45, 0))

    def test21(self):
        solution = Curling()
        self.assertEqual(0.5, solution.push_stones(1.525, 0, 1.525, -1))

    def test22(self):
        solution = Curling()
        self.assertEqual(0.98, solution.push_stones(1.525, 0, 1.525, 0.6))

    def test23(self):
        solution = Curling()
        self.assertEqual(0.05, solution.push_stones(1.54, 0.9, 1.59, 0.6))


class MyCurlingTests(unittest.TestCase):
    def test1(self):
        solution = Curling()
        self.assertEqual(0.6, solution.push_stones(-1.2, 0, 1.5, 0.6))


if __name__ == '__main__':
    unittest.main()
