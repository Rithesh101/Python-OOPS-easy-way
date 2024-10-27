# Python-OOPS-easy-way
This repository provides a simple Microwave class example to demonstrate the basics of classes and objects in Python. It covers fundamental concepts like initialization, methods, and dunder (special) methods in an easy-to-understand format.

Project Overview
The Microwave class models a basic microwave with attributes and methods that illustrate core OOP principles:

Attributes:

brand: The brand name of the microwave.
power_rating: The microwave’s power rating.
turned_on: Indicates if the microwave is on (default is False).
Methods:

turn_on(): Turns on the microwave and updates the turned_on state.
turn_off(): Turns off the microwave.
run(seconds): Runs the microwave for a given duration if it’s turned on.
Special (Dunder) Methods:

__str__(): Returns a user-friendly description.
__repr__(): Provides a developer-friendly description for debugging.
__add__() and __mul__(): Custom behaviors for + and * operators.
Getting Started
To explore how classes and objects work, you can create Microwave objects and experiment with calling their methods. For example:

samsung = Microwave('Samsung', 'B')
samsung.turn_on()
samsung.run(30)
samsung.turn_off()
