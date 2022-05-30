import pygame
import time

from pygame.sprite import Sprite
from random import randint
from bullet import EnemyState


class Enemy(Sprite):
    """
    Класс, представляющий одного противника.
    """
    def __init__(self, ot_game):
        """
        Инициализирует вражеский танк и задает его начальную позицию.
        """
        super().__init__()
        self.screen = ot_game.screen
        self.settings = ot_game.settings

        # Загрузка изображения противника и назначение атрибута rect.
        self.image = pygame.image.load('images/tank_black.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 7, self.image.get_height() // 7))
        self.rect = self.image.get_rect()
        self.image_t = pygame.transform.rotate(self.image, 0)
        self.image_r = pygame.transform.rotate(self.image, 270)
        self.image_b = pygame.transform.rotate(self.image, 180)
        self.image_l = pygame.transform.rotate(self.image, 90)

        # Каждый новый вражеский танк появляется в случайном месте.
        self._dir = randint(1, 4)
        self.__time_move = time.time() + randint(1, 5)
        self.rect.x = randint(self.rect.width, (self.screen.get_rect().right - self.rect.width))
        self.rect.y = randint(self.rect.height, (self.screen.get_rect().bottom - self.rect.height))

        # Сохранение точной позиции танка.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """
        Перемещает танки.
        """
        if time.time() > self.__time_move:
            self._dir = randint(1, 4)
            self.__time_move = time.time() + randint(1, 5)
        if self.rect.bottom >= self.screen.get_rect().bottom:
            self._dir = 1
        if self.rect.y <= 0:
            self._dir = 3
        if self.rect.right >= self.screen.get_rect().right:
            self._dir = 4
        if self.rect.x <= 0:
            self._dir = 2
        if self._dir == 2:
            self.x += self.settings.enemy_speed
            self.image = self.image_r
        elif self._dir == 4:
            self.x -= self.settings.enemy_speed
            self.image = self.image_l
        elif self._dir == 3:
            self.y += self.settings.enemy_speed
            self.image = self.image_b
        elif self._dir == 1:
            self.y -= self.settings.enemy_speed
            self.image = self.image_t
        EnemyState.direction = self._dir
        self.rect.y = self.y
        self.rect.x = self.x
