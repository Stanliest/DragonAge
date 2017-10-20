import pygame
import gameData
from dragon import Dragon

def setDragons():
    fireDragon =MyParty(1,gameData.dragonDatabase)
    waterDragon = MyParty(2,gameData.dragonDatabase)
    iceDragon = MyParty(3,gameData.dragonDatabase)
    gameData.party.append(fireDragon)
    gameData.party.append(waterDragon)
    gameData.party.append(iceDragon)

class MyParty(Dragon):
    def __init__(self,dragon,dragonDatabase,level=1,x=None,y=None):
        #super
        Dragon.__init__(self,dragon,dragonDatabase)
        self.x = x
        self.y = y
        self.setRange()
        #when to shoot next bullet
        self.maxCounter = 8
        self.counter = self.maxCounter
        self.target = None
        self.bullets = []
        self.onBoard = False
        self.radius = False
        self.level = level
        self.numOfUpgrade = 0
        self.attack = self.baseAttack

    def setRange(self):
        if self.upgrade == 0:
            self.range = 50
        if self.upgrade == 1:
            self.range = 80
        if self.upgrade == 2:
            self.range = 120

    #using the right triangle theory to calculate if the enemy is in range
    def isInRangeEquation(self,x,y):
        return (x-self.x)**2 + (y-self.y)**2 < self.range**2

    def isInRange(self,bounds):
        x0,x1,y0,y1 = bounds
        if (self.isInRangeEquation(x0,y0) or self.isInRangeEquation(x0,y1) or
            self.isInRangeEquation(x1,y0) or self.isInRangeEquation(x1,y1)):
            return True
        else:
            return False    
    
    def drawTower(self,canvas):#draw dragon once set on board
        gameData.screen.blit(self.img,(self.x-self.size,self.y-self.size))

    def drawRadius(self,canvas):#draws radius sof pokemon
        pygame.draw.circle(canvas,(255,255,255),(self.x,self.y),self.range,3)


