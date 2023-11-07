import sys

import pygame


class Menu:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.Font(None, 40)

    def show_menu(self):
        button_color = self.settings.bg_color
        text_color = (255, 255, 255)
        button_text = self.font.render(" Начать ", True, text_color)
        button_rect = button_text.get_rect()
        button_rect.center = (
            self.settings.screen_width // 2,
            self.settings.screen_height // 2
        )

        show_menu = True
        while show_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            pygame.draw.rect(self.screen, button_color, button_rect)
            self.screen.blit(button_text, button_rect.topleft)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(self.screen, (0, 0, 255), button_rect, 3)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    show_menu = False
            else:
                pygame.draw.rect(self.screen, button_color, button_rect, 3)

            pygame.display.flip()
