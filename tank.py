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
        self.image = pygame.image.load('images/tank_green.png')  # Загружает изображение танка
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 7, self.image.get_height() // 7))
        self.tank_img_r = pygame.transform.rotate(self.image, 270)
        self.tank_img_b = pygame.transform.rotate(self.image, 180)
        self.tank_img_l = pygame.transform.rotate(self.image, 90)
        self.tank_img_t = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # Танк появляется у нижнего края экрана.

    def blitme(self):
        """
        Рисует танк в текущей позиции
        """
        self.screen.blit(self.image, self.rect)
