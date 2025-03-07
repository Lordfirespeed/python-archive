def primes(checkTo):
    primeList = [2]

    for num in range(3, checkTo+1):
        sqrtNum = num ** 0.5
        for checknum in primeList:
            if num % checknum == 0:
                break
            elif checknum > sqrtNum:
                primeList.append(num)
                break
            
    return primeList
