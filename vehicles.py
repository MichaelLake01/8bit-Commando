import weapon as wp

class Vehicles:
    def __init__(self, name, weapon, state, veterancy, crew_num, red):
        self.name = name
        self.weapon = weapon
        self.state = state
        self.crew_num = crew_num
        self.veterancy = veterancy

    def display(self):
        print(f"Weapon: {self.weapon}")
        print(f"State: {self.state}")
        print(f"Veterancy: {self.veterancy}")

    def define_crew(self):
        pass

    def define_parts(self):
        pass

    def define_armor(self):
        pass

class Tank(Vehicles):
    def __init__(self, name, weapon, red):
        super().__init__(name, weapon, "Operational", "Experienced", 4, red)

class Halftrack(Vehicles):
    def __init__(self, red):
        super().__init__("Sd.Kfz. 251", wp.mg42, "Operational", "Experienced", 6, red)

class MgNest(Vehicles):
    def __init__(self, red):
        super().__init__("Mg", wp.mg42, "Operational", "Experienced", 2, red)

class Pak40(Vehicles):
    def __init__(self, red):
        super().__init__("Pak40", wp.pak_40_gun, "Operational", "Experienced", 4, red)

class Granatwerfer34(Vehicles):
    def __init__(self, red):
        super().__init__("8cm Granatwerfer 34", wp._8cm_mortar, "Operational", "Experienced", 4, red)

tiger = Tank("Tiger 1", wp._88mm_kwk_gun)
panther = Tank("Panther", wp._75mm_kwk_gun)
half_track = Halftrack()
mg_nest = MgNest()
pak_40 = Pak40()
mortar = Granatwerfer34()