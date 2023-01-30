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
screen_rect = screen.get_rect()
print(screen_rect.width)
print(screen_rect.height)
print(screen_rect.size)
print(screen_rect.centerx) # screen_w // 2 = 300
print(screen_rect.centery) # screen_h // 2 = 150
print(screen_rect.center)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False     
    pygame.display.update()
pygame.quit()