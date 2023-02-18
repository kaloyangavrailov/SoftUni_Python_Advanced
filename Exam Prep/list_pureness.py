from collections import deque


def best_list_pureness(*args):
    lst, num = args
    lst = deque(lst)
    d = {}
    pureness = 0
    for iteration in range(0,num+1):

        for el in lst:
            pureness += lst.index(el) * el
        if pureness in d:
            pureness = 0
            continue

        else:
            d[pureness] = iteration
        pureness = 0
        lst.rotate(-(len(lst) - 1))
    return f'Best pureness {max(d.keys())} after {d[max(d.keys())]} rotations'



test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
# #
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)