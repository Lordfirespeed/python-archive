alphabet = "abcdefghijklmnopqrstuvwxyz"
alphadict = {}
for char in alphabet:
    alphadict[char] = char

griddict = {}
for index in range(len(alphabet)):
    griddict[alphabet[index]] = dict(alphadict)
    alphaiter = list(alphadict)
    alphaiter.reverse()
    for key in alphaiter[:-1]:
        newkey = alphabet[(alphabet.index(key) - 1)]
        alphadict[key], alphadict[newkey] = alphadict[newkey], alphadict[key]

a = "llkjmlmpadkkc"
b = "thisisalilkey"

output = []
for index in range(len(a)):
    output.append(griddict[b[index]][a[index]])
print("".join(output))
    
