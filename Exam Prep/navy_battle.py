d_d = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

size = int(input())

field = []

s_p = 0

for row in range(size):
    sublist = list(input())
    for element in sublist:
        if element == 'S':
            s_p = [row, sublist.index(element)]
    field.append(sublist)
hit_count = 0
destroyed_cruisers = 0
while hit_count < 3 and destroyed_cruisers < 3:
    command = input()
    new_pos_x = d_d[command][0] + s_p[0]
    new_pos_y = d_d[command][1] + s_p[1]
    field[s_p[0]][s_p[1]] = '-'
    if 0 <= new_pos_x < size and 0 <= new_pos_y < size:
        if field[new_pos_x][new_pos_y] == '*':
            hit_count += 1
            field[new_pos_x][new_pos_y] = '-'
            s_p[0], s_p[1] = new_pos_x, new_pos_y
        elif field[new_pos_x][new_pos_y] == 'C':
            destroyed_cruisers += 1
            field[new_pos_x][new_pos_y] = '-'
            s_p[0], s_p[1] = new_pos_x, new_pos_y
        else:
            s_p[0], s_p[1] = new_pos_x, new_pos_y

if hit_count == 3:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{s_p[0]}, {s_p[1]}]!')
    field[s_p[0]][s_p[1]] = 'S'
if destroyed_cruisers == 3:
    print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
    field[s_p[0]][s_p[1]] = 'S'
for sublist in field:
    print(f'{"".join(sublist)}')