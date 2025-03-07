from itertools import product
from math import sqrt


def match(num):
    numstr = "".join([c if i % 2 == 0 else "_" for i, c in enumerate(str(num))])
    return numstr == number


number = "1_2_3_4_5_6_7_8_9_0"

start = int(sqrt(1020304050607080900))
end = int(sqrt(1929394959697989990)) + 1

for i in range(start, end+1, 10):
    if match(i ** 2):
        print(i)
        break
