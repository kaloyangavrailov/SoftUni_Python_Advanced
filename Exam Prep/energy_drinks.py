from collections import deque
MAX_CAFFEINE = 300
mg_caffeine = deque(map(int, input().split(', ')))  # last

energy_drinks = deque(map(int, input().split(', ')))  # first

initial_caffeine = 0

while mg_caffeine and energy_drinks:
    intake = mg_caffeine[-1] * energy_drinks[0]
    if initial_caffeine + intake <= MAX_CAFFEINE:
        mg_caffeine.pop()
        energy_drinks.popleft()
        initial_caffeine += intake
    else:
        mg_caffeine.pop()
        energy_drinks.rotate(len(energy_drinks)-1)
        if initial_caffeine - 30 >= 0:
            initial_caffeine -= 30
        else:
            initial_caffeine = 0
if energy_drinks:
    print(f'Drinks left: {", ".join(list(map(str, energy_drinks)))}')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f'Stamat is going to sleep with {initial_caffeine} mg caffeine.')