import pygame
import os
import sys
import random as r
from settings import *
from objects import *
import Levels
from Towers import *
from sounds import *
from Menu import Menu

from os import path

game_menu=Menu(screen)

currentScore = 0

pygame.init()
pygame.mixer.init()
pygame.font.init()

pygame.mixer.music.load('sounds/bg_music_0.wav')
pygame.mixer.music.play()

run = True

dir = path.dirname(__file__)

tilePath=[pygame.image.load('images/tiles/tile0.png'), #0
          pygame.image.load('images/tiles/path1.png'), #1
          pygame.image.load('images/tiles/path8.png'), #2
          pygame.image.load('images/tiles/path3.png'), #3
          pygame.image.load('images/tiles/path4.png'), #4
          pygame.image.load('images/tiles/path5.png'), #5
          pygame.image.load('images/tiles/path4.png'), #6
          pygame.image.load('images/tiles/path7.png'), #7
          pygame.image.load('images/tiles/path8.png'), #8
          pygame.image.load('images/tiles/path9.png'), #9

          pygame.image.load('images/tiles/portal.png'),#10

          pygame.image.load('images/tiles/spawn close.png'), #11
          pygame.image.load('images/tiles/spawn open.png')  #12
          ]

road=[]
for a in range(len(tilePath)):
    road.append(Sprite(x,y,tileSize,tileSize,screen,tilePath[a]))

#HUD:
heart=Sprite(0,0,64,64,screen,iconHeart)
coin=iconCoin
coin1=pygame.transform.scale(coin,(20,20))

##Fonts
global font_Main
font_Main=pygame.font.SysFont('Courier New',40,bold=True)
font_Towers=pygame.font.SysFont('Bookman Old Style',20,bold=False)
font_Price=pygame.font.SysFont('Courier New',30,bold=True)
#Tower names:
archer_name=font_Towers.render('Archer Tower',True,(50,50,50))
lightningTower_name=font_Towers.render('Lightning Tower',True,(50,50,50))
fireTower_name=font_Towers.render('Fire Tower',True,(50,50,50))
minigun_name=font_Towers.render('Minigun Tower',True,(50,50,50))
frostTower_name=font_Towers.render('Frost Tower',True,(50,50,50))

##alll Tower Names (text):
tower_names=[archer_name,lightningTower_name,frostTower_name,minigun_name]

button_pressed_icon=Sprite(0,0,128,128,screen,button_pressed)

lvl_random = r.randrange(1,6)

level=Levels.Level(lvl_random,50)

#########################################################################################################
for name in tower_names:
    if tower_names.index(name) % 2 == 0:
        rectX = 1064
    else:
        rectX += 168

    towerIconsPositions.append((rectX,rectY))
    if tower_names.index(name) % 2 != 0:
        rectY += 168
################################################################################################

c1 = 0  # Counter 1
c2 = 0  # Counter 2
# Draw Tiles
for j in level.path:
    for i in j:
        if i == 0:
            tilePositions.append((c1, c2 ))
        c1 += 1
    c1 = 0
    c2+=1

lastWave = False

def drawMap():
    global clickedOnButton
    global selectOn
    global selectedTower
    global towerPositions
    global portalCount
    global ind_range
    liveSurface = font_Main.render(str(level.lives),True, (85, 7, 15))
    coinSurface = font_Main.render(str(level.money),True, (215, 160, 0))

    ##TOWER PRICES
    towerPriceSurface=[font_Price.render("60",True, (215, 160, 0)),
                       font_Price.render("175", True, (215, 160, 0)),
                       font_Price.render("100", True, (215, 160, 0)),
                       font_Price.render("240", True, (215, 160, 0)),
                       ]

    c1 = 0 # Counter 1
    c2 = 0 # Counter 2

    #Draw Tiles
    for j in level.path:
        for i in j:

            if i == 11:
                if level.started:
                    road[i].tile=tilePath[12]
                else:
                    road[i].tile=tilePath[11]
            if mouseX//tileSize==c1 and mouseY//tileSize==c2 and road[i].tile==tilePath[0] and selectOn:
                road[i].tile=pygame.image.load('images/tiles/tile2.png')

            else:
                if i!=11:
                    road[i].tile=tilePath[i]


            road[i].draw(c1 * tileSize, c2 * tileSize)

            c1 += 1
        c1 = 0
        c2 += 1

    ###################################################HUD
    heart.draw(1054,8)#Иконка жизней
    screen.blit(coin,(1228,8))
    #coin.draw(1228,8)#Иконка монет
    screen.blit(liveSurface, (1130, 18)) #Текст жизней
    screen.blit(coinSurface, (1300, 18))#Текст монет

    ####LINES(HUD)
    pygame.draw.line(screen,(0,0,0),(1024,0),(1024,1024),4)#Line main
    pygame.draw.line(screen,(0,0,0),(1024,80),(1400,80),4)#Line horizontal
    pygame.draw.line(screen,(0,0,0),(1212,0),(1212,80),4)#Line vertical

    rectX=1064
    rectY=140

    #Draw Tower icons
    for icon in towerIcons:
        if towerIcons.index(icon)%2==0:
            rectX=1064
            screen.blit(icon,(rectX, rectY))
        else:
            rectX += 168
            screen.blit(icon,(rectX+168,rectY))
        screen.blit(icon, (rectX, rectY))
        screen.blit(icon, (rectX + 168, rectY))


        if towerIcons.index(icon) % 2 != 0:
            rectY +=188

    rectX = 1064
    rectY = 140

    # Текста башен:
    for name in tower_names:
        if tower_names.index(name)%2==0:
            rectX=1064
            screen.blit(name, (rectX, rectY  - 30))#Tower left text
            screen.blit(towerPriceSurface[tower_names.index(name)],(rectX, rectY +156  - 30))#Price left

            screen.blit(coin1, (rectX+60, rectY+162-30))#Coin Icon
            pygame.draw.rect(screen, (0, 0, 0), (rectX, rectY, 128, 128), 4)  # left Tower square
        else:
            rectX += 168
            screen.blit(name, (rectX, rectY - 30))  # Tower right text
            screen.blit(towerPriceSurface[tower_names.index(name)], (rectX, rectY + 156 - 30))#Price right

            screen.blit(coin1, (rectX + 60, rectY + 162 - 30))  # Coin Icon
            pygame.draw.rect(screen, (0, 0, 0), (rectX + 168, rectY, 128, 128),4)  # right Tower square
        pygame.draw.rect(screen, (0, 0, 0), (rectX, rectY , 128, 128), 4)  # left Tower square
        pygame.draw.rect(screen, (0, 0, 0), (rectX + 168, rectY , 128, 128), 4)  # right Tower square


        #Click on Tower icons
        mouseOnButton=(mouseX >= rectX and mouseX <= rectX + 128 and mouseY>=rectY and mouseY<=rectY+128)
        if pygame.mouse.get_pressed()[0]:
            if mouseOnButton:
                button_pressed_icon.draw(rectX,rectY)


        if tower_names.index(name) % 2 != 0:
            rectY +=188

c1 = 0
c2 = 0
for j in level.path:
    for i in j:
        if i == 11:
            spawnX=c1*tileSize
            spawnY=c2*tileSize

        c1 += 1
    c1 = 0
    c2 += 1
##############################################################################################
#TOWERS:                #
#########################

for i in range(len(towerImages)):
    ableTowers=[Tower(surface=screen,type=i,tile=towerImages[i])]
#############################################################################################

def drawTowers():
    for tower in level.towers:

        tower.draw(towerPositions[level.towers.index(tower)][0]*tileSize,\
                   towerPositions[level.towers.index(tower)][1]*tileSize)


#############MOBS:
def create_mobs():
    """"CREATES MOBS"""
    global waves
    waves=[
        [[Unit(x=spawnX,y=spawnY,
               w=80,h=51,
               speed=10,hp=9,
               surface=screen,tile=0,
               walkAnims=flyWalk,dieAnims=0,gold=5) for a in range(25)] ,
         25], #Wave 1

        [[Unit(x=spawnX, y=spawnY,
               w=80, h=51,
               speed=11, hp=14,
               surface=screen, tile=0,
               walkAnims=batWalk, dieAnims=0, gold=7) for a in range(20)],
         20], #Wave2
        [[Unit(x=spawnX, y=spawnY,
                   w=80, h=51,
                   speed=16, hp=20,
                   surface=screen, tile=0,
                   walkAnims=spiderWalk, dieAnims=0, gold=7) for a in range(15)],
             15],#Wave3
        [[Unit(x=spawnX, y=spawnY,
                   w=80, h=51,
                   speed=18, hp=23,
                   surface=screen, tile=0,
                   walkAnims=batWalk, dieAnims=0, gold=8) for a in range(20)],
             20], #Wave4
        [[Unit(x=spawnX, y=spawnY,
                   w=80, h=51,
                   speed=20, hp=25,
                   surface=screen, tile=0,
                   walkAnims=spiderGreenWalk, dieAnims=0, gold=9) for a in range(25)],
             25],#5

        [[Unit(x=spawnX,y=spawnY,
                   w=80,h=51,
                   speed=6,hp=100,
                   surface=screen,tile=0,
                   walkAnims=flyBigWalk,dieAnims=0,gold=50) for a in range(20)] ,
             20],#6

        [[Unit(x=spawnX, y=spawnY,
                   w=80, h=51,
                   speed=19, hp=90,
                   surface=screen, tile=0,
                   walkAnims=batRedWalk, dieAnims=0, gold=11) for a in range(35)],
             35]#7
    ]

create_mobs()

level.waves=waves
print("INIT <LEVEL.WAVES>:",level.waves)

level.wave=waves[0]

SPAWNEVENT=pygame.USEREVENT+1

newTime=pygame.time.get_ticks()

while run:
    clock.tick(FPS)
    td=clock.tick(FPS)
    screen.fill((100,100,90))

    #TIMER , TICKS
    oldTime=newTime
    newTime=pygame.time.get_ticks()
    deltaTime=newTime-oldTime

    if not isMenu:

        #pygame.mouse.get_pressed()
        drawMap()
        drawTowers()
        if level.towers!=[]:
            if level.units!=[]:
                level.attack(deltaTime)

        if selectOn:
            pygame.draw.circle(screen, choiceColor, (mouseX//tileSize*tileSize + 64, mouseY//tileSize*tileSize + 64),
                               Tower(surface=screen,
                                            type=selectedTower,
                                            tile=towerImages[selectedTower]).atk_range,1)

        if level.units:
            level.move()

        if level.units==[]:
            #print("NO UNITS")
            if not isWave:
               # print("NOT IS WAVE")
                if lastWave:
                    #print("LAST WAVE")
                    isMenu=True
                    game_menu.game_finished=True
                    game_menu.bg=bg_finished
                    if currentScore > int(game_menu.scores[game_menu.save_slot]):
                        game_menu.scores[game_menu.save_slot] = currentScore

                        with open(path.join(dir, HS_FILE), 'w') as f:
                            for i in range(5):
                                f.write(str(game_menu.nicknames[i]) + ":" + str(game_menu.scores[i]) + "\n")




        for unit in level.units:
            if unit.i==len(level.trajectory):
                level.units.pop(level.units.index(unit))
                level.lives-=1
                if unit.hp>=30:
                    level.lives-=2
                    if unit.hp>=50:
                        level.lives-=2
                lifeLost.play()
                if level.lives<=0:
                    isMenu=True
                    game_menu.game_finished = True
                    game_menu.bg=bg_game_over
                    if currentScore > int(game_menu.scores[game_menu.save_slot]):
                        game_menu.scores[game_menu.save_slot] = currentScore

                        with open(path.join(dir, HS_FILE), 'w') as f:
                            for i in range(5):
                                f.write(str(game_menu.nicknames[i]) + ":" + str(game_menu.scores[i]) + "\n")



    elif isMenu:
        game_menu.draw()
        isMenu=game_menu.events()

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run=False

        if not isMenu:
            if event.type == pygame.MOUSEMOTION:
                mouseX=event.pos[0]
                mouseY=event.pos[1]

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX=event.pos[0]
                mouseY=event.pos[1]
                mouseDown=True
                mouseUp=False

            if event.type == pygame.MOUSEBUTTONUP:
                mouseX=event.pos[0]
                mouseY=event.pos[1]
                mouseDown=False
                mouseUp=True
                if selectOn:
                    if event.button == 3 or mouseX >= 1024:
                        selectOn = False
                        selectedTower=None
                if event.button==1: #LeftClick
                    if not selectOn:
                        #Clicks on tower-buttons
                        for pos in towerIconsPositions:
                            if mouseX in range(pos[0],pos[0]+tileSize) and \
                                    mouseY in range(pos[1],pos[1]+tileSize):
                                        selectOn=True
                                        selectedTower=towerIconsPositions.index(pos)
                                        break
                        #Click on SPAWN and initiate start event,change wave.
                        if mouseX in range(spawnX,spawnX+128) and \
                            mouseY in range(spawnY,spawnY+128) and not isWave:
                            print("level.waveCount:",level.waveCount)
                            print("waves:",waves)
                            print("len(waves):",len(waves))
                            if level.waveCount>=len(waves):
                                level.waveCount=0
                                print("+1")
                                create_mobs()
                                for wave in waves:
                                    for mob in wave[0]:
                                        randomInt = r.randrange(2)
                                        if randomInt == 1:
                                            mob.speed += mob.speed * r.randrange(5, 7) / 100
                                        else:
                                            mob.hp += mob.hp * r.randrange(5, 7) / 100
                                    print("HP:",wave[0][0].hp)


                                level.waves=waves
                            isWave = True
                            level.started = True
                            pygame.time.set_timer(SPAWNEVENT, 1000)

                            currentScore += 1
                            print("CURRENT SCORE:", currentScore)




                            level.wave=waves[level.waveCount%len(waves)]
                            level.waveCount+=1

                    else:
                        #Build Towers:
                        if (mouseX//128,mouseY//128) in tilePositions \
                                and (mouseX//128,mouseY//128) not in towerPositions:
                            #If enough money:
                            if Tower(surface=screen,
                                     type=selectedTower,
                                     tile=towerImages[selectedTower]).cost<=level.money:

                                towerPositions.append((mouseX//tileSize,mouseY//tileSize))
                                level.towers.append(Tower(surface=screen,
                                                          type=selectedTower,
                                                          tile=towerImages[selectedTower],
                                                            x=(mouseX//tileSize)*128,
                                                            y=(mouseY//tileSize)*128))
                                ind_range=Tower(surface=screen,
                                                          type=selectedTower,
                                                          tile=towerImages[selectedTower]).atk_range
                                level.money-=level.towers[-1].cost
                                selectedTower=None
                                buildSound.play()
                            else:
                                #Play Sound:
                                noMoneySound.play()
                        selectOn=False

            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    isMenu=True
                    break

            if event.type == SPAWNEVENT and isWave:
                if level.max_waves == level.waveCount:
                    lastWave = True
                    print("LASTWAVE")
                if level.wave[1]>0:
                    print("level.wave:",level.wave)
                    print("level.wave[1]:",level.wave[1])
                    level.wave[1]-=1
                    level.spawn()
                    isWave=True

                else:
                    print("SPAWN FINISHED")
                    pygame.time.set_timer(SPAWNEVENT,0)
                    level.started=False
                    isWave=False
                    if level.units!=[]:
                        level.lives+=len(level.units)//7
                        level.money+=20+len(level.units)*10

if currentScore > int(game_menu.scores[game_menu.save_slot]):
    game_menu.scores[game_menu.save_slot] = currentScore

    with open(path.join(dir, HS_FILE), 'w') as f:
        for i in range(5):
            f.write(str(game_menu.nicknames[i]) + ":" + str(game_menu.scores[i]) + "\n")
pygame.quit()





