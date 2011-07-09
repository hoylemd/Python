# Project name
# module name
# short description
# by Michael D. Hoyle
# Last modified: 7/9/2011

import pygame 

pygame.init() 
# Set the height and width of the screen
size=[700,500]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("My Game") 

#Loop until the user clicks the close button.
quit=False 

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# Main Program Loop
while !quit==False:

	# Handle events
    for event in pygame.event.get():
		if event.type == pygame.QUIT: # exit
			quit=True

	# Limit to 20 frames per second
    clock.tick(30)     
	
	# update the screen.
	pygame.display.flip()

# Be IDLE friendly.
pygame.quit ()