def even_odd_filter(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if key == 'even':
            lst = [el for el in value if el%2 == 0]
            dict[key] = lst
        elif key == 'odd':
            lst = [el for el in value if el%2 != 0]
            dict[key] = lst
    dict = sorted(dict.items(), key= lambda x: -len(x[1]))
    dict = {key: value for key, value in dict}
    return dict

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))