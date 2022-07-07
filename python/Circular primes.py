def findRotations(num, rotation=1):
    digits = len(list(str(num)))
    if rotation>digits: return []
    rot = (num%10) * pow(10,digits-1) + (num//10)
    return [rot] + findRotations(rot,rotation+1)

def isPrime(num):
    if num<=3:
        return num>1
    if not num%2 or not num%3:
        return False
    i = 5
    stop = int(num**0.5)
    while i <= stop:
        if not num%i or not num%(i+2):
            return False
        i+=6
    return True

circPrimes = []
for num in range(1,(10**6)+1):
    circularPrime = True
    if isPrime(num)==True:
        for rot in findRotations(num):
            if isPrime(rot)==False:
                circularPrime = False
    else: circularPrime = False
    if circularPrime:
        print(num)
        circPrimes.append(num)
print("num of circ primes: ", len(circPrimes))