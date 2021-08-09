with open("#67-input.txt") as inputfile:
    inputdata = [[int(i) for i in line.strip().split(" ")] for line in inputfile.readlines()]

sumtriangle = []

for index, numline in enumerate(inputdata[::-1]):
    if index == 0:
        sumtriangle.append(numline)
    else:
        sumtriangle.append([])
        for numi, num in enumerate(numline):
            sumtriangle[index].append(num + max([sumtriangle[index-1][numi], sumtriangle[index-1][numi+1]]))

sumtriangle.reverse()

print("Maximum path sum in the triangle: %s" % sumtriangle[0][0])
