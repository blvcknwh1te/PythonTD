import pygame
from Anims import *

class GameObject:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.w=width
        self.h=height

class Sprite(GameObject):
    def __init__(self,x,y,w,h,surface,tile):
        GameObject.__init__(self,x,y,w,h)
        #self.rect=pygame.Rect((self.x,self.y,self.w,self.h))
        self.surface=surface
        self.tile=tile

    def draw(self,x,y):
        self.surface.blit(self.tile,(x,y))

class Unit(Sprite):
    def __init__(self,x,y,w,h,speed,hp,surface,tile,walkAnims,dieAnims,gold=0):
        Sprite.__init__(self,x,y,w,h,surface,tile)
        self.speed=speed
        self.hp=hp
        self.walkAnims=walkAnims
        self.dieAnims=dieAnims
        self.animCount=0
        self.direction='right'
        self.count=0
        self.i=0
        self.moving=False
        self.gold=gold

    def draw(self):



        if self.animCount +1 >=16:
            self.animCount=0

        self.surface.blit(self.walkAnims[self.animCount//8], (self.x, self.y))
        self.animCount+=1


    def walk(self,trajectory):
        if self.moving==False:
            if trajectory[self.i][1]=='right':
                self.x+=self.speed
            elif trajectory[self.i][1]=='left':
                self.x-=self.speed
            elif trajectory[self.i][1]=='up':
                self.y-=self.speed
            elif trajectory[self.i][1]=='down':
                self.y+=self.speed

            if type(self.walkAnims[0]) is tuple:
                if trajectory[self.i][1] == 'down':
                    #self.walkAnims = self.walkAnims[0]
                    self.dir=0
                elif trajectory[self.i][1] == 'up':
                    #self.walkAnims = self.walkAnims[1]
                    self.dir = 1
                elif trajectory[self.i][1] == 'left':
                    #self.walkAnims = self.walkAnims[2]
                    self.dir = 2
                elif trajectory[self.i][1] == 'right':
                    #self.walkAnims = self.walkAnims[3]
                    self.dir = 3




            self.count += self.speed
            if self.count >= trajectory[self.i][0] * 128:
                self.count = 0
                if self.i<len(trajectory):
                    self.i+=1



        if self.animCount +1 >=8:
            self.animCount=0
        if type(self.walkAnims[0]) is tuple:
            self.surface.blit(self.walkAnims[self.dir][self.animCount // 4], (self.x, self.y))
        else:
            self.surface.blit(self.walkAnims[self.animCount//4], (self.x, self.y))
        self.animCount+=1




