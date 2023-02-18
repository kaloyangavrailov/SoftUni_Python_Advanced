r, c = input().split(', ')

matrix = [list(map(int, input().split())) for _ in range(int(r))]

column_sum = []

for column in range(len(matrix[0])):
    for row in range(len(matrix)):
        column_sum.append(matrix[row][column])
    print(sum(column_sum))
    column_sum.clear()


