#Main
import pygame, sys, os
from pygame.locals import *
from Player import *
from Vector import *


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowSurfaceObj = pygame.display.set_mode((1280,720), DOUBLEBUF)
    pygame.display.set_caption("William Wallce Defender X-Treme 2140")
    desertBackground = pygame.image.load(os.path.join(os.curdir, 'desert-background.jpg')).convert_alpha()
    level = pygame.image.load(os.path.join(os.curdir, 'LEVEL.png')).convert_alpha()
    player = Player()
    pygame.key.set_repeat(1,50)
    #Main Loop
    while True:
        windowSurfaceObj.blit(desertBackground,(0,0))
        windowSurfaceObj.blit(level,(0,0))
        
        mousex = player.x
        mousey = player.y
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                player.updateVector(mousex,mousey)
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if event.button in (1,2,3):
                    blah = "blah"
                    #left, middle, right button
                elif event.button in (4,5):
                    blah = "blah"
                    #scroll up or down
            elif event.type == KEYDOWN:
                x = 0
                y = 0
                if event.key == K_LEFT:
                    x = -10
                if event.key == K_RIGHT:
                    x = 10
                if event.key == K_DOWN:
                    y = 10
                if event.key == K_UP:
                    
                    y = -10
                keystate =  pygame.key.get_pressed()
                if keystate[pygame.locals.K_UP]:
                    y = -10
                if keystate[pygame.locals.K_DOWN]:
                    y = 10
                if keystate[pygame.locals.K_RIGHT]:
                    x = 10
                if keystate[pygame.locals.K_LEFT]:
                    x = -10

                player.updatePlayerPos(x,y)
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
            #else:
        x = 0
        y = 0
        keystate =  pygame.key.get_pressed()
        if keystate[pygame.locals.K_UP]:
            y = -10
        if keystate[pygame.locals.K_DOWN]:
            y = 10
        if keystate[pygame.locals.K_RIGHT]:
            x = 10
        if keystate[pygame.locals.K_LEFT]:
            x = -10
        if(x != 0 or y != 0):
            player.updatePlayerPos(x,y)
        #player.updateVector(mousex,mousey)
        #player.updatePos()
        windowSurfaceObj.blit(player.images[player.image],player.rect)
        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)



if __name__ == '__main__':
    main()
