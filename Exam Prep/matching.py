from collections import deque

males = list(map(int, input().split()))  # last
females = deque(list(map(int, input().split())))  # first
matches = 0
males = deque(males[::-1])

while males and females:
    if males[0] <= 0:
        males.popleft()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    if males[0] % 25 == 0:
        males.popleft()
        males.popleft()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[0] == females[0]:
        males.popleft()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[0] -= 2
print(f'Matches: {matches}')
if males:
    print(f"Males left: {', '.join(list(map(str, males)))}")
else:
    print(f'Males left: none')
if females:
    print(f"Females left: {', '.join(list(map(str, females)))}")
else:
    print(f'Females left: none')