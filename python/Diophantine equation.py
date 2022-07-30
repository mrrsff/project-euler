import itertools
import math


def findxy(D):
    if int(math.sqrt(D)) == math.sqrt(D):
        return 1
    for x in itertools.count(2):
        if x % D == 1 or x % D == D - 1:
            continue
        print(D, x)
        y = ((x ** 2 - 1) / D) ** 0.5
        if int(y) == y:
            return int(x)


maxx = 0
maxindex = 0
for i in range(1, 1001):
    if findxy(i) > maxx:
        maxindex = i
        maxx = findxy(i)
