import time

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def isCurious(number):
    sum = 0
    for i in list(str(number)):
        sum += factorial(int(i))
    return sum==number

ans = []
for i in range(2,40586):
    if isCurious(i):
        ans.append(i)
print(sum(ans))
print("elapsed time: ", time.process_time())