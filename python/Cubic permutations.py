import eulerLibrary

limit = 150000
cubeDigitsSorted = []
for i in range(limit):
    cubeDigitsSorted.append(eulerLibrary.getDigits(i**3))
for i in range(limit):
    print(i)
    if cubeDigitsSorted.count(cubeDigitsSorted[i]) == 5:
        print(i**3)
        break