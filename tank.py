import pygame


class Tank:
    """
    Класс для управления танком
    """

    def __init__(self, ot_game):
        """
        Инициализирует танк и задает его начальную позицию
        """
        self.screen = ot_game.screen
        self.settings = ot_game.settings
        self.screen_rect = ot_game.screen.get_rect()  # Координаты края экрана
        self.image = pygame.image.load('images/tank.png')  # Загружает изображение корабля
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # Каждый новый корабль появляется у нижнего края экрана.

        # Параметры снаряда
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = (178, 34, 34)

    def blitme(self):
        """
        Рисует танк в текущей позиции
        """
        self.screen.blit(self.image, self.rect)
