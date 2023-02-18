n = int(input())
matrix = [list(input()) for _ in range(n)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    r, c, value = command[1], command[2], command[3]
    if 0 <= int(r) < n and 0 <= int(c) < n:
        if command[0] == 'Add':
            matrix[int(r)][int(c)] += int(value)
        else:
            matrix[int(r)][int(c)] -= int(value)
    else:
        print(f'Invalid coordinates')
for lst in matrix:
    print(*lst, sep=' ')