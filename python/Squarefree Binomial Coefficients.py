from eulerLibrary import *


def pascalRow(n):
    ans = set()
    for i in range(1, n // 2 + 1):
        ans.add(combination(n, i))
    return ans


def pascalTriangle(n):
    ans = set()
    for i in range(1, n):
        for a in pascalRow(i):
            ans.add(a)
    return ans


def squareFree(n):
    if not n%4:
        return False
    for i in range(3, int(n**0.5)+2,2):
        if not isPrime(i):
            continue
        if not n%(i**2):
            return False
    return True


print(sum(i for i in pascalTriangle(51) if squareFree(i))+1)
