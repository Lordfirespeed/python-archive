class Solution:
    def __init__(self, inputLines):
        self.inputLines = inputLines

    def foo(self):
        return len(self.inputLines)


if __name__ == "__main__":
    with open(r"Input\[year]day[day]test.txt") as inputFile:
        inputLines = [line.strip() for line in inputFile.readlines()]

    solver = Solution(inputLines)
    result = solver.foo()
    print(f"foo: {result}")
