class Dog:
    def __init__(self, ip_name, ip_age):
        self.name = ip_name
        self.age = ip_age
        # print(self.name)
    def print_name(self):
        return self.name
    def seperation(self):
        print("------------------------------------")
    def bark(self):
        print("Bark")
    def add_one(self,x):
        return x + 1
    def change_age(self, ip_age):
        self.age = ip_age
        return self.age
d0 = Dog("Dummy",0)
d0.seperation()
d = Dog("Jimmy",4)
# print(d.name)
print(d.print_name())
print("Age : " + str(d.age))
# d.bark()
# print(d.add_one(39))
# print(type(d))
d2 = Dog("Rocky",2)
# print(d2.name)
print(d2.print_name())
print("Age : " + str(d2.age))
print("Rocky's age changed to - " , d2.change_age(20))
d.seperation()