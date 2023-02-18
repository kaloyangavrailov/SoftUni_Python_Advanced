from collections import deque

quantity_food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

while quantity_food and orders:
    if orders and orders[0] <= quantity_food:
        quantity_food -= orders[0]
        orders.popleft()
    else:break



if not orders:
    print(f'Orders complete')
else:
    print('Orders left: ' + " ".join(map(str, orders)))