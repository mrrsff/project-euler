import itertools
from typing import List, Union, Any

with open("p79input.txt") as txt:
    input = txt.readlines()
    for i in range(len(input)):
        input[i] = input[i][:3]


digits = set()
for i in input:
    digits.add(int(i[0]))
    digits.add(int(i[1]))
    digits.add(int(i[2]))

combs = list(itertools.permutations(digits, 8))
input = set(map(int, input))
for i in range(len(combs)):
    if combs[i][0]!=7:
        continue
    found = 0
    combs[i] = list(combs[i])
    perm1 = list(itertools.permutations(combs[i],3))
    for j in range(len(perm1)):
        if combs[i].index(perm1[j][0]) < combs[i].index(perm1[j][1]) < combs[i].index(perm1[j][2]):
            perm1[j] = "".join(map(str,list(perm1[j])))
            if perm1[j][0] == "0":
                perm1[j] = 0
        else:
            perm1[j] = 0
    combs[i] = int("".join(map(str,combs[i])))
    newPerm = {int(perm1[j]) for j in range(len(perm1)) if perm1[j]!=0}
    inters = newPerm.intersection(input)
    if len(inters) == len(input):
        print("found:", combs[i])