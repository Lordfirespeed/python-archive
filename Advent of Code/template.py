class Solution:
    @staticmethod
    def foo():
        return "bar"


if __name__ == "__main__":
    with open(r"[year]/Input/[year]day[day](test).txt") as inputFile:
        inputLines = [line.strip() for line in inputFile.readlines()]

    solver = Solution(inputLines)
    result = solver.foo()
    print(f"bar: {result}")
