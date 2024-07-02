# inputs= 156,178,165,171,187

students_height= input("Enter a list of students height!!").split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
# print(students_height)

total_height = 0
for height in students_height:
    total_height += height
# print(total_height)

number_of_students=0
for students in students_height:
    number_of_students += 1
# print(number_of_students)

average_height=round(total_height/number_of_students)
print(average_height)


# NEXT METHOD without using for loop
total_height=sum(students_height)
number_of_student=len(students_height)
average_height= round(total_height/number_of_student)
print(average_height)