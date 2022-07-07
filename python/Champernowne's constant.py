def concatenateInts():
    ans = ""
    for i in range(1,(10**6)+1):
        ans += str(i)
    ans = list(map(int, list(ans)))
    return ans
num = concatenateInts()
print(num[0]*num[9]*num[99]*num[999]*num[9999]*num[99999]*num[999999])