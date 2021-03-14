#!/usr/bin/python3
import pygame
from classes.settings import Settings
from classes.ship import Ship
import classes.game_functions as gf
from pygame.sprite import Group
from classes.alien import Alien
from classes.game_stats import GameStats
from classes.button import Button

# Commands
print("")
print("\033[36m📚 HOW TO PLAY?\033[0m")
print("\033[32m🟢 Click the \"PLAY\" button to start \033[0m")
print("\033[32m🟡 Shoot bullets using the \"SPACE\" KEY\033[0m")
print("\033[32m🟠 Move the ship using LEFT KEY ◀️  and RIGHT KEY ▶️ \033[0m")
print("\033[31m🔴 Press the \"ESCAPE\" KEY on the Alien Invasion screen to end the game! \033[0m")
print("")

def run(mode):
    # Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings(mode)

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")

	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")

	# Create an instance to store game statistics.
	stats = GameStats(ai_settings)

	# Make a ship
	ship = Ship(ai_settings, screen)

	# Make a group to store bullets in.
	bullets = Group()

	# Make a group of aliens.
	aliens = Group()

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	game_over = False

	# Start the main loop for the game
	while not game_over:
		# Watch for the keyboard and mouse events
		gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, mode)

		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
