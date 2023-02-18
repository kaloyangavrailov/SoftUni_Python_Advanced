matrix = [list(map(int, input().split(', '))) for row in range(int(input()))]
even_matrix = [[el for el in matrix[row] if el % 2 == 0] for row in range(len(matrix))]
print(even_matrix)