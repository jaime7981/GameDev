import pygame
import math

class GUI():
    def __init__(self, width = 500, height = 500, assets_path = './assets') -> None:
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = 60

        self.width = width
        self.height = height

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 10)


        loaded_backgound = pygame.image.load(f'{assets_path}/background.jpg')
        self.background = pygame.transform.scale(loaded_backgound, (width, height))

        loaded_arrow = pygame.image.load(f'{assets_path}/arrow.png')


    def draw_background(self) -> None:
        self.screen.blit(self.background, (0, 0))


    def draw_mouse_position(self) -> None:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, (0, 10, 155), (x, y), 5)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('mouse down')


    def run_game(self) -> None:
        while self.running:
            self.clock.tick(self.tick)
            self.check_events()

            self.draw_background()
            self.draw_mouse_position()

            pygame.display.update()

