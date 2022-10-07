from time import process_time
from eulerLibrary import isPrime_miller_rabin, list_primes
from itertools import combinations

def concat(a,b):
    return int(str(a)+str(b))

def check(nums):
    for i,j in combinations(nums, 2):
        p1 = concat(i,j)
        p2 = concat(j,i)
        if not isPrime_miller_rabin(p1) or not isPrime_miller_rabin(p2):
            return False
    return True

primes = list_primes(20000)
sums = []
for a in primes:
    print(a)
    for b in primes:
        if b <= a:
            continue
        if check([a,b]):
            for c in primes:
                if c <= b:
                    continue
                if check([a,c]) and check([b,c]):
                    for d in primes:
                        if d <= c:
                            continue
                        if check([a,d]) and check([c,d]) and check([b,d]):
                            for e in primes:
                                if e <= d:
                                    continue
                                if check([a,e]) and check([b,e]) and check([c,e]) and check([d,e]):
                                    sums.append(a+b+c+d+e)
                                    print(a+b+c+d+e)
                                    print(process_time())