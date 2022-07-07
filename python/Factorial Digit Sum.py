answer = 1
k = 0
for i in range(2,101):
    answer *= i 
for i in list(str(answer)):
    k += int(i)
print(k)