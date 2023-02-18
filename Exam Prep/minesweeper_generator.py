SIZE = int(input())
bombs = int(input())
bomb_positions = []
field = []

d_d = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

for iteration in range(bombs):
    info = list(input())
    if '-' in info:
        continue
    for char in info.copy():
        if not char.isdigit():
            info.remove(char)
    if len(info) == 2:
        bomb_x = int(info[0])
        bomb_y = int(info[1])
        if 0 <= bomb_x < SIZE and 0 <= bomb_y < SIZE:
            if (bomb_x, bomb_y) not in bomb_positions:
                bomb_positions.append((bomb_x, bomb_y))

for iteration in range(SIZE):
    sublist = list('0' * SIZE)
    sublist = [int(el) for el in sublist]
    field.append(sublist)


for x in range(SIZE):
    for y in range(SIZE):
        if (x, y) in bomb_positions:
            field[x][y] = '*'

for bomb in bomb_positions:
    for direction in d_d:
        x, y = bomb[0] + direction[0], bomb[1] + direction[1]
        if 0 <= x < SIZE and 0 <= y < SIZE and field[x][y] != '*':
            field[x][y] += 1

for sublist in field:
    print(' '.join(list(map(str, sublist))))