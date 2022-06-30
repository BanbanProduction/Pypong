import pygame
import sys

from ball import Ball
from player import Player
from player import Player2
from background import Background
from end_screen import EndScreen
from start_screen import StartScreen


class Jeu:

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 700))
        self.icone = pygame.image.load('assets/pingpong.ico')

        self.is_start_screen = True
        self.is_end_screen = False
        self.is_playing = False

        pygame.display.set_caption("Pypong")
        pygame.display.set_icon(self.icone)

        self.players = [Player(self.screen), Player2(self.screen)]

        self.ball = Ball(self)

        self.start_screen = StartScreen(self.screen, self)
        self.background = Background(self.screen)
        self.end_screen = EndScreen(self.screen)

        self.clock = pygame.time.Clock()

    def main_function(self):
        while True:
            if self.is_start_screen:
                self.start_screen_update()

            if self.is_playing:
                self.game_update()

            if self.is_end_screen:
                self.end_screen_update()

            self.clock.tick(60)

            pygame.display.flip()

    def game_update(self):
        self.screen.fill((0, 0, 0))

        for event in pygame.event.get():

            for player in self.players:
                player.events(event)

            if event.type == pygame.QUIT:
                sys.exit()

        for player in self.players:
            player.update()

        self.background.update()

        self.ball.update()

        self.check_end()

    def check_end(self):
        for player in self.players:

            if player.score == 8:
                self.is_end_screen = True
                self.is_playing = False

                self.end_screen.player_number = self.players.index(player) + 1

    def end_screen_update(self):
        self.end_screen.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and self.end_screen.restart_rect.collidepoint(event.pos)
            ):
                self.reset()

    def start_screen_update(self):
        self.start_screen.update(pygame.event.get())

    def reset(self):
        self.is_playing = True
        self.is_end_screen = False

        for player in self.players:
            player.reset()

    def start(self, ball_velocity):
        self.is_start_screen = False
        self.is_playing = True
        self.ball.velocity = ball_velocity

    @staticmethod
    def delay(delay):
        pygame.display.flip()
        pygame.time.delay(delay)


if __name__ == '__main__':
    pygame.init()
    Jeu().main_function()
    pygame.quit()