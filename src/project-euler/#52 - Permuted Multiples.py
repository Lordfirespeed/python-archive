def checkpermu(numlist):
    splitnumlist = [[int(i) for i in list(str(num))] for num in numlist]
    [numlist.sort() for numlist in splitnumlist]
    return splitnumlist.count(splitnumlist[0]) == len(splitnumlist)


found = False
num = 0
while not found:
    num += 1
    if checkpermu([num, 2 * num, 3 * num, 4 * num, 5 * num, 6 * num]):
        found = True

print("Smallest number x such that the specification occurs: %s" % num)
