import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning! Fonts disabled')
if not pygame.mixer: print('Warning! Sound disabled')

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print("Cannot load image: ", name)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
