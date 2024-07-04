import pygame
import time
import os
import random
from dotenv import load_dotenv
from Player import Player
from Bot import Bot


# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les dimensions de la fenêtre depuis les variables d'environnement
window_x: int = int(os.getenv("WIN_X"))
window_y: int = int(os.getenv("WIN_Y"))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
# Initialiser Pygame et configurer la fenêtre
pygame.init()
pygame.display.set_caption('Learning Environment')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

goal_position = [random.randrange(1, (window_x // 10)) * 10,
                 random.randrange(1, (window_y // 10)) * 10]
goal_spawn = True

# Instancier le joueur et plusieurs bots
player = Player()
bots = [Bot() for _ in range(3)]

score = 0

# Générer des segments de murs aléatoires
wall_segments = []
for _ in range(10):
    start_pos = [random.randrange(1, (window_x // 10)) * 10,
                 random.randrange(1, (window_y // 10)) * 10]
    length = random.randint(3, 7)
    direction = random.choice(['H', 'V'])
    segment = []
    for i in range(length):
        if direction == 'H':
            segment.append([start_pos[0] + i * 10, start_pos[1]])
        else:
            segment.append([start_pos[0], start_pos[1] + i * 10])
    wall_segments.append(segment)

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('Courier', 50)
    game_over_surface = my_font.render('Your score : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    # Déplacer le joueur
    player.move(wall_segments, keys)

    # Déplacer chaque bot
    for bot in bots:
        bot.random_move(wall_segments, bots)

    # Obtenir la vision de chaque bot
    for bot in bots:
        vision = bot.get_vision(wall_segments, bots)
        # print(f"Vision du bot à {bot.position}:", vision)  # Afficher la vision de chaque bot

    game_window.fill(black)
    pygame.draw.rect(game_window, white, [player.position[0], player.position[1], 10, 10])
    pygame.draw.rect(game_window, green, [goal_position[0], goal_position[1], 10, 10])
    for bot in bots:
        pygame.draw.rect(game_window, red, [bot.position[0], bot.position[1], 10, 10])
    
    for segment in wall_segments:
        for wall in segment:
            pygame.draw.rect(game_window, blue, [wall[0], wall[1], 10, 10])

    if player.position == goal_position:
        score += 1
        goal_spawn = False

    if player.position in [bot.position for bot in bots]:
        game_over()

    if not goal_spawn:
        goal_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
        goal_spawn = True

    # show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(15)
        
