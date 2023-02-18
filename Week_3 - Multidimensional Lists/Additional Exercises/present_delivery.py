directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


presents = int(input())
size = int(input())


count_nice_kids = 0
santa_pos = []
hood = []
nice_kids_happy = 0
for r in range(size):
    sublist = input().split()
    for c in range(size):
        if sublist[c] == 'V':
            count_nice_kids += 1
        if sublist[c] == 'S':
            santa_pos = [r, c]
    hood.append(sublist)

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break
    sx, sy = directions[command][0], directions[command][1]
    if 0 <= santa_pos[0] + sx < size and 0 <= santa_pos[1] + sy < size:
        hood[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos[0], santa_pos[1] = santa_pos[0] + sx, santa_pos[1] + sy
        if hood[santa_pos[0]][santa_pos[1]] == 'V':
            presents -= 1
            nice_kids_happy += 1
        elif hood[santa_pos[0]][santa_pos[1]] == 'C':
            for direction in directions.values():
                cr, cc = direction[0], direction[1]
                if 0 <= santa_pos[0] + cr < size and 0 <= santa_pos[1] + cc < size:
                    if hood[santa_pos[0] + cr][santa_pos[1] + cc] in 'XV':
                        presents -= 1
                        if hood[santa_pos[0] + cr][santa_pos[1] + cc] == 'V':
                            nice_kids_happy += 1
                        hood[santa_pos[0] + cr][santa_pos[1] + cc] = '-'
        hood[santa_pos[0]][santa_pos[1]] = 'S'


if not presents and count_nice_kids > nice_kids_happy:
    print(f'Santa ran out of presents!')
for sublist in hood:
    print(*sublist, sep=' ')
if count_nice_kids == nice_kids_happy:
    print(f'Good job, Santa! {count_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {count_nice_kids-nice_kids_happy} nice kid/s.')