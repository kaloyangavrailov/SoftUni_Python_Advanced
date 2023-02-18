numbers = tuple(map(float, input().split()))
numbers_iterated = []
for number in numbers:
    if number not in numbers_iterated:
        print(f'{number:.1f} - {numbers.count(number)} times')
        numbers_iterated.append(number)
    else:
        continue
