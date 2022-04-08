with open("../CodeCo/Curling/testcases.txt") as testcasesfile:
    testString = """    [Test]
    public void Test%s()
    {
        var solution = new Curling();
        
        Assert.AreEqual("""
    tests = [testString % index + (line.strip() % "solution.push_stones") + "\n\t}" for index, line in enumerate(testcasesfile.readlines(), 1)]

print("\n\n".join(tests))
