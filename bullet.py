import pygame

from pygame.sprite import Sprite


class TankState:
    direction = 1


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
        self.tank_position = ot_game.check_pressed_btns
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.__direction = TankState.direction
        self.__bullet_pos(ot_game)
        self.y = float(self.rect.y)  # Позиция снаряда хранится в виде десятичной дроби.
        self.x = float(self.rect.x)

    def update(self):
        """
        Перемещает снаряд по экрану.
        """
        if self.__direction == 1:
            self.y -= self.settings.bullet_speed  # Обновление позиции снаряда.
        elif self.__direction == 2:
            self.x += self.settings.bullet_speed
        elif self.__direction == 3:
            self.y += self.settings.bullet_speed
        elif self.__direction == 4:
            self.x -= self.settings.bullet_speed
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """
        Вывод снаряда на экран.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

    def __bullet_pos(self, ot_game):
        if self.__direction == 1:
            self.rect.midtop = ot_game.tank.rect.midtop
        elif self.__direction == 2:
            self.rect.midright = ot_game.tank.rect.midright
        elif self.__direction == 3:
            self.rect.midbottom = ot_game.tank.rect.midbottom
        elif self.__direction == 4:
            self.rect.midleft = ot_game.tank.rect.midleft
