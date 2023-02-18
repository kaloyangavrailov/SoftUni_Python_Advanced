from collections import deque

box_clothes = deque(map(int, input().split()))
rack_capacity = int(input())
number_racks = 1
current_rack_capacity = rack_capacity
while box_clothes:
    if box_clothes[-1] > current_rack_capacity:
        number_racks += 1
        current_rack_capacity = rack_capacity
        continue
    else:

        current_rack_capacity -= box_clothes[-1]
        box_clothes.pop()
print(number_racks)
