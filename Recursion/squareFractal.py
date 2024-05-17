import pygame

pygame.init()
screen = pygame.display.set_mode((900, 900))
#screen backgroud black
screen.fill((0, 0, 0))


def drawSquare(screen, x,y,size, depth):
    if depth == 0:
        return
    else:
        size = size/3
        #split the square into 9 squares and colour only the corners
        #top left corner
        pygame.draw.rect(screen, (255, 255, 255), (x,y, size, size))
        #top right corner
        pygame.draw.rect(screen, (255, 255, 255), (x+size*2,y, size, size))
        #bottom left corner
        pygame.draw.rect(screen, (255, 255, 255), (x,y+size*2, size, size))
        #bottom right corner
        pygame.draw.rect(screen, (255, 255, 255), (x+size*2,y+size*2, size, size))
        #recursive call for the 5 squares
        drawSquare(screen, x+size, y, size, depth-1)
        drawSquare(screen, x, y+size, size, depth-1)
        drawSquare(screen, x+size*2, y+size, size, depth-1)
        drawSquare(screen, x+size, y+size*2, size, depth-1)
        drawSquare(screen, x+size, y+size, size, depth-1)

drawSquare(screen, 0, 0, 900,5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

