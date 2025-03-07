from string import ascii_uppercase as uppercase

with open("Resources/el-shabazz2.txt") as inputfile:
    inputlist = [line for line in inputfile.readlines()]
    inputstring = "".join([line.strip() for line in inputlist])

outputstring = [character for character in inputstring if character in uppercase]
print("".join(outputstring))

#with open("Resources/capitals-el-shabazz.txt", "w") as outputfile:
    #outputfile.write("".join(outputstring))
