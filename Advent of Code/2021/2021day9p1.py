class Solution:
    pass

if __name__ == "__main__":
    with open(r"Input\2021day7.txt") as inputFile:
        inputNums = [int(number) for number in inputFile.readline().strip().split(",")]

    solver = Solution()
    result = solver.find_min_fuel_cost(inputNums)
    print(f"Minimum fuel cost {result}")
