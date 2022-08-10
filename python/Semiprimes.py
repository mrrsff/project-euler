from eulerLibrary import list_primes
import time

LIMIT = 100000000
primecnt = 0
primes = list_primes(LIMIT // 2 + 200)
lastj = len(primes)-1
for i in range(len(primes)):
    for j in range(lastj,i-1,-1):
        if primes[i] * primes[j] < LIMIT:
            lastj = j
            primecnt += j-i+1
            break

print(f"Answer is {primecnt}. found in {time.process_time()} seconds.")
