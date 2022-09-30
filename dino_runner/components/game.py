import pygame
from dino_runner.components.Dinossauro import Dinossauro
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, DUCKING, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
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
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.point = 0
        self.deathC = 0

    def execute(self):
        self.running = True
        while self.running:
           if not self.playing:
                self.menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        self.point = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.point += 1
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(f"Score:{self.point}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)



    def tecla_menu(self):         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.run()

    def menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT//2 #altura
        half_screen_width =  SCREEN_WIDTH//2 #largura
        
        if self.deathC >= 1:
            font = pygame.font.Font(FONT_STYLE, 25)
            text = font.render("TRY AGAIN", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect) 

            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(f"Death:{self.deathC}", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height+40)
            self.screen.blit(text, text_rect)

        else:
            font = pygame.font.Font(FONT_STYLE, 25)
            text = font.render("Press any key to start", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect) 

      

        self.screen.blit(DUCKING[0], (half_screen_width-50, half_screen_height-90))

        
        pygame.display.update()
        self.tecla_menu()



