#!/usr/bin/python3
import time
import pygame
import random

# Screen colors settings
white = (255, 255, 255)
green = (34, 139, 34)
blue = (64, 224, 208)

# Screen resolution: width,height
surface_width = 800
surface_height = 500
surface = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

# Image configuration
img = pygame.image.load('images/flap.png')
img_width = img.get_size()[0]
img_height = img.get_size()[1]
print("")
print("\033[36m📚 HOW TO PLAY?\033[0m")
print("\033[32m🟢 Start moving Flappy Bird with UP KEY 🔼 \033[0m")
print("\033[38;5;214m🟠 Play using UP KEY 🔼 and DOWN KEY 🔽 \033[0m")
print("\033[31m🔴 Press the ESCAPE KEY on the Flappy Bird GAME OVER screen to end the game! \033[0m")
print("")

def run(difficulty):
    pygame.init()

    # Starting Position 
    x = 150
    y = 200
    y_move = 0

    # Blocks configurations
    x_block = surface_width
    y_block = 0
    block_width = 50
    block_height = random.randint(0, surface_height / 2)
    gap = img_height * 5

    # Blocks Speed
    block_move = 4

    score = 0
    game_over = False

    # Game Loop
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            # Keydown - when button is pressed keyup - when it's released
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if difficulty == "EASY":
                        y_move = -2
                    if difficulty == "MEDIUM":
                        y_move = -4
                    if difficulty == "HARD":
                        y_move = -6

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if difficulty == "EASY":
                        y_move = 2
                    if difficulty == "MEDIUM":
                        y_move = 4
                    if difficulty == "HARD":
                        y_move = 6

        y = y + y_move

        surface.fill(blue)
        bird(x, y, img)
        show_score(score)

        # Adding difficulty relative to score
        # Increasing the speed and decreasing the gap of blocks
        
        if 5 <= score < 10:
            block_move = 5
            gap = img_height * 3.3

        if 10 <= score < 15:
            block_move = 6
            gap = img_height * 3.1

        if 15 <= score < 20:
            block_move = 7
            gap = img_height * 3

        if score >= 20:
            block_move = 8
            gap = img_height * 2.5

        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        # Boundaries
        if y > surface_height - img_height or y < 0:
            game_over(difficulty)

        # Blocks on screen or not
        if x_block < (-1 * block_width):
            x_block = surface_width
            block_height = random.randint(0, surface_height / 2)

        # Collision Detection (Screen or Blocks)
        if x + img_width > x_block and x < x_block + block_width:
            if y < block_height or y + img_height > block_height + gap:
                game_over(difficulty)

        if x > x_block + block_width and x < x_block + block_width + img_width / 5:
            score += 1

        pygame.display.update()
        clock.tick(80)
    pygame.quit()

def show_score(current_score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score:' + str(current_score), True, white)
    surface.blit(text, [3, 3])

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, green, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, green, [x_block, y_block + block_height + gap, block_width, surface_height])

def make_text_objs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

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

def msg_surface(text, difficulty):
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    large_text = pygame.font.Font('freesansbold.ttf', 130)

    title_text_surf, title_text_rect = make_text_objs(text, large_text)
    title_text_rect.center = surface_width / 2, surface_height / 2
    surface.blit(title_text_surf, title_text_rect)

    type_text_surf, type_text_rect = make_text_objs('Press ANY KEY to continue or ESC to exit', small_text)
    type_text_rect.center = surface_width / 2, ((surface_height / 2) + 100)
    surface.blit(type_text_surf, type_text_rect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        clock.tick()
    
    run(difficulty)

def game_over(difficulty):
    msg_surface('Game over', difficulty)

def bird(x, y, image):
    surface.blit(image, (x, y))
