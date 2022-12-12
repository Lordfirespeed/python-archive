class TreasureHunter:
    numeral_values = {"M": 1000,
                      "D": 500,
                      "C": 100,
                      "L": 50,
                      "X": 10,
                      "V": 5,
                      "I": 1}

    def tokenize_roman_numerals(self, numerals: str) -> tuple[str, ...]:
        if len(numerals) == 1:
            return numerals[0],

        if self.numeral_values[numerals[-1]] > self.numeral_values[numerals[-2]]:
            return self.tokenize_roman_numerals(numerals[:-2]) + (numerals[-2:],)

        return self.tokenize_roman_numerals(numerals[:-1]) + (numerals[-1],)

    def numeral_value(self, numeral: str):
        if len(numeral) > 2:
            raise ValueError

        if len(numeral) == 2:
            return self.numeral_values[numeral[1]] - self.numeral_values[numeral[0]]

        return self.numeral_values[numeral]

    def parse_roman_numerals(self, numerals: str) -> int:
        if len(numerals) == 0:
            return 0
        return sum(self.numeral_value(token) for token in self.tokenize_roman_numerals(numerals))
