from collections import deque
energy_used = 0
toys_made = 0
elf_energy = deque(map(int, input().split()))  # first
materials = deque(map(int, input().split()))  # last
iteration = 1
while True:
    if not elf_energy or not materials:
        break

    if elf_energy[0] < 5:
        elf_energy.popleft()
        continue
    else:
        elf = elf_energy.popleft()
        toy = materials.pop()

    if iteration % 5 == 0:
        if iteration % 3 == 0:
            toy *= 2
        if elf >= toy:
            energy_used += toy
            elf -= toy
        else:
            elf *= 2
            if iteration % 3 == 0:
                toy /= 2
            materials.append(toy)
        elf_energy.append(elf)
    elif iteration % 3 == 0:
        toy *= 2
        if elf >= toy:
            elf -= toy - 1
            toys_made += 2
            energy_used += toy
        else:
            elf *= 2
            materials.append(int(toy/2))
        elf_energy.append(elf)
    else:
        if elf >= toy:
            elf -= toy - 1
            energy_used += toy
            toys_made += 1
        else:
            elf *= 2
            materials.append(toy)
        elf_energy.append(elf)
    iteration += 1
print(f'Toys: {toys_made}')
print(f'Energy: {energy_used}')
if elf_energy:
    print(f'Elves left: {", ".join(map(str, elf_energy))}')
if materials:
    print(f'Boxes left: {", ".join(map(str, materials))}')
