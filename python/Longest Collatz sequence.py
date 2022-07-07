chain = []
a = 1
while a < 1000000:
    n = a
    length = 0
    while n > 1:
        if n % 2:
            n = 3*n + 1
        else:
            n = n/2
        length += 1
    a += 1
    chain.append(length)

print(chain.index(max(chain)))