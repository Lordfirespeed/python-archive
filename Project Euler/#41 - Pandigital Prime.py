def checkpandigital(string):
    string = "".join([str(c) for c in string if c.isdigit()])
    vals = [string.count(str(i)) for i in range(10)]
    if vals[0] > 0:
        return False
    else:
        return all([val == 1 for val in vals[1:]])


def efficientprime(number):
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


primefound = False
i = 10
while not primefound:
    values = list(range(1, i))
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

    numbers = [int("".join([str(c) for c in nums])) for nums in permutations[::-1]]

    for num in numbers:
        if efficientprime(num):
            print("Largest pandigital prime: %s" % num)
            primefound = True
            break
    i -= 1
