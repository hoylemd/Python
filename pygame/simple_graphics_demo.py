# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

# initialize
pygame.init()

# define some colours
black 	= [  0,  0,  0]
white 	= [255,255,255]
blue	= [  0,  0,255]
green	= [  0,255,  0]
red 	= [255,  0,  0]

# define tau
tau = 6.283185307179586

# set some function shorthands
DrawLine = pygame.draw.line
DrawArc = pygame.draw.arc

# set up font
font = pygame.font.Font(None, 25)

# set heigh and width of screen
size = [400,500]
screen = pygame.display.set_mode(size)

# set caption
pygame.display.set_caption("Professor Craven's Cool game")

# loop until user clicks close
done = False
clock = pygame.time.Clock()
while done == False:

	clock.tick(10) # limit while loop to 10x / second
	
	# event handling
	for event in pygame.event.get(): # examine each event
		if event.type == pygame.QUIT: # user clicked close
			done = True
	
	# drawing logic
	screen.fill(white) # clear screen
	
	# draw line from 0,0 to 100,100 5 px wide
	DrawLine(screen, green, [0,0], [100,100], 5)
	
	# draw more lines
	yOffset = 0
	while yOffset < 100:
		DrawLine(screen, red, [0, 10 + yOffset], [100,110 + yOffset], 5)
		yOffset += 10
		
	# render text into an image
	textImage = font.render("My text", True, black)
	
	# display text image
	screen.blit(textImage, [250,250])
	
	# draw a rectangle
	pygame.draw.rect(screen,black, [20,20,250,100], 2)
	
	# draw an ellipse with a rectangle as the bounds
	pygame.draw.ellipse(screen, black, [20,20,250,100], 2)
	
	# draw some coloured arcs
	anchor = [20,220,250,200]
	DrawArc(screen, black, anchor, 0, tau/4, 2)
	DrawArc(screen, green, anchor, tau/4, tau/2, 2)
	DrawArc(screen, blue, anchor, tau/2, 3 * tau/4, 2)
	DrawArc(screen, red, anchor, 3 * tau/4, tau, 2)
	
	# draw a triangle
	pygame.draw.polygon(screen, black, [[100,100],[0,200],[200,200]],5)
	
	# update the screen
	pygame.display.flip()
	
# be IDLE friendly
pygame.quit()
	