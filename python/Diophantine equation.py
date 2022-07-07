import itertools
import math


def findxy(D):
    print(D)
    if int(math.sqrt(D)) == math.sqrt(D):
        return 1
    for y in itertools.count(1):
        x = math.sqrt(y * y * D + 1)

        if int(x) == x:
            return int(x)
    return 0


maxx = 0
maxindex = 0
for i in range(1, 1001):
    if findxy(i) > maxx:
        maxindex = i
        maxx = findxy(i)
