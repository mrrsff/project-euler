def check_pythagorean(a, b, c):
    return a**2 + b**2 == c**2 and a + b + c == 1000

for i in range(1, 1000):
    for j in range(i+1, 1000):
        k = 1000 - j - i
        if check_pythagorean(i, j, k):
            print(i * j * k)