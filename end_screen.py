import pygame


class EndScreen:

    def __init__(self, screen):
        self.screen = screen
        self.player_number = None

        self.restart_rect = pygame.rect.Rect(0, 0, 325, 45)
        self.restart_rect.x = self.screen.get_width() / 2 - self.restart_rect.width / 2
        self.restart_rect.y = self.screen.get_height() / 2.25

        self.quit_rect = pygame.rect.Rect(0, 0, 200, 45)
        self.quit_rect.x = self.screen.get_width() / 2 - self.quit_rect.width / 2
        self.quit_rect.y = self.screen.get_height() / 1.70

        self.win_message_rect = pygame.rect.Rect(200, 100, 530, 45)
        self.win_message_rect.x = self.screen.get_width() / 2 - self.win_message_rect.width / 2
        self.win_message_rect.y = self.screen.get_height() / 6

    def update(self):
        self.screen.fill((0, 0, 0))

        font = pygame.font.SysFont('Lato', 70, True)

        win_message = font.render(f"Le joueur {self.player_number} a gagné !", True, (255, 255, 255))
        restart_message = font.render('Redémarrer', True, (255, 255, 255))
        quit_message = font.render('Quitter', True, (255, 255, 255))

        self.screen.blit(win_message, self.win_message_rect)
        self.screen.blit(restart_message, self.restart_rect)
        self.screen.blit(quit_message, self.quit_rect)