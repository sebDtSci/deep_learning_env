import random
from dotenv import load_dotenv
import os

load_dotenv()

window_x:int = int(os.getenv("WIN_X"))
window_y:int = int(os.getenv("WIN_Y"))

class Bot:
    def __init__(self, position_spawn:str =True ):
        self.position = [random.randrange(1, (window_x//10)) * 10,
                                random.randrange(1, (window_y//10)) * 10]
        self.position_spawn = position_spawn
    
    def random_move(self, wall, bot:list[int,int] = None):
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        new_position = self.position[:]
        if direction == 'UP' and self.position[1] > 0:
            new_position[1] -= 10
        elif direction == 'DOWN' and self.position[1] < window_y - 10:
            new_position[1] += 10
        elif direction == 'LEFT' and self.position[0] > 0:
            new_position[0] -= 10
        elif direction == 'RIGHT' and self.position[0] < window_x - 10:
            new_position[0] += 10
        if new_position not in [pos for segment in wall for pos in segment]:
            self.position = new_position

        return self.position
    
    def get_vision(self,wall, bots, vision_range:int=10):
        directions = {
            'UP': (0, -10),
            'DOWN': (0, 10),
            'LEFT': (-10, 0),
            'RIGHT': (10, 0)
        }
        vision = {'UP': [], 'DOWN': [], 'LEFT': [], 'RIGHT': []}
        for direction, (dx, dy) in directions.items():
            for step in range(1, vision_range + 1):
                new_x = self.position[0] + step * dx
                new_y = self.position[1] + step * dy

                if [new_x, new_y] in [pos for segment in wall for pos in segment]:
                    vision[direction].append({'position': [new_x, new_y], 'type': 'wall'})
                    break  # Mur rencontré, vision bloquée dans cette direction

                if 0 <= new_x < window_x and 0 <= new_y < window_y:
                    # vision[direction].append([new_x, new_y])
                    # liste de Bots
                    # if [new_x, new_y] in [bot for bot in bots if bot != self.position]:
                    # Un seul Bot
                    if [new_x, new_y] == bots :
                        vision[direction].append({'position': [new_x, new_y], 'type': 'bot'}) 
                        # print("Detected")
                    else:
                        vision[direction].append({'position': [new_x, new_y], 'type': 'empty'})
                else:
                    vision[direction].append({'position': [new_x, new_y], 'type': 'border'})
                    break  # En dehors de la fenêtre

        return vision
    
    def find_closest_bot(self, vision):
        # print(vision)
        for direction in vision:
            # print(direction)
            for item in vision[direction]:
                # print(item)
                if item['type'] == 'bot':
                    return item['position']
        return None