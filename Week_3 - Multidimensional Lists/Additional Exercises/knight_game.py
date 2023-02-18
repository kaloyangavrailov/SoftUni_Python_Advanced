size = int(input())


knights = []
board = []
attacks = 0
max_attacks = 0
knight_to_remove = ''
knights_removed = 0
knight_directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
)

knights_attack_dict = {

}

for row in range(size):
    sublist = list(input())
    for cell in range(size):
        if sublist[cell] == 'K':
            knights.append([row, cell])
    board.append(sublist)

flag = True
same_value_flag = False
while flag:

    for knight in knights:
        for direction in knight_directions:
            kr = knight[0] + direction[0]
            kc = knight[1] + direction[1]

            if 0 <= kr < size and 0 <= kc < size:
                knights_attack_dict[str(knight[0])+str(knight[1])]: 0
                if board[kr][kc] == 'K':
                    attacks += 1

        knights_attack_dict[str(knight[0])+str(knight[1])] = attacks
        attacks = 0
    for knight in knights_attack_dict.keys():
        if knights_attack_dict[knight] > 0:
            if knights_attack_dict[knight] >= max_attacks:
                max_attacks = knights_attack_dict[knight]
                same_value_flag = False
                knight_to_remove = knight
                if knights_attack_dict[knight] == max_attacks:
                    continue
            else:
                continue
    if sum(knights_attack_dict.values()) == 0:
        break
    max_attacks = 0
    board[int(knight_to_remove[0])][int(knight_to_remove[1])] = '0'
    knights_removed += 1
    knights.remove([int(knight_to_remove[0]),int(knight_to_remove[1])])
    knights_attack_dict.clear()
    knight_to_remove = ''

print(knights_removed)