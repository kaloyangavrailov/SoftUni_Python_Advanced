from collections import deque

SIZE = 6
matrix = []
rover_pos = []

d_d = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

water, metal, concrete = False, False, False

for row in range(SIZE):
    sublist = input().split()
    for item in sublist:
        if item == 'E':
            rover_pos = [row, sublist.index(item)]
    matrix.append(sublist)

directions = deque(input().split(', '))

while directions:
    direction = directions.popleft()
    d_x, d_y = d_d[direction][0], d_d[direction][1]
    new_player_pos_x = rover_pos[0] + d_x
    new_player_pos_y = rover_pos[1] + d_y
    # if 0 <= new_player_pos_x < SIZE and 0 <= new_player_pos_y < SIZE:
    #     pass
    if new_player_pos_x < 0 or new_player_pos_x > SIZE - 1 or new_player_pos_y < 0 or new_player_pos_y > SIZE - 1:
        if new_player_pos_x == -1:
            new_player_pos_x = SIZE - 1
        elif new_player_pos_x == SIZE:
            new_player_pos_x = 0
        if new_player_pos_y == -1:
            new_player_pos_y = SIZE - 1
        elif new_player_pos_y == SIZE:
            new_player_pos_y = 0
    if matrix[new_player_pos_x][new_player_pos_y] == 'W':
        water = True
        print(f'Water deposit found at ({new_player_pos_x}, {new_player_pos_y})')
    elif matrix[new_player_pos_x][new_player_pos_y] == 'M':
        metal = True
        print(f'Metal deposit found at ({new_player_pos_x}, {new_player_pos_y})')
    elif matrix[new_player_pos_x][new_player_pos_y] == 'C':
        # value = int(matrix[new_player_pos_x][new_player_pos_y])
        # value += 1
        # matrix[new_player_pos_x][new_player_pos_y] = str(value)
        concrete = True
        print(f'Concrete deposit found at ({new_player_pos_x}, {new_player_pos_y})')
    elif matrix[new_player_pos_x][new_player_pos_y] == 'R':
        print(f"Rover got broken at ({new_player_pos_x}, {new_player_pos_y})")
        break
    rover_pos[0], rover_pos[1] = new_player_pos_x, new_player_pos_y
if water and metal and concrete:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')