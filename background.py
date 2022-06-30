import pygame


class Background:

    def __init__(self, screen):
        self.screen = screen
        self.widht = 30
        self.height = 100
        self.rect = pygame.rect.Rect(self.screen.get_width() / 2 - self.widht / 2, 0, self.widht, self.height)

    def update(self):
        self.rect.y = 0

        while self.rect.y < self.screen.get_height():
            pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
            self.rect.y += self.height * 2