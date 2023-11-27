import pygame

class Player:
    def __init__(self, a_game) -> None:
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("assets/player_size.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.direction = 1
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.game = a_game


    def move(self):
        if self.move_left and self.rect.left > 0:
            self.x -= self.game.speed_player
            self.rect.x = self.x
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.game.speed_player
            self.rect.x = self.x
        if self.move_up and self.rect.top > 0:
            self.y -= self.game.speed_player
            self.rect.y = self.y
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.game.speed_player
            self.rect.y = self.y
    

    def run(self):
        self.screen.blit(self.image, self.rect)