def findDivisorNum(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    total = []
    for factor in set(factors):
        total.append(factors.count(factor))
    ans = 1
    for k in total:
        ans *= k+1
    return ans



a = 1
triangleNum = 0
while 1:
    triangleNum += a
    a += 1
    if findDivisorNum(triangleNum)>500:
        print(triangleNum)
        break