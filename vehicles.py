from weapon import *

class Vehicles:
    def __init__(self, weapon, state, exp):
        self.weapon = weapon
        self.state = state
        self.exp = exp

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"State: {self.state}")
        print(f"Veterancy: {self.exp}")

class AttackHelicopter(Vehicles):
    def __init_subclass__(self):
        super().__init__((Minigun(), RocketLauncher()), 1, "Expert")


class ChinookTransport(Vehicles):
    def __init_subclass__(self):
        super().__init__("None", 1, "Expert")


