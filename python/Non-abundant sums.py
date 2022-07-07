import functools


@functools.cache
def isAbundant(n):
    sumOfDivisors = 1
    for x in range(2, (n//2 + 1)):
        if n % x == 0:
            sumOfDivisors += x
    return sumOfDivisors > n

abundants = [number for number in range(1,28124) if isAbundant(number)]
abundantSums = set()
for one in abundants:
    for two in abundants:
        if one+two<28124:
            abundantSums.add(one+two)
        else:
            break

print(sum([number for number in range(1,28124) if number not in abundantSums]))