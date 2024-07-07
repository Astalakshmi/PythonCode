student_heights = input("Enter the Student's heights:").split()
total = 0
# total of student's height
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total += student_heights[n]
print(f"total height = {total}")
# total length of students
no_of_students = 0
for students in student_heights:
    no_of_students += 1
print(f"number of students = {no_of_students}")
average_height = round(total / no_of_students)
print(f"average height = {average_height}")
