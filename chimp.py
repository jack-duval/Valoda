import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning! Fonts disabled')
if not pygame.mixer: print('Warning! Sound disabled')

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Cannot load image: ", name)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound: ', name)
        raise SystemExit(message)
    return sound

class First(pygame.sprite.Sprite):
    """Moves a clenched fist on the screen, follows mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('fist.bmp', -1)
        self.punching = 0

    def update(self):
        """Moves the fist based on mouse pos"""
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5,10)
