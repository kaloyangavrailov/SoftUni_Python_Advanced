from collections import deque


def player_func(grid, x, y, px, py, w, d, p_pos):
    if px < 0 or px > int(x)-1 or py < 0 or py > int(y)-1:
        w = True
    elif grid[px][py] == 'B':
        p_pos[0], p_pos[1] = px, py
        d = True
    else:
        grid[px][py] = 'P'
        p_pos[0], p_pos[1] = px, py
    return grid, p_pos, w, d


def bunny_func(grid, row, colum, bunny_directions, flag_dead):
    bunny_start_pos = []
    for r in range(int(row)):
        for c in range(int(colum)):
            if grid[r][c] == 'B':
                bunny_start_pos.append((r, c))
    for bunny_position in bunny_start_pos:
        for bunny_direction in bunny_directions:
            bunny_next_step = [bunny_position[0]+bunny_direction[0],bunny_position[1]+bunny_direction[1]]
            if bunny_next_step[0] < 0 or bunny_next_step[0] > int(rows)-1 or bunny_next_step[1] < 0 or bunny_next_step[1] > int(columns)-1:
                continue
            else:
                if grid[bunny_next_step[0]][bunny_next_step[1]] == 'P':
                    flag_dead = True
                if grid[bunny_next_step[0]][bunny_next_step[1]] == 'B':
                    continue
                if grid[bunny_next_step[0]][bunny_next_step[1]] == '.' or grid[bunny_next_step[0]][bunny_next_step[1]] == 'P':
                    grid[bunny_next_step[0]][bunny_next_step[1]] = 'B'
    bunny_start_pos.clear()
    return grid, flag_dead


def print_func(grid, d, p_pos):
    for lst in grid:
        print("".join(lst))
    if d:
        print(f'dead: {p_pos[0]} {p_pos[1]}')
    else:
        print(f'won: {p_pos[0]} {p_pos[1]}')


rows, columns = input().split()
p_start_pos = []
matrix = []

for r in range(int(rows)):
    sublist = list(input())
    if 'P' in sublist:
        p_start_pos.append(r)
        p_start_pos.append(sublist.index('P'))
    matrix.append(sublist)

dict_directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
tuple_dir_bunnies = ((1, 0), (-1, 0), (0, -1), (0, 1))

p_dir = deque(input())

dead = False
game_won = False

while not dead and not game_won:

    direction = dict_directions[p_dir.popleft()]
    pr, pc = p_start_pos[0]+direction[0], p_start_pos[1]+direction[1]
    matrix[p_start_pos[0]][p_start_pos[1]] = '.'

    matrix, p_start_pos, game_won, dead = player_func(matrix,int(rows), int(columns), pr, pc, game_won, dead, p_start_pos)

    matrix, dead = bunny_func(matrix, int(rows), int(columns), tuple_dir_bunnies, dead)


print_func(matrix, dead, p_start_pos)