import pygame
import time
import random
from Danger import Danger
from Goal import Goal
from Friend import Friend

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('Learning Environment')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

bot_position = [100, 50]

goal = Goal()
goal_position = goal.goal_position
goal_position_spawn = goal.goal_position_spawn

danger = Danger()
danger_position = danger.position
danger_position_spawn = danger.danger_position_spawn

friend = Friend()
friend_position = friend.position
friend_position_spawn = friend.friend_position_spawn

score_friend = 0
score_danger = 0

wall_segments = []
for _ in range(10):  # Nombre de segments de murs
    start_pos = [random.randrange(1, (window_x//10)) * 10, 
                 random.randrange(1, (window_y//10)) * 10]
    length = random.randint(3, 7)  # Longueur du segment de mur
    direction = random.choice(['H', 'V']) 
    segment = []
    for i in range(length):
        if direction == 'H':
            segment.append([start_pos[0] + i * 10, start_pos[1]])
        else:
            segment.append([start_pos[0], start_pos[1] + i * 10])
    wall_segments.append(segment)


def show_score(choice, color, font, size):

    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score_friend : ' + str(score_friend) + ' Score_danger : ' + str(score_danger), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
    
def game_over():
    my_font = pygame.font.SysFont('Courier', 50)
    game_over_surface = my_font.render('Your score : ' + str(score_friend), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()
                
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_position_bot = bot_position[:]
    if keys[pygame.K_LEFT] and new_position_bot[0] > 0:
        new_position_bot[0] -= 10
    if keys[pygame.K_RIGHT] and new_position_bot[0] < window_x - 10:
        new_position_bot[0] += 10
    if keys[pygame.K_UP] and new_position_bot[1] > 0:
        new_position_bot[1] -= 10
    if keys[pygame.K_DOWN] and new_position_bot[1] < window_y - 10:
        new_position_bot[1] += 10
    
   
    if new_position_bot not in [pos for segment in wall_segments for pos in segment]:
        bot_position = new_position_bot
    
    danger_position = danger.move(wall_segments, friend_position)
    friend_position = friend.random_move(wall_segments, danger_position)
    
    # vision = danger.get_vision(wall_segments, friend_position)
    # print("Vision:", vision) 
    
    game_window.fill(black)
    pygame.draw.rect(game_window, white, [bot_position[0], bot_position[1], 10, 10])
    pygame.draw.rect(game_window, green, [goal_position[0], goal_position[1], 10, 10])
    pygame.draw.rect(game_window, red, [danger_position[0], danger_position[1], 10, 10])
    pygame.draw.rect(game_window, white, [friend_position[0], friend_position[1], 10, 10])
    for segment in wall_segments:
        for wall in segment:
            pygame.draw.rect(game_window, blue, [wall[0], wall[1], 10, 10])
    
    if bot_position[0] == goal_position[0] and bot_position[1] == goal_position[1]:
        score_friend += 1
        score_danger -= 1
        goal_position_spawn = False
        danger = Danger(False)
    
    if bot_position[0] == danger_position[0] and bot_position[1] == danger_position[1]:
        # game_over()
        score_friend -= 1
        score_danger += 1
        goal_position_spawn = False
        danger = Danger(False)
        
    if not goal_position_spawn:
        goal_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
    if not danger_position_spawn:
        danger_position = [random.randrange(1, (window_x//10)) * 10, 
                           random.randrange(1, (window_y//10)) * 10]
        
        
    goal_position_spawn = True
    danger_position_spawn = True
    
    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(15)
        