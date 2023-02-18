SIZE = int(input())
field = []
p = []
coins = 0
d = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_path = []

for i in range(SIZE):
    sublist = input().split()
    for el in sublist:
        if el == 'P':
            p = [i, sublist.index(el)]
    field.append(sublist)

game_lost = False

player_path.append([p[0], p[1]])

while not game_lost and coins < 100:
    direction = input()
    x, y = p[0] + d[direction][0], p[1] + d[direction][1]
    if 0 <= x < SIZE and 0 <= y < SIZE:
        field[p[0]][p[1]] = '-'
        if field[x][y] == 'X':
            game_lost = True
            coins = int(coins * 0.5)
            p[0], p[1] = x, y
            player_path.append(p)
        elif field[x][y].isdigit():
            coins += int(field[x][y])
            p[0], p[1] = x, y
            player_path.append([p[0], p[1]])
        else:
            p[0], p[1] = x, y
            player_path.append([p[0], p[1]])
    else:
        if x == -1:
            x = SIZE-1
        elif x == SIZE:
            x = 0
        if y == -1:
            y = SIZE - 1
        elif y == SIZE:
            y = 0
        field[p[0]][p[1]] = '-'
        if field[x][y] == 'X':
            game_lost = True
            coins = int(coins * 0.5)
            p[0], p[1] = x, y
            player_path.append([p[0], p[1]])
        elif field[x][y].isdigit():
            coins += int(field[x][y])
            p[0], p[1] = x, y
            player_path.append([p[0], p[1]])
        else:
            p[0], p[1] = x, y
            player_path.append([p[0], p[1]])
if game_lost:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print(f'Your path:')
[print(el) for el in player_path]