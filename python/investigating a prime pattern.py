import time
#
#
#   NOT FINISHED
#
#
#

def calculate():
    ans = 10
    MAX = 150 * (10 ** 6)
    for i in range(10, MAX, 10):
        print("%", round(i * 100 / MAX, 2), i, end="\r")
        if i % 3 == 0 or i % 7 == 0 or i % 13 == 0:
            continue
        square = i*i
        if square % 3 != 1 and square % 7 != 2:
            continue
        if isPrime(square+1) and isPrime(square+3) and isPrime(square+7) and isPrime(square+9) and isPrime(square+13) and isPrime(square+27) and not isPrime(
                square+19) and not isPrime(square+21):
            ans += i
    return ans

def isPrime(n):
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

if __name__ == "__main__":
    print("answer is:", calculate(), "\ntotal time elapsed:", time.process_time())
