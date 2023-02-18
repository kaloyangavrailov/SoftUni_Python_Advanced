SIZE = 6
p1, p2 = input().split(', ')
matrix = []
rest_1 = False
rest_2 = False
for row in range(SIZE):
    matrix.append(input().split())
player_1 = [p1, 1]
player_2 = [p2, 2]

player = 1

while True:

    command = input()

    coordinates = (int(command[1]), int(command[4]))
    if (not rest_1 and player == 1) or (not rest_2 and player == 2):
        if matrix[coordinates[0]][coordinates[1]] == 'E':
            if player == 1:
                print(f'{player_1[0]} found the Exit and wins the game!')
            else:
                print(f'{player_2[0]} found the Exit and wins the game!')
            break
        elif matrix[coordinates[0]][coordinates[1]] == 'T':
            if player == 1:
                print(f'{player_1[0]} is out of the game! The winner is {player_2[0]}.')
            else:
                print(f'{player_2[0]} is out of the game! The winner is {player_1[0]}.')
            break
        elif matrix[coordinates[0]][coordinates[1]] == 'W':
            if player == 1:
                print(f'{player_1[0]} hits a wall and needs to rest.')
            else:
                print(f'{player_2[0]} hits a wall and needs to rest.')
            if player == 1:
                rest_1 = True
            else:
                rest_2 = True
    elif rest_1 and player == 1:
        rest_1 = False
    elif rest_2 and player == 2:
        rest_2 = False

    if player == 2:
        player = 1
    else:
        player = 2