from math import log


class BigExponential:
    def __init__(self, base: int, exponent: int) -> None:
        self.base = base
        self.exponent = exponent

    @property
    def value_as_natural_exponent(self):
        return self.exponent * log(self.base)

    def __gt__(self, other):
        if not isinstance(other, BigExponential):
            raise TypeError

        return self.value_as_natural_exponent > other.value_as_natural_exponent

    def __repr__(self):
        return f"{self.base}^{self.exponent}"


def main():
    with open("#99 - base_exp.txt") as input_file:
        highest_exponential = BigExponential(1, 0)
        highest_line_number = None
        for index, line in enumerate(input_file, 1):
            base, exponent = (int(num) for num in line.split(","))
            new_exponential = BigExponential(base, exponent)
            if new_exponential > highest_exponential:
                highest_exponential = new_exponential
                highest_line_number = index
        print(f"Highest exponential was {highest_exponential} on line #{highest_line_number}.")


if __name__ == "__main__":
    main()
