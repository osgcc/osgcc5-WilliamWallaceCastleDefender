#Main
import pygame, sys, os, random
import math
from pygame.locals import *
from Player import *
from Vector import *
from Enemy import *
from Enemyflying import *
from Arrow import *
from Explo import *
from Missile import *
from Bomb import *
from PowerUp import *
from Shield import *

def main():
    menu = True
    pygame.init()
    deathcounter = 0
    textcounter = 0
    fpsClock = pygame.time.Clock()
    message = ""
    windowSurfaceObj = pygame.display.set_mode((1280,720), DOUBLEBUF)
    pygame.display.set_caption("William Wallace Castle Defender X-Treme 2140")
    soundObjectExplosion = pygame.mixer.Sound('explosion.wav')
    desertBackground = pygame.image.load(os.path.join(os.curdir, 'desert-background.jpg')).convert_alpha()
    SurfaceObjLife = pygame.image.load("life.png")
    level = pygame.image.load(os.path.join(os.curdir, 'LEVEL.png')).convert_alpha()
    player = Player()
    ArrowList = []
    missileList = []
    ShieldList = []
    BombList = []
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

        #DRAW EXLPLOSIONS
        count = len(exploList) - 1
        while(count >= 0):
            windowSurfaceObj.blit(exploList[count].images[exploList[count].image], exploList[count].rect)
            if(exploList[count].updateEnemyPos()):
                exploList.pop(count)
            count = count - 1
        if(textcounter > 0):
                #print message
                textMessage = fontObj.render(str(message), False, pygame.Color(0,0,0))
                windowSurfaceObj.blit(textMessage, ((1280-textMessage.get_rect().width)/2*1,670))
                textcounter -= 1
        if(deathcounter > 0):
            if(player.Lives <= 0):
                player.fall()
                player.updatePlayerSprite(21,1)
            else:
                player.updatePlayerSprite(20,1)
            deathcounter -= 1
            windowSurfaceObj.blit(player.images[player.image],player.rect)
            pygame.display.flip()
            fpsClock.tick(30)

        else:
            if(player.Lives <= 0):
                retry = gameOver(points, windowSurfaceObj,fpsClock, desertBackground)
                playing = False
            #Enemy code
            enemyGenerator(enemyList, maxEnemies,points)
            count = len(enemyList) - 1
            while(count >= 0):
                windowSurfaceObj.blit(enemyList[count].images[enemyList[count].image], enemyList[count].rect)


                enx = enemyList[count].x
                eny = enemyList[count].y
                chance = 1
                if enemyList[count].boss:
                    chance = 5
                if random.randint(0,100) < chance: #1% chance that an enemy shoots
                    if enemyList[count].right:
                        speed = -enemyList[count].speed
                    else:
                        speed = enemyList[count].speed
                    tmp = random.randint(0,100)
                    if player.DecoyCounter > 0:
                        playerX = player.DecoyX
                        playerY = player.DecoyY
                    else:
                        playerX = player.x
                        playerY = player.y
                    if enemyList[count].boss:
                        for i in range(0,30):
                            m = Missile(enx+random.randint(-180,180),eny+random.randint(-180,180),player.x+random.randint(-180,180),player.y+random.randint(-180,180),speed)
                            missileList.append(m)
                    elif tmp < 30:
                        m = Missile(enx,eny,playerX,playerY+20, speed)
                        missileList.append(m)
                        m = Missile(enx,eny,playerX,playerY, speed)
                        missileList.append(m)
                        m = Missile(enx,eny,playerX,playerY-20, speed)
                        missileList.append(m)
                    elif tmp < 50:
                        m = Missile(enx,eny,playerX,playerY+20, speed)
                        missileList.append(m)
                        m = Missile(enx,eny,playerX,playerY, speed)
                        missileList.append(m)
                        m = Missile(enx,eny,playerX,playerY-20, speed)
                        missileList.append(m)
                        m = Missile(enx,eny,playerX,playerY+40, speed)
                        missileList.append(m)
                        m = Missile(enx,eny,playerX,playerY-40, speed)
                        missileList.append(m)
                    else:
                        missileList.append(Missile(enx,eny,playerX,playerY, speed))
                if enemyList[count].updateEnemyPos(enemyList, count):
                    HP = HP - 2
                    if HP < 0:
                        HP = 0
                    exploList.append(Explo(enx, eny, False))
                    soundObjectExplosion.play()
                    if HP == 0:
                        retry = gameOver(points, windowSurfaceObj,fpsClock, desertBackground)
                        playing = False

                    exploList.append(Explo(enx, eny, False))
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
                        #if player.Arrows - 1 >= 0:
                        if 1:
                            arrow = Arrow(player.x,player.y+24,mousex,mousey,player.gunmode)
                            ArrowList.append(arrow)
                            if player.MultiShot2:
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
                            #player.Arrows -= 1

                        #left, middle, right button
                    elif event.button in (4,5):
                        blah = "blah"
                        #scroll up or down
                elif event.type == KEYDOWN:
                    x = 0
                    y = 0
                    if event.key == K_SPACE:
                        if player.Repel > 0:
                            ShieldList.append(Shield(player.x, player.y))
                            player.Repel -= 1

                        #rep = pygame.image.load("pexpl1.png")
                        #windowSurfaceObj.blit(rep,rep.get_rect())
                            for i in range(0,len(missileList)):
                                missXp = missileList[i].x
                                missYp = missileList[i].y

                                diffX = missileList[i].x - player.x
                                diffY = missileList[i].y - player.y

                                if diffX != 0 and diffY!= 0:
                                    missileList[i].vector = Vector((diffX / sqrt(diffX*diffX + diffY*diffY)), (diffY / sqrt(diffX*diffX + diffY*diffY)))
                                else:
                                    if diffX == 0:
                                        if diffY < 0:
                                            missileList[i].vector = Vector(0,-1)
                                        elif diffY > 0:
                                            missileList[i].vector = Vector(0,1)
                                    elif diffY == 0:
                                        if diffX < 0:
                                            missileList[i].vector = Vector(-1,0)
                                        elif diffX > 0:
                                            missileList[i].vector = Vector(1,0)
                                    else:
                                        missileList[i].vector = Vector(1,0)
                                missileList[i].vel = 15
                    if event.key == K_LSHIFT:
                        if player.DecoyNum > 0:
                            player.Decoy(player.x,player.y)
                            player.DecoyNum -= 1

                    if event.key == K_LEFT or event.key == K_a:
                        x = -10
                    if event.key == K_RIGHT or event.key == K_d:
                        x = 10
                    if event.key == K_UP or event.key == K_w:
                        y = -.5
                    keystate =  pygame.key.get_pressed()
                    if keystate[pygame.locals.K_UP] or keystate[pygame.locals.K_w]:
                        y = -10
                    if keystate[pygame.locals.K_RIGHT] or keystate[pygame.locals.K_d]:
                        x = 10
                    if keystate[pygame.locals.K_LEFT] or keystate[pygame.locals.K_a]:
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
            if keystate[pygame.locals.K_UP] or keystate[pygame.locals.K_w]:
                y = -10
            if keystate[pygame.locals.K_RIGHT] or keystate[pygame.locals.K_d]:
                x = 10
            if keystate[pygame.locals.K_LEFT] or keystate[pygame.locals.K_a]:
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
            livesSurfaceObj = fontObj.render("Lives:", False, pygame.Color(255,255,255))
            windowSurfaceObj.blit(livesSurfaceObj,(300,25))
            for i in range(0, player.Lives):
                windowSurfaceObj.blit(SurfaceObjLife,(300+livesSurfaceObj.get_rect().width +(i*(SurfaceObjLife.get_rect().width+25)),25-SurfaceObjLife.get_rect().height/4))
            #Display Arrows and gravity
            decoysSurfaceObj = fontObj.render("Decoys: " + str(player.DecoyNum), False,pygame.Color(255,255,255))
            #arrowsSurfaceObj = fontObj.render("Arrows: " + str(player.Arrows)+"/"+str(player.ArrowsMax), False, pygame.Color(255,255,255))
            #gravitySurfaceObj = fontObj.render("Anti-Gravity: ", False, pygame.Color(255,255,255))
            windowSurfaceObj.blit(decoysSurfaceObj,(40,15))
            repelSurfaceObj = fontObj.render("Repels: " + str(player.Repel), False,pygame.Color(255,255,255))
            windowSurfaceObj.blit(repelSurfaceObj,(40,70))

            pygame.draw.rect(windowSurfaceObj, pygame.Color(255,255,0), (20, 120, 200, 20))
            pygame.draw.rect(windowSurfaceObj, pygame.Color(255,0,0), (20, 120, 40, 20))
            pygame.draw.rect(windowSurfaceObj, pygame.Color(0,255,0), (20, 120, player.Gravity*2, 20))
            #windowSurfaceObj.blit(arrowsSurfaceObj, (25, 25))
            #windowSurfaceObj.blit(gravitySurfaceObj, (25, arrowsSurfaceObj.get_rect().height + 50))
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
                                exploList.append(Explo(enx, eny, False))
                                x = random.randint(0,100)
                                #print x
                                if x <= 25:
                                    tmp = PowerUp(enx,eny)
                                    PowerUpList.append(tmp)
                                elif x > 95:
                                    b = Bomb(enx,eny)
                                    BombList.append(b)
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

            #Bomb Code
            i = len(BombList) - 1
            while i >= 0:
                if BombList[i].rect.colliderect(player.rect):
                    killAllEnemies(enemyList, exploList, soundObjectExplosion)
                    #deathcounter=45
                    points = points + 30
                    if points / LifeUp >= 100:
                        LifeUp += 1
                        player.Lives += 1
                    for i in range(0,60):
                        x = random.randint(0,1280)
                        y = random.randint(0,720)
                        z = random.randint(0,1)
                        exploList.append(Explo(x, y, z))
                    BombList = []
                    missileList = []
                    arrowList = []
                    i = -1
                else:
                    windowSurfaceObj.blit(BombList[i].image, BombList[i].rect)
                i = i - 1


            #Missile Code
            end = len(missileList)
            i = end - 1

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
                        #i = i - 1
                        if player.Lives <= 0 and playing == True:
                            killAllEnemies(enemyList, exploList, soundObjectExplosion)
                            deathcounter=70
                        else:
                            i = -1
                            player.ArrowsMax = 20
                            player.ArrowsReplRate = 0.05
                            missileList = []
                            arrowList = []
                            #TODO
                            killAllEnemies(enemyList, exploList, soundObjectExplosion)
                            deathcounter=45
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
                i = i - 1


            i = len(PowerUpList) - 1
            while i >= 0:
                PowerUpList[i].updateBoxSprite()
                if player.rect.colliderect(PowerUpList[i].rect):
                    if PowerUpList[i].type == 0:
                        player.Repel += 1
                        message = "Repel!"
                        textcounter = 120
                    elif PowerUpList[i].type == 1:
                        if player.MultiShot:
                            player.MultiShot2 = True
                        player.MultiShot = True
                        message = "Multi Shot!"
                        textcounter = 120
                    elif PowerUpList[i].type == 2:
                        player.DecoyNum += 1
                        message = "Decoy!"
                        textcounter = 120
                    elif PowerUpList[i].type == 3:
                        if HP + 10 >= 100:
                            HP = 100
                        else:
                            HP += 10
                        message = "Castle HP restored!"
                        textcounter = 120
                    elif PowerUpList[i].type == 4:
                        player.gunmode = True
                        message = "Piercing bullets!"
                        textcounter = 120
                        soundObjectArrow = pygame.mixer.Sound("gun.wav")
                    PowerUpList.pop(i)
                else:
                    windowSurfaceObj.blit(PowerUpList[i].images[PowerUpList[i].image], PowerUpList[i].rect)
                i = i - 1
            #check enemy detection with player
            i = len(enemyList) - 1
            while i >= 0:
                if player.rect.colliderect(enemyList[i].rect):
                    player.Lives -= 1
                    exploList.append(Explo(enemyList[i].x, enemyList[i].y,True))
                    soundObjectExplosion.play()
                    exploList.append(Explo(enemyList[i].x, enemyList[i].y, True))
                    enemyList.pop(i)
                    if player.Lives <= 0 and playing == True:
                        killAllEnemies(enemyList, exploList, soundObjectExplosion)
                        deathcounter=70
                    else:
                        player.ArrowsMax = 20
                        player.ArrowsReplRate = 0.05
                        killAllEnemies(enemyList, exploList, soundObjectExplosion)
                        deathcounter=45
                        missileList=[]
                        arrowsList=[]
                        player.RapidFire = False
                        player.MultiShot = False
                        player.MultiShot2 = False
                        player.gunmode = False
                    i = len(enemyList)
                i = i - 1


            windowSurfaceObj.blit(player.images[player.image],player.rect)
            player.DecoyCounter -= 5
            if player.DecoyCounter > 0:
                windowSurfaceObj.blit(player.images[21],(player.DecoyX,player.DecoyY))
            #DRAW SHIELD
            count = len(ShieldList) - 1
            while(count >= 0):
                windowSurfaceObj.blit(ShieldList[count].images[ShieldList[count].image], ShieldList[count].rect)
                ShieldList[count].x = player.x
                ShieldList[count].y = player.y

                if(ShieldList[count].move(0,0)):
                    ShieldList.pop(count)
                count = count - 1


            #pygame.display.update()
            pygame.display.flip()
            fpsClock.tick(30)
            #if player.Arrows + 1 <= player.ArrowsMax:
            #    player.ArrowsRepl += player.ArrowsReplRate
             #   if player.ArrowsRepl >= 1.0:
             #       player.Arrows += 1
              #      player.ArrowsRepl = 0.0
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

def killAllEnemies(enemyList, exploList, soundObjectExplosion):
    count = len(enemyList) - 1
    while(count >= 0):
        enx = enemyList[count].x
        eny = enemyList[count].y
        exploList.append(Explo(enx, eny, False))
        soundObjectExplosion.play()
        enemyList[count].Hit(enemyList, count, 50)
        count = count - 1


#Game Over Function
def gameOver(points, windowSurfaceObj,fpsClock, desertBackground):
    redColor = pygame.Color(255,0,0)
    blueColor = pygame.Color(0,0,255)

    headSurfaceObj = pygame.image.load('dead.png')
    soundObjBounce = pygame.mixer.Sound("select.wav")
    soundObjectSelect = pygame.mixer.Sound("click.wav")
    menubkg = pygame.image.load(os.path.join(os.path.curdir, 'braveheart.jpg')).convert_alpha()
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
        windowSurfaceObj.blit(menubkg,(0,0))

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
    return retry

#Enemy Function
def enemyGenerator(enemyList, maxEnemies,points):
    x = random.randint(0, 100)
    tmp = points
    if points < 75:
        tmp = 75
    if x < (2*tmp/75) and len(enemyList) < maxEnemies: # chance enemy will be generated
        x = random.randint(0,1)
        if x == 1:
            right = True
        else:
            right = False
        speed = random.randint(1, 4)
        speed += random.randint(0, 4)
        speed += random.randint(0, 4)
        if random.randint(0, 100) < 50: # 50% chance enemy will be flying
            e = Enemyflying(right,speed)
            if random.randint(0,20) < 2 * math.ceil(points/100):
                e.boss = True
                e.speed = 8
            else:
                e.boss = False
            enemyList.append(e)
            #enemyList.append(Enemyflying(right, speed))
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

    headSurfaceObj = pygame.image.load('start.png')
    soundObjBounce = pygame.mixer.Sound("select.wav")
    soundObjStart = pygame.mixer.Sound("start.wav")
    soundObjectSelect = pygame.mixer.Sound("click.wav")
<<<<<<< HEAD
    menubg = pygame.image.load(os.path.join(os.path.curdir, 'braveheart.jpg')).convert_alpha()
    shift = pygame.image.load(os.path.join(os.path.curdir, 'shift.png')).convert_alpha()
    arrowkeys = pygame.image.load(os.path.join(os.path.curdir, 'arrowkeys.png')).convert_alpha()
    wasd = pygame.image.load(os.path.join(os.path.curdir, 'wasd.png')).convert_alpha()
    space = pygame.image.load(os.path.join(os.path.curdir, 'space.png')).convert_alpha()

    tmp = arrowkeys.get_rect()
    wasd = pygame.transform.scale(wasd,(tmp.width,tmp.height))
    tmp = shift.get_rect()
    shift = pygame.transform.scale(shift,(tmp.width/6,tmp.height/6))
    tmp = space.get_rect()
    space = pygame.transform.scale(space,(tmp.width/7,tmp.height/7))
=======
    menubkg = pygame.image.load(os.path.join(os.path.curdir, 'braveheart.jpg')).convert_alpha()
>>>>>>> origin/master

    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    fontObj1 = pygame.font.Font('freesansbold.ttf', 40)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 110)
    fontObjT = pygame.font.Font('freesansbold.ttf', 22)

    selection = 1
    menuType = 0

    while menu:
        windowSurfaceObj.blit(menubkg,(0,0))

        #Top Menu
        if menuType == 0:
            menuTitle1 = fontObj1.render("William Wallace Castle Defender", False,
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
            textLine1 = fontObjT.render("Use for Movement", False, blueColor)
            textLine2 = fontObjT.render("Press Up to Use Anti-Gravity Boots", False, blueColor)
            textLine3 = fontObjT.render("Press For Decoy (3 to use)", False, blueColor)
            textLine4 = fontObjT.render("Press to Repel Enemy Fire (3 to use)", False, blueColor)
            textLine5 = fontObjT.render("Defend the castle, you will find powerups on the way", False, blueColor)
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
((1280-textLine1.get_rect().width)/2+50,325))
            windowSurfaceObj.blit(textLine2,
((1280-textLine2.get_rect().width)/2+50,375))
            windowSurfaceObj.blit(textLine3,
((1280-textLine3.get_rect().width)/2-150,500))
            windowSurfaceObj.blit(textLine4,(750,575))
            windowSurfaceObj.blit(textLine5,
((1280-textLine5.get_rect().width)/2,625))
            windowSurfaceObj.blit(arrowkeys,(75,300))
            windowSurfaceObj.blit(wasd,(300,300))
            windowSurfaceObj.blit(shift,(75,475))
            windowSurfaceObj.blit(space,(700,475))
            windowSurfaceObj.blit(menuObjOne,
((1280-menuObjOne.get_rect().width)/5*1,670))
            windowSurfaceObj.blit(menuObjTwo,
((1280-menuObjTwo.get_rect().width)/5*4,670))
        #Story Menu
        elif menuType == 2:
            menuTitle = fontObj1.render("Story", False, blueColor)
<<<<<<< HEAD
            textLine1 = fontObjT.render("It was 2139 when the meteors fell. ",False, greenColor)
            textLine2 = fontObjT.render("Sir William Wallace stood over his once great kingdom",False, greenColor)
            textLine3 = fontObjT.render("and marveled at what had happened", False, greenColor)
            textLine4 = fontObjT.render("In 2140, the machines invaded...", False, greenColor)
=======
            textLine1 = fontObjT.render("Text goes here", False, blueColor)
>>>>>>> origin/master
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
            windowSurfaceObj.blit(textLine2,
((1280-textLine2.get_rect().width)/2,380))
            windowSurfaceObj.blit(textLine3,
((1280-textLine3.get_rect().width)/2,410))
            windowSurfaceObj.blit(textLine4,
((1280-textLine4.get_rect().width)/2,440))
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
