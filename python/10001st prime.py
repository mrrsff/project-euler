from math import sqrt
import time

def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

primes = []
n = 1
while len(primes) < 10001:
    if is_prime(n):
        primes.append(n)
    n += 1

print(primes[-1])
print("time elapsed: ", time.process_time())