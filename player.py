import pygame


class Player:

    def __init__(self, screen):
        self.screen = screen

        self.velocity = 1
        self.velocity = 7
        self.pressed = {}
        self.score = 0
        self.start_x_position = 20
        self.rect = pygame.rect.Rect(self.start_x_position, 300, 20, 120)

        self.scores_sheet = pygame.image.load('assets/scores_sheet.png')
        self.scores = {
            '0': self.get_image(0, 0),
            '1': self.get_image(100, 0),
            '2': self.get_image(200, 0),
            '3': self.get_image(300, 0),
            '4': self.get_image(400, 0),
            '5': self.get_image(500, 0),
            '6': self.get_image(600, 0),
            '7': self.get_image(700, 0),
            '8': self.get_image(0, 112)
        }
        self.score_rect = (self.screen.get_width() / 3, 50, 50, 200)

        self.score_image = self.scores[str(self.score)]
        self.score_image.set_colorkey((0, 0, 0))

    def update(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

        self.score_image = self.scores[str(self.score)]
        self.screen.blit(self.score_image, self.score_rect)

        self.score_image.set_colorkey((0, 0, 0))

        self.move()

    def events(self, event):
        if event.type == pygame.KEYDOWN and (
            (event.key == pygame.K_z or pygame.K_s or pygame.K_UP or pygame.K_DOWN)
        ):
            self.pressed[event.key] = True

        if event.type == pygame.KEYUP and (
                event.key == pygame.K_z or pygame.K_s or pygame.K_UP or pygame.K_DOWN
        ):
            self.pressed[event.key] = False

    def in_screen(self):
        if 0 < self.rect.y < (self.screen.get_height() - self.rect.height):
            return True

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move(self):
        if self.pressed.get(pygame.K_z):
            self.move_up()

            if not self.in_screen():
                self.move_down()

        if self.pressed.get(pygame.K_s):
            self.move_down()

            if not self.in_screen():
                self.move_up()

    def get_point(self):
        self.score += 1
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([50, 100])
        image.blit(self.scores_sheet, (0, 0), (x, y, 50, 100))
        return image

    def reset(self):
        self.score = 0
        self.rect = pygame.rect.Rect(self.start_x_position, 300, 20, 120)


class Player2(Player):

    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x = self.screen.get_width() - self.rect.width - 20
        self.start_x_position = self.screen.get_width() - self.rect.width - 20
        self.score_rect = (self.screen.get_width() / 3 * 2, 50, 50, 200)

    def move(self):
        if self.pressed.get(pygame.K_UP):
            self.move_up()

            if not self.in_screen():
                self.move_down()

        if self.pressed.get(pygame.K_DOWN):
            self.move_down()

            if not self.in_screen():
                self.move_up()
