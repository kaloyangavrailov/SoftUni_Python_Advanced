r = int(input())
matrix = [list(input()) for _ in range(r)]
query_char = input()
flag = False
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == query_char:
            print(f'({r}, {c})')
            flag = True


if not flag:
    print(f'{query_char} does not occur in the matrix')