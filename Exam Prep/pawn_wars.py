def pawn_movement(grid, pawn_position, directions, flag, color):
    if color == 1 and not flag:
        for item in (directions['diagonal_up_left'], directions['diagonal_up_right'], directions['up']):
            new_p_pos_x, new_p_pos_y = pawn_position[0] + item[0], pawn_position[1] + item[1]
            if 0 <= new_p_pos_x < len(grid[0]) and 0 <= new_p_pos_y < len(grid[0]):
                if grid[new_p_pos_x][new_p_pos_y] == 'b' and (item[0] != -1 or item[1] != 0):
                    flag = True
                    break
                elif item[0] == -1 and item[1] == 0:
                    if grid[new_p_pos_x][new_p_pos_y] == '-':
                        grid[pawn_position[0]][pawn_position[1]] = '-'
        pawn_position[0], pawn_position[1] = new_p_pos_x, new_p_pos_y
        grid[pawn_position[0]][pawn_position[1]] = 'w'
        if not flag:
            color = 0
    elif color == 0 and not flag:
        for item in (directions['diagonal_down_left'], directions['diagonal_down_right'], directions['down']):
            new_p_pos_x, new_p_pos_y = pawn_position[0] + item[0], pawn_position[1] + item[1]
            if 0 <= new_p_pos_x < len(grid[0]) and 0 <= new_p_pos_y < len(grid[0]):
                if grid[new_p_pos_x][new_p_pos_y] == 'w' and (item[0] != -1 and item[1] != 0):
                    flag = True
                    break
                elif item[0] == 1 and item[1] == 0:
                    if grid[new_p_pos_x][new_p_pos_y] == '-':
                        grid[pawn_position[0]][pawn_position[1]] = '-'
        pawn_position[0], pawn_position[1] = new_p_pos_x, new_p_pos_y
        grid[pawn_position[0]][pawn_position[1]] = 'b'
        if not flag:
            color = 1
    return grid, pawn_position, flag, color


SIZE = 8

board = []
w_pos = []
b_pos = []
for row in range(SIZE):
    sublist = input().split()
    for element in sublist:
        if element == 'b':
            b_pos = [row, sublist.index(element)]
        elif element == 'w':
            w_pos = [row, sublist.index(element)]
    board.append(sublist)

piece_captured = False
turn = 1 #1 is white, 0 is black

d_d = {
    'up': (-1, 0),
    'down': (1, 0),
    'diagonal_up_left': (-1, -1),
    'diagonal_up_right': (-1, 1),
    'diagonal_down_left': (1, -1),
    'diagonal_down_right': (1, 1)
}

letters_dict = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}
numbers_dict = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1',
}

while w_pos[0] != 0 and b_pos[0] != SIZE-1 and not piece_captured:
    board, w_pos, piece_captured, turn = pawn_movement(board, w_pos, d_d, piece_captured, turn)
    # print(f'=========================')
    # for sublist in board:
    #     print(' '.join(sublist))
    board, b_pos, piece_captured, turn = pawn_movement(board, b_pos, d_d, piece_captured, turn)
    # print(f'=========================')
    # for sublist in board:
    #     print(' '.join(sublist))

if w_pos[0] == 0 and not piece_captured:
    position = f'{letters_dict[w_pos[1]]}{numbers_dict[w_pos[0]]}'
    print(f'Game over! White pawn is promoted to a queen at {position}.')
elif b_pos[0] == SIZE - 1 and not piece_captured:
    position = f'{letters_dict[b_pos[1]]}{numbers_dict[b_pos[0]]}'
    print(f'Game over! Black pawn is promoted to a queen at {position}.')
elif piece_captured:
    if turn == 1:
        position = f'{letters_dict[w_pos[1]]}{numbers_dict[w_pos[0]]}'
        print(f'Game over! White win, capture on {position}.')
    elif turn == 0:
        position = f'{letters_dict[b_pos[1]]}{numbers_dict[b_pos[0]]}'
        print(f'Game over! Black win, capture on {position}.')
