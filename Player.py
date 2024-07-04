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
        self.last_vision = {}
    
    def move(self, wall, keys):
        keys = pygame.key.get_pressed()
        new_position = self.position[:]
        if keys[pygame.K_LEFT] and self.position[0] > 0:
            new_position[0] -= 10
        if keys[pygame.K_RIGHT] and self.position[0] < window_x - 10:
            new_position[0] += 10
        if keys[pygame.K_UP] and self.position[1] > 0:
            new_position[1] -= 10
        if keys[pygame.K_DOWN] and self.position[1] < window_y - 10:
            new_position[1] += 10
        if new_position not in [pos for segment in wall for pos in segment]:
            self.position = new_position
        return self.position
                    
    def god_view(self, wall, bots):
        current_vision = self.get_vision(wall, bots)
        if current_vision != self.last_vision:
            self.last_vision = current_vision
            item_viewed = []
            for direction in current_vision:
                item_viewed.append(direction)
                for item in current_vision[direction]:
                    if item['type'] not in item_viewed:
                        item_viewed.append(item['type'])
            print("Vision:", item_viewed)