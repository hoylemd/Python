# Mouse Practice
# main module
# a few exercises i did to familiarize myself with using the mouse in pygame
# by Michael D. Hoyle
# Last modified: 7/9/2011

# import the libraries
import pygame 
from hutils import colours

# box sprite
class Box(pygame.sprite.Sprite):
	def __init__(self, colour, initial_position):
		# initialize base class
		pygame.sprite.Sprite.__init__(self)
		
		# make the surface
		self.image = pygame.Surface([15,15])
		self.image.fill(colour)
		
		# position it
		self.rect = self.image.get_rect()
		self.rect.topleft = initial_position

# wrapper function to blit a sprite
def drawSprite(s):
	screen.blit(s.image, s.rect)
	
# check if a box exists at the given position
def boxHere(position):
	for b in boxes:
		if b.rect.collidepoint(position):
			return True
	return False
		
# get a box at the current position
def getBoxAt(position):
	for b in boxes:
		if b.rect.collidepoint(position):
			return b
	
	return None

# initialize pygame
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
boxes = []

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
			theBox = getBoxAt(clickPosition)
			if theBox != None:
				boxes.remove(theBox)
			else:
				boxPosition = (clickPosition[0] - 7, clickPosition[1] -7)
				boxes.append(Box(colours.blue, boxPosition))
			

	# render text
	clickPosImage = font.render(str(clickPosition), True, colours.black)
			
	# drawing logic
	# clear screen
	screen.fill(colours.white)
	
	# draw text
	screen.blit(clickPosImage, [0,0])
	
	# draw boxes
	for b in boxes:
		drawSprite(b)
		
	# update the screen.
	pygame.display.flip()

# Be IDLE friendly.
pygame.quit ()