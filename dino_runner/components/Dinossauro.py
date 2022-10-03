from ast import If
import pygame
from pygame.sprite import Sprite 
from dino_runner.utils.constants import DBZ_TYPE, DUCKING, DUCKING_DBZ, DUCKING_HAMMER, HAMMER_TYPE, JUMPING, JUMPING_DBZ, JUMPING_HAMMER, RUNNING, DEFAULT_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_DBZ, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, DBZ_TYPE: DUCKING_DBZ}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, DBZ_TYPE: JUMPING_DBZ}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, DBZ_TYPE: RUNNING_DBZ}




class Dinossauro(Sprite):

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 344
    JUMP_VEL = 8.5
    DBZ_POS = 155
    DBZ_POS_DUCK = 260



    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_duck = False
        self.shield = False
        self.shild_time_up = 0
        self.hammer = False
        self.hammer_time_up = 0
        self.dbz = False
        self.dbz_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_SPACE] or user_input[pygame.K_UP] and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not self.dino_jump :
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0


    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        if self.type == DBZ_TYPE:
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.DBZ_POS
            self.step_index += 1
        else:
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.step_index += 1


    def jump(self):
        
        if self.type == DBZ_TYPE:
            self.image = DUCK_IMG[self.type][self.step_index //5]
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.9
            if self.jump_vel < -self.JUMP_VEL:
                self.dino_rect.y = self.DBZ_POS
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL

        else:
            self.image = JUMP_IMG[self.type]
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
            if self.jump_vel < -self.JUMP_VEL:
                self.dino_rect.y = self.Y_POS
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL


    def duck(self):
        if self.type == DBZ_TYPE:
            self.image = DUCK_IMG[self.type][self.step_index //5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.DBZ_POS_DUCK
            self.step_index += 1
        else:
            self.image = DUCK_IMG[self.type][self.step_index //5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS_DUCK
            self.step_index += 1
        
    def check_invicibility(self):
        if self.shield:
            time_shield = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_shield < 0:
                self.shield = False
                self.update_to_defauld(SHIELD_TYPE)

    def H_invicibility(self):
        if self.hammer:
            time_hammer = round((self.hammer_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_hammer < 0:
                self.hammer = False
                self.update_to_defauld(HAMMER_TYPE)

    def dbz_invicibility(self):
        if self.dbz:
            time_dbz = round((self.hammer_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_dbz < 0:
                self.dbz = False
                self.update_to_defauld(DBZ_TYPE)

    def update_to_defauld(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))