import eulerLibrary

primes = [i for i in range(1,10**5) if eulerLibrary.isPrime(i)]
consecutiveAmount = 0
maxPrime = 0
for limit in range(21,len(primes)):
    for i in range(len(primes)-limit):
        summation = sum(primes[i:i+limit])
        if summation<10**6 and eulerLibrary.isPrime(summation) and consecutiveAmount<limit:
            maxPrime = summation
            consecutiveAmount = limit
            print(maxPrime,consecutiveAmount)   