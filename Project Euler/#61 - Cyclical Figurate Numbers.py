pnums = __import__("#61-2 - Cyclical Figurate Numbers - Polygonal")


def permute(values):
    values = list(values)
    values.sort()
    end = list(values[::-1])
    permutations = [list(values)]
    current = list(values)
    while current != end:
        indexk = max([index for index in range(len(current)-1) if current[index] < current[index+1]])
        indexl = max([index for index in range(indexk, len(current)) if current[indexk] < current[index]])
        current[indexk], current[indexl] = current[indexl], current[indexk]
        current[indexk+1:] = current[:indexk:-1]
        permutations.append(list(current))
    return permutations


tris = [[n, pnums.triangle(n)] for n in range(45, 141)]  # T(45) = first 4 digit, T(140) = last 4 digit
squares = [[n, pnums.square(n)] for n in range(32, 100)]  # S(32) = first 4 digit, S(99) = last 4 digit
pentas = [[n, pnums.pentagonal(n)] for n in range(26, 82)]  # P(26) = first 4 digit, P(81) = last 4 digit
hexas = [[n, pnums.hexagonal(n)] for n in range(23, 71)]  # Hx(23) = first 4 digit, H(70) = last 4 digit
heptas = [[n, pnums.heptagonal(n)] for n in range(21, 64)]  # Hp(21) = first 4 digit, Hp(63) = last 4 digit
octas = [[n, pnums.octagonal(n)] for n in range(19, 59)]  # O(19) = first 4 digit, O(58) = last 4 digit

possible = []

# The following code doesn't work, and is unlikely to.
# I wrote it after having interpreted the problem incorrectly.

for triI, triN in tris:
    cusquares = list(squares)
    delsquindexes = {int(triI)}
    cusquares = [[i, n] for i, n in cusquares if i not in delsquindexes]
    tribegins = [str(triN)[:2]]
    triends = [str(triN)[2:]]
    cusquares = [[i, n] for i, n in cusquares if (str(n)[2:] in tribegins) or (str(n)[:2] in triends)]

    for squI, squN in cusquares:
        cupentas = list(pentas)
        delpenindexes = set(delsquindexes)
        delpenindexes.add(int(squI))
        cupentas = [[i, n] for i, n in cupentas if i not in delpenindexes]
        squbegins = tribegins.copy() + [str(squN)[:2]]
        squends = triends.copy() + [str(squN)[2:]]
        cupentas = [[i, n] for i, n in cupentas if (str(n)[2:] in squbegins) or (str(n)[:2] in squends)]

        for penI, penN in cupentas:
            cuhexas = list(hexas)
            delhexindexes = set(delpenindexes)
            delhexindexes.add(int(penI))
            cuhexas = [[i, n] for i, n in cuhexas if i not in delhexindexes]
            penbegins = squbegins.copy() + [str(penN)[:2]]
            penends = squends.copy() + [str(penN)[2:]]
            cuhexas = [[i, n] for i, n in cuhexas if (str(n)[2:] in penbegins) or (str(n)[:2] in penends)]

            for hexI, hexN in cuhexas:
                cuheptas = list(heptas)
                delhepindexes = set(delhexindexes)
                delhepindexes.add(int(hexI))
                cuheptas = [[i, n] for i, n in cuheptas if i not in delhepindexes]
                hexbegins = penbegins.copy() + [str(hexN)[:2]]
                hexends = penends.copy() + [str(hexN)[2:]]
                cuheptas = [[i, n] for i, n in cuheptas if (str(n)[2:] in hexbegins) or (str(n)[:2] in hexends)]

                for hepI, hepN in cuheptas:
                    cuoctas = list(octas)
                    deloctindexes = set(delhepindexes)
                    deloctindexes.add(int(hepI))
                    cuoctas = [[i, n] for i, n in cuoctas if i not in deloctindexes]
                    hepbegins = hexbegins.copy() + [str(hepN)[:2]]
                    hepends = hexends.copy() + [str(hepN)[2:]]
                    cuoctas = [[i, n] for i, n in cuoctas if (str(n)[2:] in hepbegins) or (str(n)[:2] in hepends)]

                    for octI, octN in cuoctas:
                        nums = [triN, squN, penN, hexN, hepN, octN]
                        possible.append(nums)

found = False
length = len(possible)
for numsi, nums in enumerate(possible):
    for check in permute(nums):
        works = True
        for i in range(-1, len(check)-1):
            works = False if str(check[i])[2:] != str(check[i+1])[:2] else works
        if works:
            found = check.copy()
            break
    if found:
        break
    if numsi % 15 == 0:
        print("Completed %s of %s possible sequence checks." % (numsi, length))

if found:
    print("FOUND SEQUENCE!")
    print(found)
    print("Sum: %s" % sum(found))
