
from objects import Sprite
import math
from Anims import *
from sounds import *
import random as r



class Bullet(Sprite):
    def __init__(self,x=0, y=0, w=128, h=128, surface=0, tile=0,speed=33,type=0,target=None,dmg=0,dmgSurface=0):
        Sprite.__init__(self, x, y, w, h, surface, tile)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed=speed
        self.alpha=0
        self.Dx=0
        self.Dy=0
        self.target=target
        self.dmg=dmg
        self.animCount=0
        self.newSurface=dmgSurface
        self.tile=tile

    def draw(self,D):

        self.Dx=math.fabs(self.x+64-(self.target.x+64))
        self.Dy=math.fabs(self.y+64-(self.target.y+64))
        self.Dc=D

        if self.x<self.target.x and self.y>self.target.y:
            ###1 ЧЕТВЕРТЬ
           # print((self.Dx**2+self.Dc**2-self.Dy**2)/(2*self.Dx*self.Dc))
            self.alpha=math.acos((self.Dx**2+self.Dc**2-self.Dy**2)/(2*self.Dx*self.Dc))
            self.Dx=self.speed*math.cos(self.alpha)
            self.Dy=-self.speed*math.sin(self.alpha)
            #print("\n1\n")

        elif self.x>self.target.x and self.y>self.target.y:
            ###2 ЧЕТВЕРТЬ
            #print((self.Dx ** 2 + self.Dc ** 2 - self.Dy ** 2) / (2 * self.Dx * self.Dc))
            self.alpha = math.acos((self.Dx ** 2 + self.Dc ** 2 - self.Dy ** 2) / (2 * self.Dx * self.Dc))
            self.Dx = -self.speed * math.sin(self.alpha)
            self.Dy = -self.speed * math.cos(self.alpha)
            #print("\n2\n")

        elif self.x > self.target.x and self.y < self.target.y:
            ###3 ЧЕТВЕРТЬ
            #print((self.Dc ** 2 + self.Dy ** 2 - self.Dx ** 2) / (2 * self.Dy * self.Dc))
            self.alpha = math.acos((self.Dc ** 2 + self.Dy ** 2 - self.Dx ** 2) / (2 * self.Dy * self.Dc))
            self.Dx = -self.speed * math.sin(self.alpha)
            self.Dy = self.speed * math.cos(self.alpha)
            #print("\n3\n")

        elif self.x < self.target.x and self.y <self.target.y:
            ###4 ЧЕТВЕРТЬ
            #print((self.Dy ** 2 + self.Dc ** 2 - self.Dx ** 2) / (2 * self.Dy * self.Dc))
            self.alpha = math.acos((self.Dy ** 2 + self.Dc ** 2 - self.Dx ** 2) / (2 * self.Dy * self.Dc))
            self.Dx = self.speed * math.sin(self.alpha)
            self.Dy = self.speed * math.cos(self.alpha)
            # print("\n4\n")
            # print("Dy, Dc, Dx:",self.Dy,self.Dc,self.Dy)
            # print("alpha:",self.alpha)

        else:
            if self.x==self.target.x and self.y>self.target.y:
                ### 0 градусов
                self.alpha=0
                self.Dx=0
                self.Dy=-self.speed

            elif self.y==self.target.y and self.x<self.target.x:
                ### 270 градусов
                self.alpha = 270
                self.Dx=self.speed
                self.Dy=0

            elif self.x==self.target.x and self.y<self.target.y:
                ### 180 градусов
                self.alpha = 180
                self.Dx=0
                self.Dy=self.speed

            elif self.y==self.target.y and self.x>self.target.x:
                ### 90 градусов
                self.alpha = 90
                self.Dx=-self.speed
                self.Dy=0



        self.x+=self.Dx
        self.y+=self.Dy
        #print(towerImages)
        if self.animCount+1>=2*len(self.tile):
            self.animCount=0
        self.surface.blit(self.tile[self.animCount//2], (self.x, self.y))
        self.animCount+=1

        #print(self.alpha)

    def drawDamage(self):
        if self.animCount +1 >=12:
            self.animCount=0
        self.surface.blit(damageEffect[self.animCount//4], (self.x,self.y))
        self.animCount+=1


class Tower(Sprite):
    def __init__(self, x=0, y=0, w=128, h=128, surface=0, tile=0,atk=0,atk_speed=0,atk_range=0,type=0):
        Sprite.__init__(self,x,y,w,h,surface,tile)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.atk=0
        self.atk_speed=0
        self.atk_range=0
        self.animCount=0
        self.cost=0
        self.bullets=[]
        self.deltaTime=0
        self.type=type
        self.isOnTarget=None

        #lightning list of enemies:
        self.lightninglist=[]

        if self.type==0:
            self.atk=3
            self.atk_speed=7
            self.atk_range=335
            self.cost=60
            self.tileBullet = allBullets[0]

        elif self.type==1:
            self.atk=7
            self.atk_speed=0
            self.atk_range=400
            self.cost=175


        elif self.type == 2:
            self.atk = 3
            self.atk_speed = 9
            self.atk_range = 400
            self.cost = 100
            self.tileBullet = allBullets[1]
            self.freezes = 0



        elif self.type==3:
            self.atk=1.5
            self.atk_speed=18
            self.atk_range=250
            self.cost=240




        self.soundAttack = towerAttackSounds[self.type]
        self.delay=1000-(50*self.atk_speed)
        self.deltaTime=self.delay

    def lightning_atk(self):
        self.soundAttack.play()
        target1=(self.x+64,self.y+64)
        k=1
        for enemy in self.lightninglist:
            target2=(enemy.x+64,enemy.y+64)
            pygame.draw.line(self.surface, (255, 215, 15), target1, target2, r.randint(3, 8))
            target1=target2
            enemy.hp-=self.atk*k
            k-=0.33

        self.lightninglist.clear()



    def attack(self,unit,dt,units):
        #####Archer Tower:
        if self.type==0 or self.type==2:
            self.deltaTime+=dt
            if self.deltaTime>=self.delay:
                if unit in units:
                    self.soundAttack.play()
                    self.bullets.append(Bullet(x=self.x,y=self.y,type=self.type,tile=self.tileBullet,
                                               surface=self.surface,
                                               target=unit,dmg=self.atk))
                    #print("\nSHOT!")
                    self.deltaTime=0
                else:
                    self.isOnTarget=None
                    self.freezes=0

            if self.bullets!=[]:
                for bullet in self.bullets:
                    if bullet.target:
                        D = (((bullet.x+64 - (bullet.target.x+64)) ** 2 + (bullet.y+64 - (bullet.target.y+64)) ** 2) ** 0.5)
                        inRect = (bullet.x >=bullet.target.x and bullet.x <= bullet.target.x + 128\
                                  and bullet.y >=bullet.target.y and bullet.y<= bullet.target.y + 128)
                        if D>=bullet.speed and not inRect:
                            bullet.draw(D)
                        else:
                            bullet.drawDamage()
                            self.bullets.pop(self.bullets.index(bullet))
                            bullet.target.hp-=bullet.dmg
                            if self.type==2:
                                #frostCrushSound.play()
                                if self.freezes<=3:
                                    bullet.target.speed*=0.8
                                    self.freezes+=1
                                if bullet.target.hp<=0:
                                    self.freezes=0
                    elif self.type==2:
                        self.freezes=0

        #####Lightning Tower:
        elif self.type==1:
            self.deltaTime+=dt
            D = ((self.x+64 - unit.x+64) ** 2 + (self.y+64 - unit.y+64) ** 2) ** 0.5
            inRange = D <= self.atk_range


            if len(self.lightninglist) < 3 and len(self.lightninglist) < len(units):
                if unit not in self.lightninglist:
                    self.lightninglist.append(unit)


            if self.deltaTime>=self.delay:
                if unit in units:
                    if inRange:
                        #print("\nLIGHT SHOT\n",len(self.lightninglist),"\n",self.lightninglist)
                        self.lightning_atk()
                        self.deltaTime=0
                    else:
                        self.lightninglist.pop(self.lightninglist.index(unit))
                else:
                    self.isOnTarget=None

        elif self.type==3:
            self.deltaTime += dt
            D = ((self.x+64 - (unit.x+64)) ** 2 + (self.y+64 - (unit.y+64)) ** 2) ** 0.5
            inRange = D <= self.atk_range


            if self.deltaTime>=self.delay:
                if unit in units:
                    if inRange:
                        self.Dc = D
                        self.Dx = math.fabs(self.x + 64 - (unit.x + 64))
                        self.Dy = math.fabs(self.y + 64 - (unit.y + 64))

                        #Вычисление угла поворота башни
                        if self.x+64 < unit.x+64 and self.y+64 > unit.y+64:
                            ###1 ЧЕТВЕРТЬ
                            self.alpha = math.acos(self.Dx/self.Dc)*100+270
                            self.quarter=1



                        elif self.x+64 > unit.x+64 and self.y+64 > unit.y+64:
                            ###2 ЧЕТВЕРТЬ
                            self.alpha = math.acos(self.Dx/self.Dc)*100-360
                            self.quarter = 2

                        elif self.x+64 > unit.x+64 and self.y+64 < unit.y+64:
                            ###3 ЧЕТВЕРТЬ
                            self.alpha = math.acos(self.Dy/self.Dc)*100+90
                            self.quarter = 3

                        elif self.x+64 < unit.x+64 and self.y+64 < unit.y+64:
                            ###4 ЧЕТВЕРТЬ
                            self.alpha =math.acos(self.Dy/self.Dc)*100+180
                            self.quarter = 4



                        else:
                            if self.x+64 == unit.x+64 and self.y+64 > unit.y+64:
                                ### 0 градусов
                                self.alpha = 0
                                self.quarter=r.randint(1,2)

                            elif self.y+64 == unit.y+64 and self.x+64 < unit.x+64:
                                ### 270 градусов
                                self.alpha = 270
                                self.quarter = r.choice((1, 4))

                            elif self.x+64 == unit.x+64 and self.y+64 < unit.y+64:
                                ### 180 градусов
                                self.alpha = 180
                                self.quarter = r.randint(3, 4)

                            elif self.y+64 == unit.y+64 and self.x+64 > unit.x+64:
                                ### 90 градусов
                                self.alpha = 90
                                self.quarter = r.randint(2, 3)

                        self.tile = minigun_Shoot[self.quarter - 1]

                        self.deltaTime=0
                        self.soundAttack.play()
                        unit.hp-=self.atk
                        #print(self.quarter,"\t",self.alpha)


                        if unit.hp<=0:
                            self.tile = towerImages[self.type]
                    else:
                        self.tile = towerImages[self.type]
                else:
                    self.isOnTarget=None
                    self.tile = towerImages[self.type]



    def draw(self,x,y):
        if self.type==3:
            if not self.isOnTarget:
                self.tile = towerImages[self.type]

        try:
            if self.animCount +1 >=2*len(self.tile):
                self.animCount=0
            self.surface.blit(self.tile[self.animCount//2], (x,y))
            self.animCount += 1
        except:
            self.surface.blit(self.tile, (x, y))



