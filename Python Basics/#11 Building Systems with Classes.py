#Model four classes: 1 'Animal' class, 3 classes that inherit from 'Animal'
#Each class should have a few attributes and at least one method
#Model two more classes: 'field', 'barn'
#Make the places have an attribute where they can store 'Animal' objects

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # Placeholder for the method that will be overridden by subclasses

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def __init__(self, name, type):
        super().__init__(name, species="Bird")
        self.type = type

    def make_sound(self):
        return "Chirp!"

class Field:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

class Barn:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

# Creating instances of the classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")
bird = Bird("Tweety", "Canary")

field = Field()
barn = Barn()

field.add_animal(dog)
field.add_animal(cat)
barn.add_animal(bird)

# Accessing attributes and methods
for animal in field.animals:
    print(f"{animal.name} is a {animal.species} and makes the sound: {animal.make_sound()}")

for animal in barn.animals:
    print(f"{animal.name} is a {animal.species} and makes the sound: {animal.make_sound()}")

#Buddy is a Dog and makes the sound: Woof!
#Whiskers is a Cat and makes the sound: Meow!
#Tweety is a Bird and makes the sound: Chirp!
