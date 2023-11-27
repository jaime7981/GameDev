import pygame
import sys

from classes.player import Player

#COSTINANTS
WIDTH = 800
HIGH = 600
 
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,255,0)
BACKGROUND_COLOR = (100,60,180)

clock = pygame.time.Clock()

class Game:
    def __init__(self) -> None: 
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HIGH))
        pygame.display.set_caption("Juego de Prueba")
        self.game_over = False
        self.color = BACKGROUND_COLOR
        #self.background=pygame.image.load("Fondo.png").convert()
        self.speed_walk = 2
        self.speed_run = 4
        self.speed_player = self.speed_walk
        self.player = Player(self)

    def run_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = True
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = True
                    if event.key == pygame.K_UP:
                        self.player.move_up = True
                    if event.key == pygame.K_DOWN:
                        self.player.move_down = True
                    if event.key == pygame.K_LSHIFT:
                        self.player.event = 1
                        self.speed_player = self.speed_run

                elif event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.player.move_left = False
                        self.player.frame = 0
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = False
                        self.player.frame = 0
                    if event.key == pygame.K_UP:
                        self.player.move_up = False
                        self.player.frame = 0
                    if event.key == pygame.K_DOWN:
                        self.player.move_down = False
                        self.player.frame = 0
                    if event.key == pygame.K_LSHIFT:
                        self.player.event = 0
                        self.speed_player = self.speed_walk

            self.player.move()
            self.screen.fill(self.color)
            self.player.run()
            #self.screen.blit(self.background, [0,0])
            pygame.display.flip()
            clock.tick(60) #FPS

if __name__ == "__main__":
    game = Game()
    game.run_game()