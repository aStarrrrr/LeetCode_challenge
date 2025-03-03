class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Iam {self.name} and iam {self.age} years old")
    def sounds(self):
        print("Common sound")

class Dog(Pet):
    def sounds(self):
        print("Bow bow")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def sounds(self):
        print("Meow")
    def show(self):
        print(f"Iam {self.name} and iam {self.age} year old and iam aaaaaaaaaaaaa {self.color}")

class Bird(Pet):
    pass

print("-----------------------------------")

d = Dog("Bob", 7)

c = Cat("Swarnam", 4, "Orange Cat")
print(c.name)

p = Pet("Common pet", 100)
p.show()
p.sounds()

d.show()
d.sounds()

c.show()
c.sounds()

b = Bird("Crow", 5)
print(b.name)
b.sounds()

print("-----------------------------------")