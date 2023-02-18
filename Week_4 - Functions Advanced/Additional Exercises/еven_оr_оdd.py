def even_odd(*args):
    lst = args[:len(args)-1]
    command = args[-1]
    if command == 'even':
        even_lst = [int(el) for el in lst if el % 2 == 0]
        return even_lst
    elif command == 'odd':
        odd_lst = [el for el in lst if el % 2 != 0]
        return odd_lst


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))