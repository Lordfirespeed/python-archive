power = 5
maxnum = power * 9**power
values = [n for n in range(10, maxnum+1) if sum([int(c) ** power for c in str(n)]) == n]
print("Sum of all numbers that can be written as sum of specific power of their digits: %s" % sum(values))
