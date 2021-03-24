#!/usr/bin/python3
import pygame
from classes.wall import Wall
from classes.block import Block
from classes.player import Player
from classes.ghost import Ghost

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)
yellow   = (255,255,0)

# Commands
print("")
print("\033[36m📚 HOW TO PLAY?\033[0m")
print("\033[32m🟢 Move Pacman using UP KEY 🔼, DOWN KEY 🔽, LEFT KEY ◀️  and RIGHT KEY ▶️ \033[0m")
print("\033[31m🔴 Press the \"ESCAPE\" KEY on the PACMAN GAME OVER screen to end the game! \033[0m")
print("")

#Add music
pygame.mixer.init()
pygame.mixer.music.load('pacman.mp3')
pygame.mixer.music.play(-1, 0.0)

# Default locations for Pacman and Ghosts
w = 303-16 #Width
pacman_height = (7*60)+19
monster_height = (4*60)+19
blinky_height = (3*60)+19
inky_width = 303-16-32
clyde_width = 303+(32-16)

#Pinky movements
Pinky_directions = [
[0,-30,4],
[15,0,9],
[0,15,11],
[-15,0,23],
[0,15,7],
[15,0,3],
[0,-15,3],
[15,0,19],
[0,15,3],
[15,0,3],
[0,15,3],
[15,0,3],
[0,-15,15],
[-15,0,7],
[0,15,3],
[-15,0,19],
[0,-15,11],
[15,0,9]
]

#Blinky movements
Blinky_directions = [
[0,-15,4],
[15,0,9],
[0,15,11],
[15,0,3],
[0,15,7],
[-15,0,11],
[0,15,3],
[15,0,15],
[0,-15,15],
[15,0,3],
[0,-15,11],
[-15,0,3],
[0,-15,11],
[-15,0,3],
[0,-15,3],
[-15,0,7],
[0,-15,3],
[15,0,15],
[0,15,15],
[-15,0,3],
[0,15,3],
[-15,0,3],
[0,-15,7],
[-15,0,3],
[0,15,7],
[-15,0,11],
[0,-15,7],
[15,0,5]
]

#Inky movements
Inky_directions = [
[30,0,2],
[0,-15,4],
[15,0,10],
[0,15,7],
[15,0,3],
[0,-15,3],
[15,0,3],
[0,-15,15],
[-15,0,15],
[0,15,3],
[15,0,15],
[0,15,11],
[-15,0,3],
[0,-15,7],
[-15,0,11],
[0,15,3],
[-15,0,11],
[0,15,7],
[-15,0,3],
[0,-15,3],
[-15,0,3],
[0,-15,15],
[15,0,15],
[0,15,3],
[-15,0,15],
[0,15,11],
[15,0,3],
[0,-15,11],
[15,0,11],
[0,15,3],
[15,0,1],
]

#Clyde movements
Clyde_directions = [
[-30,0,2],
[0,-15,4],
[15,0,5],
[0,15,7],
[-15,0,11],
[0,-15,7],
[-15,0,3],
[0,15,7],
[-15,0,7],
[0,15,15],
[15,0,15],
[0,-15,3],
[-15,0,11],
[0,-15,7],
[15,0,3],
[0,-15,11],
[15,0,9],
]

pl = len(Pinky_directions)-1
bl = len(Blinky_directions)-1
il = len(Inky_directions)-1
cl = len(Clyde_directions)-1

pygame.init()

# Create an 606x606 sized screen
screen = pygame.display.set_mode([606, 606])

# Window Title
pygame.display.set_caption('Pacman')

# Surface Creation
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)

def run():
    startGame()
    pygame.quit()

def startGame():

  all_sprites_list = pygame.sprite.RenderPlain()
  block_list = pygame.sprite.RenderPlain()
  monsta_list = pygame.sprite.RenderPlain()
  pacman_collide = pygame.sprite.RenderPlain()
  wall_list = setupRoomOne(all_sprites_list)
  gate = setupGate(all_sprites_list)

  pinky_turn = 0
  pinky_steps = 0

  blinky_turn = 0
  blinky_steps = 0

  inky_turn = 0
  inky_steps = 0

  clyde_turn = 0
  clyde_steps = 0

  Pacman = Player(w, pacman_height, "images/pacman.png" )
  all_sprites_list.add(Pacman)
  pacman_collide.add(Pacman)

  Blinky = Ghost(w, blinky_height, "images/Blinky.png" )
  monsta_list.add(Blinky)
  all_sprites_list.add(Blinky)

  Pinky = Ghost(w, monster_height, "images/Pinky.png" )
  monsta_list.add(Pinky)
  all_sprites_list.add(Pinky)

  Inky = Ghost(inky_width, monster_height, "images/Inky.png" )
  monsta_list.add(Inky)
  all_sprites_list.add(Inky)

  Clyde = Ghost(clyde_width, monster_height, "images/Clyde.png" )
  monsta_list.add(Clyde)
  all_sprites_list.add(Clyde)

  # Draw the grid
  for row in range(19):
      for column in range(19):
          if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
              continue
          else:
            block = Block(yellow, 4, 4)

            # Set a random location for the block
            block.rect.x = (30*column+6)+26
            block.rect.y = (30*row+6)+26

            b_collide = pygame.sprite.spritecollide(block, wall_list, False)
            p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
            if b_collide:
              continue
            elif p_collide:
              continue
            else:
              # Add the block to the list of objects
              block_list.add(block)
              all_sprites_list.add(block)

  bll = len(block_list)

  score = 0

  done = False

  i = 0

  while done == False:
      # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              done=True

          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT or event.key == ord('a'):
                  Pacman.changespeed(-30,0)
              if event.key == pygame.K_RIGHT or event.key == ord('d'):
                  Pacman.changespeed(30,0)
              if event.key == pygame.K_UP or event.key == ord('w'):
                  Pacman.changespeed(0,-30)
              if event.key == pygame.K_DOWN or event.key == ord('s'):
                  Pacman.changespeed(0,30)

          if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == ord('a'):
                  Pacman.changespeed(30,0)
              if event.key == pygame.K_RIGHT or event.key == ord('d'):
                  Pacman.changespeed(-30,0)
              if event.key == pygame.K_UP or event.key == ord('w'):
                  Pacman.changespeed(0,30)
              if event.key == pygame.K_DOWN or event.key == ord('s'):
                  Pacman.changespeed(0,-30)

      # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
      Pacman.update(wall_list,gate)

      returned = Pinky.changespeed(Pinky_directions, False, pinky_turn, pinky_steps, pl)
      pinky_turn = returned[0]
      pinky_steps = returned[1]
      Pinky.changespeed(Pinky_directions, False, pinky_turn, pinky_steps, pl)
      Pinky.update(wall_list, False)

      returned = Blinky.changespeed(Blinky_directions, False, blinky_turn, blinky_steps, bl)
      blinky_turn = returned[0]
      blinky_steps = returned[1]
      Blinky.changespeed(Blinky_directions, False, blinky_turn, blinky_steps, bl)
      Blinky.update(wall_list, False)

      returned = Inky.changespeed(Inky_directions, False, inky_turn, inky_steps, il)
      inky_turn = returned[0]
      inky_steps = returned[1]
      Inky.changespeed(Inky_directions, False, inky_turn, inky_steps, il)
      Inky.update(wall_list,False)

      returned = Clyde.changespeed(Clyde_directions, "clyde", clyde_turn, clyde_steps, cl)
      clyde_turn = returned[0]
      clyde_steps = returned[1]
      Clyde.changespeed(Clyde_directions, "clyde", clyde_turn, clyde_steps, cl)
      Clyde.update(wall_list,False)

      # See if the Pacman block has collided with anything.
      blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)

      # Check the list of collisions.
      if len(blocks_hit_list) > 0:
          score += len(blocks_hit_list)

      # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
      screen.fill(black)

      wall_list.draw(screen)
      gate.draw(screen)
      all_sprites_list.draw(screen)
      monsta_list.draw(screen)

      text = font.render("Score: " + str(score) + "/" + str(bll), True, red)
      screen.blit(text, [10, 10])

      if score == bll:
        doNext("Congratulations, you won!",145,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)

      monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

      if monsta_hit_list:
        doNext("Game Over",235,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)

      pygame.display.flip()

      clock.tick(10)

# This creates all level 1 walls
def setupRoomOne(all_sprites_list):
    # Make the walls (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()

    # List of walls to display on level.
    # Each is in the form [x, y, width, height]
    walls = [ [0,0,6,600],
              [0,0,600,6],
              [0,600,606,6],
              [600,0,6,606],
              [300,0,6,66],
              [60,60,186,6],
              [360,60,186,6],
              [60,120,66,6],
              [60,120,6,126],
              [180,120,246,6],
              [300,120,6,66],
              [480,120,66,6],
              [540,120,6,126],
              [120,180,126,6],
              [120,180,6,126],
              [360,180,126,6],
              [480,180,6,126],
              [180,240,6,126],
              [180,360,246,6],
              [420,240,6,126],
              [240,240,42,6],
              [324,240,42,6],
              [240,240,6,66],
              [240,300,126,6],
              [360,240,6,66],
              [0,300,66,6],
              [540,300,66,6],
              [60,360,66,6],
              [60,360,6,186],
              [480,360,66,6],
              [540,360,6,186],
              [120,420,366,6],
              [120,420,6,66],
              [480,420,6,66],
              [180,480,246,6],
              [300,480,6,66],
              [120,540,126,6],
              [360,540,126,6]
            ]

    # Loop creating the walls, adding them to the list
    for item in walls:
        wall = Wall(item[0],item[1],item[2],item[3],blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    return wall_list

def setupGate(all_sprites_list):
      gate = pygame.sprite.RenderPlain()
      gate.add(Wall(282,242,42,2,white))
      all_sprites_list.add(gate)
      return gate

def doNext(message,left,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate):
  while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
          if event.key == pygame.K_RETURN:
            del all_sprites_list
            del block_list
            del monsta_list
            del pacman_collide
            del wall_list
            del gate
            startGame()

      # Grey background
      w = pygame.Surface((400,200))  # the size of your rect
      w.set_alpha(10)                # alpha level
      w.fill((128,128,128))          # this fills the entire surface
      screen.blit(w, (100,200))      # (0,0) are the top-left coordinates

      # WON or QUIT
      text1 = font.render(message, True, white)
      screen.blit(text1, [left, 233])

      text2 = font.render("To play again, press ENTER.", True, white)
      screen.blit(text2, [135, 303])
      text3 = font.render("To quit, press ESCAPE.", True, white)
      screen.blit(text3, [165, 333])

      pygame.display.flip()
      clock.tick(10)