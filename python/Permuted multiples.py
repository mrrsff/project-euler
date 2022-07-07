def isPermutation(n,x):
    if x == n:
        return True
    digit1 = sorted(list("".join(str(n))))
    digit2 = sorted(list("".join(str(x))))
    return digit1 == digit2

for i in range(1,10**6):
    if isPermutation(i,i*2) and isPermutation(i,i*3) and isPermutation(i,i*4) and isPermutation(i,i*5) and isPermutation(i,i*6):
        print(i, i*2,i*3,i*4,i*5,i*6)