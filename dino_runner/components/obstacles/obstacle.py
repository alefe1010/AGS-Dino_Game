import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Obstacle(Sprite):
    def __init__(self, image, type, bird):  
        self.type = type
        self.image = image[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, obstacles):
        if self.step_index >= 10:
            self.step_index = 0
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        self.rect.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        


