import time

sqr = 0
a = 0
for i in range(101):
    sqr += i*i
    a += i
end = time.process_time()
print(a*a - sqr)
print("elapsed time: ",end)