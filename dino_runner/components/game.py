import random
import pygame
from dino_runner.components.Dinossauro import Dinossauro
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power.powerupmanager import PowerUpManager
from dino_runner.utils.constants import BG, DUCKING, ICON, METEORO_SKY, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinossauro()
        self.obstacle_manager = ObstacleManager()
        self.powerupmanager = PowerUpManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 2000
        self.y_pos_cloud = 120
        self.x_pos_meteoros = 2000
        self.y_pos_meteoros = 120
        self.points = 0
        self.deathC = 0
        self.record = 0
        self.rec = []
  
      
        
    def execute(self):
        self.running = True
        while self.running:
           if not self.playing:
                self.menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        
        self.playing = True
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.points += 1
        if self .points % 100 == 0 :
            self.game_speed += 1

        self.player.check_invicibility()
        self.player.H_invicibility()
        self.player.dbz_invicibility()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerupmanager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.nuvem()
        self.meteoro()
        self.draw_score()       
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerupmanager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()


    def nuvem(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud+250, self.y_pos_cloud-40))
        self.screen.blit(CLOUD, (self.x_pos_cloud-125, self.y_pos_cloud-30))
        self.screen.blit(CLOUD, (self.x_pos_cloud-500, self.y_pos_cloud+15))

        if self.x_pos_cloud <= -image_width - 200:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1800
        self.x_pos_cloud -= 1

    def meteoro(self):
        image_width = METEORO_SKY.get_width()
        self.screen.blit(METEORO_SKY, (self.x_pos_meteoros+50, self.y_pos_meteoros-55))
        if self.x_pos_meteoros <= -image_width - 200:
            self.screen.blit(METEORO_SKY, (image_width + self.x_pos_meteoros, self.y_pos_meteoros))
            self.x_pos_meteoros = 1800
        self.x_pos_meteoros -= 10

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        if self.record >= self.points:
            self.txt(18, (f"Score:{self.points}"), "#000000",  1000, 40)
        else:
            self.txt(18, (f"Score:{self.points}"), "#7b68ee",  1000, 40)

    def tecla_menu(self):         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.run()
                
    def txt(self, Font, Txt, cor, X, Y):
        font = pygame.font.Font(FONT_STYLE, Font)
        text = font.render(Txt, True, (cor))
        text_rect = text.get_rect()
        text_rect.center = (X, Y)
        self.screen.blit(text, text_rect) 


    def menu(self):
        self.obstacle_manager.reset_obstacles()
        self.powerupmanager.reset_powerups()
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT//2 #altura
        half_screen_width =  SCREEN_WIDTH//2 #largura
        if self.deathC >= 1:
            self.game_speed = 20
            # self.screen.blit(GAME_OVER, (half_screen_width-100, half_screen_height-10))
            self.txt(25, ("TRY AGAIN"), "#000000",  half_screen_width, half_screen_height)
            self.txt(20, (f"Death:{self.deathC}"), "#000000",  half_screen_width, half_screen_height+80)
            if self.points >= self.record:
                self.record = self.points -1
                self.rec.append(self.record)
                self.rec.insert(0, self.record)    
            self.txt(20, (f"Record:{self.rec[0]}"), "#7b68ee",  half_screen_width, half_screen_height+40)            
        else:
            self.txt(25, ("Press any key to start"), "#000000", half_screen_width, half_screen_height) 
            self.game_speed = 20
        
        self.screen.blit(DUCKING[0], (half_screen_width-50, half_screen_height-90))
        self.game_speed = 20
        pygame.display.update()
        self.tecla_menu()


        


     
 




