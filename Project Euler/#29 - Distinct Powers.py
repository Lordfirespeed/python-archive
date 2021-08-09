abound = [2, 100]
bbound = [2, 100]
a = list(range(abound[0], abound[1]+1))
b = list(range(bbound[0], bbound[1]+1))

values = []
for aval in a:
    for bval in b:
        values.append(aval**bval)

values = list(set(values))
print("Number of distinct terms: %s" % len(values))
