import pygame
from assets.load_assets import get_asset_resource_path

TILE_SIZE = 32

class Tile(pygame.sprite.Sprite):
    def __init__(
            self, 
            image: str = get_asset_resource_path('tiles/default_tiles.png'),
            position: [int, int] = [0,0],
            size:int = 32,
            image_start: [int, int] = [0,0],
            image_end: [int, int] = [0,0]
        ):
        super().__init__()

        self.size = size
        self.real_size_x = image_end[0] - image_start[0]
        self.real_size_y = image_end[1] - image_start[1]

        self.image_start: [int, int] = image_start

        self.image = pygame.image.load(image)

        self.image = self.image.subsurface(
            (
                self.image_start[0], 
                self.image_start[1], 
                self.real_size_x, 
                self.real_size_y
            )
        )

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

def tile_generator(width: int, height: int) -> list[Tile]:
    tile_list = []
    size = TILE_SIZE

    count_x = width // size + 2
    count_y = height // size + 2

    print(count_x, count_y)

    for x in range(count_x):
        for y in range(count_y):
            tile_list.append(
                Tile(
                    position=[x * size, y * size], 
                    size=size,
                    image_start=[1047, 66],
                    image_end=[1142, 161]
                )
            )
    
    return tile_list