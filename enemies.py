import pygame

from pygame.sprite import Sprite
from random import randint


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

        # Загрузка изображения противника и назначение атрибута rect.
        self.image = pygame.image.load('images/tank_black.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 7, self.image.get_height() // 7))
        self.rect = self.image.get_rect()

        # Каждый новый вражеский танк появляется в случайном месте.
        self.rect.x = randint(self.rect.width, (self.screen.get_rect().right - self.rect.width))
        self.rect.y = randint(self.rect.height, (self.screen.get_rect().bottom - self.rect.height))

        # Сохранение точной позиции танка.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
