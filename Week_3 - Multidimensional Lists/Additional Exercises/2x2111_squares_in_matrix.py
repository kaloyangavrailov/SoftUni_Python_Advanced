rows, columns = input().split()

matrix = [list(input().split()) for _ in range(int(rows))]

counter = 0
flag = False
for r in range(int(rows)-1):
    for c in range(int(columns)-1):
        if not flag:
            symbol = matrix[r][c]
            flag = True
        if matrix[r+1][c] == symbol and matrix[r][c+1] == symbol and matrix[r+1][c+1] == symbol:
           counter += 1
        else:
            flag = False
            continue
print(counter)