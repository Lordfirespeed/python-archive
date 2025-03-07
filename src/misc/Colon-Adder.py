with open("Colon-Adder-Input.txt") as inputfile:
    inputlines = [line.strip() for line in inputfile.readlines()]

outputlines = [line + ":\n" for line in inputlines]

with open("Colon-Adder-Output.txt", "w") as outputfile:
    [outputfile.write(line) for line in outputlines]

