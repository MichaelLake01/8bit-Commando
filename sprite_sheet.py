import pygame

class Sprite:
    def __init__(self, filename, rows, columns):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
        self.rows = rows
        self.columns = columns
        self.total_cell_count = rows * columns
        self.rect = self.spritesheet.get_rect()
        self.cell_width = self.rect.width / columns
        self.cell_height = self.rect.height / rows
        self.cells = []
        self.handle_spritesheet()

    def handle_spritesheet(self):
        for row in range(self.rows):
            for column in range(self.columns):
                x = column * self.cell_width
                y = row * self.cell_height
                rect = (x, y, self.cell_width, self.cell_height)
                self.cells.append(self.spritesheet.subsurface(rect))

    def get_frame(self, frame_number):
        return self.cells[frame_number % self.total_cell_count]
