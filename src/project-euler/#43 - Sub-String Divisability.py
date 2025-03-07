values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
values.sort()
end = list(values[::-1])
permutations = [list(values)]
current = list(values)
while current != end:
    indexk = max([index for index in range(len(current)-1) if current[index] < current[index+1]])
    indexl = max([index for index in range(indexk, len(current)) if current[indexk] < current[index]])
    current[indexk], current[indexl] = current[indexl], current[indexk]
    current[indexk+1:] = current[:indexk:-1]
    permutations.append(list(current))

numstrings = ["".join([str(c) for c in nums]) for nums in permutations]
print("Generated pandigital permutations for digits 0-9.")

divisors = [2, 3, 5, 7, 11, 13, 17]
values = []
for num in numstrings:
    valid = True
    for i in range(0, 7):
        if not int(num[i+1:i+1+3]) % divisors[i] == 0:
            valid = False
            break
    values.append(int(num)) if valid else None

print("Sum of all 0-9 pandigital numbers with this property: %s" % sum(values))
