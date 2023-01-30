class Ammo:
    def __init__(self, ammo_type, piercing, explosive):
        self.ammo_type = ammo_type
        self.piercing = piercing
        self.explosive = explosive

    def display(self):
        print(f"Ammo Type: {self.ammo_type}")
        print(f"Piercing: {self.piercing}")
        print(f"Explosive: {self.explosive}")

class Ball(Ammo):
    def __init__(self):
        super().__init__("Ball", "Low", "None")

class HollowPoint(Ammo):
    def __init__(self):
        super().__init__("Hollow Point", "High", "None")

class Buckshot(Ammo):
    def __init__(self):
        super().__init__("Buckshot", "Low", "None")

class Rocket(Ammo):
    def __init__(self):
        super().__init__("Rocket", "Low", "High")

class Missile(Ammo):
    def __init__(self):
        super().__init__("Missile", "Very High", "Very High")

class Nato556mm(Ammo):
    def __init__(self):
        super().__init__("5.56mm", "Moderate", "None")

class Standard762mm(Ammo):
    def __init__(self):
        super().__init__("7.62mm", "High", "None")