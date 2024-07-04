import random
from dotenv import load_dotenv
import os

load_dotenv()
window_x:int = int(os.getenv("WIN_X"))
window_y:int = int(os.getenv("WIN_Y"))

class Goal:
    def __init__(self, goal_position_spawn:str =True ):
        self.goal_position = [random.randrange(1, (window_x//10)) * 10,
                                random.randrange(1, (window_y//10)) * 10]
        self.goal_position_spawn = goal_position_spawn
        
    