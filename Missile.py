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


class Missile(pygame.sprite.Sprite):
    def __init__(self,enemyX,enemyY,playerX,playerY,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.curdir, 'laser.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(enemyX,enemyY)
        self.x = enemyX
        self.y = enemyY
        diffX = playerX - enemyX
        diffY = playerY - enemyY
        if diffX != 0 and diffY!= 0:
            self.vector = Vector((diffX / sqrt(diffX*diffX + diffY*diffY)), (diffY / sqrt(diffX*diffX + diffY*diffY)))
        else:
            if diffX == 0:
                if diffY < 0:
                    self.vector = Vector(0,-1)
                elif diffY > 0:
                    self.vector = Vector(0,1)
            elif diffY == 0:
                if diffX < 0:
                    self.vector = Vector(-1,0)
                elif diffX > 0:
                    self.vector = Vector(1,0)
                else:
                    self.vector = Vector(1,0)
        self.valid = True
        self.vel = 5 + speed
        if self.vector.x > 0:
            self.missileObj = pygame.transform.rotate(self.image, 180 + direction(-self.vector.x,self.vector.y))
        else:
            self.missileObj = pygame.transform.rotate(self.image, -direction(self.vector.x,self.vector.y))

    def updateMissilePos(self):
        self.x += self.vector.x * self.vel
        self.y += self.vector.y * self.vel
        self.rect = self.rect.move(self.vector.x * self.vel, self.vector.y * self.vel)
        if self.x > 1280 or self.x < 0 or self.y > 720 or self.y < 0:
            self.valid = False
            return False
        else:
            return True

