n = int(input())

elements = set()

for iteration in range(n):
    chem_element = input().split()
    for piece in chem_element:
        elements.add(piece)
print(*elements, sep='\n')