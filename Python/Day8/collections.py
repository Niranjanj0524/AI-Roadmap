#List
print("---list---")
list1 = [11,55,22,88,44,66,77,88,99,22]
print(list[:10])
print("Max : " , max(list1))
print("Min : " , min(list1))
sum1 = sum(list1)
print("Avg : " , sum1/len(list1))
result = list(dict.fromkeys(list1))
print("Unique List : ", result)
print("Reverse list : " , list1[::-1])

#Tuple
print("\n ---Tuple---")
my_tuple = (11,33,22,77,22)
print("Printing elements using loop:")
for num in my_tuple:
    print(num)
print("Min : ",min(my_tuple))
print("Max : ",max(my_tuple))
print("Count of 2 times 22 : " , my_tuple.count(22))
convert = tuple(list1)
print("convert list into tuple : ",convert)
if 33 in my_tuple:
    print("Yes 33 is in tuple")
else:
    print("33 is not in tuple")

#Set
print("\n ---Set---")
set_my = set(list1)
set1 = {1,2,3,4,5,6,7,8}
set2 = {1,4,3,5}
print("Set from list : " , set(set_my))
print("Union of set1 & set2 : ",set1.union(set2))
print("Intersection of set1 & set2 : ", set1.intersection(set2))
print("difference between set1 & set2 : ",set1.difference(set2))

student1_subjects = {"Maths", "Science", "English"}
student2_subjects = {"History", "Science", "Maths"}

common_subjects = student1_subjects.intersection(student2_subjects)
print("Common subjects:", common_subjects)

#Dictionary
print("\n ---Dictionary---")
student ={
    "Name" : "Niranjan",
    "Age" : 22,
    "Marks" : 88
}
print(student)
student["City"] = "Solapur"
print(student)
student["Marks"] = 99
print(student)
for key,value in student.items():
    print(f"{key} : {value}")

students_marks = {
    "Amit": 82,
    "Sania": 95,
    "Rohit": 78,
    "Neha": 91,
    "Vikas": 88
}

top_student = max(students_marks, key=students_marks.get)

print("All Students:", students_marks)
print(f"Student with highest marks is {top_student} with {students_marks[top_student]} marks.")
