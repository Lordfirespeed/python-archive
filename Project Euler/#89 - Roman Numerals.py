r2i = {"I": 1,
       "V": 5,
       "X": 10,
       "L": 50,
       "C": 100,
       "D": 500,
       "M": 1000}

i2r = dict(zip(r2i.values(), r2i.keys()))


def romToInt(numeral):
    global r2i
    numeral = list(numeral.upper())
    val = 0
    index = 0
    while index < len(numeral):
        char = numeral[index]
        if char == "C":
            try:
                if numeral[index+1] == "M":
                    val += 900
                    index += 1
                elif numeral[index+1] == "D":
                    val += 400
                    index += 1
                else:
                    val += r2i[char]
            except IndexError:
                val += r2i[char]
        elif char == "X":
            try:
                if numeral[index+1] == "C":
                    val += 90
                    index += 1
                elif numeral[index+1] == "L":
                    val += 40
                    index += 1
                else:
                    val += r2i[char]
            except IndexError:
                val += r2i[char]
        elif char == "I":
            try:
                if numeral[index+1] == "X":
                    val += 9
                    index += 1

                elif numeral[index+1] == "V":
                    val += 4
                    index += 1
                else:
                    val += r2i[char]
            except IndexError:
                val += r2i[char]
        else:
            val += r2i[char]

        index += 1
    return val


def intToRom(num):
    global i2r
    global r2i
    splitnum = [int(c) for c in str(num)]
    numunits = [n * (10 ** i) for i, n in zip(range(len(splitnum)-1, -1, -1), splitnum)]
    numeral = ""
    for n in numunits:
        if n == 0:
            pass
        elif n == 900:
            numeral += "CM"
        elif n == 400:
            numeral += "CD"
        elif n == 90:
            numeral += "XC"
        elif n == 40:
            numeral += "XL"
        elif n == 9:
            numeral += "IX"
        elif n == 4:
            numeral += "IV"
        else:
            found = False
            possible = [v for v in i2r if v <= n]
            useval = max(possible)
            while not found:
                useval = max(possible)
                found = not n % useval
                if not found:
                    possible = possible[:-1]
            numeral += i2r[useval] * int(n / useval)
    numeral = list(numeral)
    i = 0
    while i+5 < len(numeral):
        if len(set(numeral[i:i+5])) == 1:
            if numeral[i] != "M":
                numeral[i:i+5] = i2r[list(i2r)[list(r2i).index(numeral[i])+1]]
            else:
                i += 1
        else:
            i += 1
    return "".join(numeral)


def charsSaved(numeral):
    return len(numeral) - len(intToRom(romToInt(numeral)))


with open("#89-roman.txt") as inputfile:
    inputlines = [line.strip() for line in inputfile.readlines()]

amount = sum([charsSaved(numeral) for numeral in inputlines])
# print(amount)
