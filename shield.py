import pygame, os



class Shield(pygame.sprite.Sprite):


    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.framenumber = 0
        self.image = 0
        self.images = [pygame.image.load(os.path.join(os.curdir, 'shield1.png')).convert_alpha(),
                        pygame.image.load(os.path.join(os.curdir, 'shield2.png')).convert_alpha(),
                        pygame.image.load(os.path.join(os.curdir, 'shield3.png')).convert_alpha(),
                        pygame.image.load(os.path.join(os.curdir, 'shield2.png')).convert_alpha()]
        self.rect = self.images[self.image].get_rect()
        
        self.x = x
        self.y = y
        
        self.rect = self.rect.move(x-32,y-32)
        
    def move(self, x, y):
        print self.x
        print self.y
        self.x += x
        self.y += y
        self.framenumber+=0.5
        self.image = (int(self.framenumber)) % 4
        if(self.framenumber > 2):
            return True;
        
        