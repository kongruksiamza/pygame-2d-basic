import pygame
pygame.init()
pygame.display.set_caption("My Game")
#ตั้งค่าสี (RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
#ขนาดหน้าจอเกม
SCREEN_W = 600
SCREEN_H = 300
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
screen.fill(WHITE)
#ออกแบบรูปทรงต่างๆ 
pygame.draw.line(screen,RED,(0,0),(100,100),5)
pygame.draw.rect(screen,BLUE,(170,20,100,100))
pygame.draw.circle(screen,BLACK,(400,80),50,3)
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()