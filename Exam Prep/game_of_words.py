word = list(input())

SIZE = int(input())
field = []
player = []

movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(SIZE):
    sublist = list(input())
    for el in sublist:
        if el == 'P':
            player = [r, sublist.index(el)]
    field.append(sublist)

command_number = int(input())

for iteration in range(command_number):
    command = input()
    x, y = player[0] + movement[command][0], player[1] + movement[command][1]
    if 0 <= x < SIZE and 0 <= y < SIZE:
        field[player[0]][player[1]] = '-'

        if field[x][y] != '-':
            word.append(field[x][y])

        field[x][y] = 'P'
        player[0], player[1] = x, y
    else:
        if word:
            word.pop()


print(f'{"".join(word)}')
for sublist in field:
    print(''.join(sublist))