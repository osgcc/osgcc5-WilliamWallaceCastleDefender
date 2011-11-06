#Main
import pygame, sys, os, random
from pygame.locals import *
from Player import *
from Vector import *
from Enemy import *
from Enemyflying import *
from Arrow import *


def main():
    menu = False
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowSurfaceObj = pygame.display.set_mode((1280,720), DOUBLEBUF)
    pygame.display.set_caption("William Wallce Defender X-Treme 2140")
    desertBackground = pygame.image.load(os.path.join(os.curdir, 'desert-background.jpg')).convert_alpha()
    level = pygame.image.load(os.path.join(os.curdir, 'LEVEL.png')).convert_alpha()
    player = Player()
    pygame.key.set_repeat(1,50)
    ArrowList = []

    #Enemy variables
    maxEnemies = 10
    enemyList = []


    if menu == True:
        Menu(menu, windowSurfaceObj, fpsClock, desertBackground)
    #Main Loop
    while True:
        windowSurfaceObj.blit(desertBackground,(0,0))
        windowSurfaceObj.blit(level,(0,0))
        mousex = player.x
        mousey = player.y

        #Enemy code
        enemyGenerator(enemyList, maxEnemies)
        for enemy in enemyList:
            windowSurfaceObj.blit(enemy.images[enemy.image],enemy.rect)
            enemy.updateEnemyPos()

        skipFall = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                player.updateVector(mousex,mousey)
            elif event.type == MOUSEBUTTONUP:
                if event.button in (1,2,3):
                    mousex, mousey = event.pos
                    arrow = Arrow(player.x,player.y,mousex,mousey)
                    ArrowList.append(arrow)
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
                if event.key == K_UP:
                    y = -.5
                keystate =  pygame.key.get_pressed()
                if keystate[pygame.locals.K_UP]:
                    y = -10
                if keystate[pygame.locals.K_RIGHT]:
                    x = 10
                if keystate[pygame.locals.K_LEFT]:
                    x = -10
                #player.updatePlayerPos(x,0)
                if y != 0:
                    player.jet()
                    skipFall = True
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
            #else:
        x = 0
        y = 0
        keystate =  pygame.key.get_pressed()
        if keystate[pygame.locals.K_UP]:
            y = -10
        if keystate[pygame.locals.K_RIGHT]:
            x = 10
        if keystate[pygame.locals.K_LEFT]:
            x = -10
        if(x != 0 or y != 0):
            player.updatePlayerPos(x,0)
        if y != 0:
            player.jet()
            skipFall = True

        #player.updateVector(mousex,mousey)
        #player.updatePos()
        if not skipFall:
            player.fall()

        for i in range(len(ArrowList)):
            chk = ArrowList[i].updateArrowPos()
            if chk:
                ArrowObj = ArrowList[i].ArrowObj
                windowSurfaceObj.blit(ArrowObj, ArrowList[i].rect)

        windowSurfaceObj.blit(player.images[player.image],player.rect)
        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)

#Enemy Function
def enemyGenerator(enemyList, maxEnemies):
    x = random.randint(0, 100)
    if x < 2 and len(enemyList) < maxEnemies: # 2% chance enemy will be generated
        x = random.randint(0,1)
        if x == 1:
            right = True
        else:
            right = False
        speed = random.randint(1, 15)
        if random.randint(0, 100) < 33: # 33% chance enemy will be flying
            enemyList.append(Enemyflying(right, speed))
        else:
            enemyList.append(Enemy(right, speed))

#Menu function
def Menu(menu, windowSurfaceObj, fpsClock, desertBackground):
    redColor = pygame.Color(255,0,0)
    greenColor = pygame.Color(0,255,0)
    blueColor = pygame.Color(0,0,255)
    whiteColor = pygame.Color(255,255,255)

    pygame.mixer.music.load("Menu.mp3")
    pygame.mixer.music.play(-1)

    headSurfaceObj = pygame.image.load('spritel1.png')
    soundObjBounce = pygame.mixer.Sound("select.wav")
    soundObjStart = pygame.mixer.Sound("start.wav")
    soundObjectSelect = pygame.mixer.Sound("click.wav")

    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    fontObj1 = pygame.font.Font('freesansbold.ttf', 40)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 110)
    fontObjT = pygame.font.Font('freesansbold.ttf', 18)

    selection = 1
    menuType = 0

    while menu:
        windowSurfaceObj.blit(desertBackground,(0,0))

        #Top Menu
        if menuType == 0:
            menuTitle1 = fontObj1.render("William Wallace Defender", False,
greenColor)
            menuTitle2 = fontObj2.render("X-TREME 2140", False, redColor)
            if selection == 0:
                menuObjOne = fontObj.render("Play Game", False, redColor)
                menuObjTwo = fontObj.render("How to Play", False, blueColor)
                menuObjThree = fontObj.render("Story", False, blueColor)
                windowSurfaceObj.blit(headSurfaceObj, (450,
250-headSurfaceObj.get_rect().height/4))
            elif selection == 1:
                menuObjOne = fontObj.render("Play Game", False, blueColor)
                menuObjTwo = fontObj.render("How to Play", False, redColor)
                menuObjThree = fontObj.render("Story", False, blueColor)
                windowSurfaceObj.blit(headSurfaceObj, (450,
350-headSurfaceObj.get_rect().height/4))
            else:
                menuObjOne = fontObj.render("Play Game", False, blueColor)
                menuObjTwo = fontObj.render("How to Play", False, blueColor)
                menuObjThree = fontObj.render("Story", False, redColor)
                windowSurfaceObj.blit(headSurfaceObj, (450,
450-headSurfaceObj.get_rect().height/4))

            windowSurfaceObj.blit(menuTitle1,
((1280-menuTitle1.get_rect().width)/2,50))
            windowSurfaceObj.blit(menuTitle2,
((1280-menuTitle2.get_rect().width)/2,120))
            windowSurfaceObj.blit(menuObjOne,
((1280-menuObjOne.get_rect().width)/2,250))
            windowSurfaceObj.blit(menuObjTwo,
((1280-menuObjTwo.get_rect().width)/2,350))
            windowSurfaceObj.blit(menuObjThree,
((1280-menuObjThree.get_rect().width)/2,450))
        #How to play menu
        elif menuType == 1:
            menuTitle = fontObj1.render("How to Play", False, blueColor)
            textLine1 = fontObjT.render("Text goes here", False, blueColor)
            if selection == 0:
                menuObjOne = fontObj.render("Play Game", False, redColor)
                menuObjTwo = fontObj.render("Back to Main Menu", False, blueColor)
                windowSurfaceObj.blit(headSurfaceObj, (150,
670-headSurfaceObj.get_rect().height/4))
            else:
                menuObjOne = fontObj.render("Play Game", False, blueColor)
                menuObjTwo = fontObj.render("Back to Main Menu", False, redColor)
                windowSurfaceObj.blit(headSurfaceObj, (715,
670-headSurfaceObj.get_rect().height/4))

            windowSurfaceObj.blit(menuTitle1,
((1280-menuTitle1.get_rect().width)/2,50))
            windowSurfaceObj.blit(menuTitle2,
((1280-menuTitle2.get_rect().width)/2,120))
            windowSurfaceObj.blit(menuTitle,
((1280-menuTitle.get_rect().width)/2,250))
            windowSurfaceObj.blit(textLine1,
((1280-textLine1.get_rect().width)/2,350))
            windowSurfaceObj.blit(menuObjOne,
((1280-menuObjOne.get_rect().width)/5*1,670))
            windowSurfaceObj.blit(menuObjTwo,
((1280-menuObjTwo.get_rect().width)/5*4,670))
        #Story Menu
        elif menuType == 2:
            menuTitle = fontObj1.render("Story", False, blueColor)
            textLine1 = fontObjT.render("Text goes here", False, blueColor)
            if selection == 0:
                menuObjOne = fontObj.render("Play Game", False, redColor)
                menuObjTwo = fontObj.render("Back to Main Menu", False, blueColor)
                windowSurfaceObj.blit(headSurfaceObj, (150,
670-headSurfaceObj.get_rect().height/4))
            else:
                menuObjOne = fontObj.render("Play Game", False, blueColor)
                menuObjTwo = fontObj.render("Back to Main Menu", False, redColor)
                windowSurfaceObj.blit(headSurfaceObj, (715,
670-headSurfaceObj.get_rect().height/4))

            windowSurfaceObj.blit(menuTitle1,
((1280-menuTitle1.get_rect().width)/2,50))
            windowSurfaceObj.blit(menuTitle2,
((1280-menuTitle2.get_rect().width)/2,120))
            windowSurfaceObj.blit(menuTitle,
((1280-menuTitle.get_rect().width)/2,250))
            windowSurfaceObj.blit(textLine1,
((1280-textLine1.get_rect().width)/2,350))
            windowSurfaceObj.blit(menuObjOne,
((1280-menuObjOne.get_rect().width)/5*1,670))
            windowSurfaceObj.blit(menuObjTwo,
((1280-menuObjTwo.get_rect().width)/5*4,670))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                #Arrow Keys
                if event.key == K_UP or event.key == K_LEFT:
                    soundObjBounce.play()
                    if menuType == 0:
                        selection = (selection - 1) % 3
                    else:
                        selection = (selection - 1) % 2
                if event.key == K_DOWN or event.key == K_RIGHT:
                    soundObjBounce.play()
                    if menuType == 0:
                        selection = (selection + 1) % 3
                    else:
                        selection = (selection + 1) % 2
                #Enter Key
                if event.key == K_RETURN:
                    if selection == 0:
                            menu = False
                    elif menuType == 0:
                        soundObjectSelect.play()
                        menuType = selection
                        selection = 1
                    elif menuType == 1:
                        if selection == 1:
                            soundObjectSelect.play()
                            menuType = 0
                    elif menuType == 2:
                        if selection == 1:
                            soundObjectSelect.play()
                            menuType = 0

        pygame.display.update()
        fpsClock.tick(30)
    pygame.mixer.music.stop()
    soundObjStart.play()

if __name__ == '__main__':
    main()
