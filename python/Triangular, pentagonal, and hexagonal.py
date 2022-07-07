import time

def findTriangulars():
    return [int(i*(i+1)/2) for i in range(285,100000)]

def findPentagonals():
    return [int(i*(3*i-1)/2) for i in range(165,100000)]

def findHexagonals():
    return [int(i*(2*i-1)) for i in range(143,100000)]

triangular = set(findTriangulars())
pentagonal = set(findPentagonals())
hexagonal = set(findHexagonals())
tripenta = set.intersection(triangular,pentagonal,hexagonal)
print(tripenta)
print("elapsed time:", time.process_time())