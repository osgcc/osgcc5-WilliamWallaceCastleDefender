import pygame
import os
from Vector import *
from math import sqrt

def direction(x, y):
    """Return the direction component of a vector (in radians), given
    cartesian coordinates.
    """
    if x > 0:
        if y >= 0:
            return atan(y / x)
        else:
            return atan(y / x) + TwoPI
    elif x == 0:
        if y > 0:
            return HalfPI
        elif y == 0:
            return 0
        else:
            return OneAndHalfPI
    else:
        return (atan(y / x) + PI) *  57.2957795


class Arrow(pygame.sprite.Sprite):
    def __init__(self,playerX,playerY,mouseX,mouseY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.curdir, 'arrow.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(playerX,playerY)
        self.x = playerX
        self.y = playerY
        diffX = mouseX - playerX
        diffY = mouseY - playerY
        if diffX != 0 and diffY!= 0:
            self.vector = Vector((diffX / sqrt(diffX*diffX + diffY*diffY)), (diffY / sqrt(diffX*diffX + diffY*diffY)))
        self.valid = True
        self.vel = 25
        if self.vector.x > 0:
            self.ArrowObj = pygame.transform.rotate(self.image, 180 + direction(-self.vector.x,self.vector.y))
        else:
            self.ArrowObj = pygame.transform.rotate(self.image, -direction(self.vector.x,self.vector.y))

    def updateArrowPos(self):
        self.x += self.vector.x * self.vel
        self.y += self.vector.y * self.vel
        self.rect = self.rect.move(self.vector.x * self.vel, self.vector.y * self.vel)
        if self.x > 1280 or self.x < 0 or self.y > 720 or self.y < 0:
            return -1
            self.valid = False
        else:
            return 1

