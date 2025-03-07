import json

def calcrebirths(value):
    multiplier = ((value - 100) // 75) + 1
    return ((value - 1) / multiplier)

data = {}
endpoint = 100 + (75 * 10000)
values = range(100, endpoint, 75)
for value in values:
    data[value] = calcrebirths(value)

with open("hmm.json", "w") as output:
    json.dump(data, output, ensure_ascii=False)

maxval = 100 + (75 * 100000000000000)
print(calcrebirths(maxval))
