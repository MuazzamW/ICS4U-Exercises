import pygame
class Ship:
    def __init__(self, screen, xPos, yPos):
        self.__image = pygame.image.load("Space Invader/Assets/spaceinvaders.png")
        self.__xPos = xPos
        self.__yPos = yPos
        self.__screen = screen
        self.__hitbox = pygame.Rect(xPos, yPos, 50, 50)
    
    def draw(self):
        self.__screen.draw(self.__image, self.__xPos, self.__yPos)
    
    def move(self, direction):
        if direction == "left":
            self.__xPos -= 5
        elif direction == "right":
            self.__xPos += 5
        self.__hitbox = pygame.Rect(self.__xPos, self.__yPos, 50, 50)

    def getHitbox(self):
        return self.__hitbox
    