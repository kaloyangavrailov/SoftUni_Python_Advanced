def shopping_list(budget, **kwargs):
    d = kwargs
    total_sum = 0
    bought_items = []
    if budget < 100:
        return f'You do not have enough budget.'
    else:
        for item in d.items():
            if total_sum + (item[1][0] * item[1][1]) <= budget:
                total_sum += item[1][0] * item[1][1]
                if len(bought_items) == 5:
                    break
                bought_items.append([item[0], item[1][0] * item[1][1]])
    print_string = []
    for el in bought_items:
        print_string.append(f'You bought {el[0]} for {el[1]:.2f} leva.\n')
    return ''.join(print_string)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

#
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))


# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),))