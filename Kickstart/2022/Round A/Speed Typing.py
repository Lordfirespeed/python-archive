class Solution:
    @staticmethod
    def number_of_characters_to_remove(stringI, stringP):
        characterStack = list(stringI)
        for character in stringP:
            if character == characterStack[0]:
                characterStack.pop(0)
            if len(characterStack) == 0:
                return len(stringP) - len(stringI)
        return "IMPOSSIBLE"


if __name__ == "__main__":
    numberOfTestCases = int(input())
    solver = Solution()

    for testcaseIndex in range(1, numberOfTestCases + 1):
        inputI = input()
        inputP = input()

        charactersToRemove = solver.number_of_characters_to_remove(inputI, inputP)

        print(f"Case #{testcaseIndex}: {charactersToRemove}")
