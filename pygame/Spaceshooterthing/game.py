# Practice excercise with pygame to familiarize myself with it
# hoylemd@gmail.com

# import libraries
import pygame

# grab my colours library
from hutils import colours

#initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Shooty practice game excersize thing")
background = pygame.Surface(screen.get_size())
background.fill(colours.black)

# get the game clock
clock = pygame.time.Clock()

# load the sprites
arrow_image = pygame.image.load("img\\arrow.png").convert()
circle_image = pygame.image.load("img\\circle.png").convert()
arrow_image.set_colorkey(colours.white)
circle_image.set_colorkey(colours.white)

# initialize game entities
playerPosition = (150,150)
enemyPosition = (650,450)

# main loop
done = False
while done == False:
	
	# limit updates
	clock.tick(10)

	# handle events
	for event in pygame.event.get():
	
		# clicked the close button
		if event.type == pygame.QUIT:
			done = True
		
		# clicked anywhere else
		if event.type == pygame.MOUSEBUTTONDOWN:
			print "Mouse clicked!"
			playerPosition = pygame.mouse.get_pos()
			
	
	# draw stuff

pygame.quit()