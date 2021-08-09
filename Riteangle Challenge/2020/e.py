from itertools import product

for listn in product(range(0, 10), repeat=7):
    if listn[0] != "0":
        strn = "".join([str(c) for c in listn])
        n = int(strn)
        for remove_index in range(len(strn)):
            strm = strn[:remove_index] + strn[remove_index+1:]
            if strm[0] != "0":
                m = int(strm)
                if m + n == 7654321:
                    print(f"{m}, {n}")
