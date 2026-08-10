#List Comprehension
print("List Comprehension")

list1 = [i for i in range(1,21)]
print(list1)

square_list = [i * i for i in range(1,11)]
print(square_list)

cube_list = [i * i * i for i in range(1,11)]
print(cube_list)

even_num = [i for i in range(1,51) if i % 2 == 0]
print(even_num)

odd_num = [i for i in range(1,51) if i % 2 == 1]
print(odd_num)

num = [10, 5, 20, 3, 8, 15]
res = [i for i in num if i > 10]
print(res)

lower = ["python", "java", "c++"]
upper = [name.upper() for name in lower]
print(upper)

len_find = ["Python", "AI", "MachineLearning", "LLM"]
list_len = [len(name) for name in len_find]
print(list_len)

list_divisible_5 = [i for i in range(1,51) if i % 5 == 0]
print(list_divisible_5)

Even_Odd = [i %2 == 0 for i in range(1,21)]
print(Even_Odd)
print("\n Dictionary Comprehension")


#Dictionary Comprehension
number = range(1,11)
sqr_num = {
    x: x** 2
    for x in number
}
print(sqr_num)

cube_num = {
    x: x** 3
    for x in number
}
print(cube_num)

even_sqr = {
    x: x** 2
    for x in number
    if x % 2 == 0
}
print(even_sqr)

names = ["Amit", "Rahul", "Priya"]
names_len = {
    x: len(x) 
    for x in names
}
print(names_len)

marks = {
    "Amit": 80, 
    "Rahul": 55, 
    "Priya": 90, 
    "Sneha": 45
}
passed_stud = {
    name: score for name, 
    score in marks.items() 
    if score > 70
}
print(passed_stud)

increse_marks_10 = {
    name: score + 10 for name, 
    score in marks.items()
}
print(increse_marks_10)

mark = [99,88,77]
mark_name = dict(zip(names,mark))
print(mark_name)

even_odd_dict = {
    num: "Even" if num % 2 == 0 else "Odd"  for num in range(1,21)
}
print(even_odd_dict)

original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {
    value: key for key, 
    value in original_dict.items()
}
print(inverted_dict)

sentence = "Python is very easy to learn"
word_length_dict = {
    word: len(word) 
    for word in sentence.split()
}
print(word_length_dict)
