import pygame
import time
import random
pygame.init()
#colour = (random.randint(1, 15))

windowSize = [600, 600]
screen = pygame.display.set_mode(windowSize)

done = 0

while done != 1:
    X = (random.randint(1, 600))
    Y = (random.randint(1, 600))
    colour1 = hex((random.randint(1, 255)))
    colour1 = colour1.lstrip('0x')
    colour2 = hex((random.randint(1, 255)))
    colour2 = colour2.lstrip('0x')
    colour3 = hex((random.randint(1, 255)))
    colour3 = colour3.lstrip('0x')
    num = '#' + colour1 + colour2 + colour3
    try:
        color = pygame.color.Color(num)
    except ValueError:
        num = '#' + colour1 + colour2 + colour3 + 'a'
        try:
            color = pygame.color.Color(num)
        except ValueError:
            num = '#' + colour1 + colour2 + colour3 + 'a' + '7'
            try:
                color = pygame.color.Color(num)
            except ValueError:
                num = '#' + colour1 + colour2 + colour3 + 'a' + '7' + 'c'
                color = pygame.color.Color(num)
    pygame.draw.circle(screen, color, [X, Y], 10)
    pygame.display.flip()
    #time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1
pygame.quit()