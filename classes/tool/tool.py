import pygame
from pygame.sprite import Sprite
from assets.load_assets import get_asset_resource_path

class Tool(Sprite):
    def __init__(
            self,
            name: str = 'Default Tool',
            tool_type: str = 'generic',
            image: str = get_asset_resource_path('tools/default_tool.png'),
            position: [int,int] = [0,0],
            power: int = 10,
            durability: int = 100,
            range: int = 1,
            area_of_effect = None,
            use_speed: int = 1,
            required_level: int = 1,
            max_uses: int = 100
        ) -> None:
        
        Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.position = position

        self.name = name

        self.tool_type = tool_type
    
        self.power = power
        self.durability = durability
        self.range = range
        self.area_of_effect = area_of_effect
        self.use_speed = use_speed

        self.required_level = required_level

        self.max_uses = max_uses
        self.remaining_uses = max_uses

    def use(self, target):
        '''
        Usar herramienta en un objetivo (ej: una planta).
        lógica específica de cada herramienta.
        '''
        pass

    def reduce_durability(self, amount):
        self.durability -= amount
        if self.durability < 0:
            self.durability = 0

    def repair(self, amount):
        self.durability += amount

    def update(self):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.position)