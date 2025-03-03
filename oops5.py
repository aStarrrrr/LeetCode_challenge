class student:
    school_name = 'UCE' #class variable

    def __init__(self, name, roll_num): #instance variable --> constructor
        self.name = name
        self.roll_number = roll_num
        print('Iam constructor')

    def display(self):
        print('Iam ',self.name,' and my roll number is ',self.roll_number)

s1 = student('Abhi', 4)
s1.display()
s2 = student('Kaattu', 40)
print(s2.school_name)
s2.display()
print(s2.school_name)