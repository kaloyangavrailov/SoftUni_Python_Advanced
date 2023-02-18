SIZE = 7
field = []
p_1, p_2 = input().split(', ')
p_1_score = 501
p_2_score = 501
turn = ''
turns_count_p_1 = 0
turns_count_p_2 = 0
score = 0
for iteration in range(SIZE):
    sublist = input().split()
    field.append(sublist)

turn = p_1

while p_1_score > 0 and p_2_score > 0:
    command = list(input())

    for char in command.copy():
        if not char.isdigit():
            command.remove(char)
    if len(command) == 2:
        x, y = int(command[0]), int(command[1])
    else:
        continue

    if 0 <= x < SIZE and 0 <= y < SIZE:
        if field[x][y] not in "DTB":
            if turn == p_1:
                p_1_score -= int(field[x][y])
                turns_count_p_1 += 1
            else:
                p_2_score -= int(field[x][y])
                turns_count_p_2 += 1
        elif field[x][y] == "D":
            score = 2*(int(field[0][y]) + int(field[SIZE - 1][y]) + int(field[x][0]) + int(field[x][SIZE - 1]))
            if turn == p_1:
                p_1_score -= score
                turns_count_p_1 += 1
            else:
                p_2_score -= score
                turns_count_p_2 += 1
        elif field[x][y] == 'T':
            score = 3 * (int(field[0][y]) + int(field[SIZE - 1][y]) + int(field[x][0]) + int(field[x][SIZE - 1]))
            if turn == p_1:
                p_1_score -= score
                turns_count_p_1 += 1
            else:
                p_2_score -= score
                turns_count_p_2 += 1
        elif field[x][y] == 'B':
            if turn == p_1:
                p_1_score = 0
                turns_count_p_1 += 1
            else:
                p_2_score = 0
                turns_count_p_2 += 1
    if turn == p_1:
        turn = p_2
    else:
        turn = p_1
if p_1_score <= 0:
    print(f'{p_1} won the game with {turns_count_p_1} throws!')
elif p_2_score <= 0:
    print(f'{p_2} won the game with {turns_count_p_2} throws!')