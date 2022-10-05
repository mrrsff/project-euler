def entropy(i,j,table):
    available = set(range(1,10)).difference(getRow(i,j,table).union(getCol(i,j,table),getSquare(i,j,table)))
    return available

def getRow(i,j,table):
    temp = table[i]
    row = set(map(int,temp))-{0}
    return row

def getCol(i,j,table):
    temp = list(zip(*table[::-1]))
    col = set(map(int, temp[j]))-{0}
    return col

def getSquare(i,j,table):
    x, y = i//3, j//3
    square = set(map(int, table[a][y*3:y*3+3]) for a in range(x*3,x*3+3))
    return square

with open("p096_sudoku.txt") as f:
    tables = []
    for i in range(50):
        table = []
        for j in range(10):
            row = f.readline().strip("\n")
            if "Grid" in row:
                table.append(row)
                continue
            row = list(map(int,list(row)))
            table.append(row)
        tables.append(table[1:])


for i in range(len(tables)-49):
    print(f"Grid {i+1}")
    table = tables[i]
    k = 0
    while k < len(table):
        l = 0
        while l < len(table[0]):
            cell = table[k][l]
            if cell == 0:
                ent = entropy(k,l,table)
                print(ent, k,l)
                if len(ent) == 1:
                    print(ent, k,l)
                    table[k][l] = list(ent)[0]
                    print(table)
                    k,l = 0,0
            l += 1
        k += 1
    for i in table:
        print(i)