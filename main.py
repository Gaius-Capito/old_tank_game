import pygame
import random
import sys
import time

from bullet import Bullet, EnemyBullet, TankState
from enemies import Enemy
from menu import Menu
from random import randint
from settings import Settings
from tank import Tank


class OldTank:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.tank = Tank(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_rect = []
        self.__time_fire = time.time() + randint(1, 4)
        self.enemy_bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self._create_enemies()
        self.font = pygame.font.Font(self.settings.font_path, 14)

        pygame.display.set_caption("Old Tank")

    def run_game(self):
        while True:
            self.clock.tick(self.settings.FPS)
            self._check_events()
            self.check_pressed_btns()
            self._update_bullets()
            self._update_enemies()
            self._check_hits()  # Проверка попаданий вражеских танков
            self._check_player_hits()
            self._check_enemy_collisions()
            self._update_enemy_bullets()
            self._update_screen()

    def _check_events(self):
        current_time = time.time()
        for enemy in self.enemies:
            if current_time > enemy._fire_time:
                enemy._fire_bullet()
                enemy._fire_time = current_time + random.uniform(1, 4)

        if time.time() > self.__time_fire and self.enemies:
            self._enemy_fire_bullet()

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
        if button[pygame.K_d] and self.tank.rect.right < (
                self.tank.screen_rect.right + 50
        ):
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
        elif (button[pygame.K_s] and self.tank.rect.bottom <
              self.tank.screen_rect.bottom):
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
            if self.enemies:
                new_bullet = EnemyBullet(self,
                                         self.enemies.sprites()[0].get_rect())
            self.enemy_bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Обновление позиции снаряда и удаление снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.bullets.update()

        # Удаление снарядов за краем окна.
        for bullet in self.bullets.copy():
            if (
                    bullet.rect.bottom <= 0 or
                    bullet.rect.top >= self.screen.get_rect().bottom or
                    bullet.rect.left >= self.screen.get_rect().right or
                    bullet.rect.right <= 0
            ):
                self.bullets.remove(bullet)

        # Проверка попаданий в противника.
        # При обнаружении попадания удалить снаряд и вражеский танк.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

    def _update_enemy_bullets(self):
        """
        Обновление позиции снаряда противника и удаление
        снарядов за краем окна.
        """
        # Обновление позиции снаряда.
        self.enemy_bullets.update()

        # Удаление снарядов за краем окна.
        for bullet in self.enemy_bullets.copy():
            if (
                    bullet.rect.bottom <= 0 or
                    bullet.rect.top >= self.screen.get_rect().bottom or
                    bullet.rect.left >= self.screen.get_rect().right or
                    bullet.rect.right <= 0
            ):
                self.enemy_bullets.remove(bullet)

    def _create_enemies(self):
        """
        Создание танков противника.
        """
        for _ in range(self.settings.enemy_number):
            enemy = Enemy(self)

            # Проверка на пересечение с другими танками
            while pygame.sprite.spritecollide(enemy, self.enemies, False):
                enemy = Enemy(self)

            self.enemies.add(enemy)

    def _update_enemies(self):
        """
        Обновляет позиции вражеских танков.
        """
        self.enemies.update()

    def _check_hits(self):
        """
        Проверяет попадания во вражеские вражеских
        танков и удаляет их при попадании.
        """
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies,
                                                True, True)
        for bullets, enemies in collisions.items():
            for enemy in enemies:
                self.enemies.remove(enemy)

    def _check_player_hits(self):
        """
        Проверяет попадания в танк игрока и управляет жизнями и флагом живости.
        """
        for bullet in self.enemy_bullets:
            if bullet.rect.colliderect(self.tank.rect):
                self.tank.lives -= 1
                if self.tank.lives <= 0:
                    self.tank.alive = False
                self.enemy_bullets.remove(bullet)
                break  # Выход из цикла после первого попадания


    def _check_enemy_collisions(self):
        for enemy in self.enemies:
            if enemy._check_collision(self.enemies):
                enemy.change_direction(self.tank.rect)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # Цвет главного экрана

        if self.tank.alive:
            self.tank.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.enemies.draw(self.screen)
            for bullet in self.enemy_bullets.sprites():
                bullet.draw_bullet()

            lives_text = self.font.render(
                f"Lives: {self.tank.lives}",
                True,
                (255, 255, 255)
            )
            self.screen.blit(lives_text, (10, 10))
        else:
            game_over_text = self.font.render(
                "Game Over",
                True,
                (255, 0, 0)
            )
            self.screen.blit(game_over_text, (
            self.settings.screen_width // 2 - 50,
            self.settings.screen_height // 2))

        pygame.display.flip()  # Отображение экрана.


if __name__ == '__main__':
    ot = OldTank()
    menu = Menu(ot.screen, ot.settings)

    # Отображение меню
    menu.show_menu()

    # Запуск игры
    ot.run_game()
