import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Ave(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type, 'ave')
        if self.type <= 1:
            self.rect.y = 260
 