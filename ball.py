import pygame
import random
import math


class Ball:

    def __init__(self, game):
        self.game = game

        self.velocity = 10
        self.angle = random.randint(0, 360)
        self.radius = 20

        self.rect = pygame.rect.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = (self.game.screen.get_width() / 2, self.game.screen.get_height() / 2)

        self.generate_angle()

    def update(self):
        pygame.draw.circle(self.game.screen, (255, 255, 255), self.rect.center, self.radius)
        self.collisions()
        self.move()

    def move(self):
        self.rect.x += math.cos(math.radians(self.angle)) * self.velocity
        self.rect.y -= math.sin(math.radians(self.angle)) * self.velocity

    def collisions(self):
        if self.rect.y <= 0 or self.rect.y >= self.game.screen.get_height() - self.rect.height:
            self.bounce_y()

        for player in self.game.players:
            if self.rect.colliderect(player):
                self.bounce_x()

        if self.rect.x <= 25:
            self.game.players[1].get_point()
            self.reset()

        if self.rect.x >= self.game.screen.get_width() - self.rect.width - 25:
            self.game.players[0].get_point()
            self.reset()

    def reset(self):
        pygame.draw.circle(self.game.screen, (0, 0, 0), self.rect.center, self.radius)

        self.generate_angle()
        self.rect.center = (self.game.screen.get_width() / 2, self.game.screen.get_height() / 2)

        self.game.delay(1000)

    def bounce_x(self): self.angle = 180 - self.angle * random.randint(9, 11) / 10

    def bounce_y(self): self.angle = 360 - self.angle

    def generate_angle(self):
        self.angle = random.randint(0, 360)

        while 105 > self.angle > 75 or 285 > self.angle > 255:
            self.angle = random.randint(0, 360)