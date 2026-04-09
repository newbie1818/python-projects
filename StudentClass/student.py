# Создай класс Student с:
# - атрибутами: name, grades (список оценок)
# - методами:
#   - add_grade(grade)     — добавить оценку в список
#   - get_average()        — вернуть среднюю оценку
#   - get_highest()        — вернуть самую высокую оценку

class Student():

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) ==0:
            return None
        else:
            return round(sum(self.grades) / len(self.grades))

    def get_highest(self):
        return max(self.grades)


student1 = Student("James", [])
student2 = Student("Anna", [90, 45, 87, 70])

print(student1.name)
print(student1.grades)
student1.add_grade(95)
print(student1.grades)
print(student1.get_average())
print(student1.get_highest())

print(student2.name)
print(student2.grades)
student2.add_grade(85)
print(student2.grades)
print(student2.get_average())
print(student2.get_highest())
