import pygame
import numpy as np
import sys
from source import Button
con = {
        0: (0, 0, 0),       
        1: (0, 0, 255),     
        2: (0, 255, 0),      
        3: (255, 192, 203),
        4: (255, 0, 0),      
        5: (255, 215, 0),    
        6: (255, 255, 255),  
    }
COLOR_TABLE = np.array([con[i] for i in range(7)], dtype=np.uint8)
# due to the fuckass fractal calling a fonction 190k times to render a damn page , i m resorting to numpy arrays for c speed.
MAX=100
def mandel_nump(left,right,bottom,top,width,height,MAX=100):
    real=np.linspace(left,right,width)
    imag=np.linspace(bottom,top,height)
    X,Y=np.meshgrid(real,imag)
    C= X + 1j * Y
    Z=np.zeros_like(C,dtype=np.complex128)
    mandel=np.zeros(C.shape,dtype=np.int32)
    for i in range (MAX):
        mask=np.abs(Z)<=2
        Z[mask]=Z[mask]*Z[mask] + C[mask]
        mandel[mask]+=1
    result=np.zeros_like(mandel)
    result = (mandel % 7).astype(np.uint8) 
    result[mandel == MAX] = 0
    return result.astype(np.uint8)
def render_mandel(screen,left,right,bottom,top,width,height):
    result=mandel_nump(left,right,bottom,top,width,height,MAX=100)
    surface=pygame.Surface((width,height))

    
    rgb_array = COLOR_TABLE[result]
    surface = pygame.surfarray.make_surface(np.transpose(rgb_array, (1, 0, 2)))
    screen.blit(surface,(0,0))
    
    return surface



























































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
fractal_surface = None















left=-2.5
right=1.5
up=1.5
down=-1.5


needs_render=False
while True:
    screen.fill(BlACK)
    for event in  pygame.event.get():
        
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        if mode==0:
            
            brot.handle_event(event)
            julia.handle_event(event)
            start.handle_event(event)
            
            if event.type==pygame.MOUSEBUTTONDOWN :
                if brot.handle_event(event):
                    s="mandelbrot"
                elif julia.handle_event(event):
                    s="julia"
                elif start.handle_event(event):
                    mode=1
                    needs_render=True
                    if s=="mandelbrot":
                        left=-3.16
                        right=2.16
                        up=1.5
                        down=-1.5
            txt=font.render(f"current set : {s}",True,WHITE)
            txtr=font.render(intsr,True,WHITE)
            txtr1=font.render(instr1,True,WHITE)
            txtr2=font.render(instr2,True,WHITE)
            
        elif mode==1:
            
            if event.type==pygame.KEYDOWN:
                vert = 0.1 * (up - down)
                if event.key==pygame.K_LEFT:
                    left=left-0.1*(right-left)
                    right=right-0.1*(right-left)
                    needs_render = True
                if event.key==pygame.K_RIGHT:
                    left=left+0.1*(right-left)
                    right=right +0.1*(right-left)
                    needs_render = True
                if event.key==pygame.K_UP:
                    up=up-vert
                    down=down-vert
                    needs_render = True
                if event.key==pygame.K_DOWN:
                    up=up+vert
                    down=down+vert
                    needs_render = True  
            if event.type==pygame.MOUSEBUTTONDOWN:
                height=up-down
                width=right-left
                center_x=(left+right)/2
                center_y=(up+down)/2

                if pygame.mouse.get_pressed()[0]:
                    left=center_x - (width*0.9)/2
                    right=center_x+(width*0.9)/2 
                    up=center_y +(height*0.9)/2
                    down=center_y -(height*0.9)/2
                    needs_render = True 
                if pygame.mouse.get_pressed()[2]:
                    left=center_x - (width*1.2)/2
                    right=center_x+(width*1.2)/2 
                    up=center_y +(height*1.2)/2
                    down=center_y -(height*1.2)/2
                    needs_render = True
                
    if mode==0:
            brot.draw(screen)
            julia.draw(screen)
            start.draw(screen)
            screen.blit(txt,(450,300))
            screen.blit(txtr,(250,500))
            screen.blit(txtr1,(255,550))
            screen.blit(txtr2,(500,600))
    if fractal_surface:
        screen.blit(fractal_surface, (0, 0)) 
    if needs_render:
                fractal_surface = render_mandel(screen, left, right,down,up, WINDOW_WIDTH, WINDOW_HEIGHT)
                needs_render = False    
    

    pygame.display.flip()
    
    