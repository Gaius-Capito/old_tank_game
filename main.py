import sys
import time
import pygame

from random import randint
from settings import Settings
from tank import Tank
from bullet import Bullet, EnemyBullet, EnemyBullet2, EnemyBullet3, EnemyBullet4, TankState
from enemies import Enemy, Enemy2, Enemy3, Enemy4


class OldTank:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.tank = Tank(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemies2 = pygame.sprite.Group()
        self.enemies3 = pygame.sprite.Group()
        self.enemies4 = pygame.sprite.Group()
        self.enemy_rect = []
        self.enemy_rect2 = []
        self.enemy_rect3 = []
        self.enemy_rect4 = []
        self.__time_fire = time.time() + randint(1, 4)
        self.__time_fire2 = time.time() + randint(1, 4)
        self.__time_fire3 = time.time() + randint(1, 4)
        self.__time_fire4 = time.time() + randint(1, 4)

        print('tanks', self.enemy_rect)
        self.enemy_bullets = pygame.sprite.Group()
        self.enemy_bullets2 = pygame.sprite.Group()
        self.enemy_bullets3 = pygame.sprite.Group()
        self.enemy_bullets4 = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self._create_enemies()
        self._create_enemies2()
        self._create_enemies3()
        self._create_enemies4()
        pygame.display.set_caption("Old Tank")
        print(self.enemies)
        print(self.enemies2)
        print(self.enemies3)
        print(self.enemies4)

    def run_game(self):
        while True:
            self.clock.tick(self.settings.FPS)
            self._check_events()
            self.check_pressed_btns()
            self._update_bullets()
            self._update_enemies()
            self._update_enemies2()
            self._update_enemies3()
            self._update_enemies4()
            self._update_enemy_bullets()
            self._update_enemy_bullets2()
            self._update_enemy_bullets3()
            self._update_enemy_bullets4()
            self._update_screen()

    def _check_events(self):
        if time.time() > self.__time_fire and self.enemies:
            self._enemy_fire_bullet()
        if time.time() > self.__time_fire2 and self.enemies2:
            self._enemy_fire_bullet2()
        if time.time() > self.__time_fire3 and self.enemies3:
            self._enemy_fire_bullet3()
        if time.time() > self.__time_fire4 and self.enemies4:
            self._enemy_fire_bullet4()
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

    def _enemy_fire_bullet(self):
        """
        Создание снарядов противника и добавление в 'pygame.sprite.Group()'.
        """
        if len(self.enemy_bullets) < self.settings.enemy_bullets_allowed:
            new_bullet = EnemyBullet(self)
            self.enemy_bullets.add(new_bullet)

    def _enemy_fire_bullet2(self):
        """
        Создание снарядов противника и добавление в 'pygame.sprite.Group()'.
        """
        if len(self.enemy_bullets2) < self.settings.enemy_bullets_allowed:
            new_bullet = EnemyBullet2(self)
            self.enemy_bullets2.add(new_bullet)

    def _enemy_fire_bullet3(self):
        """
        Создание снарядов противника и добавление в 'pygame.sprite.Group()'.
        """
        if len(self.enemy_bullets3) < self.settings.enemy_bullets_allowed:
            new_bullet = EnemyBullet3(self)
            self.enemy_bullets3.add(new_bullet)

    def _enemy_fire_bullet4(self):
        """
        Создание снарядов противника и добавление в 'pygame.sprite.Group()'.
        """
        if len(self.enemy_bullets4) < self.settings.enemy_bullets_allowed:
            new_bullet = EnemyBullet4(self)
            self.enemy_bullets4.add(new_bullet)

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

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies2, True, True)

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies3, True, True)

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies4, True, True)

    def _update_enemy_bullets(self):
        """
        Обновление позиции снаряда противника и удаление снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.enemy_bullets.update()

        # Удаление снарядов за краем окна.
        for bullet in self.enemy_bullets.copy():
            if (bullet.rect.bottom <= 0 or bullet.rect.top >= self.screen.get_rect().bottom
                    or bullet.rect.left >= self.screen.get_rect().right or bullet.rect.right <= 0):
                self.enemy_bullets.remove(bullet)

    def _update_enemy_bullets2(self):
        """
        Обновление позиции снаряда противника и удаление снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.enemy_bullets2.update()

        # Удаление снарядов за краем окна.
        for bullet in self.enemy_bullets2.copy():
            if (bullet.rect.bottom <= 0 or bullet.rect.top >= self.screen.get_rect().bottom
                    or bullet.rect.left >= self.screen.get_rect().right or bullet.rect.right <= 0):
                self.enemy_bullets2.remove(bullet)

    def _update_enemy_bullets3(self):
        """
        Обновление позиции снаряда противника и удаление снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.enemy_bullets3.update()

        # Удаление снарядов за краем окна.
        for bullet in self.enemy_bullets3.copy():
            if (bullet.rect.bottom <= 0 or bullet.rect.top >= self.screen.get_rect().bottom
                    or bullet.rect.left >= self.screen.get_rect().right or bullet.rect.right <= 0):
                self.enemy_bullets3.remove(bullet)

    def _update_enemy_bullets4(self):
        """
        Обновление позиции снаряда противника и удаление снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.enemy_bullets4.update()

        # Удаление снарядов за краем окна.
        for bullet in self.enemy_bullets4.copy():
            if (bullet.rect.bottom <= 0 or bullet.rect.top >= self.screen.get_rect().bottom
                    or bullet.rect.left >= self.screen.get_rect().right or bullet.rect.right <= 0):
                self.enemy_bullets4.remove(bullet)

    def _create_enemies(self):
        """
        Создание танков противника.
        """
        for _ in range(1):
            enemy = Enemy(self)
            self.enemies.add(enemy)

    def _create_enemies2(self):
        """
        Создание танков противника.
        """
        for _ in range(1):
            enemy = Enemy2(self)
            self.enemies2.add(enemy)

    def _create_enemies3(self):
        """
        Создание танков противника.
        """
        for _ in range(1):
            enemy = Enemy3(self)
            self.enemies3.add(enemy)

    def _create_enemies4(self):
        """
        Создание танков противника.
        """
        for _ in range(1):
            enemy = Enemy4(self)
            self.enemies4.add(enemy)

    def _update_enemies(self):
        """
        Обновляет позиции вражеских танков.
        """
        for i in self.enemies:
            self.enemy_rect.append(i)
        for enemy in self.enemies:
            enemy.update()

    def _update_enemies2(self):
        """
        Обновляет позиции вражеских танков.
        """
        for i in self.enemies2:
            self.enemy_rect2.append(i)
        for enemy in self.enemies2:
            enemy.update()

    def _update_enemies3(self):
        """
        Обновляет позиции вражеских танков.
        """
        for i in self.enemies3:
            self.enemy_rect3.append(i)
        for enemy in self.enemies3:
            enemy.update()

    def _update_enemies4(self):
        """
        Обновляет позиции вражеских танков.
        """
        for i in self.enemies4:
            self.enemy_rect4.append(i)
        for enemy in self.enemies4:
            enemy.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # Цвет главного экрана
        self.tank.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)
        self.enemies2.draw(self.screen)
        self.enemies3.draw(self.screen)
        self.enemies4.draw(self.screen)
        for bullet in self.enemy_bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.enemy_bullets2.sprites():
            bullet.draw_bullet()
        for bullet in self.enemy_bullets3.sprites():
            bullet.draw_bullet()
        for bullet in self.enemy_bullets4.sprites():
            bullet.draw_bullet()

        pygame.display.flip()  # Отображение экрана.


if __name__ == '__main__':
    ot = OldTank()
    ot.run_game()
