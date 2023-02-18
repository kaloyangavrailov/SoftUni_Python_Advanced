r, c = input().split(', ')
matrix = [list(map(int,input().split(', '))) for row in range(int(r))]
sum_all_numbers = 0
for i in range(len(matrix)):
    sum_all_numbers += sum(matrix[i])
print(sum_all_numbers)
print(matrix)