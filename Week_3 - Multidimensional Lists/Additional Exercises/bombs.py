r_sq = int(input())

matrix = [list(map(int, input().split())) for _ in range(r_sq)]

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
)
bomb_coordinates = input().split()

bomb_damage_coordinates_list = []

for coordinates in bomb_coordinates:
    bomb_damage_coordinates_list.append(matrix[int(coordinates[0])][int(coordinates[2])])
    bomb_damage_coordinates_list.append(coordinates)

for index in range(0,len(bomb_damage_coordinates_list)-1,2):
    row = int(bomb_damage_coordinates_list[index+1][0])
    col = int(bomb_damage_coordinates_list[index+1][2])
    damage = bomb_damage_coordinates_list[index]
    matrix[row][col] = 0
    for direction in directions:
        if row + direction[0] < 0:
            continue
        elif row + direction[0] >= r_sq:
            continue
        elif col + direction[1] < 0:
            continue
        elif col + direction[1] >= r_sq:
            continue
        else:
            if matrix[row + direction[0]][col + direction[1]] <= 0:
                continue
            else:
                matrix[row+direction[0]][col+direction[1]] -= damage
alive_cells = 0
alive_cell_sum = 0
for r in range(len(matrix)):
    for c in range(len(matrix)):
        cell = matrix[r][c]
        if cell > 0:
            alive_cells += 1
            alive_cell_sum += cell
print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cell_sum}')
for lst in matrix:
    print(*lst, sep=" ")