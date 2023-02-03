import pygame
import combatants as cb

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.infantry = cb.Infantry(True)
        self.lmg_gunner = cb.LMG_Gunner(False)
        self.engineer = cb.Engineer(True)
        self.medic = cb.Medic(False)
        self.sniper = cb.Sniper(True)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.infantry.seq["idle"], (100, 100))
            self.screen.blit(self.lmg_gunner.seq["idle"], (200, 200))
            self.screen.blit(self.engineer.seq["idle"], (300, 300))
            self.screen.blit(self.medic.seq["idle"], (400, 400))
            self.screen.blit(self.sniper.seq["idle"], (500, 500))
            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    Main().run()


