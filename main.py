import sys
import pygame

from settings import Settings
from tank import Tank


class OldTank:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.tank = Tank(self)
        pygame.display.set_caption("Old Tank")

    def run_game(self):
        while True:
            self._check_events()
            self._check_pressed_btns()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши.
            if event.type == pygame.QUIT:
                sys.exit()

    def _check_pressed_btns(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_d] and self.tank.rect.right < (self.tank.screen_rect.right + 50):
            self.tank.rect.x += self.settings.tank_speed
        elif button[pygame.K_a] and self.tank.rect.left > -50:  # Оператор "and" отслеживает координаты края
            self.tank.rect.x -= self.settings.tank_speed        # прямоугольника (танка) и края экрана
        elif button[pygame.K_w] and self.tank.rect.top > 0:
            self.tank.rect.y -= self.settings.tank_speed
        elif button[pygame.K_s] and self.tank.rect.bottom < self.tank.screen_rect.bottom:
            self.tank.rect.y += self.settings.tank_speed
        elif button[pygame.K_ESCAPE]:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # Цвет главного экрана
        self.tank.blitme()
        pygame.display.flip()  # Отображение экрана.


if __name__ == '__main__':
    ot = OldTank()
    ot.run_game()
