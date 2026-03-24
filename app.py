import pygame
import sys



BlACK=(0,0,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
WINDOW_HEIGHT=720
WINDOW_WIDTH=1280

pygame.init()
pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("fuckass fractal")
while True:
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        
    pygame.display.flip()
    