from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents_crafted = {
    'Bicycle':0,
    'Doll': 0,
    'Teddy bear': 0,
    'Wooden train': 0,
}

magic_needed = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while materials and magic:
    if materials[-1] * magic[0] in magic_needed.keys():
        presents_crafted[magic_needed[materials.pop()*magic.popleft()]] += 1
    elif materials[-1] * magic[0] < 0:
        materials.append(materials.pop() + magic.popleft())
    elif materials[-1] * magic[0] not in magic_needed.keys() and materials[-1] * magic[0] > 0:
        magic.popleft()
        materials[-1] += 15
    if materials and magic:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.pop()
else:
    for item in presents_crafted.copy().items():
        if item[1] == 0:
            del presents_crafted[item[0]]
    if {"Doll", "Wooden train"}.issubset(list(presents_crafted.keys())) or {"Teddy bear","Bicycle"}.issubset(list(presents_crafted.keys())):
        print(f'The presents are crafted! Merry Christmas!')
    else:
        print(f'No presents this Christmas!')
    if materials:
        print(f'Materials left: {", ".join(list(map(str,materials)))}')
    if magic:
        print(f'Magic left: {", ".join(list(map(str,magic)))}')

    for item in presents_crafted.items():
        print(f'{item[0]}: {item[1]}')
