import grade
import datetime
import time
import threading
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.__marks = 0
        self.addmission = datetime.date.today()

    def display(self):
        print("Student Name:",self.name)
        print("Student Rollno:",self.rollno)
        print("Admission date:",self.addmission)
        print("Student Marks:",self.__marks)
        print("Student Grade:",self.cal_grade())

    def set_marks(self,marks):
        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks as input")
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def cal_grade(self):
        return grade.get_grade(self.__marks)

def report_generation(student):
    print("Student profile creating")
    time.sleep(2)
    return student.display()


s1 = student("jhon", 114)

try:
    s1.set_marks(101)
except ValueError as e:
    print("Invlid marks entered",e)

t1 =threading.Thread(target=report_generation,args=(s1,))
t1.start()
t1.join()

print("Done")