from collections import deque

seats = tuple(input().split(', '))

first_sequence = deque(list(map(int, input().split(', '))))  # first
second_sequence = deque(list(map(int, input().split(', '))))  # last

seats_matched = []
rotations = 0


for iteration in range(1,11):
    if len(seats_matched) == 3:
        break
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    option_a = f'{first_number}{chr(first_number + second_number)}'
    option_b = f'{second_number}{chr(first_number + second_number)}'
    for seat in seats:
        if option_a == seat or option_b == seat:
            if seat not in seats_matched:
                seats_matched.append(seat)
                break
            else:
                break
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)
    rotations = iteration
print(f'Seat matches: {", ".join(seats_matched)}')
print(f'Rotations count: {rotations}')