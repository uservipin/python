

# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
# 2. setAge - It should assign age to student
# 3. setMarks - It should assign marks to the student.

class student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.marks)

    def setName(self,name):
        self.name = name

    def setMarks(self,marks):
        self.marks= marks
        
    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks


# initially both studen have same details
student_1=  student('vipin',34)
student_2=  student('vipin',34)

# print details of student_1
print(student_1.display())

# set student_2 details
student_2.setName('Mohit')
student_2.setMarks(50)

# print student 2 student
print(student_2.display())

# set student 2 name
student_2.setName('Chahar')

# get student 2 name and marks
print(student_2.getName())
print(student_2.getMarks())