def isPentagonal(n):
    return not (1+(1+24*n)**0.5) % 6

def findPentagonal(n):
    return n*(3*n-1)/2

dmin = 9999
limit = 4
found = 0
for j in range(1,10**limit):
    pent1 = findPentagonal(j)
    if found:
        break
    for k in range(j,10**limit):
        pent2 = findPentagonal(k)
        if isPentagonal(pent2+pent1) and isPentagonal(pent2-pent1):
            print(int(pent2-pent1))
            found = 1
            break