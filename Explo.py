#AN EXPLOSION
#LOOKS LIKE I'M GONNA HAVE TO JUMP...
import pygame
import os


class Explo(pygame.sprite.Sprite):

    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = 0
        self.framenumber = 0
        if player: 
            self.images = [pygame.image.load(os.path.join(os.curdir, 'pexpl1.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'pexpl2.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'pexpl3.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'pexpl4.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'pexpl5.png')).convert_alpha()]
        else:
            self.images = [pygame.image.load(os.path.join(os.curdir, 'expl1.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'expl2.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'expl3.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'expl4.png')).convert_alpha(),
                          pygame.image.load(os.path.join(os.curdir, 'expl5.png')).convert_alpha()]
        self.rect = self.images[self.image].get_rect()
        self.x = x
        self.y = y
        self.rect = self.rect.move(self.x, self.y)

    def updateEnemySprite(self, framestart, totalframes):
        self.framenumber += 0.5
        if self.framenumber > 5:
            return True
        if(self.framenumber > framestart + totalframes or self.framenumber < framestart):
            self.framenumber = framestart
        self.image = (int(self.framenumber)) % totalframes + framestart

    def updateEnemyPos(self):
        return self.updateEnemySprite(0,5)

    def Hit(self, enemyList, index, dmg):
        self.HP = self.HP - dmg
        if self.HP < 1:
            enemyList.pop(index)
