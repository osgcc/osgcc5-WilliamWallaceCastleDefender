#Main
import pygame, sys, os, random
from pygame.locals import *
from Player import *
from Vector import *
from Enemy import *
from Enemyflying import *
from Arrow import *
from Explo import *
from Missile import *

from PowerUp import *
def main():
    menu = False
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowSurfaceObj = pygame.display.set_mode((1280,720), DOUBLEBUF)
    pygame.display.set_caption("William Wallce Defender X-Treme 2140")
    desertBackground = pygame.image.load(os.path.join(os.curdir, 'desert-background.jpg')).convert_alpha()
    level = pygame.image.load(os.path.join(os.curdir, 'LEVEL.png')).convert_alpha()
    player = Player()
    ArrowList = []
    missileList = []

    PowerUpList = []
    #EXPLOSION
    exploList = []

    #Enemy variables
    maxEnemies = 50
    enemyList = []

    #Castle HP
    HP = 100
    points = 0
    if menu == True:
        Menu(menu, windowSurfaceObj, fpsClock, desertBackground)
    pygame.key.set_repeat(1,50)
    playing = True
    gravityLimit = False

    soundObjectExplosion = pygame.mixer.Sound("explosion.wav")
    soundObjectArrow = pygame.mixer.Sound("arrow.wav")
    pygame.mixer.music.load("BackgroundMusic.mp3")
 #   pygame.mixer.music.play(-1)
    #pygame.mixer.music.play(-1)

    gravityLimit = False
    #Main Loop
    LifeUp = 1
    while playing:
        windowSurfaceObj.blit(desertBackground,(0,0))
        windowSurfaceObj.blit(level,(0,0))
        mousex = player.x
        mousey = player.y

        #Enemy code
        enemyGenerator(enemyList, maxEnemies)
        count = len(enemyList) - 1
        while(count >= 0):
            windowSurfaceObj.blit(enemyList[count].images[enemyList[count].image], enemyList[count].rect)
            enx = enemyList[count].x
            eny = enemyList[count].y
            if random.randint(0,100) < 1: #1% chance that an enemy shoots
                if enemyList[count].right:
                    speed = -enemyList[count].speed
                else:
                    speed = enemyList[count].speed
                missileList.append(Missile(enx,eny,player.x,player.y, speed))
            if enemyList[count].updateEnemyPos(enemyList, count):
                HP = HP -5
                if HP < 0:
                    HP = 0
                exploList.append(Explo(enx, eny, False))
                soundObjectExplosion.play()
                if HP == 0:
                    retry = gameOver(points, windowSurfaceObj,fpsClock, desertBackground)
                    playing = False

                exploList.append(Explo(enx, eny, False))
            count = count - 1

        #DRAW EXLPLOSIONS
        count = len(exploList) - 1
        while(count >= 0):
            windowSurfaceObj.blit(exploList[count].images[exploList[count].image], exploList[count].rect)
            if(exploList[count].updateEnemyPos()):
                exploList.pop(count)
            count = count - 1


        skipFall = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                player.updateVector(mousex,mousey)
            elif event.type == MOUSEBUTTONDOWN:
                myx, myy = event.pos
                if(myx < player.x):
                    player.updatePlayerSprite(18,1)
                else:
                    player.updatePlayerSprite(19,1)
            elif event.type == MOUSEBUTTONUP:
                if event.button in (1,2,3):
                    mousex, mousey = event.pos
                    if player.Arrows - 1 >= 0:
                        arrow = Arrow(player.x,player.y+24,mousex,mousey,player.gunmode)
                        ArrowList.append(arrow)
                        if player.MultiShot2:
                            if player.vector.y == 1 and player.vector.x == 0:
                                arrow = Arrow(player.x,player.y+24,mousex,mousey+20,player.gunmode)
                                ArrowList.append(arrow)
                                arrow = Arrow(player.x,player.y+24,mousex,mousey-20,player.gunmode)
                                ArrowList.append(arrow)
                                arrow = Arrow(player.x,player.y+24,mousex,mousey+40,player.gunmode)
                                ArrowList.append(arrow)
                                arrow = Arrow(player.x,player.y+24,mousex,mousey-40,player.gunmode)
                                ArrowList.append(arrow)
                        elif player.MultiShot:
                            arrow = Arrow(player.x,player.y+24,mousex,mousey+30,player.gunmode)
                            ArrowList.append(arrow)
                            arrow = Arrow(player.x,player.y+24,mousex,mousey-30,player.gunmode)
                            ArrowList.append(arrow)
                        soundObjectArrow.play()
                        player.Arrows -= 1

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
                    if player.Gravity - 1 >= 0 and gravityLimit:
                        player.jet()
                        skipFall = True
                        player.Gravity -= 1
                    else:
                        if player.Gravity >= 20:
                            gravityLimit = True
                        else:
                            gravityLimit = False
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
            if player.Gravity - 1 >= 0 and gravityLimit:
                player.jet()
                skipFall = True
                player.Gravity -= 1
            else:
                if player.Gravity >= 20:
                    gravityLimit = True
                else:
                    gravityLimit = False

        #player.updateVector(mousex,mousey)
        #Castle health bar
        pygame.draw.rect(windowSurfaceObj, pygame.Color(255,0,0), (540, 260, 200, 20))
        pygame.draw.rect(windowSurfaceObj, pygame.Color(0,255,0), (540, 260, HP * 2, 20))
        #Display Points
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        pointsSurfaceObj = fontObj.render("Points: " + str(points), False, pygame.Color(255,255,255))
        windowSurfaceObj.blit(pointsSurfaceObj, (windowSurfaceObj.get_rect().width-pointsSurfaceObj.get_rect().width-25, 25))
        #Display Lives
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        pointsSurfaceObj = fontObj.render("Lives: " + str(player.Lives), False, pygame.Color(255,255,255))
        windowSurfaceObj.blit(pointsSurfaceObj,(300,25))
        #Display Arrows and gravity
        arrowsSurfaceObj = fontObj.render("Arrows: " + str(player.Arrows)+"/"+str(player.ArrowsMax), False, pygame.Color(255,255,255))
        gravitySurfaceObj = fontObj.render("Anti-Gravity: " + str(player.Gravity)+"%", False, pygame.Color(255,255,255))
        windowSurfaceObj.blit(arrowsSurfaceObj, (25, 25))
        windowSurfaceObj.blit(gravitySurfaceObj, (25, arrowsSurfaceObj.get_rect().height + 50))
        #player.updatePos()
        if not skipFall:
            player.fall()
        #Arrow Code
        end = len(ArrowList)
        i = end - 1
        while i >= 0:
            chk = ArrowList[i].updateArrowPos()
            if not chk:
                ArrowList.pop(i)
                i = i - 1
            else:
                end = len(enemyList) - 1
                count = end
                chk = True
                while count >= 0:
                    if ArrowList[i].rect.colliderect(enemyList[count].rect):
                        if(not player.gunmode):
                            ArrowList.pop(i)
                            i = i - 1
                        enx = enemyList[count].x
                        eny = enemyList[count].y
                        if(enemyList[count].Hit(enemyList,count,5)):
                            exploList.append(Explo(enx, eny, True))
                            x = random.randint(0,100)
                            #print x
                            if x <= 90:
                                tmp = PowerUp(enx,eny)
                                PowerUpList.append(tmp)
                            soundObjectExplosion.play()
                        points = points + 5
                        if points / LifeUp >= 100:
                            LifeUp += 1
                            player.Lives += 1
                        chk = False
                    count -= 1
                    if i < 0:
                        count = -1
                if chk:
                    ArrowObj = ArrowList[i].ArrowObj
                    windowSurfaceObj.blit(ArrowObj, ArrowList[i].rect)
            i = i - 1

        #Missile Code
        end = len(missileList)
        i = end - 1
        #print str(i)+" "+str(len(missileList))
        while i >= 0:
            chk = missileList[i].updateMissilePos()
            if not chk:
                missileList.pop(i)
                i = i - 1
            else:
                if missileList[i].rect.colliderect(player.rect):
                    exploList.append(Explo(missileList[i].x, missileList[i].y, True))
                    soundObjectExplosion.play()
                    missileList.pop(i)
                    player.Lives -= 1
                    if player.Lives <= 0:
                        gameOver(points, windowSurfaceObj,fpsClock, desertBackground)
                    else:
                        player.ArrowsMax = 20
                        player.ArrowsReplRate = 0.05
                        player.RapidFire = False
                        player.MultiShot = False
                        player.MultiShot2 = False
                        player.gunmode = False
                    chk = False
                if i<0:
                    count = -1
            if chk:
                missileObj = missileList[i].missileObj
                windowSurfaceObj.blit(missileObj, missileList[i].rect)
            i = i -1


        i = len(PowerUpList) - 1
        while i >= 0:
            PowerUpList[i].updateBoxSprite()
            if player.rect.colliderect(PowerUpList[i].rect):
                if PowerUpList[i].type == 0:
                    player.ArrowsMax += 10
                elif PowerUpList[i].type == 1:
                    if player.MultiShot:
                        player.MultiShot2 = True
                    player.MultiShot = True
                elif PowerUpList[i].type == 2:
                    player.ArrowsReplRate += .1
                elif PowerUpList[i].type == 3:
                    if HP + 10 >= 100:
                        HP = 100
                    else:
                        HP += 10
                elif PowerUpList[i].type == 4:
                    player.gunmode = True
                    #soundObjectArrow = pygame.mixer.Sound("laser.wav")
                PowerUpList.pop(i)
            else:
                windowSurfaceObj.blit(PowerUpList[i].images[PowerUpList[i].image], PowerUpList[i].rect)
            i = i - 1
        #check enemy detection with player
        i = len(enemyList) - 1
        while i >= 0:
            if player.rect.colliderect(enemyList[i].rect):
                player.Lives -= 1
                exploList.append(Explo(enemyList[i].x, enemyList[i].y, False))
                enemyList.pop(i)
                if player.Lives <= 0:
                    gameOver(points, windowSurfaceObj,fpsClock, desertBackground)
                else:
                    player.ArrowsMax = 20
                    player.ArrowsReplRate = 0.05
                    player.RapidFire = False
                    player.MultiShot = False
                    player.MultiShot2 = False
                    player.gunmode = False
                i = len(enemyList)
            i = i - 1


        windowSurfaceObj.blit(player.images[player.image],player.rect)
        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)
        if player.Arrows + 1 <= player.ArrowsMax:
            player.ArrowsRepl += player.ArrowsReplRate
            if player.ArrowsRepl >= 1.0:
                player.Arrows += 1
                player.ArrowsRepl = 0.0
        if player.Gravity + 1 <= 100:
            player.GravityRepl += .5
            if player.GravityRepl >= 1.0:
                player.Gravity += 1
                player.GravityRepl = 0.0

    if retry:
        pygame.mixer.music.stop
        main()
    else:
        pygame.quit()

#Game Over Function
def gameOver(points, windowSurfaceObj,fpsClock, desertBackground):
    redColor = pygame.Color(255,0,0)
    blueColor = pygame.Color(0,0,255)

    headSurfaceObj = pygame.image.load('spritel1.png')
    soundObjBounce = pygame.mixer.Sound("select.wav")
    soundObjectSelect = pygame.mixer.Sound("click.wav")

    fontObj = pygame.font.Font('freesansbold.ttf', 110)
    fontObj1 = pygame.font.Font('freesansbold.ttf', 40)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 32)

    menuTitle = fontObj.render("Game Over", False,redColor)
    textObj = fontObj1.render("Congratulations, your high score was "+str(points), False,blueColor)

    selection = 1
    retry = False
    notSelected = True

    pygame.key.set_repeat(1,99999)
    while(notSelected):
        windowSurfaceObj.blit(desertBackground,(0,0))

        if selection == 0:
            selectObj1 = fontObj2.render("Retry", False,redColor)
            selectObj2 = fontObj2.render("Quit", False,blueColor)
            windowSurfaceObj.blit(headSurfaceObj, (175, 670-headSurfaceObj.get_rect().height/4))
        else:
            selectObj1 = fontObj2.render("Retry", False,blueColor)
            selectObj2 = fontObj2.render("Quit", False,redColor)
            windowSurfaceObj.blit(headSurfaceObj, (915, 670-headSurfaceObj.get_rect().height/4))

        windowSurfaceObj.blit(menuTitle,((1280-menuTitle.get_rect().width)/2,50))
        windowSurfaceObj.blit(textObj,((1280-textObj.get_rect().width)/2,250))
        windowSurfaceObj.blit(selectObj1, ((1280-selectObj1.get_rect().width)/5*1,670))
        windowSurfaceObj.blit(selectObj2, ((1280-selectObj2.get_rect().width)/5*4,670))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                #Arrow Keys
                if event.key == K_UP or event.key == K_LEFT:
                    soundObjBounce.play()
                    selection = (selection - 1) % 2
                if event.key == K_DOWN or event.key == K_RIGHT:
                    soundObjBounce.play()
                    selection = (selection - 1) % 2
                #Enter Key
                if event.key == K_RETURN:
                    soundObjectSelect.play()
                    notSelected = False
                    if selection == 0:
                        retry = True
                    else:
                        retry = False

        pygame.display.update()
        fpsClock.tick(30)
    if retry:
        main()
    else:
        pygame.quit()
    #return retry

#Enemy Function
def enemyGenerator(enemyList, maxEnemies):
    x = random.randint(0, 100)
    if x < 3 and len(enemyList) < maxEnemies: # 5% chance enemy will be generated
        x = random.randint(0,1)
        if x == 1:
            right = True
        else:
            right = False
        speed = random.randint(1, 4)
        speed += random.randint(0, 4)
        speed += random.randint(0, 4)
        if random.randint(0, 100) < 50: # 50% chance enemy will be flying
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
