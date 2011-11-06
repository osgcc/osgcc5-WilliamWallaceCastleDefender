#A villianous flying enemy
import pygame, random
import os


class Enemyflying(pygame.sprite.Sprite):

    def __init__(self, right, speed):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 5
        self.image = 0
        self.right = right
        self.framenumber = 0
        self.images = [pygame.image.load(os.path.join(os.curdir, 'flyingenemy1.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy2.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy3.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy4.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy5.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy6.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy7.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy8.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy9.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'flyingenemy10.png')).convert_alpha()
                      ]
        self.images = [pygame.image.load(os.path.join(os.curdir, 'boss1.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss2.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss3.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss4.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss5.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss6.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss7.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss8.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss9.png')).convert_alpha(),
                      pygame.image.load(os.path.join(os.curdir, 'boss10.png')).convert_alpha()
                      ]
        self.rect = self.images[self.image].get_rect()
        if right == True:
            self.x = 1280
            self.y = random.randint(80, 550)
            self.speed = -speed
        else:
            self.x = 0
            self.y = random.randint(80, 550)
            self.speed = speed
        self.rect = self.rect.move(self.x, self.y)

    def updateEnemySprite(self, framestart, totalframes):
        self.framenumber += 0.33
        if(self.framenumber > framestart + totalframes or self.framenumber < framestart):
            self.framenumber = framestart
        self.image = (int(self.framenumber)) % totalframes + framestart

    def updateEnemyPos(self, enemyList, index):
        #self.image = (self.image + 1) % 8
        if(self.right):
            self.updateEnemySprite(5,5)
        else:
            self.updateEnemySprite(0,5)
        if self.x + self.speed < 513 or self.x + self.speed > 745:
            self.x += self.speed
            self.rect = self.rect.move(self.speed,0)
        else:
            enemyList.pop(index)
            return True
        return False

    def swordHit(self, enemyList, index):
        self.HP = slef.HP - 5
        if self.HP < 1:
            enemyList.pop(index)
    def Hit(self, enemyList, index, dmg):
        self.HP = self.HP - dmg
        if self.HP < 1:
            enemyList.pop(index)
            return True;
