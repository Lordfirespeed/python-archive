def i2h(integer):
    hexmap = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
        }

    hexlist = []
    number = integer
    temp = int(number)
    while True:
        hexlist.insert(0, hexmap[temp % 16])
        temp //= 16
        if str(int("".join(hexlist), 16)) == number:
            break

    finalhex = "".join(hexlist)
    #print("Hexidecimal '" + number + "' is '" + finalhex + "'.")
    return(finalhex)

def h2i(hexadecimal):
    return int(hexadecimal, 16)

