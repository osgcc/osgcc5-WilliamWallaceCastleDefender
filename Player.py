#William Wallace himself
import pygame
import os
from Vector import *
from math import sqrt


class Player(pygame.sprite.Sprite):

    bottom = 630
    left = 0
    right = 720

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = 0
        self.images = [pygame.image.load(os.path.join(os.curdir, 'spritel1.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel2.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel3.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel4.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel5.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel6.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel7.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'spritel8.png')).convert_alpha()]
        self.rect = self.images[self.image].get_rect()
        self.rect = self.rect.move(300,600)
        self.vel = 0
        self.x = 300
        self.y = 600
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
        self.image = (self.image + 1) % 8
        x = int(x)
        y = int(y)
        if self.x + x < 1252 and self.x + x > -5:
            self.x += x
            self.rect = self.rect.move(x,0)
        if self.y + y < 600 and self.y + y > 0:
            self.y += y
            self.rect = self.rect.move(0,y)
        if self.y + y > 600:
            self.rect = self.rect.move(0,600-self.y)
            self.y = 600

    def updateArrowPos(self):
        self.x += self.vector.x * self.vel
        self.y += self.vector.y * self.vel
        self.rect = self.rect.move(self.vector.x * self.vel, self.vector.y * self.vel)

    def jet(self):
        if self.vel <= 0:
            self.vel = 3
        else:
            self.vel *= 1.1
            if self.vel > 10:
                self.vel = 10
        self.updatePlayerPos(0,-self.vel)

    def fall(self):
        self.vel -= 1
        self.updatePlayerPos(0,-self.vel)


    def arrow(self):
        print "hi"



