rows, columns = input().split()

matrix = [list(map(int, input().split())) for _ in range(int(rows))]

matrix_results = {}

submatrix = []
submatrix_index = 0
flag = False
submatrix_sum = 0
for r in range(int(rows)-2):
    for c in range(int(columns)-2):
        starting_index = (r,c)
        for row in range(starting_index[0], starting_index[0]+3):
            submatrix.append([])
            for column in range(starting_index[1], starting_index[1]+3):
                submatrix[submatrix_index].append(matrix[row][column])
            submatrix_sum += sum(submatrix[submatrix_index])
            submatrix_index += 1

        matrix_results[submatrix_sum] = submatrix.copy()
        submatrix.clear()
        submatrix_index = 0
        submatrix_sum = 0

print(f'Sum = {max(matrix_results.keys())}')
[print(' '.join(map(str,el))) for el in matrix_results[max(matrix_results.keys())]]