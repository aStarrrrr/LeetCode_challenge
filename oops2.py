class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.mark = marks
    def mark_printing(self):
        return self.mark
class Course:
    def __init__(self, name, maximum_capacity):
        self.name = name
        self.maximum_capacity = maximum_capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.maximum_capacity:
            self.students.append(student)
            return True
        return False
    def get_average(self):
        total = 0
        for student in self.students:
            total += student.mark_printing()
        return total / len(self.students)

s1 = Student("Aaron", 21, 100)
s2 = Student("Babu", 20, 65)
s3 = Student("Jayan", 22, 70)

c1 = Course("CS", 2)
c2 = Course("EC", 3)

c1.add_student(s1)
c1.add_student(s2)

print(c1.students[0].name)
print(c1.students[1].mark)

print(c1.get_average())

print(c1.add_student(s3))