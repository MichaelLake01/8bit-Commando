import pygame

class SpriteSheet:
    def __init__(self, filename, rows, columns, red, char):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
        self.rows = rows
        self.columns = columns
        self.total_cell_count = rows * columns
        self.rect = self.spritesheet.get_rect()
        self.cell_width = self.rect.width / columns
        self.cell_height = self.rect.height / rows
        self.cells = []
        self.frames = self.define_type(red, char)
        self.handle_spritesheet()
   

    def define_type(self, red, char):
        if char:
            if red:
                frames = {
                    "inf_sprite": {"idle": 32, "unarmed": 33, "armed_idle": 34, "shoot": 35, "prone": 36, "prone_shoot": 37, "crawl1": 38, "crawl2": 39},
                    "engineer_sprite": {"idle": 40, "shoot": 41, "prone": 42, "prone_shoot": 43, "crawl1": 44, "crawl2": 45},
                    "sniper_sprite": {"idle": 46, "shoot": 47, "prone": 48, "prone_shoot": 49, "crawl1": 50, "crawl2": 51},
                    "medic_sprite": {"idle": 52, "shoot": 53, "prone": 54, "prone_shoot": 55, "crawl1": 56, "crawl2": 57},
                    "lmg_sprite": {"idle": 58, "shoot": 59, "prone": 60, "prone_shoot": 61, "crawl1": 62, "crawl2": 63}
                }

            else:
                frames = {
                    "inf_sprite" : { "idle" : 0, "unarmed" : 1, "armed_idle" : 2, "shoot" : 3, "prone" : 4, "prone_shoot" : 5, "crawl1" : 6, "crawl2": 7}, 
                    "engineer_sprite" : {"idle" : 8, "shoot" : 9, "prone" : 10, "prone_shoot" : 11, "crawl1" : 12, "crawl2": 13},
                    "sniper_sprite" : {"idle" : 14, "shoot" : 15, "prone" : 16, "prone_shoot" : 17, "crawl1" : 18, "crawl2": 19},
                    "medic_sprite" : {"idle" : 20, "shoot" : 21, "prone" : 22, "prone_shoot" : 23, "crawl1" : 24, "crawl2": 25},
                    "lmg_sprite" : {"idle" : 26, "shoot" : 27, "prone" : 28, "prone_shoot" : 29, "crawl1" : 30, "crawl2": 31}

                }

            

        return frames

    def handle_spritesheet(self):
        for row in range(self.rows):
            for column in range(self.columns):
                x = column * self.cell_width
                y = row * self.cell_height
                rect = (x, y, self.cell_width, self.cell_height)
                self.cells.append(self.spritesheet.subsurface(rect))

    def get_seq(self, name):
        indices = self.frames[name]
        return {k: self.cells[v] for k, v in indices.items()}


