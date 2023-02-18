r, c = input().split(',')

matrix = [list(map(int, input().split(', '))) for _ in range(int(r))]

dict_submatrices = {}
submatrix_sum = 0
submatrix = []
submatrix_index = 0
r_i = 0
c_i = 0
while c_i < len(matrix[0]):
    for r in range(r_i, r_i + 2):
        submatrix.append([])
        for c in range(c_i, c_i + 2):
            submatrix_sum += matrix[r][c]
            submatrix[submatrix_index].append(matrix[r][c])
        submatrix_index += 1
    if submatrix_sum in dict_submatrices.keys():
        submatrix_sum = 0
        submatrix.clear()
        submatrix_index = 0
        if r_i < len(matrix) - 2:
            r_i += 1
        else:
            if c_i < len(matrix[0]) - 2:
                c_i += 1
                r_i = 0
            else:
                break
        continue
    dict_submatrices[submatrix_sum] = submatrix.copy()
    submatrix_sum = 0
    submatrix.clear()
    submatrix_index = 0
    if r_i < len(matrix) - 2:
        r_i += 1
    else:
        if c_i < len(matrix[0]) - 2:
            c_i += 1
            r_i = 0
        else:
            break

for item in dict_submatrices[max(dict_submatrices.keys())]:
    print(*item, sep=' ')
print(max(dict_submatrices.keys()))