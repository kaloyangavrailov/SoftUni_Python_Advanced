from collections import deque

effects = deque(list(map(int, input().split(', '))))  # first
power = deque(list(map(int, input().split(', '))))  # last

palm_firework = 0
willow_firework = 0
crossette_firework = 0

goal_reached = False

while not goal_reached and effects and power:
    if effects[0] <= 0:
        effects.popleft()
        continue
    elif power[-1] <= 0:
        power.pop()
        continue

    mix = effects[0] + power[-1]
    if mix % 3 == 0 and mix % 5 != 0:
        palm_firework += 1
        effects.popleft()
        power.pop()
    elif mix % 5 == 0 and mix % 3 != 0:
        willow_firework += 1
        effects.popleft()
        power.pop()
    elif mix % 5 == 0 and mix % 3 == 0:
        crossette_firework += 1
        effects.popleft()
        power.pop()
    else:
        effects[0] -= 1
        effects.rotate(len(effects) - 1)
        continue
    if willow_firework >= 3 and palm_firework >= 3 and crossette_firework >= 3:
        goal_reached = True

if goal_reached:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can't make the perfect firework show.")
if effects:
    print(f'Firework Effects left: {", ".join(list(map(str, effects)))}')
if power:
    print(f'Explosive Power left: {", ".join(list(map(str, power)))}')
print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossette_firework}')