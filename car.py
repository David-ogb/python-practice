class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.sale = for_sale

# method are actions object can perform

    def drive(self):
        print(f"You are driving {self.color} {self.model}")

    def stop(self):
        print(f"You stopped the {self.color} {self.model}")
    
    def details(self):
        print(f"Your car is a {self.year} {self.color} {self.model}")