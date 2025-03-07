threedigits = list(range(999, 99, -1))

palindromeproducts = []
for indexa in threedigits:
    for indexb in threedigits:
        string = str(indexa * indexb)
        if string == string[::-1]:
            palindromeproducts.append(int(string))

print(max(palindromeproducts))
