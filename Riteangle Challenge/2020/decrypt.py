from math import sqrt

long = "43523731911734141372331417123317193375174111977417337233141613174113732971231373417123132731319337753171913617111361317416131741137337233133743523737123137319337"


def prime(number):
    if number == 1 or number == 0:
        return False
    for x in range(2, int(sqrt(number))):
        if not (number % x):
            return False
    return True


# currindex = 0
# while currindex < len(long):
#     seen_prime = False
#     takelength = 0
#     for length in range(2, 1, -1):
#         n = int(long[currindex:currindex+length])
#         if prime(n):
#             seen_prime = n
#             takelength = length
#             break
#     print(seen_prime)
#     currindex = currindex + takelength

def getprimeindices(primes):
    primes = [int(n) for n in primes.split(" ")]
    primelist = [n for n in range(max(primes)+1) if prime(n)]
    return " ".join([str(primelist.index(n)+1) for n in primes])


long2 = """14 3 9 21 8 5 21 13 13
12 9 11 13 20 9 2 7 8 2 12
3 7 13 5 8 4 4 13 21 12 9 11 13
18 11 4 13 6 21 10 20 9 6 21 13
20 9 6 1 4 11 2 8 12 4 16 7 8
6 18 20 5 2 18 2 7 13
18 11 4 13 6 21 12 9 11 2 12
14 3 9 21 20 9 6 21 8 2 12"""

from string import ascii_lowercase

long3 = long2.split("\n")
long4 = [[int(c) for c in line.split(" ")] for line in long3]

long45 = "".join([ascii_lowercase[n-1] for row in long4 for n in row])

long5 = [[] for x in range(max([len(row) for row in long4]))]
for row in long4:
    for i, u in enumerate(row):
        long5[i].append(u)

long6 = [n for row in long5 for n in row]

long7 = "".join([ascii_lowercase[n-1] for n in long6])
