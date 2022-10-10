from solution import TreasureHunter
import unittest


class TreasureHunterTests(unittest.TestCase):

    def test1(self):
        result = TreasureHunter()
        self.assertEqual(result.parse_roman_numerals("MCMLXI"), 1961)


if __name__ == '__main__':
    unittest.main()