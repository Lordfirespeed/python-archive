from solution import TreasureHunter
import unittest


class TreasureHunterTests(unittest.TestCase):
    numeral_tests = {
        "MCMLXI": 1961,
        "MMXV": 2015,
        "CCCIX": 309,
        "CCLXXXVI": 286,
        "LIV": 54,
        "XX": 20,
        "DXX": 520,
        "CCLXVII": 267,
        "CXXXV": 135,
        "CDLIV": 454,
        "DXXXVI": 536,
        "DCCLII": 752
    }

    @classmethod
    def populate(cls):
        for numeral, expected_value in cls.numeral_tests.items():
            setattr(cls, f"test_{numeral}", lambda self: self.generic_numeral_test(numeral, expected_value))

    def generic_numeral_test(self, numerals: str, expected: int) -> None:
        result = TreasureHunter()
        self.assertEqual(expected, result.parse_roman_numerals(numerals))


TreasureHunterTests.populate()

if __name__ == '__main__':
    unittest.main()
