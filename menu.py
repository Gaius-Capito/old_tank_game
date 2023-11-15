import sys

import pygame


class Menu:
    """
    Класс отвечающий за меню игры
    """
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.Font(None, 40)
        self.description_font = pygame.font.Font(None, 20)
        self.mode_description = ''
        self.is_normal_mode_hovered = False  # Флаги для отслеживания
        self.is_dark_mode_hovered = False  # наведения на кнопки

    def show_menu(self):
        show_menu = True

        while show_menu:
            event = pygame.event.poll()  # Получаем последнее событие в очереди
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.screen.fill(self.settings.bg_color)

            # Добавление кнопки "Начать"
            start_button_color = (150, 150, 150)
            start_text_color = (255, 255, 255)
            start_button_text = self.font.render(
                ' Начать ',
                True,
                start_text_color
            )
            start_button_rect = start_button_text.get_rect()
            start_button_rect.center = (
                self.settings.screen_width // 2,
                self.settings.screen_height // 2 - 50
            )

            # Добавление кнопки "Режимы"
            modes_button_color = (150, 150, 150)
            modes_text_color = (255, 255, 255)
            modes_button_text = self.font.render(
                ' Режимы ',
                True,
                modes_text_color
            )
            modes_button_rect = modes_button_text.get_rect()
            modes_button_rect.center = (
                self.settings.screen_width // 2,
                self.settings.screen_height // 2 + 50
            )

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Обработка событий для кнопки "Начать"
            if start_button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 255),
                    start_button_rect,
                    3
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    show_menu = False
            else:
                pygame.draw.rect(
                    self.screen,
                    start_button_color,
                    start_button_rect,
                    3
                )

            # Обработка событий для кнопки "Режимы"
            if modes_button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 255),
                    modes_button_rect,
                    3
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.show_modes_menu()
            else:
                pygame.draw.rect(
                    self.screen,
                    modes_button_color,
                    modes_button_rect,
                    3
                )

            self.screen.blit(start_button_text, start_button_rect.topleft)
            self.screen.blit(modes_button_text, modes_button_rect.topleft)

            description_text = self.description_font.render(
                self.mode_description,
                True,
                (255, 255, 255)
            )
            self.screen.blit(description_text,
                             (10, self.settings.screen_height - 40))

            pygame.display.flip()

    def show_modes_menu(self):
        modes_menu = True

        while modes_menu:
            event = pygame.event.poll()  # Получаем последнее событие в очереди
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.screen.fill(self.settings.bg_color)

            # Добавление кнопки "Обычный режим"
            normal_mode_button_color = (150, 150, 150)
            normal_mode_text_color = (255, 255, 255)
            normal_mode_button_text = self.font.render(
                ' Обычный режим ',
                True,
                normal_mode_text_color
            )
            normal_mode_button_rect = normal_mode_button_text.get_rect()
            normal_mode_button_rect.center = (
                self.settings.screen_width // 2,
                self.settings.screen_height // 2 - 50
            )

            # Добавление кнопки "Ночной бой"
            dark_mode_button_color = (0, 0, 0)
            dark_mode_text_color = (255, 255, 255)
            dark_mode_button_text = self.font.render(
                ' Ночной бой ',
                True,
                dark_mode_text_color
            )
            dark_mode_button_rect = dark_mode_button_text.get_rect()
            dark_mode_button_rect.center = (
                self.settings.screen_width // 2,
                self.settings.screen_height // 2 + 50
            )

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if normal_mode_button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(self.screen, (0, 0, 255),
                                 normal_mode_button_rect, 3)
                self.is_normal_mode_hovered = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.settings.bg_color = (150, 150, 150)
                    modes_menu = False
            else:
                pygame.draw.rect(self.screen, normal_mode_button_color,
                                 normal_mode_button_rect, 3)
                self.is_normal_mode_hovered = False

                # Обработка событий для кнопки "Ночной бой"
            if dark_mode_button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(self.screen, (0, 0, 255),
                                 dark_mode_button_rect, 3)
                self.is_dark_mode_hovered = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.settings.bg_color = (0, 0, 0)
                    modes_menu = False
            else:
                pygame.draw.rect(self.screen, dark_mode_button_color,
                                 dark_mode_button_rect, 3)
                self.is_dark_mode_hovered = False

                # Отображение описания режима при наведении на кнопку
            if self.is_normal_mode_hovered:
                description_text = self.description_font.render(
                    (
                     'Обычный режим: В этом режиме вам необходимо выжить '
                     'и уничтожить все танки противника. Столкновение с '
                     'вражеским танком ведет к поражению'
                     ),
                    True,
                    (255, 255, 255)
                )
                self.screen.blit(description_text,
                                 (10, self.settings.screen_height - 40))
            elif self.is_dark_mode_hovered:
                description_text = self.description_font.render(
                    (
                     'Обычный режим: В этом режиме Сражение проходит ночью. '
                     'Противник будет незаметен. Ориентируйтесь на выстрелы.'
                    )
                    ,
                    True,
                    (255, 255, 255)
                )
                self.screen.blit(description_text,
                                 (10, self.settings.screen_height - 40))

            self.screen.blit(
                normal_mode_button_text,
                normal_mode_button_rect.topleft
            )
            self.screen.blit(
                dark_mode_button_text,
                dark_mode_button_rect.topleft
            )

            pygame.display.flip()
