class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

# Creating objects of different classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Using polymorphism to call the same method on different objects
animals = [dog, cat, bird]

for animal in animals:
    print(animal.speak())
