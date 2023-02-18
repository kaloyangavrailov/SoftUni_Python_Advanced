matrix = [list(map(int, input().split())) for _ in range(int(input()))]

sum_diagonal = 0

for index in range(len(matrix)):
    sum_diagonal += matrix[index][index]
print(sum_diagonal)