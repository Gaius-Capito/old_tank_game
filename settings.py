

class Settings:
    """
    Класс для хранения настроек игры Old Tank
    """
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 10
        self.bg_color = (192, 192, 192)
        self.tank_speed = 5

        # настройки снаряда
        self.bullet_speed = 15
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (128, 0, 0)
        self.bullets_allowed = 7

        # настройки вражеских танков
        self.enemy_number = 4
        self.enemy_speed = 4
