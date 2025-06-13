class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    
    students = []

    def __init__(self, name, age, subject):
        
        super().__init__(name, age)
        self.subject = subject
    
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        try:
            self.students.remove(student)
        except ValueError:
            print(f"Студента {student} нет в списке.")

    def list_students(self):
        print(f"Преподаватель: {self.name}\nЕго студенты: {' | '.join(str(n) for n in self.students)}")


peter = Person("Peter", 88)
mary = Person("Mary", 15)
ann = Person("Ann", 12)
oleg = Teacher("Ivan", 22, "math")
oleg.add_student("Peter")
oleg.add_student("Mary")
oleg.add_student("Ann")
oleg.list_students()
oleg.remove_student("Peter")
oleg.list_students()