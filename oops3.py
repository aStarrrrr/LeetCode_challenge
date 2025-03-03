class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_details(self):
        print(f"The car is {self.brand} {self.model}")
car1 = Car("BMW", "M5")
car2 = Car("Porsche", 911)
car1.display_details()
car2.display_details()