def start_spring(**kwargs):
    spring_collections = {}
    for value, key in kwargs.items():
        if key not in spring_collections:
            spring_collections[key] = [value]
        else:
            spring_collections[key].append(value)
    spring_collections = {i:sorted(j) for i, j in spring_collections.items()}
    spring_collections = sorted(spring_collections.items(), key=lambda x: (-len(x[1]), x[0]))
    print_list = []

    for el in spring_collections:
        print_list.append(f'{el[0]}:\n')
        for list_el in el[1]:
            print_list.append(f'-{list_el}\n')
    return ''.join(print_list)






# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
#
# print(start_spring(**example_objects))

#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))