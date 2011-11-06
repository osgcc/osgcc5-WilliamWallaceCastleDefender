#William Wallace himself
import pygame
import os
from Vector import *
from math import sqrt


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.curdir, 'wallacetemp.png')).convert()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(300,300)
        self.vel = 10
        self.x = 330
        self.y = 330
        self.dir = 1 # 1: Right -1: Left
        self.vector = Vector(self.x,self.y)


    def updateVector(self,x,y):
        diffX = x - self.x
        diffY = y - self.y
        if diffX != 0 and diffY!= 0:
            newX = diffX / (sqrt((diffX*diffX)+(diffY*diffY)))
            newY = diffY / (sqrt((diffX*diffX)+(diffY*diffY)))
        else:
            newX = 0
            newY = 0
        temp = Vector(newX,newY)
        self.vector.add(temp)
        if self.vector.x != 0 and self.vector.y != 0:
            self.vector.x = self.vector.x / (sqrt((self.vector.x*self.vector.x)+(self.vector.y*self.vector.y)))
            self.vector.y = self.vector.y / (sqrt((self.vector.x*self.vector.x)+(self.vector.y*self.vector.y)))

    def updatePlayerPos(self,x,y):
        self.x += x
        self.y += y
        self.rect = self.rect.move(x,y)

    def updateArrowPos(self):
        self.x += self.vector.x * self.vel
        self.y += self.vector.y * self.vel
        self.rect = self.rect.move(self.vector.x * self.vel, self.vector.y * self.vel)

