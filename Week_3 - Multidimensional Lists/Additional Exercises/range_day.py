def shoot_func(matrix, x, y, player,t, t_hit):
    player_copy = player.copy()
    while True:
        sr, sc = player_copy[0] + x, player_copy[1] + y
        if 0 <= sr < len(matrix) and 0 <= sc < len(matrix):
            player_copy[0], player_copy[1] = sr, sc
            if matrix[player_copy[0]][player_copy[1]] == 'x':
                matrix[player_copy[0]][player_copy[1]] = '.'
                t_hit.append(player_copy)
                t += 1
                break
        else:
            break
    return matrix, t


def move_func(matrix,x, y, player, count_steps):
    steps_made = 0
    while steps_made < int(count_steps):
        sr, sc = player[0] + x, player[1] + y
        if 0 <= sr < len(matrix) and 0 <= sc < len(matrix):
            if matrix[sr][sc] == '.':
                matrix[player[0]][player[1]] = '.'
                matrix[sr][sc] = 'A'
                steps_made += 1
                player[0], player[1] = sr, sc
            else:
                break
        else:
            break
    return matrix, player




size = 5
player_pos = []
shooting_range = []
max_targets = 0
targets = 0
targets_hit = []
for r in range(size):
    sublist = input().split()
    max_targets += sublist.count('x')
    if not player_pos:
        for c in range(size):
            if sublist[c] == 'A':
                player_pos = [r, c]
                break
    shooting_range.append(sublist)

dict_directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

number_commands = int(input())

for number in range(number_commands):
    type_of_command = input().split()
    if type_of_command[0] == 'shoot':
        direction = type_of_command[1]
        dr, dc = dict_directions[direction][0], dict_directions[direction][1]
        shooting_range, targets = shoot_func(shooting_range, dr, dc, player_pos, targets, targets_hit)

    elif type_of_command[0] == 'move':
        direction = type_of_command[1]
        steps = type_of_command[2]
        mr, mc = dict_directions[direction][0], dict_directions[direction][1]
        shooting_range, player_pos = move_func(shooting_range,mr, mc, player_pos, steps)

if max_targets > targets:
    print(f'Training not completed! {max_targets-targets} targets left.')
    for sublist in targets_hit:
        print(sublist)
elif max_targets == targets:
    print(f'Training completed! All {max_targets} targets hit.')
    for sublist in targets_hit:
        print(sublist)