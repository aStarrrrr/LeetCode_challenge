class Cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_car(self):
        print(f"The car is {self.brand} {self.model}")
bmw = Cars("BMW", "M5")
porsche = Cars("Porsche", 911)
porsche.display_car()