def isFifthPowSum(number):
    sum = 0
    for i in list(str(number)):
        sum += int(i)**5
    return sum == number
maxi = (9**5)*5
ans = []
for i in range(64,maxi):
    i += 1
    if isFifthPowSum(i):
        ans.append(i)
print(sum(ans))