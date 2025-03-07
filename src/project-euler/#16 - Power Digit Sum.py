power = 1000
value = 2 ** power
digits = [int(char) for char in str(value)]
print("Result: " + str(sum(digits)))
