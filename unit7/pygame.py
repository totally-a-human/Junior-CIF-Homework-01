import pygame
pygame.init()

red = (255, 0, 0)
black = (0, 0, 0)

width = 800
height = 600

x = 0
y = 0
rect1 = pygame.Rect(x,y,30,30)

clock=pygame.display.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

x += 5
y += 5
rect1 = pygame.Rect(x,y,30,30)
pygame.draw.rect(screen, red , rect1)

pygame.display.update()
screen.fill(black)