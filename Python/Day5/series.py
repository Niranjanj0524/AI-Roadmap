#Print 1 to 100
for i in range(1,101):
    print(i)


#Print even
for i in range(2,20,2):
    print(i)

#print odd
for i in range(1,21,2):
    print(i)


#Multiplication Table
num = int(input("Enter Number : "))
for i in range(1,11):
    print(num * i)


#Sum of 100 Number
print(sum(range(1,101)))


#Print 1 to 10 using while
i = 1
while i <= 10:
    print(i)
    i+=1


#break in loop
for i in range(1,11):
    if i==6:
        break
    print(i)


#continue in loop
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)