#1. Modify the Doggo class to include another attribute coat_color, and add it to the .__init__() constructor.

class Doggo:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old, and is a good doggo."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

#2. Create a Car class with a few instances that are appropriate for cars.

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def description(self):
        return f"{self.year} {self.make} {self.model} in {self.color}"

    def honk(self):
        return "Honk! Honk!"

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Ford", "Mustang", 2023, "Red")
car3 = Car("Honda", "Civic", 2021, "Silver")

# Calling methods on the instances
print(car1.description())  # Output: "2022 Toyota Camry in Blue"
print(car2.honk())         # Output: "Honk! Honk!"
print(car3.description())  # Output: "2021 Honda Civic in Silver"

#3. Add a .mileage attribute to the Car class and add a .drive() instance method to the class which will add a number of miles to the mileage.

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0  # Initialize mileage to zero

    def description(self):
        return f"{self.year} {self.make} {self.model} in {self.color}"

    def honk(self):
        return "Honk! Honk!"

    def drive(self, miles):
        self.mileage += miles
        return f"Drive {miles} miles. Total mileage: {self.mileage} miles"

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Ford", "Mustang", 2023, "Red")
car3 = Car("Honda", "Civic", 2021, "Silver")

# Calling methods on the instances
print(car1.description())  # Output: "2022 Toyota Camry in Blue"
print(car2.honk())         # Output: "Honk! Honk!"
print(car3.description())  # Output: "2021 Honda Civic in Silver"

# Driving the cars and updating mileage
print(car1.drive(100))     # Output: "Drive 100 miles. Total mileage: 100 miles"
print(car2.drive(50))      # Output: "Drive 50 miles. Total mileage: 50 miles"
print(car3.drive(75))      # Output: "Drive 75 miles. Total mileage: 75 miles"