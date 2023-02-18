input_string = input()

input_string_list = [item for item in input_string]

while len(input_string_list) > 0:
    character = input_string_list.pop()
    print(character, end='')