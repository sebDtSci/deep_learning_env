from Bot import Bot

class Danger(Bot):
    def __init__(self, danger_position_spawn:str =True ):
        super().__init__(danger_position_spawn)
        self.danger_position_spawn = danger_position_spawn
    
    def move(self, wall, bots: list):
        vision = self.get_vision(wall, bots)
        target_bot_position = self.find_closest_bot(vision)
        # target_bot_position = None
        if target_bot_position:
            self.move_towards(target_bot_position, wall)
        else:
            self.random_move(wall)

        return self.position
    
    
    def move_towards(self, target, wall):
        direction = None
        if target[0] > self.position[0]:
            direction = 'RIGHT'
        elif target[0] < self.position[0]:
            direction = 'LEFT'
        elif target[1] > self.position[1]:
            direction = 'DOWN'
        elif target[1] < self.position[1]:
            direction = 'UP'

        if direction:
            new_position = self.position[:]
            if direction == 'UP':
                new_position[1] -= 10
            elif direction == 'DOWN':
                new_position[1] += 10
            elif direction == 'LEFT':
                new_position[0] -= 10
            elif direction == 'RIGHT':
                new_position[0] += 10

            if new_position not in [pos for segment in wall for pos in segment]:
                self.position = new_position
    