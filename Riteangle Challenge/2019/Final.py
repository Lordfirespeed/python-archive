from itertools import product

with open("Final Answers.txt") as answerfile:
    lines = [line.strip() for line in answerfile.readlines()]
    nums = [int(line[line.index(":")+2:]) for line in lines]

concatenated = "".join(str(n) for n in nums)
packeted = [int(concatenated[i:i+4]) for i in range(0, len(concatenated), 4)]
concatenated = int(concatenated)

grid = [["0" for _ in range(8)] for _ in range(8)]

grid = [[2, 2, 1, 2, 1, 2, 1, 3],
        [1, 2, 3, 3, 3, 2, 3, 3],
        [3, 1, 1, 2, 2, 1, 3, 3],
        [3, 1, 2, 1, 3, 1, 1, 3],
        [1, 2, 0, 0, 0, 3, 0, 2],
        [2, 2, 0, 0, 0, 2, 0, 2],
        [2, 3, 0, 0, 0, 3, 0, 1],
        [2, 1, 1, 3, 1, 2, 2, 3]]

unknown = len([v for row in grid for v in row if v == 0])

for inserts in product(range(1, 4), repeat=unknown):
    print(inserts)
    currinsertindex = 0
    currgrid = [line.copy() for line in grid]
    for yindex, row in enumerate(grid):
        for xindex, val in enumerate(row):
            if val == 0:
                currgrid[yindex][xindex] = inserts[currinsertindex]
                currinsertindex += 1
    ok = True
    for n in ([n for n in nums if len(str(n)) == 4]):
        if not any([str(n) in "".join([str(i) for i in line]) for line in grid]):
            if not any([str(n) in "".join([str(i) for i in line]) for line in list(zip(*grid))]):
                ok = False
                break
    if ok:
        [print(line) for line in grid]




