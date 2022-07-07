answer = 1
prin = 0
for i in range(1,1001):
    answer *= 2
for k in str(answer):
    prin += int(k)
print(prin)