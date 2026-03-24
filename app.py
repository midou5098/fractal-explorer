import pygame
import sys
from source import Button


BlACK=(0,0,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
WINDOW_HEIGHT=720
WINDOW_WIDTH=1280
pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("fuckass fractal")
font=pygame.font.Font(None,36)
brot=Button(50,50,160,40,"mandelbrot",pygame.Color('green'),pygame.Color('darkgreen'))
julia=Button(250,50,100,40,"julia",pygame.Color('blue'),pygame.Color('grey'))
start=Button(1150,250,100,60,"start",pygame.Color('red'),pygame.Color('darkred'))
mode=0
s="mandelbrot"
intsr="welcome to the fractal explorer , pick your set and press start! " 
instr1="use arrows for navigation and mouse right/left click for zoom " 
instr2="made by mohamed "




















while True:
    
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        if mode==0:
            screen.fill(BlACK)
            brot.handle_event(event)
            julia.handle_event(event)
            start.handle_event(event)
            brot.draw(screen)
            julia.draw(screen)
            start.draw(screen)
            if event.type==pygame.MOUSEBUTTONDOWN :
                if brot.handle_event(event):
                    s="mandelbrot"
                elif julia.handle_event(event):
                    s="julia"
                elif start.handle_event(event):
                    mode=1
            txt=font.render(f"current set : {s}",True,WHITE)
            txtr=font.render(intsr,True,WHITE)
            txtr1=font.render(instr1,True,WHITE)
            txtr2=font.render(instr2,True,WHITE)
            screen.blit(txt,(450,300))
            screen.blit(txtr,(250,500))
            screen.blit(txtr1,(255,550))
            screen.blit(txtr2,(500,600))
        elif mode==1:
            screen.fill(WHITE)
            
        


    
    pygame.display.flip()
    
    