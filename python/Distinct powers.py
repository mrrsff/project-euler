ans = set()
for i in range(2,101):
    for j in range(2,101):
        ans.add(i**j)
print(len(ans))