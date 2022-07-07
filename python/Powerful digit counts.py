ans = 0
for base in range(1,100):
    for pow in range(1,100):
        if len(str(base**pow)) == pow:
            ans += 1
            print(base,pow)
print(ans)