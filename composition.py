class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting.")

class Car:
    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.engine = Engine(horsepower)  # Car has an Engine

    def start(self):
        print(f"{self.brand} {self.model} is starting.")
        self.engine.start()

# Create an instance of Car
car = Car("Ford", "Mustang", 450)

# Start the car
car.start()
