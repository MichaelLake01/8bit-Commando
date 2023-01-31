class Ammo:
    def __init__(self, ammo_type, caliber, piercing, explosive):
        self.ammo_type = ammo_type
        self.caliber = caliber
        self.piercing = piercing
        self.explosive = explosive

    def display(self):
        print(f"Ammo Type: {self.ammo_type}")
        print(f"Caliber: {self.caliber}")
        print(f"Piercing: {self.piercing}")
        print(f"Explosive: {self.explosive}")

class _303British(Ammo):
    def __init__(self):
        super().__init__("Rifle", ".303", "Moderate", "None")

class _38_200(Ammo):
    def __init__(self):
        super().__init__("Revolver", ".38/200", "Low", "None")

class _792x57mmMauser(Ammo):
    def __init__(self):
        super().__init__("Rifle", "7.92x57mm", "High", "None")

class _9x19mmParabellum(Ammo):
    def __init__(self):
        super().__init__("Submachine Gun", "9x19mm", "Low", "None")

class _8cmPak43(Ammo):
    def __init__(self):
        super().__init__("Anti-tank Gun", "8.8cm", "Very High", "High")

class PistolAmmo(Ammo):
    def __init__(self):
        super().__init__("Pistol", "9mm", "Low", "None")

class Dynamite(Ammo):
    def __init__(self):
        super().__init__("Explosive", "N/A", "Low", "High")

class Grenade(Ammo):
    def __init__(self):
        super().__init__("Grenade", "N/A", "Low", "High")
