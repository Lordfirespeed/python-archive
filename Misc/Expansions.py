from sympy import *
from math import factorial


def iterproduct(array):
    v = 1
    for thing in array:
        v *= thing
    return v


def nCr(n, r):
    if n == 0:
        return 0
    elif n > 0 and (type(n) == int or float(n).is_integer()):
        return nsimplify(factorial(n) / factorial(r) * factorial(n - r))
    else:
        return nsimplify(iterproduct([n - i for i in range(r)]) / factorial(r))


def expand(expr, precision=2):
    terms = expr.apart().as_ordered_terms()
    terms = [term.as_powers_dict() for term in terms]
    expansions = []
    for term in terms:
        termkeys, termvals = list(term.keys()), list(term.values())
        if len(term) == 1:
            expansions.append(termkeys[0])
        else:
            multiple = termkeys[0]
            a, b = termkeys[1].as_two_terms()
            power = termvals[1]
            expansions.append(Expansion(a, b, multiple).expand(power, precision))
    return sum(expansions)


class Expansion(object):
    def __init__(self, a, b, multiple=1):
        self.posExpansionOperandA = nsimplify(a)
        self.posExpansionOperandB = nsimplify(b)
        self.Multiple = nsimplify(multiple)
        self.negExpansionMultiple = self.posExpansionOperandA
        self.negExpansionOperand = nsimplify(self.posExpansionOperandB / self.posExpansionOperandA)

    def __repr__(self):
        return "(" + str(self.posExpansionOperandA + self.posExpansionOperandB) + ") ^ n"

    def __str__(self):
        return self.__repr__()

    def expand(self, power, precision=2):
        if power == 0:
            return self.Multiple
        elif power > 0 and (type(power) == int or float(power).is_integer()):
            return str(self.Multiple * ((self.Multiple + self.posExpansionOperandB) ** power).expand()).replace("**", "^")
        else:
            if precision < 2:
                precision = 2
            precision += 1
            terms = [nCr(power, index) * (self.negExpansionOperand ** index) for index in range(precision)]
            return self.Multiple * nsimplify(self.negExpansionMultiple ** power) * sum(terms)

    def estimate(self, values, power, precision=2):
        return self.expand(power, precision).subs(values)


init_printing(use_unicode=True, wrap_line=True, order=grlex)
x, y, z = symbols("x y z")
