SIZE = int(input())

territory = []
snake = []
burrow_a = []
burrow_b = []
out_of_territory = False
food = 0

d_d = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for row in range(SIZE):
    sublist = list(input())
    for cell in sublist:
        if cell == 'S':
            snake = [row, sublist.index(cell)]
        elif cell == 'B':
            if burrow_a:
                burrow_b = [row, sublist.index(cell)]
            else:
                burrow_a = [row, sublist.index(cell)]
    territory.append(sublist)
while True:
    command = input()
    new_x, new_y = d_d[command][0] + snake[0], d_d[command][1] + snake[1]
    if 0 <= new_x < SIZE and 0 <= new_y < SIZE:
        if territory[new_x][new_y] == '*':
            food += 1
            territory[snake[0]][snake[1]] = '.'
            snake[0], snake[1] = new_x, new_y
            territory[snake[0]][snake[1]] = 'S'
        elif territory[new_x][new_y] == 'B':
            if new_x == burrow_a[0] and new_y == burrow_a[1]:
                territory[snake[0]][snake[1]] = '.'
                territory[burrow_a[0]][burrow_a[1]] = '.'
                snake[0], snake[1] = burrow_b[0], burrow_b[1]
                territory[snake[0]][snake[1]] = 'S'
            elif new_x == burrow_b[0] and new_y == burrow_b[1]:
                territory[snake[0]][snake[1]] = '.'
                territory[burrow_b[0]][burrow_b[1]] = '.'
                snake[0], snake[1] = burrow_a[0], burrow_a[1]
                territory[snake[0]][snake[1]] = 'S'
        else:
            territory[snake[0]][snake[1]] = '.'
            snake[0], snake[1] = new_x, new_y
            territory[snake[0]][snake[1]] = 'S'
    else:
        territory[snake[0]][snake[1]] = '.'
        out_of_territory = True
        break
    if food == 10:
        break
    # print(f'+++++++++++++++++++')
    # for sublist in territory:
    #     print(''.join(sublist))
if out_of_territory:
    print(f'Game over!')
elif food == 10:
    print(f'You won! You fed the snake.')
print(f'Food eaten: {food}')

for sublist in territory:
    print(''.join(sublist))