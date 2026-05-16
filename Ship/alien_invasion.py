import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self._full_screen=False
    def run_game(self):
        while True:
                self.ship.update()
                self._check_events()
                self._update_screen()
                for bullet in self.bullets.copy():
                    if bullet.rect.bottom<=0:
                        self.bullets.remove(bullet)
                self.bullets.update()
                self.clock.tick(60)
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right =True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left =True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullets()
        elif event.key==pygame.K_f:
            self._full_screen=not self._full_screen
            if self._full_screen:
                 self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            else:
                self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left =False
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()
    def _fire_bullets(self):
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)
    
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()

