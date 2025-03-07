findletters = "rbfe"
findletters = findletters.lower()
works = []

with open("Dictionary.txt") as dictionary:
    for i, line in enumerate(dictionary.readlines()):
        line = line.strip().lower()
        currfindindex = 0
        for charindex, char in enumerate(line):
            if char == findletters[currfindindex]:
                currfindindex += 1
                line = line[:charindex] + char.upper() + line[charindex+1:]
                if currfindindex == len(findletters):
                    works.append(line)
                    break

works.sort()
works.sort(key=len)
print(works)
