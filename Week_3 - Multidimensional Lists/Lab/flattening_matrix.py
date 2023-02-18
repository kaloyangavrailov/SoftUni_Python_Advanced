matrix = [list(map(int, input().split(', '))) for row in range(int(input()))]
flat_matrix = [el for sublist in matrix for el in sublist]
print(flat_matrix)