import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.Font(pygame.font.get_default_font(), 36)
culur = pygame.color.Color('#00FF00')

font=pygame.font.SysFont('monospace',50)
done=False
while not done:
    t1=font.render('Text',1,culur)
    screen.blit(t1,(400, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, culur, [300, 300, 50, 80])
    pygame.display.flip()
pygame.quit()