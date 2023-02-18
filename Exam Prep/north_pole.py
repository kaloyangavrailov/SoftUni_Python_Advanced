matrix_rows, matrix_columns = input().split(', ')
player_pos = 0
grid = []
items = 0
decorations = 0
gifts = 0
cookies = 0
collected_items = 0
d_d = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for row in range(int(matrix_rows)):
    sublist = input().split()
    for element in sublist:
        if element == 'Y':
            player_pos = [row, sublist.index(element)]
        elif element in 'DGC':
            items += 1
    grid.append(sublist)
flag = True

while flag:
    input_info = input()
    if input_info == 'End':
        break
    command, steps = input_info.split('-')
    for iteration in range(int(steps)):
        new_pos_x, new_pos_y = d_d[command][0] + player_pos[0], d_d[command][1] + player_pos[1]
        if new_pos_x < 0 or new_pos_x > int(matrix_rows) - 1 or new_pos_y < 0 or new_pos_y > int(matrix_columns) - 1:
            if new_pos_x < 0:
                new_pos_x = int(matrix_rows) - 1
            elif new_pos_x > int(matrix_rows) - 1:
                new_pos_x = 0
            if new_pos_y < 0:
                new_pos_y = int(matrix_columns) - 1
            elif new_pos_y > int(matrix_columns) - 1:
                new_pos_y = 0
        grid[player_pos[0]][player_pos[1]] = 'x'
        if grid[new_pos_x][new_pos_y] in 'DGC':
            if grid[new_pos_x][new_pos_y] == 'D':
                decorations += 1
            elif grid[new_pos_x][new_pos_y] == 'G':
                gifts += 1
            elif grid[new_pos_x][new_pos_y] == 'C':
                cookies += 1
            collected_items += 1
        player_pos[0], player_pos[1] = new_pos_x, new_pos_y
        grid[player_pos[0]][player_pos[1]] = 'Y'
        if collected_items == items:
            flag = False
            break
if not flag:
    print(f'Merry Christmas!')
print(f"You've collected:")
print(f'- {decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f'- {cookies} Cookies')
for sublist in grid:
    print(' '.join(sublist))
