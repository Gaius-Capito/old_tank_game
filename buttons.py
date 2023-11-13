import pygame


class ButtonToMenu:
    def __init__(self, screen, callback, settings):
        self.screen = screen
        self.button_rect = pygame.Rect(
            (settings.screen_width // 2 - 50,
             settings.screen_height // 2 + 50, 100, 40)
        )
        self.color = settings.bg_color
        self.border_color = (0, 0, 255)
        self.callback = callback
        self.clicked = False

        # Настройка шрифта и размера текста
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("В меню", True, (255, 255, 255))

        # Определение координат для центрирования текста
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.button_rect.center

    def draw(self):
        # Определение цвета кнопки в зависимости от положения мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_x, mouse_y):
            # Отрисовка кнопки и обводки, если мышь над кнопкой
            pygame.draw.rect(self.screen, self.color, self.button_rect)
            pygame.draw.rect(self.screen, self.border_color, self.button_rect,
                             3)
        else:
            # Иначе отрисовываем кнопку без обводки
            pygame.draw.rect(self.screen, self.color, self.button_rect)

        # Отрисовка текста
        self.screen.blit(self.text, self.text_rect.topleft)

    def handle_event(self, event):
        # Обработка событий мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(self.screen, (0, 0, 255), self.button_rect, 3)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.button_rect.collidepoint(event.pos):
                self.clicked = False
                self.callback()
