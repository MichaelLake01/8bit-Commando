import random
from ammo import ammo_types


class Weapon:
    def __init__(self, name, fire_rate, ammo_type, reliability, speed, accuracy):
        self.name = name
        self.fire_rate = fire_rate # rounds per minute
        self.ammo_type = ammo_type # caliber and cartridge type
        self.reliability = reliability # percentage of successful firings
        self.speed = speed # meters per second
        self.accuracy = accuracy # accuracy in centimeters at 100 meters
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

    def define_muzzle_velocity(speed, dir):
        pass


# Create instances of the Weapon class for each weapon
mauser_karabiner_98k = Weapon("Mauser Karabiner 98k", 60, ammo_types["mauser"], 0.95, 250, 5)
mp40 = Weapon("MP40", 600, ammo_types["parabellum"], 0.92, 300, 10)
mg42 = Weapon("MG42", 900, ammo_types["mauser"], 0.93, 350, 15)
pak_40_gun = Weapon("PAK 40", 60, [ammo_types["pak40_APCR"], ammo_types["pak40_HEAT"]], 0.95, 300, 3)
_88mm_kwk_gun = Weapon("Tiger I 88mm KwK 36 L/56", 60, [ammo_types["88mm_APCR"], ammo_types["88mm_HEAT"]], 0.98, 300, 2)
_75mm_kwk_gun = Weapon("Panther 75mm KwK 42 L/70", 60, [ammo_types["panther_APCR"], ammo_types["panther_HEAT"]], 0.98, 300, 2)
mp3008 = Weapon("MP3008", 600, ammo_types["parabellum"], 0.93, 300, 8)
p_38 = Weapon("P-38", 60, ammo_types["parabellum"], 0.96, 250, 4)
panzerschrek = Weapon("Panzerschrek", 60, ammo_types["rocket"], 0.97, 250, 3)
_8cm_mortar = Weapon(" 8cm Granatwerfer 34", 30, ammo_types["mortar"], 0.98, 250, 2)