from mortgage_calculator import MortgageCalculator
import unittest


class MortgageCalculatorTests(unittest.TestCase):

    def test1(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(2, 20000, 38000, 45000, 0), [0, 0, 0, 0])

    def test2(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(1, 18000, 29000, 0, 0), [145000, 11635.18, 232703.5, 20])

    def test3(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(2, 40000, 26000, 32000, 0), [290000, 23270.35, 465407.01, 20])

    def test4(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(1, 25000, 30000, 0, 5000), [150000, 12036.39, 240727.76, 12])

    def test5(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(1, 18000, 29000, 0, 2000), [145000, 11635.18, 232703.5, 16])


if __name__ == '__main__':
    unittest.main()