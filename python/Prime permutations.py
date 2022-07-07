import eulerLibrary

for a in range(1488,3341):
    b = a + 3330
    c = a + 6660
    if eulerLibrary.isPermutation(a,b) and eulerLibrary.isPermutation(a,c) and eulerLibrary.isPrime(a) and eulerLibrary.isPrime(b) and eulerLibrary.isPrime(c):
        print(int("".join(list(str(a)+str(b)+str(c)))))
        break