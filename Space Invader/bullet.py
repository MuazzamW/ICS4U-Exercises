import pygame

class Bullet(pygame.sprite.Sprite):
    
    BULLET_LIST = []
    def __init__(self,window,xPos,yPos):
        super().__init__()
        self.__window = window
        self.__hitbox = pygame.Rect(xPos, yPos, 10, 10)
        self.__image = pygame.image.load("Space Invader/Assets/bullet.png")
        self.__xPos = xPos
        self.__yPos = yPos
        self.__speed = 5
        Bullet.BULLET_LIST.append(self)
    
    @staticmethod
    def returnBulletList():
        return Bullet.BULLET_LIST
    
    def draw(self):
        print('bullet moving')
        self.__window.draw(self.__image, self.__xPos, self.__yPos)
        self.__yPos -= self.__speed
        self.__hitbox = pygame.Rect(self.__xPos, self.__yPos, 10, 10)

    @staticmethod
    def moveBullets():
        if len(Bullet.BULLET_LIST) > 0:
            
            for bullet in Bullet.BULLET_LIST:
                bullet.draw()
                if bullet.__yPos < 0:
                    Bullet.BULLET_LIST.remove(bullet)
                    del bullet
                    print('bullet deleted')
    
    def getHitbox(self):
        return self.__hitbox