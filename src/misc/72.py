from itertools import product


def zerone(length):
    numlists = product(["0", "1"], repeat=length)
    numlists = set(numlists) - set(product(["0", "1"], repeat=length-1))
    return [int("".join(nums)) for nums in numlists]


n = 0
found = False
while not found:
    n += 1
    checklist = zerone(n)
    for check in checklist:
        if check % 72 == 0 and check > 0 and check != 111111111000:
            print(check)
            found = True
            break
