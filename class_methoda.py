class Person:
    no_of_people = 0
    def __init__(self, name):
        self.name = name
    @classmethod
    def number_of_people(cls):
        return cls.no_of_people
    @classmethod
    def add_person(cls):
        cls.no_of_people += 1
p1 = Person("Me")
print(p1.no_of_people)
print(Person.number_of_people())