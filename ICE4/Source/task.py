class Student():
    StudentCount=0
    def __init__(self, name, rollno, grade):
        self.name=name
        self.rollno=rollno
        self.grade=grade
        Student.StudentCount += 1

    def TotalStudents(self):
        print("Total count of students" + Student.StudentCount)

    def displayStudentDetails(self):
        print("Name :" +self.name, "  Roll No: " +str(self.rollno), "  Grade :"+ self.grade )


s1=Student("Namrata",18,"A")
s2=Student("Sudheesha",19,"A")

s1.displayStudentDetails()
s2.displayStudentDetails()
print("Count of students")
print(Student.StudentCount)


class TransferStudent(Student):

    print("Transfer Students")
t1=TransferStudent("Pujita",23,"A")
t2=TransferStudent("Sravani",12,"B")
t1.displayStudentDetails()
t2.displayStudentDetails()




