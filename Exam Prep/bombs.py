from collections import deque

bomb_effects = deque(list(map(int,input().split(', '))))  # first
bomb_casings = deque(list(map(int,input().split(', '))))  # last

table = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}

datura_bombs = False
datura_bombs_count = 0

cherry_bombs = False
cherry_bombs_count = 0

smoke_bombs = False
smoke_bombs_count = 0

AMOUNT_NEEDED = 3

filled_bombs_pouch = False


while bomb_casings and bomb_casings and not filled_bombs_pouch:
    sum_bomb_value = bomb_effects[0] + bomb_casings[-1]
    if sum_bomb_value in table.values():
        for key in table.keys():
            if sum_bomb_value == table[key]:
                if key == 'Datura Bombs':
                    datura_bombs_count += 1
                    if datura_bombs_count == AMOUNT_NEEDED:
                        datura_bombs = True
                elif key == 'Cherry Bombs':
                    cherry_bombs_count += 1
                    if cherry_bombs_count == AMOUNT_NEEDED:
                        cherry_bombs = True
                elif key == 'Smoke Decoy Bombs':
                    smoke_bombs_count += 1
                    if smoke_bombs_count == AMOUNT_NEEDED:
                        smoke_bombs = True
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        if bomb_casings[-1] >= 5:
            bomb_casings[-1] -= 5

    if smoke_bombs and cherry_bombs and datura_bombs:
        filled_bombs_pouch = True

if filled_bombs_pouch:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print(f'Bomb Effects: empty')
else:
    print(f'Bomb Effects: {", ".join(map(str,bomb_effects))}')
if not bomb_casings:
    print(f'Bomb Casings: empty')
else:
    print(f'Bomb Casings: {", ".join(map(str,bomb_casings))}')
print(f'Cherry Bombs: {cherry_bombs_count}')
print(f'Datura Bombs: {datura_bombs_count}')
print(f'Smoke Decoy Bombs: {smoke_bombs_count}')