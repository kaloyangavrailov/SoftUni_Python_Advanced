matrix = [list(map(int,input().split())) for _ in range(int(input()))]

primary_diagonal = 0
secondary_diagonal = 0

for r in range(len(matrix)):
    primary_diagonal += matrix[r][r]

for r in range(len(matrix)):
    secondary_diagonal += matrix[r][len(matrix)-r-1]

print(abs(primary_diagonal-secondary_diagonal))