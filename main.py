import pygame
import random

pygame.init()
#surface1 = pygame.display.set_mode((640,480))
SPR_CLR_CHANGE = pygame.USEREVENT + 1
BG_CLR_CHANGE = pygame.USEREVENT + 2
BLUE = pygame.Color("blue")
L_BLUE = pygame.Color("lightblue")
D_BLUE = pygame.Color("darkblue")
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
        if self.rect.left <= 0 and self.rect.right >= 500:
            boundary_hit = True
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0 and self.rect.down >= 500:
            boundary_hit = True
            self.velocity[1] = -self.velocity[1]
        if boundary_hit == True:
            pygame.event.post(pygame.event.Event(SPR_CLR_CHANGE))
            pygame.event.post(pygame.event.Event(BG_CLR_CHANGE))
        def change_color():
            self.image.fill(random.choice[YELLOW,MAGENTA,ORANGE,WHITE])
    
    def bg_change_color():
        global bg_color
        bg_color = random.choice(random.choice[BLUE,D_BLUE,L_BLUE])
    
    all_spr_lst = pygame.sprite.Group()
        
pygame.display.set_caption("My Screen with Sprites")

sp1 = Sprite(WHITE,20,30)
sp1.rect.x = random.choice([0,480])
sp1.rect.y = random.choice([0,480])

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

pygame.quit()   