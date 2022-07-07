def sumdigit(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res

ans = 0
for a in range(1,100):
    for b in range(1, 100):
        p = pow(a,b)
        ans = max(ans, sumdigit(p))
print(ans)