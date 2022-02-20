import sys
import pygame

from settings import Settings
from tank import Tank
from bullet import Bullet


class OldTank:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.tank = Tank(self)
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Old Tank")

    def run_game(self):
        while True:
            self.clock.tick(self.settings.FPS)
            self._check_events()
            self._check_pressed_btns()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши.
            if event.type == pygame.QUIT:
                print('exit')
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('space')
                    self._fire_bullet()
                    print('111')
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _check_pressed_btns(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_d] and self.tank.rect.right < (self.tank.screen_rect.right + 50):
            self.tank.image = self.tank.tank_img_r
            self.tank.rect.x += self.settings.tank_speed
        elif button[pygame.K_a] and self.tank.rect.left > -50:  # Оператор "and" отслеживает координаты края
            self.tank.image = self.tank.tank_img_l              # прямоугольника (танка) и края экрана
            self.tank.rect.x -= self.settings.tank_speed
        elif button[pygame.K_w] and self.tank.rect.top > 0:
            self.tank.image = self.tank.tank_img_t
            self.tank.rect.y -= self.settings.tank_speed
        elif button[pygame.K_s] and self.tank.rect.bottom < self.tank.screen_rect.bottom:
            self.tank.image = self.tank.tank_img_b
            self.tank.rect.y += self.settings.tank_speed
        elif button[pygame.K_ESCAPE]:
            sys.exit()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        print('fb1')
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            print(self.bullets)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # Цвет главного экрана
        self.tank.blitme()
        print('us1')
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            print(bullet.draw_bullet())

        pygame.display.flip()  # Отображение экрана.


if __name__ == '__main__':
    ot = OldTank()
    ot.run_game()
