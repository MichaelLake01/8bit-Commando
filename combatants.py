class Combatant:
    def __init__(self, weapon, armor, state, exp):
        self.weapon = weapon
        self.armor = armor
        self.state = state
        self.exp = exp

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"State: {self.state}")
        print(f"Experience: {self.exp}")

class Infantry(Combatant):
    def __init__(self):
        super().__init__("M16", 1, "Healthy", "Private")

class LMG_Gunner(Combatant):
    def __init__(self):
        super().__init__("LMG", 1.5, "Healthy", "Corporal")

class Engineer(Combatant):
    def __init__(self):
        super().__init__("SMG", 1, "Healthy", "Sergeant")

class Medic(Combatant):
    def __init__(self):
        super().__init__("SMG", 1, "Healthy", "Corporal")

class Sniper(Combatant):
    def __init__(self):
        super().__init__("Sniper Rifle", 1, "Healthy", "Sergeant")

class Tank_Crew(Combatant):
    def __init__(self):
        super().__init__("Pistol", 1.5, "Healthy", "Sergeant")

class Officer(Combatant):
    def __init__(self):
        super().__init__("Pistol", 1.5, "Healthy", "Captain")
