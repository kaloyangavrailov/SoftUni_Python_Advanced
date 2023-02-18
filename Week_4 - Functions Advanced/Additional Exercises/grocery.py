def grocery_store(**kwargs):
    dict = kwargs
    dict_sorted = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []

    for el in dict_sorted:
        result.append(f"{el[0]}: {el[1]}")

    return '\n'.join(result)








print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))