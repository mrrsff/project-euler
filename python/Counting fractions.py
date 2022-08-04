from math import gcd

LIMIT = 10**6+1
properFractions = 0
for d in range(1,LIMIT):
    print("%", round(100 * d / LIMIT,3) , end="\r")
    for n in range(1,d):
        if gcd(d,n) == 1:
            properFractions += 1
print(properFractions)