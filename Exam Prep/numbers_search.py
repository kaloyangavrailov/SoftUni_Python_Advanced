def numbers_searching(*args):
    duplicates = []
    missing_value = []
    values_to_compare = []
    lst = args
    min_value = min(lst)
    max_value = max(lst)
    for number in range(min_value, max_value+1):
        if number not in lst:
            missing_value.append(number)
    for el in lst:
        if lst.count(el) > 1:
            if el not in duplicates:
                duplicates.append(el)

    duplicates = sorted(duplicates)
    missing_value.append(duplicates)
    return missing_value

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))