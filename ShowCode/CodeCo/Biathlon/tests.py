from solution import Biathlon
import unittest


class BiathlonTests(unittest.TestCase):

    def test1(self):
        solution = Biathlon()
        self.assertEqual(solution.find_winners([1000, 3000, 8400, 800, 5000], 600, ["1,7.2,5", "2,6.8,8"]), [2])

    def test2(self):
        solution = Biathlon()
        self.assertEqual(solution.find_winners([2000, 1800, 3400, 3700, 9300], 800, ["1,7.2,5", "2,6.8,8", "3,6.8,7"]),
                         [2, 3])


if __name__ == '__main__':
    unittest.main()
