from weapon import *

class Combatant:
    def __init__(self, weapon, armor, state, veterancy, sprites):
        self.weapon = weapon
        self.armor = armor
        self.state = state
        self.veterancy = veterancy

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"State: {self.state}")
        print(f"Experience: {self.veterancy}")
        

class Infantry(Combatant):
    def __init__(self):
        super().__init__(mauser_karabiner_98k, 1, "Healthy", "Private")

        def throw_grenade():
            pass

class LMG_Gunner(Combatant):
    def __init__(self):
        super().__init__(mg42, 1.5, "Healthy", "Corporal")

        def displace():
            pass

class Engineer(Combatant):
    def __init__(self):
        super().__init__([mp40, mp3008], 1, "Healthy", "Sergeant")

        def repair():
            pass

        def mine():
            pass

        def barricade():
            pass

        def set_explosives():
            pass

class Medic(Combatant):
    def __init__(self):
        super().__init__(mp40, 1, "Healthy", "Corporal")

        def revive():
            pass

class Sniper(Combatant):
    def __init__(self):
        super().__init__(mauser_karabiner_98k, 1, "Healthy", "Sergeant")

        def pick_your_targets():
            pass

class Tank_Crew(Combatant):
    def __init__(self):
        super().__init__([p_38, mp40], 1.5, "Healthy", ["Sergeant", "Captain"])

class Officer(Combatant):
    def __init__(self):
        super().__init__([p_38, mp40], 1.5, "Healthy", "Captain")

        def rally():
            pass

infantry = Infantry()
lmg_gunner = LMG_Gunner()
engineer = Engineer()
medic = Medic()
sniper = Sniper()
tank_crew = Tank_Crew()
officer = Officer()