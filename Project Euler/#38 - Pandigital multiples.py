def checkpandigital(string):
    string = "".join([str(c) for c in string if c.isdigit()])
    vals = [string.count(str(i)) for i in range(10)]
    if vals[0] > 0:
        return False
    else:
        return all([val == 1 for val in vals[1:]])


largest = 0
for i in range(98766):
    rangenum = (len("987654321") // len(str(i))) + 1
    for end in range(1, rangenum+1):
        concatenated = "".join([str(i*n) for n in range(1, end+1)])
        largest = int(concatenated) if checkpandigital(concatenated) and int(concatenated) > largest else largest

print("Largest pandigital from concatenated products: %s" % largest)
