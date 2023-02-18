size = int(input())
alice_pos = []
wonderland = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0,1)
}
bags_tea = 0
not_make_it = False
for r in range(size):
    sublist = input().split()
    if not alice_pos:
        for c in range(size):
            if sublist[c] == 'A':
                alice_pos = [r,c]
                break
    wonderland.append(sublist)

while bags_tea < 11:
    direction = directions[input()]
    ar, ac = alice_pos[0] + direction[0], alice_pos[1] + direction[1]
    if 0 <= ar < size and 0 <= ac < size:
        wonderland[alice_pos[0]][alice_pos[1]] = '*'
        alice_pos[0], alice_pos[1] = ar, ac
        if wonderland[alice_pos[0]][alice_pos[1]] == 'R':
            wonderland[alice_pos[0]][alice_pos[1]] = '*'
            not_make_it = True
            break
        elif wonderland[alice_pos[0]][alice_pos[1]] == '.':
            wonderland[alice_pos[0]][alice_pos[1]] = '*'
        elif wonderland[alice_pos[0]][alice_pos[1]].isdigit():
            bags_tea += int(wonderland[alice_pos[0]][alice_pos[1]])
            wonderland[alice_pos[0]][alice_pos[1]] = '*'
    else:
        not_make_it = True
        wonderland[alice_pos[0]][alice_pos[1]] = '*'
        break

if not_make_it:
    print(f"Alice didn't make it to the tea party.")
elif bags_tea >= 10:
    print(f'She did it! She went to the party.')
for sublist in wonderland:
    print(*sublist, sep=' ')