#Main
import pygame, sys, os
from pygame.locals import *
from Player import *


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowSurfaceObj = pygame.display.set_mode((1280,720), DOUBLEBUF)
    pygame.display.set_caption("William Wallce Defender X-Treme 2140")
    desertBackground = pygame.image.load(os.path.join(os.curdir, 'desert-background.jpg')).convert()
    player = Player()
    #Main Loop
    while True:
        windowSurfaceObj.blit(desertBackground,(0,0))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if event.button in (1,2,3):
                    blah = "blah"
                    #left, middle, right button
                elif event.button in (4,5):
                    blah = "blah"
                    #scroll up or down
            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                    x = 0
                    y = 0
                    if K_LEFT:
                        x = -1
                    elif K_RIGHT:
                        x = 1
                    if K_UP:
                        y = 1
                    elif K_DOWN:
                        y = -1
                    player.updatePos(x)

                    #ARROW KEY
                elif event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        windowSurfaceObj.blit(player.image,player.rect)
        pygame.display.update()
        #pygame.display.flip()
        fpsClock.tick(30)



if __name__ == '__main__':
    main()
