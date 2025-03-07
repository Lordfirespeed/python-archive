from math import factorial

values = []
for i in range(10, 2540162):
    if i == sum([factorial(int(c)) for c in str(i)]):
        values.append(i)

print("The sum of the numbers equal to the factorials of their digits: %s" % sum(values))