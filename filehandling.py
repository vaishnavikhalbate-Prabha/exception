# read a file

#read() - read entire file Content

# file = open("student.txt","r")
# data = file.read()
# print(data)
# file.close

# file = open("student.txt","a")
# data = file.write("Programming")
# print(data)
# file.close

# file = open("student.txt","r")
# data = file.readline()
# print(data)
# file.close

# file = open("student.txt","r")
# data = file.readlines()
# print(data)
# file.close

# import os
# if os.path.exists("studen.txt"):
#     print("File exists")
# else:
#     print("File not found")   


file = open("student.txt","w")
for i in range(5):
    name=input("enter a student name:")
    file.write(name + "\n")

file.close()

file = open("student.txt","r")

print("\nStudent Names:")
for line in files:
    print(line.strip())

file.close()    




