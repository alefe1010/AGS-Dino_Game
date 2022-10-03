from dino_runner.components.power.powerUP import Powerup
from dino_runner.utils.constants import DBZ_TYPE, ESFERA_DBZ, HAMMER, HAMMER_TYPE, SHIELD, SHIELD_TYPE
from dino_runner.components.power.powerUP import Powerup

class Shield(Powerup):
        
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)

class Hammer(Powerup):
        
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

class Dbz(Powerup):
        
    def __init__(self):
        self.image = ESFERA_DBZ
        self.type = DBZ_TYPE
        super().__init__(self.image, self.type)
