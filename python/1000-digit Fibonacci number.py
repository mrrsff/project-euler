fib = 1
prev = 0
index = 1
while 1:
    fib, prev = prev+fib, fib
    index += 1
    if len(str(fib)) == 1000:
        break
print(index)