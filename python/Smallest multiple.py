from math import gcd, lcm

a = 1
for i in range(1,21):
    a = lcm(a,i)

print(a)