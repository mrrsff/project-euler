from eulerLibrary import isPrime
import time

expr = [0,0,0]
primes = [i for i in range(3,1000,2) if isPrime(i)]
for a in range(-999, 1000, 2):
    if a == -1:
        continue
    for b in primes:
        n = 0
        while isPrime(n*n+a*n+b):
            n+=1
        if n > expr[-1]:
            expr = a,b,n
print("A sequence with the length of",expr[-1], ",created by a=",expr[0], ",b=",expr[1], ",the product is", expr[0]*expr[1])
print("took", round(time.process_time(),3),"seconds")