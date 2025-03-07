from itertools import permutations
from math import sqrt
nums = range(1, 7)
check = permutations(nums, len(nums))
lengths = {}

for checknums in check:
    if ((checknums[0] + checknums[2]) / 2 == checknums[4]) and ((checknums[1] + checknums[3]) / 2 == checknums[5]):
        a = abs(checknums[2] - checknums[0])
        b = abs(checknums[3] - checknums[1])
        length = sqrt(a ** 2 + b ** 2)
        try:
            lengths[length]
        except KeyError:
            lengths[length] = []
        lengths[length].append(checknums)

largest = max(lengths.keys())  # 5.6568...
final = int(largest * 410 + 2)

print(largest, "->", final)  # 2321
