#A villianous flying enemy
import pygame, random
import os


class Enemyflying(pygame.sprite.Sprite):

    def __init__(self, right, speed):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 5
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
        if right == True:
            self.x = 1280
            self.y = random.randint(250, 550)
            self.speed = -speed
        else:
            self.x = 0
            self.y = random.randint(250, 550)
            self.speed = speed
        self.rect = self.rect.move(self.x, self.y)


    def updateEnemyPos(self, enemyList, index):
        self.image = (self.image + 1) % 8
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
    def arrowHit(self, enemyList, index):
        self.HP = slef.HP - 2.5
        if self.HP < 1:
            enemyList.pop(index)