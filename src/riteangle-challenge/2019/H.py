

squares = [0]
n = 1
while squares[-1] < 100:
    squares.append(n ** 2)
    n += 1

cubes = [0]
n = 1
while cubes[-1] < 100:
    cubes.append(n ** 3)
    n += 1

nums = dict([(i, set()) for i in range(99)])
othernums = dict([(i, set()) for i in range(99)])
squares, cubes = squares[:-1], cubes[:-1]
for square in squares:
    for cube in cubes:
        #print(square, cube)
        val = square + cube
        if val < 100:
            nums[val].add(tuple(sorted([square, cube])))
            othernums[val].add((square, cube))

total = 0
for n, ways in zip(nums.keys(), nums.values()):
    if len(ways) > 1:
        print(n, ways)
        total += n

print(total)
print(total * 69534)

total = 0
for n, ways in zip(othernums.keys(), othernums.values()):
    if len(ways) > 1:
        print(n, ways)
        total += n

print(total)
print(total * 69534)
