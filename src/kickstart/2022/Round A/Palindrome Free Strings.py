from itertools import product
from dataclasses import dataclass


@dataclass
class State:
    state: str
    index: int


class Solution:
    def __init__(self):
        self.validFiveLengthStateMappings = {}

        self.generate_five_length_state_mappings()

    def generate_five_length_state_mappings(self):
        for initialState in self.generate_five_length_states():
            if self.five_length_palindrome_check(initialState):
                continue

            stateMapping = []

            appendZeroState = initialState + "0"
            appendOneState = initialState + "1"

            appendZeroStateIsPalindromic = self.combined_six_length_palindrome_check(appendZeroState)
            appendOneStateIsPalindromic = self.combined_six_length_palindrome_check(appendOneState)

            if not appendZeroStateIsPalindromic:
                stateMapping.append(appendZeroState[1:])

            if not appendOneStateIsPalindromic:
                stateMapping.append(appendOneState[1:])

            self.validFiveLengthStateMappings[initialState] = stateMapping

    def decide_no_palindromic_substrings(self, testString):
        if len(testString) < 5:
            return True

        initialStateString = testString[:5]

        possibleStates = [State(stateString, 0) for stateString in self.generate_possible_states_from_five_length_wildcard_string(initialStateString)]
        while possibleStates:
            extendingState = possibleStates.pop(0)
            if extendingState.index >= len(testString) - 5:
                return True

            extendsToStateStrings = self.validFiveLengthStateMappings[extendingState.state]
            for newStateString in extendsToStateStrings:
                newState = State(newStateString, extendingState.index+1)
                if self.check_state_fits_test_string(newState, testString):
                    possibleStates.append(newState)

        return False

    @staticmethod
    def check_state_fits_test_string(state, testString):
        wildcardedActualState = testString[state.index:state.index+5]
        for stateCharacter, testCharacter in zip(state.state, wildcardedActualState):
            if stateCharacter != testCharacter and testCharacter != "?":
                return False
        return True

    @staticmethod
    def generate_possible_states_from_five_length_wildcard_string(testString):
        if len(testString) != 5:
            raise ValueError
        numberOfWildcards = testString.count("?")
        stateStrings = []
        for substitutions in product("01", repeat=numberOfWildcards):
            newPossibleState = testString
            for substition in substitutions:
                newPossibleState = newPossibleState.replace("?", substition, 1)
            if not Solution.five_length_palindrome_check(newPossibleState):
                stateStrings.append(newPossibleState)
        return stateStrings

    @staticmethod
    def generate_five_length_states():
        return ["".join(characters) for characters in list(product("01", repeat=5))]

    @staticmethod
    def five_length_palindrome_check(testString):
        if len(testString) != 5:
            raise ValueError

        return testString[:2] == testString[:-3:-1]

    @staticmethod
    def six_length_palindrome_check(testString):
        if len(testString) != 6:
            raise ValueError

        return testString[:3] == testString[:-4:-1]

    @staticmethod
    def combined_six_length_palindrome_check(testString):
        if len(testString) != 6:
            raise ValueError

        if Solution.six_length_palindrome_check(testString):
            return True

        if Solution.five_length_palindrome_check(testString[:5]):
            return True

        if Solution.five_length_palindrome_check(testString[1:]):
            return True

        return False


if __name__ == "__main__":
    numberOfTestCases = int(input())
    solver = Solution()

    for testcaseIndex in range(1, numberOfTestCases + 1):
        length = input()
        result = solver.decide_no_palindromic_substrings(input())
        print(f"Case #{testcaseIndex}: {'POSSIBLE' if result else 'IMPOSSIBLE'}")
