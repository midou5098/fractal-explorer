import pygame
import numpy as np
import sys
#disclaimer : this button set is ai generated , got bigger fish to fry than designing a button class for 5 hours..
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=pygame.Color('white')):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.clicked = False
        
        # Load custom font (font.ttf in your folder)
        try:
            self.font = pygame.font.Font("font.ttf", 24)
        except:
            # Fallback to default font if custom font not found
            self.font = pygame.font.Font(None, 24)
            print("Custom font not found, using default")
    
    def handle_event(self, event):
        """Handle mouse events for the button"""
        if event.type == pygame.MOUSEMOTION:
            # Check if mouse is hovering
            self.is_hovered = self.rect.collidepoint(event.pos)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:  # Left click
                self.clicked = True
                return True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
            
        return False
    
    def draw(self, screen):
        """Draw the button on screen"""
        # Choose color based on state
        if self.clicked:
            current_color = self.hover_color  # Darker when clicked
        elif self.is_hovered:
            current_color = self.hover_color  # Darker when hovered
        else:
            current_color = self.color
        
        # Draw button background with rounded corners
        pygame.draw.rect(screen, current_color, self.rect, border_radius=8)
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2, border_radius=8)
        
        # Render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Draw text
        screen.blit(text_surface, text_rect)
    
    def set_position(self, x, y):
        """Move button to new position"""
        self.rect.x = x
        self.rect.y = y
    
    def set_text(self, new_text):
        """Change button text"""
        self.text = new_text


con = {
        0: (0, 0, 0),       
        1: (0, 0, 255),     
        2: (0, 255, 0),      
        3: (255, 192, 203),
        4: (255, 0, 0),      
        5: (255, 215, 0),    
        6: (255, 255, 255),
        7:(140,60,200),
        8:(70,140,80)
    }
COLOR_TABLE = np.array([con[i] for i in range(9)], dtype=np.uint8)
MAX=200
def mandel_nump(left,right,bottom,top,width,height,MAX=200):
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
    result = (mandel % 9).astype(np.uint8) 
    result[mandel == MAX] = 0
    return result.astype(np.uint8)
def render_mandel(screen,left,right,bottom,top,width,height):
    result=mandel_nump(left,right,bottom,top,width,height,MAX=100)
    surface=pygame.Surface((width,height))
    rgb_array = COLOR_TABLE[result]
    surface = pygame.surfarray.make_surface(np.transpose(rgb_array, (1, 0, 2)))
    screen.blit(surface,(0,0))
    
    return surface
def render_julia(screen,left,right,bottom,top,width,height):
    result=julia_nump(left,right,bottom,top,width,height,MAX=200)
    surface=pygame.Surface((width,height))
    rgb_array = COLOR_TABLE[result]
    surface = pygame.surfarray.make_surface(np.transpose(rgb_array, (1, 0, 2)))
    screen.blit(surface,(0,0))
    
    return surface
def julia_nump(left,right,bottom,top,width,height,MAX=200):
    real=np.linspace(left,right,width)
    imag=np.linspace(bottom,top,height)
    X,Y=np.meshgrid(real,imag)
    C= -0.7+0.27015j
    Z= X + 1j * Y
    mandel=np.zeros(Z.shape,dtype=np.int32)
    for i in range (MAX):
        mask=np.abs(Z)<=2
        Z[mask]=Z[mask]*Z[mask] + C
        mandel[mask]+=1
    result=np.zeros_like(mandel)
    result = (mandel % 9).astype(np.uint8) 
    result[mandel == MAX] = 0
    return result.astype(np.uint8)




def mandel(x,y):
    i=0
    Z=0
    c=complex(x,y)
    while i<100 and abs(Z)<2:
        Z=Z*Z + c
        i+=1
    if 80<i<=100:
        return 6
    elif 0<=i<=10:
        return 1
    elif 10<i<=20:
        return 2
    elif 20<i<=40:
        return 3
    elif 40<i<=60:
        return 4
    elif 60<i<=80:
        return 5


