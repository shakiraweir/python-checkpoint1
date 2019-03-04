# #1: Define a Vehicle class with the following properties and methods: 
# - `vehicle_type` 
# - `wheel_count`
# - `name` 
# - `cost` 
# - `colors` 
# - `vehicle_brand` 
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway` 
#     - `combined` 
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_count  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.

class Vehicle:
    def __init__(self, vehicle_dict):
        self.vehicle_type = vehicle_dict["vehicle_type"]
        self.wheel_count = vehicle_dict["wheel_count"]
        self.mpg = {
            "city" : vehicle_dict["mpg"]["city"],
            "highway": vehicle_dict["mpg"]["highway"],
            "combined": vehicle_dict["mpg"]["combined"]
        }
        self.name = vehicle_dict["name"]
        self.cost = vehicle_dict["cost"]
        self.colors = vehicle_dict["colors"]
        self.vehicle_brand = vehicle_dict["vehicle_brand"]

    def get_vehicle_type(self):
        return(self.vehicle_type)
    def get_vehicle_brand(self):
        return(self.vehicle_brand)
    def get_vehicle_drive(self):
        return(("I have " + self.wheel_drive + " wheel drive") if self.wheel_drive != "no wheels!" else "no wheels send it back to the shop")

# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
#       otherwise return "......pop!"

class Motorcycle(Vehicle):
    def __init__(self, vehicle_dict, wheel_drive="no wheels!"):
        super().__init__(vehicle_dict)
        self.wheel_drive = wheel_drive
        self.can_pop_wheelie = True if self.wheel_count == 2 else False

    def pop_wheelie(self):
        if (self.can_pop_wheelie):
            return("......pop!")
        else: 
            return("can't pop wheelie....must be a slingshot!")

# #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'

class Car(Vehicle):
    def __init__(self, vehicle_dict, wheel_drive="no wheels!"):
        super().__init__(vehicle_dict)
        self.wheel_drive = wheel_drive

    def can_drive(self):
        return("Vrrooooom Vroooom")

        

# #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `rev_engine` that should return 'revvvvvreeeev'
class Truck(Vehicle):
    def __init__(self, vehicle_dict, wheel_drive="no wheels!"):
      super().__init__(vehicle_dict)
      self.wheel_drive = wheel_drive

    def rev_engine(self):
        return('revvvvvreeeev')
       



# Commit when you finish working on these questions!