# Chess
# main module
# play chess!
# by Michael D. Hoyle
# Last modified: 7/9/2011

# import libraries
import pygame 
from hutils import colours
import ChessGraphics
		
# shorthand for blitting a sprite
def drawSprite(theSprite):
	if theSprite != None:
		screen.blit(theSprite.image, theSprite.rect)

# initialize pygame
pygame.init() 

# Set up the window
size=[900,900]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Chess") 

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# generate the game board
board = ChessGraphics.generateBoard()
	
# populate the game board
pieces = ChessGraphics.populateBoard()

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

	# drawing logic
	
	# background
	screen.fill(colours.white)
	
	# draw the board
	for line in board:
		for tile in line:
			drawSprite(tile)
	
	# draw the pieces
	for line in pieces:
		for piece in line:
			drawSprite(piece)
			
	# update the screen.
	pygame.display.flip()

# Be IDLE friendly.
pygame.quit ()