with open("#79-keylog.txt") as inputfile:
    codes = [[int(c) for c in list(line.strip())] for line in inputfile.readlines()]

completecode = list(codes[0])

changed = True
while changed:
    changed = False
    for code in codes[1:]:
        adjacents = [[completecode[i], completecode[i+1]] for i in range(len(completecode)-1)]
        ends = [code[0], code[2]]
        if ends in adjacents:
            if code[1] in completecode:
                if not completecode.index(code[0]) < completecode.index(code[1]) < completecode.index(code[2]):
                    pass
            else:
                completecode.insert(completecode.index(code[2]), code[1])
                changed = True
    print("Completed iteration")

# 73162890
