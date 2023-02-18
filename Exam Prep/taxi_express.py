from collections import deque

total_time = 0
customers = deque(list(map(int, input().split(', '))))  # first
taxis = deque(list(map(int, input().split(', '))))  # last

while customers and taxis:
    if customers[0] <= taxis[-1]:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if not customers:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
elif not taxis:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customers))}')

