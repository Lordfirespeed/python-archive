import fractions

values = []
for numerator in range(10, 100):
    for denominator in range(10, 100):
        if str(numerator)[1] == str(denominator)[0] and numerator < denominator:
            try:
                if int(str(numerator)[0]) / int(str(denominator)[1]) == numerator / denominator:
                    values.append([numerator, denominator])
            except ZeroDivisionError:
                pass

fractionvalues = [fractions.Fraction(num, denom) for num, denom in values]
result = fractions.Fraction(1, 1)
for fraction in fractionvalues:
    result *= fraction

print("The denominator of the product of the four non-trivial example fractions is: %s" % result.denominator)
