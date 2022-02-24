import sys
import pygame

from settings import Settings
from tank import Tank
from bullet import Bullet, TankState
from enemies import Enemy


class OldTank:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.tank = Tank(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self._create_enemies()
        pygame.display.set_caption("Old Tank")

    def run_game(self):
        while True:
            self.clock.tick(self.settings.FPS)
            self._check_events()
            self.check_pressed_btns()
            self._update_bullets()
            self._update_enemies()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши.
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

    def check_pressed_btns(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_d] and self.tank.rect.right < (self.tank.screen_rect.right + 50):
            self.tank.image = self.tank.tank_img_r
            self.tank.rect.x += self.settings.tank_speed
            TankState.direction = 2
        elif button[pygame.K_a] and self.tank.rect.left > -50:  # Оператор "and" отслеживает координаты края
            self.tank.image = self.tank.tank_img_l              # прямоугольника (танка) и края экрана
            self.tank.rect.x -= self.settings.tank_speed
            TankState.direction = 4
        elif button[pygame.K_w] and self.tank.rect.top > 0:
            TankState.direction = 1
            self.tank.image = self.tank.tank_img_t
            self.tank.rect.y -= self.settings.tank_speed
        elif button[pygame.K_s] and self.tank.rect.bottom < self.tank.screen_rect.bottom:
            self.tank.image = self.tank.tank_img_b
            self.tank.rect.y += self.settings.tank_speed
            TankState.direction = 3
        elif button[pygame.K_ESCAPE]:
            sys.exit()

    def _fire_bullet(self):
        """
        Создание снаряда и добавление в 'pygame.sprite.Group()'.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Обновление позиции снаряда и удаление снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.bullets.update()

        # Удаление снарядов за краем окна.
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0 or bullet.rect.top >= self.screen.get_rect().bottom
                    or bullet.rect.left >= self.screen.get_rect().right or bullet.rect.right <= 0):
                self.bullets.remove(bullet)

        # Проверка попаданий в противника.
        # При обнаружении попадания удалить снаряд и вражеский танк.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

    def _create_enemies(self):
        """
        Создание танков противника.
        """
        for enemy_number in range(self.settings.enemy_number):
            enemy = Enemy(self)
            self.enemies.add(enemy)

    def _update_enemies(self):
        """
        Обновляет позиции вражеских танков.
        """
        for enemy in self.enemies:
            enemy.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # Цвет главного экрана
        self.tank.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)

        pygame.display.flip()  # Отображение экрана.


if __name__ == '__main__':
    ot = OldTank()
    ot.run_game()

