def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    while len(triangle) != n:
        if len(triangle[-1]) == 2:
            triangle.append([1, 2, 1])
            continue
        last_lst_length = len(triangle[-1])
        range_indixes = []
        for index in range(1 , last_lst_length-1):
            range_indixes.append(index)
        new_sublist = []
        for i in range(0, last_lst_length):
            if i == 0:
                new_sublist.append(triangle[-1][i])
            if i in range_indixes:
                new_sublist.append(triangle[-1][i] + triangle[-1][i - 1])
            if i == last_lst_length - 1:
                new_sublist.append(triangle[-1][i] + triangle[-1][i - 1])
                new_sublist.append(triangle[-1][i])
        triangle.append(new_sublist)
    return triangle

get_magic_triangle(5)