class employees:
    company_name = 'Cognizant'

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def display(self):
        print(f"Iam {self.name} and my salary is {self.salary} and working as {self.department}")

e1 = employees('Abhinand Shaji', 60000, 'Software Engineer')
e1.display()

e2 = employees('Anjali', 6000, 'Software Engineer')
e2.display()

print(e1.company_name)
print(e2.company_name)