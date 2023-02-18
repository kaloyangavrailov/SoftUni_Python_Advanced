def students_credits(*args):
    print_string = []
    total_credits = 0
    info = args
    dict_grades = {}
    for el in info:
        subject, subject_credits, max_points, student_points = el.split('-')
        if int(student_points) == 0:
            obtained_credits = 0
        else:
            obtained_credits = int(subject_credits) / (int(max_points) / int(student_points))
        dict_grades[subject] = obtained_credits
        total_credits += obtained_credits
    dict_grades = {j:i for j, i in sorted(dict_grades.items(), key= lambda x: -x[1])}
    if total_credits >= 240:
        print_string.append(f'Diyan gets a diploma with {total_credits:.1f} credits.\n')
    else:
        print_string.append(f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n')
    for item in dict_grades.items():
        print_string.append(f"{item[0]} - {item[1]:.1f}\n")
    return ''.join(print_string)


print(students_credits("Computer Science-12-300-0"))

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )


# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )


