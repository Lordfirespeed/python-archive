from solution import FigureSkating
import unittest


class FigureSkatingTests(unittest.TestCase):

    def test1(self):
        solution = FigureSkating()
        self.assertEqual(solution.evaluate_score_cards(
            ["1.25,-5,2.5,8.5,6.25,0.25,10", "2.5,-4.75,1.75,7.75,6.5,0.75,9.5", "2,-5,2.25,8.25,6.0,0.5,9.5"],
            [5, 4.25, 2]), 35)

    def test2(self):
        solution = FigureSkating()
        self.assertEqual(solution.evaluate_score_cards(
            ["-5.5,1.5,-0.75,-1.5,3.75,1.5,8.0,4.5,5.0", "-4.5,2.5,-1.25,-2.75,3.25,1.75,9.25,3.75,7.75",
             "-3.75,-0.25,0.25,-4.0,5.25,0.25,8.5,3.0,6.0", "-5.0,0.75,-0.75,0.0,3.75,1.5,10.0,2.25,6.0",
             "-4.5,1.25,-2.0,-1.0,5.75,0.25,10.0,4.5,10.25"], [7.25, 4.75, 5.25, 4, 1.25]), 40.3333)


if __name__ == '__main__':
    unittest.main()
