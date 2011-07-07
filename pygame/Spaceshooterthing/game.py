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
background = pygame.Surface(screen.get-size())
background.fill(colours.black)

# get the game clock
clock = pygame.time.Clock()

# load the sprites
arrow_image = pygame.image.load("img\arrow.png").convert()
circle_image = pygame.image.load("img\circle.png").convert()

