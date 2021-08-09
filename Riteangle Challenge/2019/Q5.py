import itertools

works = []
for nums in itertools.product(range(1, 10), repeat=4):
    a, b, c, d = nums
    if (d*1000 + a*100 + b*10 + c) - (a*1000 + b*100 + c*10 + d) + 2 == (d*100 + c*11):
        works.append(nums)

# a,b,c,d = (1,8,9,2)
