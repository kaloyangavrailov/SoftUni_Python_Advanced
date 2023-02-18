r, c = input().split()

set_rows = {el for el in range(int(r))}
set_columns = {el for el in range(int(c))}

matrix = [input().split() for _ in range(int(r))]

while True:
    input_info = input().split()
    if input_info[0] == 'END':
        break
    if len(input_info) != 5:
        print(f'Invalid input!')
        continue
    command, row_1, col_1, row_2, col_2 = input_info[0], int(input_info[1]), int(input_info[2]), int(input_info[3]), int(input_info[4])


    set_rows_to_check = set()
    set_rows_to_check.add(int(row_1))
    set_rows_to_check.add(int(row_2))
    set_columns_to_check = set()
    set_columns_to_check.add(int(col_1))
    set_columns_to_check.add(int(col_2))

    if set_rows_to_check.issubset(set_rows) and set_columns_to_check.issubset(set_columns):
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        [print(' '.join(el)) for el in matrix]
    else:
        print(f"Invalid input!")
        continue