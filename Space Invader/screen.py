import pygame
from ship import Ship
from bullet import Bullet
from enemy import Enemy
import multiprocessing as mp
class Screen:
    def __init__(self):
        self.__window = pygame.display.set_mode((500,500))
        self.__background = pygame.image.load("Space Invader/Assets/background.png")
        pygame.display.set_caption("Space Invader")
        self.clock = pygame.time.Clock()
        self.__lose_screen = pygame.image.load("Space Invader/Assets/game_over.png")
        self.__winScreen = pygame.image.load("Space Invader/Assets/winner.png")
    
    def drawBackground(self):
        self.__window.blit(self.__background, (0,0))

    def draw(self,asset,xPos,yPos):
        self.__window.blit(asset, (xPos,yPos))

    def game_over(self):
        self.__window.blit(self.__lose_screen,(0,0))
  
    def winner(self): 
        self.screen.blit(self.win_screen,(0,0))

def main():
    window = Screen()
    ship = Ship(window, 250, 400)
    bulletCount = 0
    enemyCount = 0
    run = True
    

    #create Enemies
    for i in range(5):
        Enemy(window, 50*i, 50)

    while run:
        if len(Enemy.ENEMY_LIST) == 0:
            window.winner()
            run = False 
        window.drawBackground()
        ship.draw()
        enemyCount += 1
        if enemyCount % 2 == 0:
            Enemy.drawEnemies()
        Bullet.moveBullets()
        if(Enemy.hitShip(ship)):
            window.game_over()
            run = False 
        Enemy.collisionCheck()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ship.move("left")
        if keys[pygame.K_d]:
            ship.move("right")
        if keys[pygame.K_SPACE]:
            bulletCount +=1
            if bulletCount %8  == 0:
                Bullet(window, ship.getHitbox().centerx, ship.getHitbox().centery)
                print('bullet created')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        window.clock.tick(60)
        pygame.display.update()
        
        
        
        

if __name__ == "__main__":
    main()