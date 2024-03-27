class Student :
    def _init_(self, student_id,name,age,gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
        self.next = None
    
class StudentDatabase:
    def _init_(self):
        self.head = None
        def add_student(self, student_id, name, age, gpa):
            new_student = Student(student_id, name, age, gpa)
            if not self.head:
                self.head = new_student
            else :
                current = self.head
                while current.next:
                    current = current.next
                    current.next = new_student