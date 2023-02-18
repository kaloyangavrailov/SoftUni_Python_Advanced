input_string = sorted(input())

dict_string = {x:input_string.count(x) for x in input_string}

for item in dict_string.items():
    print(f'{item[0]}: {item[1]} time/s')