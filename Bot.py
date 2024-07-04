import random
from dotenv import load_dotenv
import os

load_dotenv()

window_x:int = int(os.getenv("WIN_X"))
window_y:int = int(os.getenv("WIN_Y"))

class Bot:
    def __init__(self, danger_position_spawn:str =True ):
        self.danger_position = [random.randrange(1, (window_x//10)) * 10,
                                random.randrange(1, (window_y//10)) * 10]
        self.danger_position_spawn = True
    
    def move(self, wall, bot:list[int,int] = None):
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        new_position_danger = self.danger_position[:]
        if direction == 'UP' and self.danger_position[1] > 0:
            new_position_danger[1] -= 10
        elif direction == 'DOWN' and self.danger_position[1] < window_y - 10:
            new_position_danger[1] += 10
        elif direction == 'LEFT' and self.danger_position[0] > 0:
            new_position_danger[0] -= 10
        elif direction == 'RIGHT' and self.danger_position[0] < window_x - 10:
            new_position_danger[0] += 10
        if new_position_danger not in [pos for segment in wall for pos in segment]:
            self.danger_position = new_position_danger

        return self.danger_position
    