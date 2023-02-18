from collections import deque

eggs = deque(map(int, input().split(', '))) # first
paper = deque(map(int, input().split(', '))) # last

BOX_SIZE = 50

boxes_filled = 0

while eggs and paper:
    if eggs[0] <= 0:
        eggs.popleft()
        continue
    elif eggs[0] == 13:
        eggs.popleft()
        paper[0], paper[-1] = paper[-1], paper[0]
        continue
    if eggs[0] + paper[-1] <= BOX_SIZE:
        boxes_filled += 1
    eggs.popleft()
    paper.pop()

if boxes_filled:
    print(f'Great! You filled {boxes_filled} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(list(map(str, eggs)))}')
if paper:
    print(f'Pieces of paper left: {", ".join(list(map(str, paper)))}')