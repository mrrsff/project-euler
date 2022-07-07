def findCombination(n,r):
    if n-r<r:
        r = n-r
    upper = 1
    for i in range(n,n-r,-1):
        upper *= i
    lower = 1
    for i in range(1,r+1):
        lower *= i
    return int(upper/lower)

ans = 0
for n in range(1,101):
    for r in range(1,n+1):
        if findCombination(n,r)>10**6:
            ans+= 1
print(ans)