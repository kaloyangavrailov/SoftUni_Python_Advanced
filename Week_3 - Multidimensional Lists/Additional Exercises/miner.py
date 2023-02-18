from collections import deque

# create matrix
r_sq = int(input())
movement_commands = deque(input().split())
coal = 0
coal_collected = 0
matrix = []
end_game_flag = False
for iteration in range(r_sq):
    sublist = input().split()
    coal += sublist.count('c')
    matrix.append(sublist)



# create dict of pre-defined movement directions
d_movement = {
    'left': (0,-1),
    'right': (0, 1),
    'up': (-1,0),
    'down': (1,0)
}

# find starting position of miner
index_miner = []
counter = 0

for lst in matrix:
    if 's' in lst:
        sublist_index = lst.index('s')
        index_miner.append(counter)
        index_miner.append(sublist_index)
    counter += 1

# start while loop to iterate through commands

for index in range(len(movement_commands.copy())):
    movement_command = movement_commands.popleft()
    coordinates = d_movement[movement_command]

    if index_miner[0]+coordinates[0] < 0 or index_miner[0]+coordinates[0] > r_sq-1:
        continue
    elif index_miner[1]+coordinates[1] < 0 or index_miner[1]+coordinates[1] > r_sq-1:
        continue
    else:
        matrix[index_miner[0]][index_miner[1]] = '*'
        if matrix[index_miner[0]+coordinates[0]][index_miner[1]+coordinates[1]] == '*' or matrix[index_miner[0]+coordinates[0]][index_miner[1]+coordinates[1]] == 'c':
            if matrix[index_miner[0]+coordinates[0]][index_miner[1]+coordinates[1]] == 'c':
                coal_collected += 1
            matrix[index_miner[0]+coordinates[0]][index_miner[1]+coordinates[1]] = 's'
            index_miner[0], index_miner[1] = index_miner[0]+coordinates[0], index_miner[1]+coordinates[1]

        elif matrix[index_miner[0]+coordinates[0]][index_miner[1]+coordinates[1]] == 'e':
            index_miner[0], index_miner[1] = index_miner[0] + coordinates[0], index_miner[1] + coordinates[1]
            print(f'Game over! ({index_miner[0]}, {index_miner[1]})')
            end_game_flag = True
            break
if coal_collected == coal:
    print(f'You collected all coal! ({index_miner[0]}, {index_miner[1]})')
elif coal_collected != coal and not end_game_flag:
    print(f'{coal - coal_collected} pieces of coal left. ({index_miner[0]}, {index_miner[1]})')