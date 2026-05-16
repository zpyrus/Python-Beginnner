import sys
import pygame
from ship import Ship
from settings import Settings
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()

