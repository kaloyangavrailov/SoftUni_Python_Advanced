SIZE = 6
board = []
buckets = []
scored_points = 0

int_count = 0

prizes = {
    'Football': [100, 199],
    'Teddy Bear': [200, 299],
    'Lego Construction Set': [300]
}

for iteration in range(SIZE):
    sublist = input().split()
    for el in sublist:
        if el == 'B':
            y = sublist.index(el)
            buckets.append([iteration, y])
            sublist[y] = '.'
    board.append(sublist)

for _ in range(3):
    throw = list(input())
    throw_x = ''
    throw_y = ''

    for char in throw.copy():
        if not char.isdigit():
            throw.remove(char)
    if len(throw) == 2:
        throw_x = int(throw[0])
        throw_y = int(throw[1])
    else:
        continue
    if [throw_x, throw_y] in buckets:
        for i in range(SIZE):
            if board[i][throw_y] != '.':
                scored_points += int(board[i][throw_y])
        buckets.remove([throw_x, throw_y])

won_prize = ''
for key in prizes.keys():
    if scored_points < 100:
        won_prize = 100 - scored_points
    elif len(prizes[key]) == 1:
        if scored_points >= prizes[key][0]:
            won_prize = key
    elif prizes[key][0] <= scored_points <= prizes[key][1]:
        won_prize = key


if won_prize:
    if isinstance(won_prize, str):
        print(f"Good job! You scored {scored_points} points, and you've won {won_prize}.")
    else:
        print(f'Sorry! You need {won_prize} points more to win a prize.')