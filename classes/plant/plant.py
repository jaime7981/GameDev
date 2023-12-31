import pygame
from pygame.sprite import Sprite
from assets.load_assets import get_asset_resource_path

class Plant(Sprite):
    def __init__(
            self, 
            name: str = 'Default Plant',
            position: [int,int] = [0,0], 
            cost: int = 100,
            level: int = 1,
            growth: int = 0,
            growth_rate: float = 0.1,
            max_growth: int = 100,
            health: int = 100,
            water: int = 0,
            sunlight: int = 0,
            image: str = get_asset_resource_path('plants/default_plant.png')
        ) -> None:
        
        Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.name = name

        self.position = position
        self.size = [16, 16]
        self.cost = cost
        self.level = level

        self.growth = growth
        self.growth_rate = growth_rate
        self.max_growth = max_growth
        
        self.health = health
        self.water = water
        self.sunlight = sunlight

    def grow(self):
        '''
        Controla el crecimiento de la planta.
        De crecer más allá del máximo, la planta sube de nivel.
        El crecimiento se ve afectado por la cantidad de agua y luz que recibe.
        '''
        if self.growth <= self.max_growth:
            self.growth += self.growth_rate * self.water + self.growth_rate * self.sunlight
        else:
            self.level = self.level + 1

    def give_water(self, amount):
        self.water += amount

    def take_water(self, amount):
        self.water -= amount

    def give_health(self, amount):
        self.health += amount

    def take_health(self, amount):
        self.health -= amount

    def set_sunlight(self, amount):
        self.sunlight = amount

    def update(self):
        self.grow()
        self.take_water(1)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.position)