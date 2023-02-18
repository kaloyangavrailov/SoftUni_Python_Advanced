n = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(n)]

primary_diagonal = [matrix[el][el] for el in range(len(matrix))]
secondary_diagonal = []

for r in range(len(matrix)):
        secondary_diagonal.append(matrix[r][n-r-1])

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')