import random
import pygame
from dino_runner.components.power.shield import Dbz, Hammer, Shield


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appear = 0
        self.hammer_at = True
        self.shield_at = True

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appear == game.points:
            self.especial = random.randint(2, 3)
            self.when_appear += random.randint(200, 300)
            if self.especial == 1:
                self.power_ups.append(Shield())
                self.shield_at = True
                self.hammer_at = False


            elif self.especial == 0:
                self.power_ups.append(Hammer())
                self.shield_at = False
                self.hammer_at = True


            else:
                self.power_ups.append(Dbz())
                self.shield_at = False
                self.hammer_at = True

            
  


           
        if self.hammer_at == True and self.shield_at == False:
            self.milagre(game)

        if self.shield_at == True and self.hammer_at == False:
            self.milagre(game)


    def milagre(self, game):
         for power_up in self.power_ups:
                power_up.update(game.game_speed, self.power_ups)           
                if game.player.dino_rect.colliderect(power_up):
                    power_up.start_time = pygame.time.get_ticks()        
                    game.player.shield = True      
                    game.player.hammer = True
                    game.player.dbz = True
                    game.player.type = power_up.type
                    game.player.hammer_time_up = power_up.start_time + (random.randint(5,8)*1000)
                    game.player.shield_time_up = power_up.start_time + (random.randint(5,8)*1000)  
                    game.player.dbz_time_up = power_up.start_time + (random.randint(5,8)*1000)                    
                    self.power_ups.remove(power_up)           
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_powerups(self):
        self.power_ups
        self.when_appear = random.randint(200, 201)
 

