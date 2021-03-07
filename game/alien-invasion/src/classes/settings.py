class Settings():
	"""A class to store all settings for Alien Invasion."""

	def __init__(self, mode):
		"""Initialize the game's settings."""
		self.score = 0

		# Screen settings
		self.screen_configurations()

		# Bullet settings
		self.bullet_configurations(mode)

		# Ship settings
		self.ship_configurations(mode)

		# Alien settings
		self.alien_configurations(mode)

	def screen_configurations(self):
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_color = (0, 0, 0)

	def bullet_configurations(self, mode):
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255, 255, 0
		if mode == "EASY":
			self.bullet_speed_factor = 3
			self.bullets_allowed = 4
		if mode == "MEDIUM":
			self.bullet_speed_factor = 2.5
			self.bullets_allowed = 3
		if mode == "HARD":
			self.bullet_speed_factor = 2
			self.bullets_allowed = 2

	def ship_configurations(self, mode):
		self.ship_limit = 3
		if mode == "EASY":
			self.ship_speed_factor = 1.5
		if mode == "MEDIUM":
			self.ship_speed_factor = 1.25
		if mode == "HARD":
			self.ship_speed_factor = 1

	def alien_configurations(self, mode):
		# fleet_direcion of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		if mode == "EASY":
			self.alien_speed_factor = 0.5
			self.fleet_drop_speed = 9
		if mode == "MEDIUM":
			self.alien_speed_factor = 1
			self.fleet_drop_speed = 10
		if mode == "HARD":
			self.alien_speed_factor = 1.5
			self.fleet_drop_speed = 11
