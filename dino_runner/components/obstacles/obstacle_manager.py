from random import randint
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.ave import Ave 


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
    def update(self, game):
        self.obs = randint(0, 1)
        if len(self.obstacles) == 0:
            if self.obs == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS + LARGE_CACTUS))
            else:
                 self.obstacles.append(Ave(BIRD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)     
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.powerupmanager.shield_at == True:
                    if game.player.shield == True:
                        pass               
                    elif game.player.hammer == True:
                        pass

                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.deathC += 1

                if  game.powerupmanager.hammer_at == True:
                    if game.player.shield == True:
                        self.obstacles.remove(obstacle)
                        
                    elif game.player.hammer == True:
                        self.obstacles.remove(obstacle)                        

                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.deathC += 1
                  

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

 
    def reset_obstacles(self):
        self.obstacles = []


