from weapon import *
from sprite_sheet import SpriteSheet
import pygame

class Combatant:
    def __init__(self, weapon, state, veterancy, name, red):
        self.weapon = weapon
        self.state = state
        self.name = name
        self.red = red
        self.veterancy = veterancy
        sprite = SpriteSheet("WW2PixelPack/WW2/Pixels/Spritesheets/Troopers.png", 8, 8, red, True)
        self.seq = sprite.get_seq(name)

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"State: {self.state}")
        print(f"Experience: {self.veterancy}")

    def shoot(self):
        pass

    def get_direction(self):
        pass


class Infantry(Combatant):
    def __init__(self, red):
        super().__init__(mauser_karabiner_98k, "Healthy", "Private", "inf_sprite", red)

    def throw_grenade(self):
        pass

class LMG_Gunner(Combatant):
    def __init__(self, red):
        super().__init__(mg42, "Healthy", "Corporal", "lmg_sprite", red)

    def displace(self):
        pass

class Engineer(Combatant):
    def __init__(self, red):
        super().__init__([mp40, mp3008],"Healthy", "Sergeant", "engineer_sprite", red)

    def repair(self):
        pass

    def mine(self):
        pass

    def barricade(self):
        pass

    def set_explosives(self):
        pass

class Medic(Combatant):
    def __init__(self, red):
        super().__init__(mp40,"Healthy", "Corporal", "medic_sprite", red)

    def revive(self):
        pass

class Sniper(Combatant):
    def __init__(self, red):
        super().__init__(mauser_karabiner_98k, "Healthy", "Sergeant", "sniper_sprite", red)

    def pick_your_targets(self):
        pass


#infantry = Infantry()
#lmg_gunner = LMG_Gunner()
#engineer = Engineer()
#medic = Medic()
#sniper = Sniper()
