import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
done=False

while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True

    pygame.draw.rect(screen,(0,239,255),pygame.Rect(140,70,140,70)) 
    pygame.display.flip()