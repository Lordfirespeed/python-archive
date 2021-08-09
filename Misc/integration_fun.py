from sympy import symbols, sympify, pi, sqrt, integrate, cos, sin, tan, ln, E, oo
from numpy import base_repr

x = symbols("x", positive=True)

questions = [
    [(2*x+1) * cos(x), 0, pi/2, "A"],
    [((3 * cos(x)) - sin(x)), 0, pi/4, "B"],
    [sqrt(1+4*x), 0, 2, "E"],
    [cos(2*x), 0, pi/4, "E"],
    [(x**3 * ln(2*x)), 1, 2, "F"],
    [((1+E**x)/(x+E**x)), 0, 1, "I"],
    [2**x, -oo, 1, "N"],
    [x*sqrt(1+x), 0, 1, "N"],
    [sqrt(1+2*x), -0.5, 4, "O"],
    [(3 - 2*x) ** 4, -1, 1, "R"],
    [(x/(sqrt(1+x))), 0, 3, "S"],
    [2*x*E**(-3*x), 0, 1, "T"],
    [1/x, 1, 2, "T"],
    [E**(3*x), 0, 2, "U"],
    [x*E**(-x), 0, 1, "W"],
    [x*sin(2*x), 0, pi/2, "Y"]
]

answers = {sympify(integrate(question[0], (x, question[1], question[2]))): question[3] for question in questions}
answers = dict(sorted(answers.items()))

print("".join([letter for answer, letter in answers.items()]))  # TWENTY IN BASE FOUR
print("One of the 'N' questions is wrong, the answer should read 'TWENTYINBASEFOUR' - the 2**x question's N needs shifting 3 characters left")
print(base_repr(20, base=4))
