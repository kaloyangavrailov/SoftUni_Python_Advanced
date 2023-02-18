from collections import deque

bowls_ramen = deque(map(int, input().split(', ')))  # last

customers = deque(map(int, input().split(', ')))  # first

while bowls_ramen and customers:
    if bowls_ramen[-1] == customers[0]:
        bowls_ramen.pop()
        customers.popleft()
    elif bowls_ramen[-1] > customers[0]:
        bowls_ramen[-1] -= customers.popleft()
        continue
    elif bowls_ramen[-1] < customers[0]:
        customers[0] -= bowls_ramen.pop()
        continue

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_ramen))}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
