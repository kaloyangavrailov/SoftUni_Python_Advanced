from collections import deque

pair_achieved = False
gemstone = False
porcelain = False
gold = False
diamond = False
crafted_gifts = []
recipe = {
    'Gemstone': [100, 199],
    'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399],
    'Diamond Jewellery': [400, 499]
}

materials = deque(list(map(int, input().split())))  # last
magic = deque(list(map(int, input().split())))  # first


while materials and magic:
    mix = materials[-1] + magic[0]
    if mix < 100:
        if mix % 2 == 0:
            mix = (materials[-1] * 2) + (magic[0] * 3)
        elif mix % 2 != 0:
            mix = mix * 2
    elif mix > 499:
        mix //= 2
    if 100 <= mix <= 499:
        for key in recipe.keys():
            if recipe[key][0] <= mix <= recipe[key][1]:
                if key == 'Gemstone':
                    crafted_gifts.append('Gemstone')
                    gemstone = True
                    break
                elif key == 'Porcelain Sculpture':
                    crafted_gifts.append('Porcelain Sculpture')
                    porcelain = True
                    break
                elif key == 'Gold':
                    crafted_gifts.append('Gold')
                    gold = True
                    break
                elif key == 'Diamond Jewellery':
                    crafted_gifts.append('Diamond Jewellery')
                    diamond = True
                    break
    materials.pop()
    magic.popleft()
    if (gemstone and porcelain) or (gold and diamond):
        pair_achieved = True
if pair_achieved:
    print(f'The wedding presents are made!')
else:
    print(f'Aladdin does not have enough wedding presents.')
if materials:
    print(f"Materials left: {', '.join(list(map(str, materials)))}")
if magic:
    print(f"Magic left: {', '.join(list(map(str, magic)))}")
for el in sorted(set(crafted_gifts.copy())):
    print(f'{el}: {crafted_gifts.count(el)}')
