with open("#59-xortext.txt") as inputfile:
    inputline = [line.strip() for line in inputfile.readlines()][0]

inputdata = [int(i) for i in inputline.split(",")]

output = []
dictoutput = dict(output)

for charnumone in range(97, 123):
    charone = chr(charnumone)
    for charnumtwo in range(97, 123):
        chartwo = chr(charnumtwo)
        for charnumthree in range(97, 123):
            charthree = chr(charnumthree)
            keynums = [charnumone, charnumtwo, charnumthree]
            decodestr = charone + chartwo + charthree
            decodednums = [keynums[i % 3] ^ n for i, n in enumerate(inputdata)]
            decodedchars = [chr(n) for n in decodednums]
            output.append([decodestr, "".join(decodedchars), decodednums])

possible = {}
possiblenums = []
for key, string, nums in output:
    if "the" in string and "and" in string:
        possible[key] = nums

print("Possible: %s" % ", ".join(possible.keys()))
key = "god"  # The key was "god"

print("Sum of ASCII values of decrypted data: %s" % sum(possible[key]))

