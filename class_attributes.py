class Person:
    no_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.no_of_people += 1

p1 = Person("Kaattu")
p2 = Person("Kaachu")
print(p1.name)
print(Person.no_of_people)
print(p1.no_of_people)
print(p1.no_of_people)
print(Person.no_of_people)
print(p2.no_of_people)