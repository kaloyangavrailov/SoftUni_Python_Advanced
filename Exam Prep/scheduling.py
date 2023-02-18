from collections import deque


jobs = deque(list(map(int, input().split(', '))))
index_cycle = int(input())

total_time = 0
jobs_copy = jobs.copy()
for el in jobs:

    min_el = min(jobs_copy)
    min_el_index = jobs_copy.index(min_el)
    total_time += min_el
    if jobs_copy.index(min_el) == index_cycle:
        break
    jobs_copy[min_el_index] = 101

print(total_time)