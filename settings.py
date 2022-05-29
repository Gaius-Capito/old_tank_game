

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
        self.enemy_bullet_speed = 11
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (128, 0, 0)
        self.enemy_bullet_color = (128, 0, 128)
        self.bullets_allowed = 4
        self.enemy_bullets_allowed = 1

        # настройки вражеских танков
        # self.enemy_number = 1
        self.enemy_speed = 4
