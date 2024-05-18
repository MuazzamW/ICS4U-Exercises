import pygame
import random
from bullet import Bullet

class Enemy:

    ENEMY_LIST = []

    def __init__(self,window,xPos, yPos):
        self.__window = window
        self.__hitbox = pygame.Rect(xPos, yPos, 50, 50)
        #scale image to 50x50
        self.__image = pygame.image.load("Space Invader/Assets/enemy.png")
        self.__image = pygame.transform.scale(self.__image, (50,50))
        self.__xPos = xPos
        self.__yPos = yPos
        self.__speed = 2 
        Enemy.ENEMY_LIST.append(self)
    
    @staticmethod
    def collisionCheck():
        if len(Enemy.ENEMY_LIST) == 0:
            return
        for enemy in Enemy.ENEMY_LIST:
            for bullet in Bullet.returnBulletList():
                if enemy.isHit(bullet):
                    enemy.delete()
                    bullet.delete()
                    break
    
    @staticmethod  
    def hitShip(ship):
        print("entered hit ship")
        for enemy in Enemy.ENEMY_LIST:
            if enemy.__hitbox.colliderect(ship.getHitbox()):
                print("ENEMY HIT SHIP")
                return True
        return False
    
    @staticmethod
    def drawEnemies():
        for enemy in Enemy.ENEMY_LIST:
            enemy.__draw()

    def __draw(self):
        xshift = random.randint(-1,1)
        self.__window.draw(self.__image, self.__xPos+xshift, self.__yPos+self.__speed)
        self.__yPos += self.__speed
        self.__xPos += xshift
        self.__hitbox = pygame.Rect(self.__xPos, self.__yPos, 50, 50)
    
    def delete(self):
        Enemy.ENEMY_LIST.remove(self)
        del self
    
    #is hit function
    def isHit(self, bullet):
        if self.__hitbox.colliderect(bullet.getHitbox()):
            self.delete()
        return False

    
        

