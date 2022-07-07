def findIntegerTris(p):
    tris = []
    for a in range(1, p//2 + 1):
        for b in range(1, p//2+1):
            c = ((a**2)+(b**2))**0.5
            if a + b + c == p:
                tris.append([a, int(b), int(c)])
    return int(len(tris)/2)

maxs = [0,0]
for p in range(2,1001):
    count = findIntegerTris(p)
    if count>maxs[1]:
        print(p)
        maxs[0] = p
        maxs[1] = count

