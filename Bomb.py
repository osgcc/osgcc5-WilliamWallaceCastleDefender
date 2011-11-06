#Bomb Bomb Bomb

import pygame, os, random



class Bomb(pygame.sprite.Sprite):


    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.curdir, 'bomb.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect = self.rect.move(x,y)