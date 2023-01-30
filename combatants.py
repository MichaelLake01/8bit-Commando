from weapon import *

class Combatants:
    def __init__(self, weapon, armor, cover, state, exp):
        self.weapon = weapon
        self.armor = armor
        self.cover = cover
        self.state = state
        self.exp = exp

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"Cover: {self.cover}")
        print(f"State: {self.state}")
        print(f"Veterancy: {self.exp}")

class Marine(Combatants):
    def __init_subclass__(self):
        super().__init__(M16(), "Slate", "None", 1, "Reg")


class Insurgent(Combatants):
    def __init_subclass__(self):
        super().__init__(AK47(), "None", "None", 1, "Conscript")


