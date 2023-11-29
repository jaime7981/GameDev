import pygame
from assets.load_assets import get_asset_resource_path
from classes.player import Player

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,255,0)
BACKGROUND_COLOR = (100,60,180)

class GUI():
    def __init__(self, width = 500, height = 500) -> None:
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = 60

        self.width = width
        self.height = height

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 10)

        pygame.display.set_caption("Juego de Prueba")

        self.background_color = BACKGROUND_COLOR
        loaded_backgound = pygame.image.load(get_asset_resource_path('background.jpg'))
        self.background = pygame.transform.scale(loaded_backgound, (width, height))

        self.initialize_players()
        self.plants = []

    def initialize_players(self):
        self.player: Player = Player(self.screen)

    def draw_background(self) -> None:
        self.screen.blit(self.background, (0, 0))


    def draw_mouse_position(self) -> None:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, (0, 10, 155), (x, y), 5)


    def draw_player(self) -> None:
        self.player.draw(self.screen)

    def draw_plants(self) -> None:
        for plant in self.plants:
            plant.draw(self.screen)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print('mouse down')

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
                    self.player.speed = self.player.speed * 2
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.move_left = False
                if event.key == pygame.K_RIGHT:
                    self.player.move_right = False
                if event.key == pygame.K_UP:
                    self.player.move_up = False
                if event.key == pygame.K_DOWN:
                    self.player.move_down = False
                if event.key == pygame.K_LSHIFT:
                    self.player.event = 0
                    self.player.speed = self.player.speed // 2

    def run_game(self) -> None:
        while self.running:
            self.clock.tick(self.tick)
            self.check_events()

            self.draw_background()
            self.draw_mouse_position()
            self.draw_plants()

            self.screen.fill(self.background_color)
            self.player.update()

            pygame.display.update()

