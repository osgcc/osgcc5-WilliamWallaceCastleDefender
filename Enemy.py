#A villianous enemy
import pygame
import os


class Enemy(pygame.sprite.Sprite):

    def __init__(self, right, speed):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 5
        self.image = 0
        self.framenumber = 0
        self.right = right
        self.images = [pygame.image.load(os.path.join(os.curdir, 'groundenemy1.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy2.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy3.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy4.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy5.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy6.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy7.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'groundenemy8.png')).convert_alpha()]
        self.rect = self.images[self.image].get_rect()
        if right == True:
            self.x = 1280
            self.y = 600
            self.speed = -speed
        else:
            self.x = 0
            self.y = 600
            self.speed = speed
        self.rect = self.rect.move(self.x, self.y)

    def updateEnemySprite(self, framestart, totalframes):
        self.framenumber += 0.33
        if(self.framenumber > framestart + totalframes or self.framenumber < framestart):
            self.framenumber = framestart
        self.image = (int(self.framenumber)) % totalframes + framestart

    def updateEnemyPos(self,enemyList, index):
        #self.image = (self.image + 1) % 8
        if(self.right):
            self.updateEnemySprite(4,4)
        else:
            self.updateEnemySprite(0,4)
        if self.x + self.speed < 513 or self.x + self.speed > 745:
            self.x += self.speed
            self.rect = self.rect.move(self.speed,0)
        else:
            enemyList.pop(index)
            return True
        return False

    def Hit(self, enemyList, index, dmg):
        self.HP = self.HP - dmg
        if self.HP < 1:
            enemyList.pop(index)
            return True;
