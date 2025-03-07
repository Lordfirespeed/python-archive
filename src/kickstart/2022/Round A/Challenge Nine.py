class Solution:
    @staticmethod
    def sum_number_digits(numberString: str):
        total = 0
        for character in numberString:
            total += int(character)
        return total

    @staticmethod
    def make_number_nine_multiple_by_insertion(numberString: str):
        digitSum = Solution.sum_number_digits(numberString)
        numberToInsert = 9 - (digitSum % 9)

        if numberToInsert == 9:
            return numberString[0] + "0" + numberString[1:]

        insertAt = len(numberString)
        for index, character in enumerate(numberString):
            characterValue = int(character)
            if characterValue > numberToInsert:
                insertAt = index
                break

        nineMultipleNumberString = numberString[:insertAt] + str(numberToInsert) + numberString[insertAt:]
        return nineMultipleNumberString


if __name__ == "__main__":
    numberOfTestCases = int(input())
    solver = Solution()

    for testcaseIndex in range(1, numberOfTestCases + 1):
        inputNumberString = input()

        nineMultipleNumberString = solver.make_number_nine_multiple_by_insertion(inputNumberString)

        print(f"Case #{testcaseIndex}: {nineMultipleNumberString}")
