import sys

import pygame


class StartScreen:

    def __init__(self, screen, game):
        self.screen = screen
        self.scr_size = self.screen.get_size()
        self.game = game

        self.messages = {
            'welcome': (pygame.rect.Rect(self.scr_size[0] / 2 - 350, self.scr_size[1] / 6, 720, 60),
                        "Bienvenue dans Pypong"),
            'easy': (pygame.rect.Rect(self.scr_size[0] / 2 - 130, self.scr_size[1] / 2.75, 260, 60),
                     "Facile", 10),
            'medium': (pygame.rect.Rect(self.scr_size[0] / 2 - 130, self.scr_size[1] / 2, 260, 60),
                       "Moyen", 15),
            'hard': (pygame.rect.Rect(self.scr_size[0] / 2 - 130, self.scr_size[1] / 1.5, 260, 60),
                     "Difficile", 20)
        }

    def update(self, events):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Corbel', 70, True)

        for message in self.messages.values():
            self.screen.blit(font.render(message[1], True, (255, 255, 255)), message[0])

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for message in self.messages.values():
                    if message[0].collidepoint(event.pos):
                        self.game.start(message[2])