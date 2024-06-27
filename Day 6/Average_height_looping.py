student_heights = input().split()
total = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total += student_heights[n]
print(f"total height = {total}")
no_of_students = len(student_heights)
print(f"number of students = {no_of_students}")
average_height = round(total / no_of_students)
print(f"average height = {average_height}")
