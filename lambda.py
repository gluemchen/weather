# Python class example

# Defining Vehicle class
class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print("Gas tank is now full.")

    def drive(self):
        print(f"The {self.model} is now driving!")


# This is an instance of a Class. Also called an object.
# Multiple Objects can be created
toyota_ridgeline_truck = Vehicle("Toyoto", "Ridgeline", "Truck")
ford_escort_compact = Vehicle("Ford", "Escort", "Compact")
jeep_renegade_small_suv = Vehicle("Jeep", "Renegade", "small SUV")

# Access attribute values
print(toyota_ridgeline_truck.brand)
print(ford_escort_compact.model)
print(jeep_renegade_small_suv.type)

# Calling methods
toyota_ridgeline_truck.fuel_up()
toyota_ridgeline_truck.drive()
