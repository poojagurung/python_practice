class Student():
   def __init__(self,student_name):
       self.student_name = student_name
   def get_name(self):
       print (f"Student name is {self.student_name}")
class Teacher(Student):
   def __init__(self,student_name,teacher_name,teaching_subjects,salary):
       super().__init__(student_name)
       self.teacher_name = teacher_name
       self.teaching_subjects =  teaching_subjects
       self.salary = salary
   def print_teacher(self):
       print (f"{self.student_name} is taught by {self.teacher_name}")
student1= Student("Gita")
teacher1= Teacher("hari","Binita Sharma","science",20000)
teacher1.print_teacher()