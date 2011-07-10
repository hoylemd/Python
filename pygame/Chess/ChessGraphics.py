import pygame
from hutils import colours

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
	def __init__(self, image, colour, rank, position):
		# initialize the base class
		pygame.sprite.Sprite.__init__(self)
		
		# record the game information
		self.colour = colour
		self.rank = rank
		
		# make the surface
		self.image = image
		
		# position it
		self.rect = self.image.get_rect()
		self.rect.topleft = ((position[0]*100)+40,(position[1]*100)+40)
		
		
# colour switcher
def switchColour(col):
	if col == colours.darkGrey:
		return colours.white;
	elif col == colours.white:
		return colours.darkGrey;
		
def generateBoard():
	board = []
	colour = colours.white
	for x in range(8):
		line = []
		for y in range(8):
			line.append(Tile(colour, [x,y]))
			colour = switchColour(colour)
		colour = switchColour(colour)
		board.append(line)
	return board
		
def populateBoard():
	# initialize lists
	pieces = []
	line = []

	# enumerate ranks
	Pawn = 0
	Rook = 1
	Knight = 2
	Bishop = 3
	Queen = 4
	King = 5

	# enumerate Colours
	Black = 0
	White = 1

	# load graphics
	rankList = ["Pawn","Rook","Knight","Bishop","Queen","King"]
	colourList = ["Black","White"]
	pieceSprites = []
	internalList = []
	for colour in colourList:
		internalList = []
		for rank in rankList:
			filename = "img\\" +colour + "\\" + colour + rank + ".png"
			print "opening " + filename
			image = pygame.image.load(filename).convert()
			image.set_colorkey(colours.green)
			internalList.append(image)
		pieceSprites.append(internalList)
		
	# construct a data version of the board
	boardData = [
		[[Black,Rook],[Black,Knight],[Black,Bishop],[Black,King],[Black,Queen],[Black,Bishop],[Black,Knight],[Black,Rook]],
		[[Black,Pawn],[Black,Pawn],[Black,Pawn],[Black,Pawn],[Black,Pawn],[Black,Pawn],[Black,Pawn],[Black,Pawn]],
		[None,None,None,None,None,None,None,None,],
		[None,None,None,None,None,None,None,None,],
		[None,None,None,None,None,None,None,None,],
		[None,None,None,None,None,None,None,None,],
		[[White,Pawn],[White,Pawn],[White,Pawn],[White,Pawn],[White,Pawn],[White,Pawn],[White,Pawn],[White,Pawn]],
		[[White,Rook],[White,Knight],[White,Bishop],[White,King],[White,Queen],[White,Bishop],[White,Knight],[White,Rook]]
		]
	
	# add the piece sprites
	y = 0
	for bLine in boardData:
		x = 0
		for bPiece in bLine:
			if bPiece != None:
				piece = Piece(pieceSprites[bPiece[0]][bPiece[1]], bPiece[0], bPiece[1], [x,y])
				print "adding " + str(bPiece)
			else:
				piece = None
			line.append(piece)
			x += 1
		y += 1
		pieces.append(line)
		
	return pieces