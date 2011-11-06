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
        self.image = 17
        self.framenumber = 0
        self.swinging = 4;
        self.gunmode = False;
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(os.path.join(os.curdir, 'spritel1.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel2.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel3.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel4.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel5.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel6.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel7.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spritel8.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter1.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter2.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter3.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter4.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter5.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter6.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter7.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'spriter8.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'jump.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'start.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'bowl.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'bowr.png')).convert_alpha(),
                    ]

        self.rect = self.images[self.image].get_rect()
        self.rect = self.rect.move(300,600)
        self.vel = 0
        self.x = 300
        self.y = 600
        self.dir = 1 # 1: Right -1: Left
        self.vector = Vector(self.x,self.y)
        self.Arrows = 20
        self.ArrowsMax = 20
        self.ArrowsRepl = 0.0
        self.ArrowsReplRate = 0.025
        self.Gravity = 100
        self.GravityRepl = 0.0
        self.RapidFire = False
        self.MultiShot = False
        self.MultiShot2 = False

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
        #self.image = (self.image + 1) % 8
        x = int(x)
        y = int(y)
        #if(x == 0):
        #    if(self.image != 19 and self.image != 18):
        #        self.updatePlayerSprite(17, 1)
        if(self.gunmode):
            self.images[18] = pygame.image.load(os.path.join(os.curdir, 'gunl.png')).convert_alpha()
            self.images[19] = pygame.image.load(os.path.join(os.curdir, 'gunr.png')).convert_alpha()
        if self.x + x < 1252 and self.x + x > -5:
            self.x += x
            self.rect = self.rect.move(x,0)
        if self.y + y < 600 and self.y + y > 0:
            self.y += y
            self.rect = self.rect.move(0,y)
            self.updatePlayerSprite(16,1)
        if self.y + y > 600:
            self.rect = self.rect.move(0,600-self.y)
            #self.updatePlayerSprite(17,1)
            self.y = 600
        if(x < 0):
            self.updatePlayerSprite(0, 8)
        if(x > 0):
            self.updatePlayerSprite(8,8)

    def updatePlayerSprite(self, framestart, totalframes):
        self.framenumber += 0.33
        if(self.framenumber > framestart + totalframes or self.framenumber < framestart):
            self.framenumber = framestart
        self.image = (int(self.framenumber)) % totalframes + framestart

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





