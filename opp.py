# class Car:
#     def __init__(self, brand, model, color, year):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.year = year

# # mycar = Car()
# # print(f"I have a {mycar.model} {mycar.brand},It's {mycar.color} and year {mycar.year}")

# mycar = Car('Toyota', 'Camry', 'Grey', 2000)
# car1 = Car('Honda', 'Civic', 'Red', 2025)
# car2 = Car('Mercedes', 'ML-250', 'Black', 2015)
# print(mycar.model)
# print(car1.brand, car1.model, car1.year, car1.color)


class Person:
    def __init__(self, name, age, gender, tribe):
        self.name = name
        self.age = age
        self.gender = gender
        self.tribe = tribe

    # def __str__(self):
    #     return f"{self.name}, {self.age} {self.gender} {self.tribe}"
    def welcome(self):
        course = input('Enter your course: ')
        cohort = input('Enter your Cohort: ')
        print(f"Welcome {self.name} to {course}, {cohort}")

    def detail(self):
        print(f"Hello everyone, my name is {self.name}, i am {self.age}, {self.tribe} by tribe and a {self.gender}")


per = Person('Adam', 24, 'Male', 'Hausa')
per2 = Person('Bola', 20, 'Female', 'Yoruba')
per3 = Person('Ada', 22, 'Female', 'Igbo')

# print(per)
# print(per2)
# print(per3)

# per2.welcome()
per.detail()