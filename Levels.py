import pygame
import random as r
from sounds import moneyFall
########Reserved Numbers:
########1,2,3,4,5,6,7,8,9,0

##10 = portal

##11 = spawn
tileSize=128
path1= (
    (0,0,0,0,10,0,0,0),
    (0,0,0,0,8,0,0,0),
    (0,0,7,4,3,0,0,0),
    (0,0,8,0,0,0,0,0),
    (0,0,1,4,4,4,9,0),
    (0,0,0,0,0,0,8,0),
    (0,0,0,7,4,4,3,0),
    (0,0,0,11,0,0,0,0)
       )

trajectory1=((1,'up'),(3,'right'),(2,'up'),(4,'left'),(2,'up'),(2,'right'),(2,'up'))

path2=(
    (0,0,11,0,0,0,0,0),
    (0,0,2,0,0,0,0,0),
    (0,0,1,4,4,9,0,0),
    (0,0,0,0,0,2,0,0),
    (0,0,7,4,4,5,4,10),
    (0,0,2,0,0,2,0,0),
    (0,0,1,4,4,3,0,0),
    (0,0,0,0,0,0,0,0)
)

trajectory2=((2,'down'),(3,'right'),(4,'down'),(3,'left'),(2,'up'),(5,'right'))

path3=(
    (0,0,0,0,0,0,0,0),
    (0,0,0,7,4,4,4,11),
    (0,0,0,2,0,0,0,0),
    (0,0,0,1,4,4,9,0),
    (0,0,0,0,0,0,8,0),
    (0,7,4,4,4,4,3,0),
    (0,1,4,4,9,0,0,0),
    (0,0,0,0,10,0,0,0)
)

trajectory3=(4,'left'),(2,'down'),(3,'right'),(2,'down'),(5,'left'),(1,'down'),(3,'right'),(1,'down')

path4=(
    (0,7,4,4,9,0,0,0),
    (0,2,0,0,1,9,0,11),
    (0,2,0,0,0,2,0,2),
    (0,1,9,0,7,3,0,2),
    (0,0,2,0,2,0,0,2),
    (0,0,2,0,1,4,4,3),
    (10,4,3,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

trajectory4=((4,'down'),(3,'left'),(2,'up'),(1,'right'),(2,'up'),(1,'left'),(1,'up'),
             (3,'left'),(3,'down'),(1,'right'),(3,'down'),(2,'left'))

path5=(
    (0,0,0,0,10,0,0,0),
    (11 ,4,9,0,1,4,9,0),
    (0,0,8,0,0,0,8,0),
    (7 ,4,5,4,9,0,8,0),
    (8 ,0,8,0,8,0,8,0),
    (8 ,0,1,4,3,0,8,0),
    (8 ,0,0,0,0,0,8,0),
    (1,4,4,4,4,4, 3,0)
)

trajectory5=((2,'right'),(4,'down'),(2,'right'),(2,'up'),(4,'left'),(4,'down'),
             (6,'right'),(6,'up'),(2,'left'),(1,'right'))

#max_waves=(7,5,5,5,5)
path = (path1,path2,path3,path4,path5)
trajectory = (trajectory1,trajectory2,trajectory3,trajectory4,trajectory5)

SHOOTEVENT=pygame.USEREVENT+2

class Level():
    def __init__(self,path_lvl,waves=100):
        global path
        global trajectory
        self.all_paths=path
        self.path_lvl=path_lvl
        self.path=self.all_paths[path_lvl-1]


        self.units=[]
        self.towers=[]

        self.waves=waves
        self.max_waves = self.waves
        self.wave=[]
        self.waveCount=0
        self.trajectory = trajectory[path_lvl-1]
        self.lives=25
        self.money=120
        self.c1=0
        self.c2=0
        for i in self.path:
            for j in i:
                if j==11:
                    self.spawnX=tileSize*self.c1
                    self.spawnY=tileSize*self.c2
                self.c1+=1
            self.c1=0
            self.c2+=1

        self.passed=False
        self.started=False

        self.timer=1000

    def move(self):
        for unit in self.units:
            if unit.hp<=0:
                self.units.pop(self.units.index(unit))
                self.money+=unit.gold+r.randint(-1,1)
                moneyFall.play()


            #if len(trajectory)
            #for j in range(len(self.trajectory)):
            unit.walk(self.trajectory)
            #print()
            #print(unit.i)
            #print(self.trajectory)

    def spawn(self):
        self.units.append(self.wave[0][self.wave[1]])

    def attack(self,dt):
        ####РАССЧЕКТ СКОРОСТИ АТАКИ , ЗАДЕРЖКИ ЧЕРЕЗ BPM
        ###BPM=100, ASPEED=3, DELAY BETWEEN BPM = 600 MS

        for tower in self.towers:
            if tower.isOnTarget not in self.units:  ##Если таргет мертв то убирает таргет
                if tower.bullets!=[]:
                    for bullet in tower.bullets:
                        if bullet.target==tower.isOnTarget:
                            bullet.target=None
                            tower.bullets.pop(tower.bullets.index(bullet))
                            tower.deltaTime=0
                tower.isOnTarget=None
                tower.freezes=0

            for unit in self.units:
                if not tower.isOnTarget:    #Выбирает таргет если его нет
                    D = ((unit.x - tower.x) ** 2 + (unit.y - tower.y) ** 2) ** 0.5
                    inRange = tower.atk_range >= D
                    if inRange:
                        tower.isOnTarget=unit

                else:       #Атакует если таргет есть
                    if unit== tower.isOnTarget :
                        D = ((unit.x - tower.x) ** 2 + (unit.y - tower.y) ** 2) ** 0.5
                        inRange = tower.atk_range >= D
                        if inRange:
                            tower.attack(tower.isOnTarget,dt,self.units)

                        else:   #Убирает таргет если таргет не в радиусе
                            tower.isOnTarget=None
                            tower.freezes=0





                    #print("\nD, RANGE: ",D,tower.atk_range,"\n")








