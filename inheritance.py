class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start(self):
        print(f"{self.brand} {self.model} with {self.doors} doors is starting.")

class Motorcycle(Vehicle):
    def start(self):
        print(f"{self.brand} {self.model} motorcycle is starting.")

# Create instances of Car and Motorcycle
car = Car("Toyota", "Corolla", 4)
motorcycle = Motorcycle("Honda", "CBR")

# Call the start method
car.start()
motorcycle.start()

# Call the stop method
car.stop()
motorcycle.stop()
