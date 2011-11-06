import pygame, os, random



class PowerUp(pygame.sprite.Sprite):


    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = 0
        self.framenumber=0
        self.images = [pygame.image.load(os.path.join(os.curdir, 'box1.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'box2.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'box3.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'box4.png')).convert_alpha()]
        self.rect = self.images[self.image].get_rect()
        self.x = x
        self.y = y
        self.rect = self.rect.move(x,y)
        x = random.randint(0,100)
        if x < 10:
            self.type = 4
        elif x < 20:
            self.type = 0
        elif x < 50:
            self.type = 3
        elif x < 60:
            self.type = 1
        elif x <= 80:
            self.type = 2
        #0 = Repel
        #1 = Multi Shot 3 Arrows
        #2 = Decoy
        #3 = Heal Castle
        #4 = Piercing rounds

    def updateBoxSprite(self):
        self.framenumber += 0.33
        self.image = (int(self.framenumber)) % 4