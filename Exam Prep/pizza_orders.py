from collections import deque

orders = deque(list(map(int, input().split(', '))))  # first
employees = deque(list(map(int, input().split(', '))))  # last
pizzas_made = 0
while orders and employees:
    if orders[0] > 10 or orders[0] <= 0:
        orders.popleft()
        continue
    if orders[0] <= employees[-1]:
        pizzas_made += orders[0]
        orders.popleft()
        employees.pop()
    elif orders[0] > employees[-1]:
        pizzas_made += employees[-1]
        orders[0] -= employees[-1]
        employees.pop()
if not orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join(map(str,employees))}')
elif not employees:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str,orders))}')

