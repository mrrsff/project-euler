ans = 0
prev, last, new = 0, 1, 0
while new<4000000:
    new = prev + last
    prev, last = last, new
    if new%2 == 0:
        ans += new
print(ans)