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
    tank_speed: int = 5
    font_path: str = 'font/d9464-arkhip_font.ttf'

    # настройки снаряда
    bullet_speed: int = 15
    enemy_bullet_speed: int = 11
    bullet_width: int = 5
    bullet_height: int = 5
    bullet_color: tuple = (128, 0, 0)
    enemy_bullet_color: tuple = (128, 0, 128)
    bullets_allowed: int = 4
    enemy_bullets_allowed: int = 1

    # настройки вражеских танков
    enemy_number: int = 8
    enemy_speed: int = 4
