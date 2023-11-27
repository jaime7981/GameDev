import pygame
from pygame.sprite import Sprite

import classes

class Player(Sprite):
    def __init__(
            self, 
            screen: pygame.Surface = None, 
            speed: int = 2
        ) -> None:

        Sprite.__init__()

        # Atributos player
        self.speed = speed

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.sprites = self.add_sprites("assets/char.png", 64, 64)
        self.animations = self.add_animation(self.sprites) # 0: walk 1: run 3: jump
        self.walk_cooldown = (135,135,135,135,135,135)
        self.run_cooldown = (80,55,125,80,55,125)
        self.push_cooldown = (300,300)
        self.pull_cooldown = (400,400)
        self.jump_cooldown = (300,150,100,300)

        self.frame = 0
        self.event = 0 # 0: walk 1: run 2: jump ...
        self.direction = 0 # 0: abajo 1: arriba 2: derecha 3: izquierda
        self.image = self.sprites[0][self.direction]
        self.last_update = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def move(self):

        self.image = self.sprites[self.direction][0]

        if self.move_left and (self.rect.left > 0):
            self.direction = 3
            self.x -= self.speed
            self.rect.x = self.x
        if self.move_right and (self.rect.right < self.screen_rect.right):
            self.direction = 2
            self.x += self.speed
            self.rect.x = self.x
        if self.move_up and (self.rect.top > 0):
            self.direction = 1
            self.y -= self.speed
            self.rect.y = self.y
        if self.move_down and (self.rect.bottom < self.screen_rect.bottom):
            self.direction = 0
            self.y += self.speed
            self.rect.y = self.y
    
    def run(self):
        current_time = pygame.time.get_ticks()

        cooldown_event = [self.walk_cooldown, self.run_cooldown]

        if (self.move_down ^ self.move_up) or (self.move_right ^ self.move_left):
            for cooldown in cooldown_event[self.event]:
                if current_time - self.last_update >= cooldown:
                    self.frame += 1
                    self.last_update = current_time
                    if self.frame >= len(self.animations[self.event][self.direction]):
                        self.frame = 0
            self.image = self.animations[self.event][self.direction][self.frame]

        self.screen.blit(self.image, self.rect)

    
    
    def add_sprites(self, url, width_sprite, high_sprite):
        image = pygame.image.load(url)
        list_sprites = []
        for row in range(image.get_height() // high_sprite):
            list_row = []
            for column in range(image.get_width() // width_sprite):
                x = column * width_sprite
                y = row * high_sprite
                list_row.append(image.subsurface(x, y, width_sprite, high_sprite))
            list_sprites.append(list_row)
        return list_sprites
    
    def add_animation(self, sprites):
        animation_list = []

        walk = []
        for row in range(4):
            list_row = []
            for column in range(6):
                list_row.append(sprites[4+row][column])
            walk.append(list_row)
        animation_list.append(walk)

        run = []
        for row in range(4):
            list_row = []
            for column in range(6):
                list_row.append(sprites[4+row][column])
            run.append(list_row)

        for group in range(len(run)):
            run[group][2] = sprites[4+group][6]
            run[group][5] = sprites[4+group][7]
        animation_list.append(run)

        jump = []
        for row in range(4):
            list_row = []
            for column in range(3):
                list_row.append(sprites[row][5+column])
            list_row.append(sprites[row][5])
            jump.append(list_row)
        animation_list.append(jump)

        return animation_list
    
