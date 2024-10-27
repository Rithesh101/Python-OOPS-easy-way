
# classes are the best way to organise our code

class Microwave:
    # initializers: here we are using dunder method
    # code comes here when an object in instantiated
    def __init__(self, brand: str, power_rating_str):
        self.brand = brand
        self.power_rating = power_rating_str
        self.turned_on: bool = False # default microwave is turned off

    # method
    def turn_on(self):
        if self.turned_on:
            print(f"Your {self.brand} microwave is already turned on.")
        else:
            self.turned_on = True
            print(" now its on")
    
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print("now its off")
        else:
            print(f"Your {self.brand} microwave is already turned off.")

    def run(self, seconds:int):
        if self.turned_on:
            print(f"Your {self.brand} microwave is running for {seconds} seconds.")
        else:
            print(f"Your {self.brand} microwave is turned off. Please turn it on first.")
            
      # dunder methods
    def __add__(self, other):
        return f"{self.brand} + {other.brand}"
    def __mul__(self,other):
        return f"{self.brand} * {other.brand}"
    def __str__(self):
        return f"{self.brand} microwave with power rating {self.power_rating}"
    def __repr__(self):
        return f'Microwave( brand = "{self.brand}" , power rating = " {self.power_rating}")'
# STR VS REPR : str should return something that is user friendly, repr should return for developer friendly.


# self : self is the actual instance of the class, it makes sure that all the data inside the def ... self() sticks to the correct instance or object we are using
# we can change the self name into whatever we want. ex this as in java.
# as soon as we insert information in the constructor , the self turns into samsung or bosch etc
# brand : brand is the parameter that we are passing to the function, it is a string
# pass : this allows the class to be defined without any methods for now

# methods:
# now our microwave have data but it doesnt function


# instantiate a microwave
# ex : samsung
# there is no need to use type annotater here i mean microwave below
# samsung: Microwave = Microwave()


samsung = Microwave('samsung','B')  # object - instance of class microwave
samsung.turn_on()
samsung.run(30)
samsung.turn_off()
samsung.run(30)

bosch = Microwave('bosch','A')
print(bosch)
print(repr(samsung))

