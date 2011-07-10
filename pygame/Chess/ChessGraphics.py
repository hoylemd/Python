import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, colour, position):
		# initialize base class
		pygame.sprite.Sprite.__init__(self)
		
		# make the surface
		self.image = pygame.Surface([100,100])
		self.image.fill(colour)
		
		# position it
		self.rect = self.image.get_rect()
		self.rect.topleft = ((position[0]*100)+40,(position[1]*100)+40)

class Piece(pygame.sprite.Sprite):
	def __init__(self, image, colour, rank, initial_position):
		# initialize the base class
		pygame.sprite.Sprite.__init__(self)
		
		# record the game information
		self.colour = colour
		self.rank = rank
		
		# make the surface
		self.image = image
		
		# position it
		self.rect = self.image.get_rect()