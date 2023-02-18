def create_func(grid, way, change_value, d_d, p_p):
    p_p_x = p_p[0]
    p_p_y = p_p[1]
    way_x = d_d[way][0]
    way_y = d_d[way][1]
    if p_p_x + way_x > 0 or p_p_x + way_x < 5 or p_p_y + way_y > 0 or p_p_y + way_y < 5:
        if grid[p_p_x + way_x][p_p_y + way_y] == '.':
            grid[p_p_x + way_x][p_p_y + way_y] = change_value
        p_p[0], p_p[1] = p_p_x + way_x, p_p_y + way_y
    return grid, p_p


def update_func(grid, way, change_value, d_d, p_p):
    p_p_x = p_p[0]
    p_p_y = p_p[1]
    way_x = d_d[way][0]
    way_y = d_d[way][1]
    if p_p_x + way_x > 0 or p_p_x + way_x < 5 or p_p_y + way_y > 0 or p_p_y + way_y < 5:
        if grid[p_p_x + way_x][p_p_y + way_y] != '.':
            grid[p_p_x + way_x][p_p_y + way_y] = change_value
        p_p[0], p_p[1] = p_p_x + way_x, p_p_y + way_y
    return grid, p_p


def delete_func(grid, way, d_d, p_p):
    p_p_x = p_p[0]
    p_p_y = p_p[1]
    way_x = d_d[way][0]
    way_y = d_d[way][1]
    if p_p_x + way_x > 0 or p_p_x + way_x < 5 or p_p_y + way_y > 0 or p_p_y + way_y < 5:
        if grid[p_p_x + way_x][p_p_y + way_y] != '.':
            grid[p_p_x + way_x][p_p_y + way_y] = '.'
        p_p[0], p_p[1] = p_p_x + way_x, p_p_y + way_y
    return grid, p_p


def read_func(grid, way, d_d, p_p):
    p_p_x = p_p[0]
    p_p_y = p_p[1]
    way_x = d_d[way][0]
    way_y = d_d[way][1]
    if p_p_x + way_x > 0 or p_p_x + way_x < 5 or p_p_y + way_y > 0 or p_p_y + way_y < 5:
        if grid[p_p_x + way_x][p_p_y + way_y] != '.':
            print(grid[p_p_x + way_x][p_p_y + way_y])
        p_p[0], p_p[1] = p_p_x + way_x, p_p_y + way_y
    return grid, p_p


dir_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

SIZE = 6
matrix = []

for iteration in range(SIZE):
    matrix.append(input().split())

position = input()

position = [int(position[1]), int(position[4])]

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        direction = command[1]
        value = command[2]
        matrix, position = create_func(matrix, direction, value, dir_dict, position)
    elif command[0] == 'Update':
        direction = command[1]
        value = command[2]
        matrix, position = update_func(matrix, direction, value, dir_dict, position)
    elif command[0] == 'Delete':
        direction = command[1]
        matrix, position = delete_func(matrix, direction, dir_dict, position)
    elif command[0] == 'Read':
        direction = command[1]
        matrix, position = read_func(matrix, direction, dir_dict, position)

for row in matrix:
    print(' '.join(row))

