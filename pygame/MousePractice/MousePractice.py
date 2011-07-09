# Mouse Practice
# main module
# a few exercises i did to familiarize myself with using the mouse in pygame
# by Michael D. Hoyle
# Last modified: 7/9/2011

# import the libraries
import pygame 
from hutils import colours

pygame.init() 

# Set the height and width of the screen
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My Game") 

# set up the font
font = pygame.font.Font(None, 25)

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# game variables
clickPosition = (0,0)


#Loop until the user clicks the close button.
quit=False 

# Main Program Loop
while quit == False:

	# Limit to 30 frames per second
	clock.tick(30)

	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # exit
			quit=True
		if event.type == pygame.MOUSEBUTTONDOWN: # click
			clickPosition = pygame.mouse.get_pos()	

	# render text
	clickPosImage = font.render(str(clickPosition), True, colours.black)
			
	# drawing logic
	# clear screen
	screen.fill(colours.white)
	
	# draw text
	screen.blit(clickPosImage, [0,0])
	
	# update the screen.
	pygame.display.flip()

# Be IDLE friendly.
pygame.quit ()