
def next(n):
    res = 0
    for i in str(n):
        res += int(i)**2
    return res
def chain(n):
    temp = n
    while 1:
        temp = next(temp)
        if temp==89:
            eigthies[n-1] = True
            break
        elif temp == 1:
            break
def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def combs(lst):
    if lst.count(0)==len(lst):
        return 0
    digits = [0]*10
    for i in lst:
        digits[i]+=1
    factdigit = 1
    for i in digits:
        factdigit *= factorial(i)
    top = factorial(len(lst))
    return top/factdigit

eigthies = [False] * 567
for i in range(1,568):
    chain(i)
ans = 0
for i in range(0,10):
    for j in range(i,10):
        for k in range(j,10):
            for l in range(k,10):
                for n in range(l,10):
                    for m in range(n,10):
                        for o in range(m,10):
                            digitsum = (i**2)+(j**2)+(k**2)+(l**2)+(n**2)+(m**2)+(o**2)
                            number = [i, j, k, l, n, m, o]
                            if eigthies[digitsum-1]:
                                ans += combs(number)
print(ans)