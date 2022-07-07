def findAllDivisorsSum(n):
    divisors = [1]
    i = 2
    while i*i<=n:
        if n%i == 0:
            divisors.append(i)
            divisors.append(n//i)
        i += 1
    return sum(divisors)
    
answer = []
for i in range(1,10000):
    isum = findAllDivisorsSum(i)
    if findAllDivisorsSum(isum) == i and i != isum and i not in answer and isum not in answer:
        answer.append(i)
        answer.append(isum)
        
print(sum(answer))