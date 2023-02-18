students = int(input())
student_grades = {}
for student in range(students):
    name, grades = input().split()
    if name not in student_grades.keys():
        student_grades[name] = []
    student_grades[name].append(float(grades))

for item in student_grades.items():
    convert_grades_to_string = ' '.join(map(lambda grade: f'{grade:.2f}', item[1]))
    average_grade = sum(item[1])/len(item[1])
    print(f'{item[0]} -> {convert_grades_to_string} (avg: {average_grade:.2f})')