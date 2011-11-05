#Main
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowSurfaceObj = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("William Wallce Defender X-Treme 2140")


    #Main Loop
    while True:
        #Not Much here as of now


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
                    blah = "blah"
                    #ARROW KEY
                elif event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        pygame.display.update()
        fpsClock.tick(30)



if __name__ == '__main__':
    main()
