def divide(n, d, p):
    i = 0  # Counts the cycles
    remainders = set()  # Empty set of remainders

    while i < p:
        if n < d:
            n = n * 10  # If the numerator < denominator, multiply by 10

        n = n % d  # sets the remainder as the new numerator
        if n in remainders:  # If this is repeated remainder, we have reached the end of a repeating cycle
            return d, i  # Returns the denominator and the length of the repeating decimal
        else:
            remainders.add(n)  # Adds the new remainder to set of remainders

        i = i + 1


longest = [0, 0]
largest_denominator = 1000

for x in range(2, largest_denominator + 1):
    y = divide(1, x, x)  # p = x due to upper bound on length of repeating decimal (see above)
    if y[1] > longest[1]:
        longest = y

print('1 / %s has longest recurring decimal (length = %s) for denominators less than %s' % (longest[0], longest[1], largest_denominator))
