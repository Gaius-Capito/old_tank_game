import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Класс для управления снарядами, выпущенными танком.
    """
    def __init__(self, ot_game):
        """
        Создает объект снарядов в текущей позиции танка.
        """
        super().__init__()
        self.screen = ot_game.screen
        self.settings = ot_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.rect.midtop = ot_game.ship.rect.midtop
        self.y = float(self.rect.y)  # Позиция снаряда хранится в виде десятичной дроби.
