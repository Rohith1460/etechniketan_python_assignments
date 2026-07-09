# Assignment 1 Answers

# Q1
import keyword
print(keyword.kwlist)


# Q2
x = 10
print(type(x))


# Q3
t = (5, 10, 15, 20)
print(t[-1])
print(t[1])


# Q4
s = "123"
n = int(s)
result = n + 10
print(result)


# Q5
f = 9.7
print(int(f))


# Q6
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(len(s3))


# Q7
flag = True
print(type(flag))


# Q8
t = (10, 20, 30, 40, 50)
print(len(t))


# Q9
language = "Python"
version = 3.13
result = language + str(version)
print(result)


# Q10
name = input("Enter Student Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")
course = input("Enter Course Name: ")
m1 = float(input("Enter Marks in Subject 1: "))
m2 = float(input("Enter Marks in Subject 2: "))
m3 = float(input("Enter Marks in Subject 3: "))

percent = (m1 + m2 + m3) / 3
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Percentage:", percent)


# Q11
subjects = ["Python", "SQL", "Excel", "Tableau"]

# a
print(subjects)

# b
print(subjects[0])
print(subjects[-1])

# c
subjects.insert(1, "Power BI")
print(subjects)

# d
subjects.remove("Excel")
print(subjects)

# e
subjects2 = subjects.copy()

# f
subjects2.sort()
print(subjects2)

# g
print("Excel" in subjects)


# Q12
attendance = True
assignment_submitted = False

# a
print(attendance or assignment_submitted)

# b
print(attendance and assignment_submitted)

# c
print(not attendance)
