import time

def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

def findPeriod(n,a=1):
    start = a
    ans = 0
    a = (a*10)%n
    ans += 1
    while a != start:
        a = (a*10) % n
        ans += 1
    return ans

def calculate():
    ans = 0
    for i in range(7,1000,2):
        if is_prime(i):
            ans = max(ans, findPeriod(i))
    return ans+1

if __name__=="__main__":
    print("answer:",calculate(),"elapsed time:",time.process_time())