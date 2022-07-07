def is_prime(x):
    if x <= 1:
        return 0
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return 0
        return x

def findPrimeFactors(n):
    factors = 0
    for i in primes:
        if i>n:
            break
        if not n % i:
            factors += 1
    return factors

primes = [i for i in range(1,150000) if is_prime(i)==i]
limit = 4
for i in range(1,150000):
    print(i)
    if findPrimeFactors(i)==limit and findPrimeFactors(i+1)==limit and findPrimeFactors(i+2)==limit and findPrimeFactors(i+3)==limit:
        print("found",i) 
        break