from dataclasses import dataclass


@dataclass
class Settings:
    """
    Класс для хранения настроек игры Old Tank
    """
    screen_width: int = 1200
    screen_height: int = 800
    FPS: int = 10
    bg_color: tuple = (192, 192, 192)
    font_path: str = 'font/d9464-arkhip_font.ttf'

    tank_speed: int = 5

    # настройки снаряда
    bullet_speed: int = 15
    enemy_bullet_speed: int = 20
    bullet_width: int = 5
    bullet_height: int = 5
    bullet_color: tuple = (128, 0, 0)
    enemy_bullet_color: tuple = (128, 0, 128)
    bullets_allowed: int = 4
    enemy_bullets_allowed: int = 1

    # настройки вражеских танков
    enemy_number: int = 10
    enemy_speed: int = 4
