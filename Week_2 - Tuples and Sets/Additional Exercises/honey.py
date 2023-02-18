from collections import deque


def print_func(bees,flower_jizz,goop):
    print(f'Total honey made: {goop}')
    if bees:
        print(f"Bees left: {', '.join(list(map(str, bees)))}")
    if flower_jizz:
        print(f"Nectar left: {', '.join(list(map(str, flower_jizz)))}")


working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
operands = deque(x for x in input().split())
honey_produced = 0

dict_operands = {
    "+": lambda x,y: abs(x + y),
    "-": lambda x,y: abs(x -y),
    "*": lambda x,y: abs(x * y),
    "/": lambda x,y: abs(x / y)
}

while working_bees and nectar:
    if working_bees[0] <= nectar[-1]:
        honey_produced += dict_operands[operands.popleft()](working_bees.popleft(), nectar.pop())
    elif working_bees[0] > nectar[-1]:
        nectar.pop()
        continue

print_func(working_bees,nectar,honey_produced)