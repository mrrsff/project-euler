import itertools

def tripleDigit(n,i):
    return int("".join(list(str(n)[i-1:i+2])))

def condition(i):
    return not tripleDigit(i, 2) % 2 and not tripleDigit(i, 3) % 3 and not tripleDigit(i,4) % 5 and not tripleDigit(i, 5) % 7 and not tripleDigit(i, 6) % 11 and not tripleDigit(i, 7) % 13 and not tripleDigit(i, 8) % 17
ans = 0
pans = [int("".join(map(str,list(i)))) for i in itertools.permutations(list(range(10))) if i[0]!=0]
for pan in pans:
    if condition(pan):
        ans+= pan
print(ans)