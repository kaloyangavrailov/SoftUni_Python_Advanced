n = int(input())
set_a = set()
set_b = set()
intersections = {}

for _ in range(n):
    range_a, range_b = input().split('-')
    start_range_a, end_range_a = range_a.split(',')
    start_range_b, end_range_b = range_b.split(',')
    set_a = {x for x in range(int(start_range_a), int(end_range_a)+1)}
    set_b = {x for x in range(int(start_range_b), int(end_range_b)+1)}
    intersection = list(set_a.intersection(set_b))
    intersections[len(intersection)] = intersection

print(f'Longest intersection is {intersections[max(intersections.keys())]} with length {max(intersections.keys())}')