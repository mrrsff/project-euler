with open("p096_sudoku.txt") as f:
    tables = []
    for i in range(50):
        table = []
        for j in range(10):
            table.append(f.readline()[:-1])
        tables.append(table[1:])
for i in tables:
    print(i)