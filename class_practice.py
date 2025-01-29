class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        print("seating capacity: ", capacity)

    def fare(self, capacity):
        return capacity * 10


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50):
        Vehicle.__init__(self, max_speed, mileage)
        self.name = name
        self.capacity = capacity
        print("Name= ", self.name, ", max speed= ", self.max_speed, ", mileage= ", self.mileage)
        super().seating_capacity(self.capacity)

    def fare(self):
        amount = super().fare(self.capacity)
        amount += amount * 10/100
        return amount


new_bus = Bus("volvo", 180, 300, 100)
print("Fare: ", new_bus.fare())
print(isinstance(new_bus, Vehicle))
