from collections import deque

rows,columns = input().split()
snake_string = deque(input())

snake_string_copy = snake_string.copy()
snake_string_for_cycle = deque()
snake_matrix = []

for row in range(int(rows)):

    snake_matrix.append([])
    if len(snake_string_for_cycle) == 0:
        snake_string_for_cycle = snake_string_copy.copy()
    else:
        for iteration in range(len(snake_string)):
            snake_string_for_cycle.append(snake_string_copy.popleft())
    for column in range(int(columns)):
        snake_matrix[row].append(snake_string_for_cycle.popleft())
    snake_string_copy = snake_string.copy()

for r in range(int(rows)):
    if (r + 2) % 2 == 0:
        print(f'{"".join(snake_matrix[r])}')
    else:
        print(f'{"".join(snake_matrix[r][::-1])}')