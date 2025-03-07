from fractions import Fraction
from math import log2


class rainbow_generator:
    @staticmethod
    def generate_column(numerator: int, denominator: int) -> [bool]:
        fraction = Fraction(numerator, denominator)
        target = fraction.numerator
        up_to_power = int(log2(fraction.denominator))
        portion_powers = list(range(up_to_power-1, -1, -1)) + [0]
        portions = [2 ** power for power in portion_powers]
        result = []
        for portion in portions:
            if portion <= target:
                target -= portion
                result.append(True)
            else:
                result.append(False)
        return result

    @staticmethod
    def generate_pattern(height: int) -> [[str]]:
        denominator = 2 ** (height - 1)
        result = []
        for numerator in range(0, denominator):
            column_top_down = rainbow_generator.generate_column(numerator, denominator)
            column = column_top_down[::-1]
            column = ["B" if element else "A" for element in column]
            column += ["G" for _ in range(height - len(column))]
            result.append(column)

        return result


if __name__ == "__main__":
    height = 6

    n_pattern = rainbow_generator.generate_pattern(height)
    patternLength = len(n_pattern[0])
    maxLineIndexLength = len(str(len(n_pattern) - 1))

    denominator = 2 ** (height - 1)
    fractionStrings = [str(Fraction(numerator, denominator)) for numerator in range(0, denominator)]
    maxFractionStringLength = max(*[len(fractionString) for fractionString in fractionStrings], 3)

    print("Output rows represents adjacent columns of blocks above beacon beams.\nG = Glass, A = Glass Colour A, B = Glass Colour B")
    print(f"{'BFA':>{maxFractionStringLength}} {'I':>{maxLineIndexLength}}: {'Pattern':^{patternLength}}")

    for line_index, line in enumerate(n_pattern):
        print(f"{fractionStrings[line_index]:>{maxFractionStringLength}} {line_index:>{maxLineIndexLength}}: {''.join(line)}")

