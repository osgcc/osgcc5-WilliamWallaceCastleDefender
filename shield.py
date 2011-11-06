import pygame, os



class Shield(pygame.sprite.Sprite):


    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.framenumber = 0
        self.images = [pygame.image.load(os.path.join(os.curdir, 'shield.png')).convert_alpha(),
                        pygame.image.load(os.path.join(os.curdir, 'shield2.png')).convert_alpha(),
                        pygame.image.load(os.path.join(os.curdir, 'shield3.png')).convert_alpha(),
                        pygame.image.load(os.path.join(os.curdir, 'shield2.png')).convert_alpha()]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect = self.rect.move(x,y)
        
    def move(self, x, y):
        self.x += x
        self.y += y
        self.framenumber+=0.5
        if(self.framenumber > 2):
            self.framenumber = 0
        self.image = (int(self.framenumber)) % 3
        