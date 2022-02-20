import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Класс для управления снарядами, выпущенными танком
    """
    def __init__(self, ot_game):
        """
        Создает объект снарядов в текущей позиции танка
        """
        super().__init__()
        self.screen = ot_game.screen
        self.settings = ot_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.rect.midtop = ot_game.tank.rect.midtop
        self.y = float(self.rect.y)  # Позиция снаряда хранится в виде десятичной дроби.

    def update(self):
        """Перемещает снаряд по экрану."""
        self.y -= self.settings.bullet_speed  # Обновление позиции снаряда.
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
