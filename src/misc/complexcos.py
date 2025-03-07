import pascals
import fractions


def trigpower(mode, power):
    theta = "\u03F4"

    if mode == "cos":
        signs = [" + " for _ in range(int(power/2))]
    elif mode == "sin":
        signs = [" + " if _ % 2 else " - " for _ in range(int(power/2))]

    termcoefficients = (nums := pascals.pascal_line(power))[:int(len(nums) / 2) + 1]
    termcoefficients = [fractions.Fraction(n, 2 ** (power-1)) for n in termcoefficients]
    thetacoefficients = list(range(power, -1, -2))
    thetacoefficients.append(0) if thetacoefficients[-1] == 2 else None

    values = []
    for termcoeff, thetacoeff in zip(termcoefficients, thetacoefficients):
        if thetacoeff == 0:
            values.append(str(termcoeff / 2))
        elif thetacoeff == 1:
            values.append(str(termcoeff) + mode + "(" + theta + ")")
        else:
            values.append(str(termcoeff) + mode + "(" + str(thetacoeff) + theta + ")")

    message = "".join([value + sign for value, sign in zip(values, signs)]) + values[-1]
    return message
