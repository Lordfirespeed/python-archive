class Solution:
    @staticmethod
    def number_operations_to_change_string_to_k_goodness(testString, targetK):
        currentK = Solution.get_k_goodness(testString)
        return abs(currentK - targetK)

    @staticmethod
    def get_k_goodness(testString):
        kGoodness = 0
        for index in range(len(testString) // 2):
            if testString[index] != testString[-(index+1)]:
                kGoodness += 1
        return kGoodness


if __name__ == "__main__":
    numberOfTestCases = int(input())
    solver = Solution()

    for testcaseIndex in range(1, numberOfTestCases + 1):
        testStringLength, targetKValue = [int(n) for n in input().split(" ")]
        testString = input()
        numberOfOperations = solver.number_operations_to_change_string_to_k_goodness(testString, targetKValue)
        print(f"Case #{testcaseIndex}: {numberOfOperations}")
