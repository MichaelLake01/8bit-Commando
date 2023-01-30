from ammo import *
import random

class Weapon:
    def __init__(self, name, accuracy, reliability, ammo):
        self.name = name
        self.accuracy = accuracy
        self.reliability = reliability
        self.ammo = ammo
        self.state = 1

    def display(self):
        print(f"Weapon Name: {self.name}")
        print(f"Accuracy: {self.accuracy}")
        print(f"Reliability: {self.reliability}")
        self.ammo.display()

    def fix(self):
        chance_to_fix = random.uniform(0,1)
        if chance_to_fix < self.reliability:
            self.state -= (1 - self.reliability)
        else:
            print("failed")
            

    def jammed(self):
        chance_to_jam = random.uniform(0,1)
        if chance_to_jam > self.reliability:
            print(f"{self.name} has jammed!")
        else:
            print(f"{self.name} is functioning properly.")


class M16(Weapon):
    def __init__(self):
        super().__init__("M16", 0.85, 0.90, Nato556mm())

class AK47(Weapon):
    def __init__(self):
        super().__init__("AK47", 0.75, 0.95, Standard762mm())

class RocketLauncher(Weapon):
    def __init__(self):
        super().__init__("Missile Launcher", 0.65, 0.80, Missile())

class Minigun(Weapon):
    def __init__(self):
        super().__init__("Minigun", 0.50, 0.85, Standard762mm())

class Sniper(Weapon):
    def __init__(self):
        super().__init__("Sniper Rifle", 0.95, 0.95, HollowPoint())

class RPG(Weapon):
    def __init__(self):
        super().__init__("RPG", 0.75, 0.90, Rocket())

class Shotgun(Weapon):
    def __init__(self):
        super().__init__("Shotgun", 0.70, 0.80, Buckshot())
