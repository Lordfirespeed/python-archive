def checkpandigital(string):
    string = "".join([str(c) for c in string if c.isdigit()])
    vals = [string.count(str(i)) for i in range(10)]
    if vals[0] > 0:
        return False
    else:
        return all([val == 1 for val in vals[1:]])


values = []
for operand in range(1, 9877):
    for multiplier in range(1, (10000//operand)+1):
        product = operand * multiplier
        if checkpandigital("%s * %s = %s" % (operand, multiplier, product)):
            values.append([operand, multiplier, product])

pandigitals = set([value[2] for value in values])
print("sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital: %s" % sum(pandigitals))
