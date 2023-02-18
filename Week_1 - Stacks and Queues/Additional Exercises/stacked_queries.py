empty_stack = []

dict_functions = {
    1: lambda x: empty_stack.append(x[1]),
    2: lambda x: empty_stack.pop() if empty_stack else None,
    3: lambda x: print(max(empty_stack)),
    4: lambda x: print(min(empty_stack)),
}
int_input = int(input())

for _ in range(int_input):
    query = [int(x) for x in input().split()]
    dict_functions[query[0]](query)
empty_stack.reverse()

empty_stack = [str(x) for x in empty_stack]
print(', '.join(empty_stack))