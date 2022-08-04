ans = []
for a in range(3,1001):
    rmax = 0
    for n in range(1,a*2+1,2):
        r = (pow(a-1,n,a**2) + pow(a+1,n,a**2)) % (a**2)
        rmax = max(r,rmax)
    ans.append(rmax)
print(sum(ans))