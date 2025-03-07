with open("../ShowCode/CodeCo/Curling/testcases.txt") as testcasesfile:
    testString = """    def test%s(self):
        solution = Curling()
        self.assertEqual(solution.push_stones("""
    tests = [testString % index + line.strip() + "), 0)" for index, line in enumerate(testcasesfile.readlines(), 1)]

print("\n\n".join(tests))
