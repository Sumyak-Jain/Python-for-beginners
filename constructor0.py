class student:
    count=0
    def __init__(self):
        student.count=student.count + 1

s1=student()
s2=student()
print(student.count)  #count no. of object created
