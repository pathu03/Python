student_heigths=input("student heigths").split()
for n in range(0,len(student_heigths)):
    student_heigths[n]=int(student_heigths[n])
print(student_heigths)


total_eigth=0
for heigth in student_heigths:
    total_eigth += heigth
print(total_eigth)

number_of_student=0
for student in student_heigths:
    number_of_student +=1
print(number_of_student)


averag_height=round(total_eigth / number_of_student)
print(averag_height)