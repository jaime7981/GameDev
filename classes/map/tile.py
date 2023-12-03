import pygame
from assets.load_assets import get_asset_resource_path

class Tile(pygame.sprite.Sprite):
    def __init__(
            self, 
            image: str = get_asset_resource_path('tiles/default_tiles.png'),
            position: [int, int] = [0,0],
            size:int = 32
        ):
        super().__init__()

        self.size = size
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.position = position

    def draw(self, screen: pygame.Surface):
        screen.blit(
            self.image, 
            (
                self.position[0] - self.size / 2, 
                self.position[1] - self.size / 2
            )
        )
