expression = input()

index_list_opening_parenthesis = []

for index in range(0, len(expression)):
    if expression[index] == '(':
        index_list_opening_parenthesis.append(index)
    elif expression[index] == ')':
        starting_index = index_list_opening_parenthesis.pop()
        print(expression[starting_index:index+1])
