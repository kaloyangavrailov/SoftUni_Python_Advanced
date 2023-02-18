from collections import deque


def fill_the_box(*args):
    lst = deque(args)
    height = lst.popleft()
    length = lst.popleft()
    width = lst.popleft()
    size_container = height * length * width
    remaining_cubes = 0

    for el in lst:
        if el == 'Finish':
            break
        if size_container < el:
            remaining_cubes += el - size_container
            size_container = 0
        else:
            size_container -= el

    if size_container:
        return f'There is free space in the box. You could put {size_container} more cubes.'
    else:
        return f"No more free space! You have {remaining_cubes} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))