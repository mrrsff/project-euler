import time
import itertools


def findDivisors(n):
    i=2
    divs = []
    while i*i<n:
        if n%i==0:
            divs.append(i)
            divs.append(n//i)
        i+=1
    return sorted(divs)


def calculate():
    ans = 0
    for i in itertools.count(1000):
        if i>10**5:
            return ans
        divisors = findDivisors(i)
        for j in range(len(divisors)):
            mult1 = divisors[j]
            mult2 = divisors[-j-1]
            allstr = str(mult1) + str(mult2) + str(i)
            if len(allstr)==9 and set(map(int,list(allstr)))==set(range(1,10)):
                ans += i
                print(mult1,"*", mult2,"=", i, "sum:",ans, end="\r")
                break

print("\nanswer:",calculate()," elapsed time:", time.process_time())