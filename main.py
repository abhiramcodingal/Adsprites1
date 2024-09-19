import pygame
import random
from time import sleep

pygame.init()
#surface1 = pygame.display.set_mode((640,480))
SPR_CLR_CHANGE = pygame.USEREVENT + 1
BG_CLR_CHANGE = pygame.USEREVENT + 2
BLUE = pygame.Color("blue")
PINK = pygame.Color("pink")
D_BLUE = pygame.Color("darkblue")
RED = pygame.Color("red")
YELLOW = pygame.Color("yellow")
MAGENTA = pygame.Color("magenta")
ORANGE = pygame.Color("orange")
WHITE = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    
    def update(self):
        boundary_hit =  False
        self.rect.move_ip(self.velocity)
        if self.rect.left <= 0 or self.rect.right >= 500:
            boundary_hit = True
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            boundary_hit = True
            self.velocity[1] = -self.velocity[1]
        if boundary_hit == True:
            pygame.event.post(pygame.event.Event(SPR_CLR_CHANGE))
            pygame.event.post(pygame.event.Event(BG_CLR_CHANGE))
    
    def change_color(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))
    
def bg_change_color():
    global bg_color
    bg_color = random.choice([PINK,RED,BLUE,D_BLUE])   
        
all_spr_lst = pygame.sprite.Group()
sp1 = Sprite(WHITE,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,480)
all_spr_lst.add(sp1)

surface1 = pygame.display.set_mode((500,500))
pygame.display.set_caption("My Screen with Sprites")
bg_color = PINK
surface1.fill(bg_color)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == SPR_CLR_CHANGE:
            sp1.change_color()
        elif event.type == BG_CLR_CHANGE:
            bg_change_color()
                
    all_spr_lst.update()
    surface1.fill(bg_color)
    all_spr_lst.draw(surface1)
    
    pygame.display.flip()
    clock.tick(400)

pygame.quit()   