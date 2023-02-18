from collections import deque


def print_func(shakes,choc,milk_c):
    if shakes == 5:
        print(f'Great! You made all the chocolate milkshakes needed!')
    else:
        print(f'Not enough milkshakes.')
    if choc:
        print(f'Chocolate: {", ".join(list(map(str, choc)))}')
    else:
        print(f'Chocolate: empty')
    if milk_c:
        print(f'Milk: {", ".join(list(map(str, milk_c)))}')
    else:
        print("Milk: empty")


chocolates = deque(int(x) for x in input().split(','))
cups_milk = deque(int(x) for x in input().split(','))
milkshakes = 0

while milkshakes < 5 and chocolates and cups_milk:
    if chocolates[-1] + cups_milk[0] <= chocolates[-1]:
        cups_milk.popleft()
    elif chocolates[-1] + cups_milk[0] <= cups_milk[0]:
        chocolates.pop()
    else:
        if chocolates[-1] == cups_milk[0]:
            milkshakes += 1
            cups_milk.popleft()
            chocolates.pop()
        else:
            cups_milk.rotate(len(cups_milk)-1)
            chocolates[-1] -= 5

print_func(milkshakes,chocolates,cups_milk)