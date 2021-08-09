from string import ascii_uppercase as alphabet

with open("#22-input.txt") as inputfile:
    inputnames = [name.replace("\"", "") for name in inputfile.readline().split(",")]
inputnames.sort()

scores = []
for index, name in enumerate(inputnames, 1):
    scores.append(sum([alphabet.index(char)+1 for char in name]) * index)

print(sum(scores))
