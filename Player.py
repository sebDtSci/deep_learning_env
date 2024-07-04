from Bot import Bot
import pygame
from dotenv import load_dotenv
import os

load_dotenv()

window_x: int = int(os.getenv("WIN_X"))
window_y: int = int(os.getenv("WIN_Y"))

class Player(Bot):
    def __init__(self, position_spawn:str =True ):
        super().__init__(position_spawn)
        self.player_position_spawn = position_spawn
    
    def move(self, wall, keys):
        new_position = self.danger_position[:]

        if keys[pygame.K_LEFT]:
            new_position[0] -= 10
        if keys[pygame.K_RIGHT]:
            new_position[0] += 10
        if keys[pygame.K_UP]:
            new_position[1] -= 10
        if keys[pygame.K_DOWN]:
            new_position[1] += 10

        if new_position not in [pos for segment in wall for pos in segment]:
            self.danger_position = new_position
        return self.danger_position