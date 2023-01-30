from weapon import *

class Vehicles:
    def __init__(self, name, weapon, state, exp, crew):
        self.name = name
        self.weapon = weapon
        self.state = state
        self.exp = exp
        self.parts = {"Engine" : 1, "Steering" : 1, "Pilot" : crew}

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"State: {self.state}")
        print(f"Veterancy: {self.exp}")

class AttackHelicopter(Vehicles):
    def __init_subclass__(self):
        super().__init__("Little Bird", (Minigun(), RocketLauncher()), 1, "Expert")


class Transport(Vehicles):
    def __init_subclass__(self):
        super().__init__("Chinook", "None", 1, "Expert")
        

