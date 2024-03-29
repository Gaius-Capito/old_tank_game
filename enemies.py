import pygame
import random
import time

from pygame.sprite import Sprite
from bullet import EnemyState, EnemyBullet


class Enemy(Sprite):
    """
    Класс, представляющий одного противника.
    """
    def __init__(self, ot_game):
        """
        Инициализирует вражеский танк и задает его начальную позицию.
        """
        super().__init__()
        self.ot_game = ot_game
        self.screen = ot_game.screen
        self.settings = ot_game.settings

        # Загрузка изображения противника и назначение атрибута rect.
        self.image = pygame.image.load('images/tank_black.png')
        self.image = pygame.transform.scale(
            self.image, (
                self.image.get_width() // 7, self.image.get_height() // 7
            )
        )
        self.rect = self.image.get_rect()
        self.image_t = pygame.transform.rotate(self.image, 0)
        self.image_r = pygame.transform.rotate(self.image, 270)
        self.image_b = pygame.transform.rotate(self.image, 180)
        self.image_l = pygame.transform.rotate(self.image, 90)

        # Каждый новый вражеский танк появляется в случайном месте.
        self._direction = random.randint(1, 4)
        self.__time_move = time.time() + random.randint(1, 5)
        self.rect.x = random.randint(
            self.rect.width, (self.screen.get_rect().right - self.rect.width)
        )
        self.rect.y = random.randint(
            self.rect.height, (
                    self.screen.get_rect().bottom - self.rect.height
            )
        )

        # Сохранение точной позиции танка.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self._fire_time = time.time() + random.uniform(1, 4)

    def update(self):
        """
        Перемещает танки.
        """
        if time.time() > self.__time_move:
            self._direction = random.randint(1, 4)
            self.__time_move = time.time() + random.randint(1, 5)
        if self.rect.bottom >= self.screen.get_rect().bottom:
            self._direction = 1
        if self.rect.y <= 0:
            self._direction = 3
        if self.rect.right >= self.screen.get_rect().right:
            self._direction = 4
        if self.rect.x <= 0:
            self._direction = 2
        if self._direction == 2:
            self.x += self.settings.enemy_speed
            self.image = self.image_r
        elif self._direction == 4:
            self.x -= self.settings.enemy_speed
            self.image = self.image_l
        elif self._direction == 3:
            self.y += self.settings.enemy_speed
            self.image = self.image_b
        elif self._direction == 1:
            self.y -= self.settings.enemy_speed
            self.image = self.image_t
        EnemyState.direction = self._direction
        self.rect.y = self.y
        self.rect.x = self.x

    def get_rect(self):
        """
        Возвращает прямоугольник rect вражеского танка.
        """
        return self.rect

    def _fire_bullet(self):
        """
        Создание снаряда для вражеского танка и
        добавление в 'pygame.sprite.Group()'.
        """
        bullet = EnemyBullet(self.ot_game, self.rect, self._direction)
        self.ot_game.enemy_bullets.add(bullet)

    def _check_collision(self, enemies):
        """
        Проверяем столкновения танков противника.
        """
        for enemy in enemies:
            if enemy != self and self.rect.colliderect(enemy.rect):
                return True
        return False

    def change_direction(self, player_rect):
        """
        Изменяет направление движения вражеского
        танка при столкновении с другим танком.
        """
        opposite_directions = {1: 3, 2: 4, 3: 1, 4: 2}
        direction = opposite_directions[self._direction]
        self._direction = direction

    def get_direction(self):
        """
        Возвращает текущее направление вражеского танка.
        """
        return self._direction
