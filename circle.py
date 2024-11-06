import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
pygame.draw.circle(screen,(0,255,0),(300,300),15)
#outline circle
pygame.draw.circle(screen,(0,255,0),(100,100),15,3)
pygame.display.update()
done=False 
while not done:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()