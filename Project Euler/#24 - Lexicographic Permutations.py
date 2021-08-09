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

print("".join(str(i) for i in permutations[1_000_000-1]))
