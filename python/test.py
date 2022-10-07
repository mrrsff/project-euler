def isPrime(num):
    num = abs(num)
    if num <= 3:
        return num > 1
    if not num % 2 or not num % 3:
        return False
    i = 5
    stop = int(num ** 0.5)
    while i <= stop:
        if not num % i or not num % (i + 2):
            return False
        i += 6
    return True 
def isPrime_miller_rabin(n):
    d = n - 1
    if not n % 2:
        return False
    while not (d & 1):
        d = d >> 1
    if not miller_rabin(n, d):
        return False
    return True

def chooseTest(n):
    if n < 1373653:
        return [2, 3]
    if n < 25326001:
        return [2, 3, 5]
    if n < 2152302898747:
        return [2, 3, 5, 7, 11]
    if n < 341550071728321:
        return [2, 3, 5, 7, 11, 13, 17]
    if n < 3825123056546413051:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23]

def miller_rabin(n, d):
    tests = chooseTest(n)
    for a in tests:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d = d << 1
            if x == n - 1:
                return True
            if x == 1:
                continue
    return False 

for i in range(100000):
    print(isPrime(i))
    print(isPrime_miller_rabin(i))