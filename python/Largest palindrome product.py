a = 1
for i in range(100,1000):
    for k in range(100,1000):
        if str(i*k) == str(i*k)[::-1]:
            a = max(a, i*k)
print(a)