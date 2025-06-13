class Student:
    
    grades = []

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    
    def add_grade(self, grade): #не проверяет на нечисловые значения
        if 0<=grade<=10:
            self.grades.append(grade)
    
    def get_average(self):
        if self.grades!=[]:
            print(sum(self.grades)/len(self.grades))
        else: print("Оценок нет.")

    def display_info(self):
        print(f"Имя студента: {self.name}\nID студента: {self.student_id}\nОценки студента: {' '.join(str(n) for n in self.grades)}")


st1=Student("Eva", 000)
st1.add_grade(9)
st1.add_grade(0)
st1.add_grade(15)
st1.add_grade(10)
st1.get_average()
st1.display_info()