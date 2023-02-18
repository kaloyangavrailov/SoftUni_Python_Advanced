rows, columns = input().split()
matrix = []
sublist = []
for r in range(97, 97+int(rows)):
    for c in range(97, 97+int(columns)):
        sublist.append(f'{chr(r)}{chr(r+c-97)}{chr(r)}')
    matrix.append(sublist.copy())
    sublist.clear()

[print(' '.join(el)) for el in matrix]
