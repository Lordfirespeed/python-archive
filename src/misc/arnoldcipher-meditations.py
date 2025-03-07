from string import ascii_letters as letters

letters += " "

with open("meditations.txt") as inputfile:
    inputlines = [line.strip() for line in inputfile.readlines()]

for index, line in enumerate(inputlines):
    inputlines[index] = "".join([c for c in line if c in letters])

inputlines = [line.split() for line in inputlines]

pages = {}
newpage = inputlines.index([])
pages[7] = inputlines[:newpage]
pages[8] = inputlines[newpage+1:]

codestring = "07.10.07 07.16.02 08.19.07 08.13.06 08.06.05 07.16.02 08.14.02 08.01.04 08.09.10 07.12.04 08.08.09 08.15.04 07.16.02 07.01.03 07.33.03 08.01.04 07.23.07 07.31.11 07.27.02"
valuescodes = [[int(i) for i in code.split(".")] for code in codestring.split()]

output = []
for code in valuescodes:
    output.append(pages[code[0]][code[1]-1][code[2]-1])

print(" ".join(output))
