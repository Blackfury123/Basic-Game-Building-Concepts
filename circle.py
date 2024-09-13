import pygame
pygame.init()
window=pygame.display.set_mode((600,600))
window.fill((0,188,255))
# pygame.draw.circle(window,(0,0,0),(300,300),80)
pygame.draw.circle(window,(0,0,0),(300,300),80,9)
pygame.display.update()
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          done = True

pygame.quit()