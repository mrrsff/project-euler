from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

primes = [2]
n = 3
while 1:
    if is_prime(n):
        primes.append(n)
    n+=1
    if primes[-1] > 2000000:
        break

print(sum(primes[:-1]))