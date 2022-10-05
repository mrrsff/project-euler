from eulerLibrary import factorial
import time

def digitFactorialSum(n):
    ans = 0
    while n>0:
        ans += factorial(n%10)
        n = n//10
    return ans

def chain(n):
    seen = [n]
    while not digitFactorialSum(n) in seen:
        seen.append(digitFactorialSum(n))
        n = digitFactorialSum(n)
    return seen

ans = 0
for i in range(1,10**6):
    print(f"current number is {i}, elapsed time: {round(time.process_time(),2)}", end="\r")
    l = len(chain(i))
    if l == 60:
        ans += 1
print(f"\nAnswer is {ans}.")