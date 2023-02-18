from collections import deque

sequence_parenthesis =deque(x for x in input())
open_parenthesis = deque()
while sequence_parenthesis:
    parenthesis = sequence_parenthesis.popleft()
    if parenthesis in '({[':
        open_parenthesis.append(parenthesis)
    elif not open_parenthesis:
        print(f'NO')
        break
    elif f'{open_parenthesis.pop()+ parenthesis}' not in '{}()[]':
        print(f'NO')
        break
else:
    print(f'YES')