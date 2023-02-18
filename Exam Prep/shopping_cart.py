def shopping_cart(*args):
    product_limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }

    print_list = []

    cart = args

    d_cart = {
        'Pizza': [],
        'Dessert': [],
        'Soup': []
    }
    for el in cart:
        if isinstance(el, tuple):
            if el[1] not in d_cart[el[0]]:
                if len(d_cart[el[0]]) < product_limits[el[0]]:
                    d_cart[el[0]].append(el[1])
        else:
            break

    if d_cart['Pizza'] or d_cart['Dessert'] or d_cart['Soup']:
        d_cart = sorted(d_cart.items(), key=lambda x: (-len(x[1]), x[0]))
        d_cart = {i: j for i, j in d_cart}
        d_cart = {i: sorted(j) for i, j in d_cart.items()}
        for item in d_cart.items():
            print_list.append(f'{item[0]}:\n')
            for element in item[1]:
                print_list.append(f' - {element}\n')
        return ''.join(print_list)
    else:
        return f'No products in the cart!'



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))