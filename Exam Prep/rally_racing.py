SIZE = int(input())
car_name = input()
tunnel_a_pos = []
tunnel_b_pos = []
track = []
for iteration in range(SIZE):
    sublist = input().split()
    for element in sublist:
        if element == 'T':
            if tunnel_a_pos:
                tunnel_b_pos = [iteration, sublist.index(element)]
            else:
                tunnel_a_pos = [iteration, sublist.index(element)]
    track.append(sublist)

d_d = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

distance = 0
p_pos = [0, 0]
track[0][0] = 'C'
finished = False
while True:

    command = input()
    if command == 'End':
        break
    new_x, new_y = d_d[command][0] + p_pos[0], d_d[command][1] + p_pos[1]
    if new_x == tunnel_a_pos[0] and new_y == tunnel_a_pos[1]:
        track[new_x][new_y] = '.'
        track[p_pos[0]][p_pos[1]] = '.'
        p_pos[0], p_pos[1] = tunnel_b_pos[0], tunnel_b_pos[1]
        track[p_pos[0]][p_pos[1]] = 'C'
        distance += 30
    elif new_x == tunnel_b_pos[0] and new_y == tunnel_b_pos[1]:
        track[new_x][new_y] = '.'
        track[p_pos[0]][p_pos[1]] = '.'
        p_pos[0], p_pos[1] = tunnel_a_pos[0], tunnel_a_pos[1]
        track[p_pos[0]][p_pos[1]] = 'C'
        distance += 30
    elif track[new_x][new_y] == 'F':
        track[p_pos[0]][p_pos[1]] = '.'
        p_pos[0], p_pos[1] = new_x, new_y
        track[p_pos[0]][p_pos[1]] = 'C'
        distance += 10
        finished = True
        break
    else:
        track[p_pos[0]][p_pos[1]] = '.'
        p_pos[0], p_pos[1] = new_x, new_y
        track[p_pos[0]][p_pos[1]] = 'C'
        distance += 10

if finished:
    print(f'Racing car {car_name} finished the stage!')
else:
    print(f'Racing car {car_name} DNF.')
print(f'Distance covered {distance} km.')
for sublist in track:
    print(''.join(sublist))
