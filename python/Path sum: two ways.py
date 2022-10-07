with open("p081_matrix.txt") as f:
    matrix = []
    for line in f.readlines():
        matrix.append(list(map(int,line.strip().split(","))))

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if x == 0 and y == 0:
            matrix[x][y] = matrix[x][y]
        elif x == 0 and y != 0:
            matrix[x][y] += matrix[x][y-1]
        elif x != 0 and y == 0:
            matrix[x][y] += matrix[x-1][y]
        else:
            matrix[x][y] += min(matrix[x-1][y], matrix[x][y-1])
print(matrix[-1][-1])