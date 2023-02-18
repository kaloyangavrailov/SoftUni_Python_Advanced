size = int(input())
output_direction = {

}
directions_dict = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0,1),
}


bunny_pos = []
bunny_move_pos = []
matrix = []
eggs = 0
max_eggs = 0
for r in range(size):
    sublist = input().split()
    if not bunny_pos:
        for c in range(size):
            if sublist[c] == 'B':
                bunny_pos = [r,c]
    matrix.append(sublist)


for item in directions_dict.items():
    br, bc = bunny_pos[0] + item[1][0], bunny_pos[1] + item[1][1]
    while 0 <= br < size and 0 <= bc < size:
        if matrix[br][bc] == 'X':
            break
        bunny_move_pos.append([br, bc])
        eggs += int(matrix[br][bc])
        br, bc = br + item[1][0], bc + item[1][1]

    output_direction[eggs] = bunny_move_pos.copy()
    output_direction[eggs].append(item[0])
    bunny_move_pos.clear()
    eggs = 0
print(output_direction[max(output_direction.keys())][-1])
for sublist in range(0,len(output_direction[max(output_direction.keys())])-1):
    print(output_direction[max(output_direction.keys())][sublist])
print(max(output_direction.keys()))