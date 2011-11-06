#William Wallace himself
import pygame
import os

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path,join(os.curdir, 'wallacetemp.png')).convert()
        self.rect = self.image.get_rect()
        self.vel = 10
        self.x = 0
        self.y = 0
        self.dir = 1 # 1: Right -1: Left

    def updatePos(self,x,y):
        self.rect.move(x,y)



