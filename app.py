import pygame
import numpy as np
import sys
from source import Button
# due to the fuckass fractal calling a fonction 190k times to render a damn page , i m resorting to numpy arrays for c speed.
MAX=100
def mandel_nump(left,right,bottom,top,width,height,MAX=100):
    real=np.linspace(left,right,width)
    imag=np.linspace(top,bottom,height)
    X,Y=np.meshgrid(real,imag)
    C=X+1j*Y
    Z=np.zeros_like(C,dtype=np.complex128)
    matc





























































BlACK=(0,0,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLUE = (0, 0, 255)
green= (0, 255, 0)
pink= (255, 192, 203)
red= (255, 0, 0)
gold= (255, 215, 0)
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



con = {
        0: (0, 0, 0),       
        1: (0, 0, 255),     
        2: (0, 255, 0),      
        3: (255, 192, 203),
        4: (255, 0, 0),      
        5: (255, 215, 0),    
        6: (255, 255, 255),  
    }
















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
            screen.fill(BlACK)
            if s=="mandelbrot":
                left=-2.5
                right=1.5
                up=1.5
                down=-1.5
                print("Starting render...")
                for x in range(0,1280):
                    if x % 100 == 0:
                        print(f"Rendering column {x}/{WINDOW_WIDTH}")
                    for y in range(0,720):
                        math_x = left + (x / WINDOW_WIDTH) * (right - left)
                        math_y = up - (y / WINDOW_HEIGHT) * (up - down)
                        try:
                            res=mandel(math_x,math_y)
                            if res not in con:
                                print(f"ERROR: Invalid result {res} at ({x}, {y})")
                                print(f"  math_x={math_x}, math_y={math_y}")
                                res = 0
                            pygame.draw.rect(screen,con[res],(x,y,1,1))
                        except Exception as e:
                            print(f"CRASH at ({x}, {y}): {e}")
                            print(f"  math_x={math_x}, math_y={math_y}")
                            print(f"  res={res if 'res' in locals() else 'not calculated'}")
                            raise
                        
        


    
    pygame.display.flip()
    
    