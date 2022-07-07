import math
with open("p099_base_exp.txt") as f:
    nums = f.readlines()
    nums = [i[:-1].split(",") for i in nums]
num = []
for base, exp in nums:
    logmillion = math.log(int(base),10**6)
    firstten = logmillion * int(exp)
    num.append(firstten)
print(num.index(max(num)))