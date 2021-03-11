import pygame
import random
pygame.init()

windowSize = [600, 600]
screen = pygame.display.set_mode(windowSize)
font = pygame.font.Font(pygame.font.get_default_font(), 36)
clock = pygame.time.Clock()
pygame.display.set_caption('Chase')
colour = pygame.color.Color('#FF0000')
colour2 = pygame.color.Color('#0000FF')
black = pygame.color.Color('#000000')
colorb = pygame.color.Color('#FFFF00')
font = pygame.font.SysFont('monospace',50)

done = 0
X = 300
Y = 300
X2 = 400
Y2 = 300
ballY = 300
ballX = 200
blockX = ballX - 10
blockY = ballY - 10
s1 = 0
s2 = 0

while done != 1:
    s1s = str(s1)
    s2s = str(s2)
    t1 = font.render(s1s,1,colour)
    t2 = font.render(s2s,1,colour2)
    players = pygame.sprite.Group()
    target = pygame.sprite.Group()
    screen.fill(black)
    pygame.draw.circle(screen, colour, [X, Y], 10)
    pygame.draw.circle(screen, colour2, [X2, Y2], 10)
    pygame.draw.circle(screen, colorb, [ballX, ballY], 10)
    screen.blit(t1,(500, 10))
    screen.blit(t2,(30, 10))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if X == 600 or X == 601 or X == 602:
        X = 5
    if X == 0 or X == -1 or X == -2:
        X = 595
    if Y == 600 or Y == 601 or Y == 602:
        Y = 5
    if Y == 0 or Y == -1 or Y == -2:
        Y = 595

    if X2 == 600 or X2 == 601 or X2 == 602 or X2 == 599:
        X2 = 5
    if X2 == 0 or X2 == -1 or X2 == -2 or X2 == 1:
        X2 = 595
    if Y2 == 600 or Y2 == 601 or Y2 == 602 or Y2 == 599:
        Y2 = 5
    if Y2 == 0 or Y2 == -1 or Y2 == -2 or Y2 == 1:
        Y2 = 595

    if keys[pygame.K_w]:
        Y = Y - 3
    if keys[pygame.K_s]:
        Y = Y + 3
    if keys[pygame.K_a]:
        X = X - 3
    if keys[pygame.K_d]:
        X = X + 3

    if keys[pygame.K_UP]:
        Y2 = Y2 - 3
    if keys[pygame.K_DOWN]:
        Y2 = Y2 + 3
    if keys[pygame.K_LEFT]:
        X2 = X2 - 3
    if keys[pygame.K_RIGHT]:
        X2 = X2 + 3
    
    if -10 < Y - ballY < 10 and -10 < X - ballX < 10:
        s1 += 1
    if -10 < Y2 - ballY < 10 and -10 < X2 - ballX < 10:
        s2 += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1
            quit2 = True 
    clock.tick(72)
if quit2 == True:
    pygame.quit()
