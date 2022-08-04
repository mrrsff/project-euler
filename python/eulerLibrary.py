def isPrime(num):
    num = abs(num)
    if num<=3:
        return num>1
    if not num%2 or not num%3:
        return False
    i = 5
    stop = int(num**0.5)
    while i <= stop:
        if not num%i or not num%(i+2):
            return False
        i+=6
    return True

def isPermutation(n,x):
    return sorted(list(str(n)))==sorted(list(str(x)))

def findDivisors(n):
    divisors = [1]
    i = 2
    while i*i<=n:
        if n%i == 0:
            divisors.append(i)
            divisors.append(n//i)
        i += 1
    return sorted(divisors)

def findRotations(num, rotation=1):
    digits = len(list(str(num)))
    if rotation>digits: return []
    rot = (num%10) * pow(10,digits-1) + (num//10)
    return [rot] + findRotations(rot,rotation+1)

def combination(n,r):
    if n-r<r:
        r = n-r
    upper = 1
    for i in range(n,n-r,-1):
        upper *= i
    lower = 1
    for i in range(1,r+1):
        lower *= i
    return int(upper/lower)

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def isPentagonal(n):
    return not (1+(1+24*n)**0.5) % 6

def findPentagonal(n):
    return n*(3*n-1)/2

def digitSum(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res

def getDigits(n):
    return sorted([int(i) for i in str(n)])