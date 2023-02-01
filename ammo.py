
#AMMO       
ammo_types = {
  "rocket": {"name": "Rocket 88mm", "caliber": 88, "weight": 12.5},
  "mortar": {"name": "Mortar 8cm", "caliber": 80, "weight": 5.5},
  "parabellum": {"name": "Parabellum 9x19mm", "caliber": 9, "weight": 0.02},
  "mauser": {"name": "Mauser 7.92x57mm", "caliber": 7.92, "weight": 0.02},
  "pak40_HEAT": {"name": "75mm HEAT", "caliber": 75, "weight": 8.5},
  "pak40_APCR": {"name": "75mm APCR", "caliber": 75, "weight": 8.5},
  "88mm_HEAT": {"name": "88mm HEAT", "caliber": 88, "weight": 30.0},
  "88mm_APCR": {"name": "88mm APCR", "caliber": 88, "weight": 30.0},
  "panther_HEAT": {"name": "75mm HEAT", "caliber": 75, "weight": 25.0},
  "panther_APCR": {"name": "75mm APCR", "caliber": 75, "weight": 25.0},
}

def generate_penetration(ammo_types):
    for ammo_type in ammo_types:
        velocity = 100 # Assume velocity is 100 for simplicity
        caliber = ammo_types[ammo_type]["caliber"]
        weight = ammo_types[ammo_type]["weight"]

        # Penetration formula
        penetration = (caliber**2) * weight * velocity

        # Store the calculated penetration value in the dictionary
        ammo_types[ammo_type]["penetration"] = penetration

# Call the function to generate the penetration values
generate_penetration(ammo_types)


