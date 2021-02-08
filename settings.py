import os
import sys
import pygame

choiceColor=(230,230,150)
ind_range=0


HEIGHT=1080
WIDTH=1400
os.environ['SDL_VIDEO_CENTERED'] = '1'
tileSize=128
TILE_AMOUNT=int(WIDTH/tileSize) # (8)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption("Medieval TD v.0.1")
FPS=60
mouseDown=False
mouseUp=False
isWave=False
isMenu=True
isGame=False
selectOn=False
clickedOnButton=False
selectedTower=0
towerIconsPositions=[]
tilePositions=[]
towerPositions=[]
selectedTower=None
portalCount=0

HS_FILE = "highscore.txt"

x=0
y=0
spawnX=0
spawnY=0
mouseX=0
mouseY=0

rectX=1064
rectY=140


