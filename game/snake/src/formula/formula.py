#!/usr/bin/python3
import pygame
import sys
import time
import random

# Colors settings
white = (255, 255, 255)
green = (34, 139, 34)
blue = (64, 224, 208)

# Screen configurations
frame_size_x = 800
frame_size_y = 500
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
clock = pygame.time.Clock()

# Commands
print("")
print("\033[36m📚 HOW TO PLAY?\033[0m")
print("\033[32m🟢 Play using UP KEY 🔼, DOWN KEY 🔽, LEFT KEY ◀️  and RIGHT KEY ▶️ \033[0m")
print("\033[31m🔴 Press the ESCAPE KEY on the Snake GAME OVER screen to end the game! \033[0m")
print("")

def run(mode):
    pygame.init()

    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction
    score = 0

    if mode == "EASY":
        difficulty = 10
    if mode == "MEDIUM":
        difficulty = 25
    if mode == "HARD":
        difficulty = 40
    if mode == "HARDER":
        difficulty = 60
    if mode == "HELL":
        difficulty = 100

    # Game Loop/ Game State
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True

        # To display only the snake body
        game_window.fill(blue)

        # Snake body
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
            game_over(mode)
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            game_over(mode)
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over(mode)

        show_score(score, 1, white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        clock.tick(difficulty)

# Game Over
def msg_surface(text, mode):
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    large_text = pygame.font.Font('freesansbold.ttf', 130)

    title_text_surf, title_text_rect = make_text_objs(text, large_text)
    title_text_rect.center = frame_size_x / 2, frame_size_y / 2
    game_window.blit(title_text_surf, title_text_rect)

    type_text_surf, type_text_rect = make_text_objs('Press ANY KEY to continue or ESC to exit', small_text)
    type_text_rect.center = frame_size_x / 2, ((frame_size_y / 2) + 100)
    game_window.blit(type_text_surf, type_text_rect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        clock.tick()

    run(mode)

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                print("➡️  Thank you for using Ritchie CLI! 🆒")
                pygame.quit()
                quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def make_text_objs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def game_over(mode):
    msg_surface('Game over', mode)

def show_score(score, choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
