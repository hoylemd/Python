# Project name
# module name
# short description
# by Michael D. Hoyle
# Last modified: 7/9/2011

# import libraries
import pygame 

# initialize pygame
pygame.init() 

# Set up the window
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My Game") 

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

#Loop until the user clicks the close button.
quit = False

# Main Program Loop
while quit == False:
	
	# Limit to 30 frames per second
	clock.tick(30)	 
	
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # exit
			quit=True

	# Limit to 30 frames per second
	clock.tick(30)	 
	
	# update the screen.
	pygame.display.flip()

# Be IDLE friendly.
pygame.quit ()